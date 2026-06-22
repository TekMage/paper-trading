"""train_hmm.py — Train and evaluate the regime HMM with QQQ as primary benchmark.

Fetches real Alpaca bar data when available (recent history via limit).
Falls back to synthetic for development.
Trains GaussianHMM, saves to models/hmm_regime.pkl, and evaluates.
"""

import sys
import pickle
from pathlib import Path

# Add project root
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
import pandas as pd
import requests
import os
from datetime import datetime, timedelta

from agents.hmm_regime import (
    compute_features,
    train_hmm,
    REGIME_LABELS,
    REGIME_BIAS,
)

ALPACA_DATA_BASE = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets/v2")
ALPACA_KEY = os.environ.get("ALPACA_API_KEY")
ALPACA_SECRET = os.environ.get("ALPACA_SECRET_KEY")
HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

MODELS_DIR = Path(__file__).parent.parent / "models"
MODELS_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODELS_DIR / "hmm_regime.pkl"


def fetch_real_bars(symbol: str, days_back: int = 400) -> pd.Series:
    """Robust multi-page fetch for training."""
    try:
        url = f"{ALPACA_DATA_BASE}/stocks/bars"
        from datetime import datetime, timedelta
        end = datetime.now()
        start = (end - timedelta(days=days_back)).date().isoformat()
        all_bars = []
        params = {"symbols": symbol, "timeframe": "1Day", "start": start, "limit": 1000, "adjustment": "all"}
        page_token = None
        for _ in range(10):
            if page_token:
                params["page_token"] = page_token
            resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            bars = data.get("bars", {}).get(symbol, [])
            all_bars.extend(bars)
            page_token = data.get("next_page_token")
            if not page_token:
                break
        if not all_bars:
            return None
        closes = [float(b["c"]) for b in all_bars]
        dates = pd.to_datetime([b["t"] for b in all_bars])
        s = pd.Series(closes, index=dates, name=symbol.lower()).sort_index()
        return s
    except Exception as e:
        print(f"  Real data fetch failed for {symbol}: {e}")
        return None
def generate_synthetic_data(days: int = 400) -> pd.DataFrame:
    """Synthetic fallback (improved for QQQ alpha simulation)."""
    dates = pd.date_range(end=pd.Timestamp.today(), periods=days, freq="B")
    np.random.seed(42)

    qqq_returns = np.random.normal(0.0009, 0.013, days)
    qqq_prices = 700 * np.cumprod(1 + qqq_returns)  # rough current level

    spy_returns = np.random.normal(0.0007, 0.010, days)
    spy_prices = 500 * np.cumprod(1 + spy_returns)

    vix = 18 + np.random.normal(0, 3.5, days).clip(10, 40)

    acct_returns = qqq_returns + np.random.normal(0.0003, 0.009, days)  # slight positive alpha bias
    acct_equity = 100_000 * np.cumprod(1 + acct_returns)

    return pd.DataFrame({
        "date": dates,
        "spy": spy_prices,
        "qqq": qqq_prices,
        "vix": vix,
        "account_equity": acct_equity,
    }).set_index("date")

def fetch_real_data(days: int = 300) -> pd.DataFrame:
    """Try real data, fall back to synthetic."""
    print("Attempting real Alpaca data fetch...")
    qqq = fetch_real_bars("QQQ", days_back=days)
    spy = fetch_real_bars("SPY", days_back=days)

    if qqq is not None and spy is not None and len(qqq) > 50 and len(spy) > 50:
        # Align
        df = pd.DataFrame({"qqq": qqq, "spy": spy}).dropna()
        # Synthetic vix and equity for now
        df["vix"] = 18 + np.random.normal(0, 3, len(df)).clip(10, 35)
        df["account_equity"] = 100000 * (df["qqq"] / df["qqq"].iloc[0]) * np.random.normal(1.0002, 0.005, len(df)).cumprod()
        print(f"  Real data loaded: {len(df)} bars for SPY/QQQ")
        return df
    else:
        print("  Falling back to synthetic data.")
        return generate_synthetic_data(days)

def main():
    print("=== HMM Training Pipeline (QQQ Benchmark Focus) ===\n")

    data = fetch_real_data(400)
    # Attach VIX proxy
    if "qqq" in data:
        data["vix"] = (data["qqq"].pct_change().rolling(20).std() * 252**0.5 * 100).fillna(18).clip(10,40)

    features = compute_features(
        spy_prices=data["spy"],
        qqq_prices=data["qqq"],
        vix=data["vix"],
        account_equity=data.get("account_equity"),
    )

    print(f"Features shape: {features.shape}")
    print(f"Columns: {list(features.columns)}")

    if "acct_vs_qqq_20" in features:
        print(f"\nRecent acct vs QQQ (20d mean): {features['acct_vs_qqq_20'].iloc[-1]:.4f}")

    # Select robust numeric features for training (avoid full cov issues)
    numeric_features = features.select_dtypes(include=[np.number]).dropna()
    # Prefer a subset of stable features
    cols = [c for c in ["spy_ret", "qqq_ret", "qqq_vol_20", "qqq_trend", "vix_level", "acct_vs_qqq_20"] if c in numeric_features.columns]
    if cols:
        X_train = numeric_features[cols]
    else:
        X_train = numeric_features
    print(f"Training on {X_train.shape[1]} features: {list(X_train.columns)}")

    model = train_hmm(X_train, n_states=5)
    print(f"\nTrained GaussianHMM with {model.n_components} states")

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")

    # Predict recent
    last_window = X_train.iloc[-30:]
    states = model.predict(last_window.values)
    probs = model.predict_proba(last_window.values)
    final_state = states[-1]
    final_probs = probs[-1]

    print(f"\nMost recent regime: {final_state} → {REGIME_LABELS[final_state]}")
    print(f"Bias: {REGIME_BIAS[final_state]}")
    print(f"Probabilities: {dict(enumerate(final_probs.round(3)))}")

    print("\n=== Training complete. Model ready for Research Agent. ===")
    print(f"To use: from agents.hmm_regime import get_current_regime; ... (will auto-load)")

if __name__ == "__main__":
    main()



def retrain_if_needed(force: bool = False):
    """Simple periodic retrain hook (call from cron or research)."""
    model_path = Path(__file__).parent.parent / "models" / "hmm_regime.pkl"
    import time
    if force or not model_path.exists() or (time.time() - model_path.stat().st_mtime > 7*86400):
        print("Retraining HMM (periodic or forced)...")
        main()
        return True
    return False
