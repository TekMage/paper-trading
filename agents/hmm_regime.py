"""
hmm_regime.py — Hidden Markov Model for Market Regime Detection

Primary benchmark: QQQ (with SPY as secondary)
Goal: Generate consistent alpha vs QQQ while respecting risk limits.

States represent different market regimes that should drive different trading behavior.
"""

from __future__ import annotations
import pickle
from pathlib import Path
MODEL_PATH = Path(__file__).parent.parent / "models" / "hmm_regime.pkl"

def load_model():
    if MODEL_PATH.exists():
        try:
            with open(MODEL_PATH, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print(f"[HMM] Load failed: {e}")
    return None

import os
from datetime import date, timedelta
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd

try:
    from hmmlearn.hmm import GaussianHMM
except ImportError:
    GaussianHMM = None

# ------------------------------------------------------------------
# Regime Definitions (5 states)
# ------------------------------------------------------------------
REGIME_LABELS = {
    0: "High Geo Stress",
    1: "Elevated Risk + Bull Trend",
    2: "Normal Bull",
    3: "Normal Bear",
    4: "Transition / Uncertainty",
}

# Trading bias per regime (high-level guidance for Trading Agent)
REGIME_BIAS = {
    0: "Defensive — reduce size, favor credit spreads, short gamma",
    1: "Selective long gamma + income, tilt toward QQQ outperformance",
    2: "Growth + Wheel, aim for strong QQQ alpha",
    3: "Defensive income, shorter duration, protect vs QQQ downside",
    4: "Reduce exposure, wait for clarity, preserve capital",
}

# ------------------------------------------------------------------
# Feature Engineering
# ------------------------------------------------------------------
def compute_features(
    spy_prices: pd.Series,
    qqq_prices: pd.Series,
    vix: Optional[pd.Series] = None,
    account_equity: Optional[pd.Series] = None,
) -> pd.DataFrame:
    """
    Tightened feature set for HMM regime detection.
    Focus: QQQ alpha generation, volatility regimes, momentum, and relative strength.
    More features but robust cleaning + selection for stability.
    """
    df = pd.DataFrame(index=qqq_prices.index)

    # --- Returns ---
    df["spy_ret"] = spy_prices.pct_change()
    df["qqq_ret"] = qqq_prices.pct_change()
    df["qqq_ret_5"] = qqq_prices.pct_change(5)
    df["qqq_ret_20"] = qqq_prices.pct_change(20)

    # --- Core Alpha ---
    df["qqq_alpha"] = df["qqq_ret"] - df["spy_ret"]
    df["qqq_alpha_5"] = df["qqq_ret_5"] - spy_prices.pct_change(5)
    df["qqq_alpha_20"] = df["qqq_ret_20"] - spy_prices.pct_change(20)
    df["alpha_ma_5"] = df["qqq_alpha"].rolling(5).mean()
    df["alpha_vol_20"] = df["qqq_alpha"].rolling(20).std()

    # --- Volatility ---
    df["qqq_vol_5"] = df["qqq_ret"].rolling(5).std() * np.sqrt(252)
    df["qqq_vol_20"] = df["qqq_ret"].rolling(20).std() * np.sqrt(252)
    df["spy_vol_20"] = df["spy_ret"].rolling(20).std() * np.sqrt(252)
    df["vol_ratio"] = (df["qqq_vol_20"] / (df["spy_vol_20"] + 1e-6)).clip(0.5, 2.0)

    # --- Momentum & Trend ---
    df["qqq_ma_10"] = qqq_prices.rolling(10).mean()
    df["qqq_ma_20"] = qqq_prices.rolling(20).mean()
    df["qqq_ma_50"] = qqq_prices.rolling(50).mean()
    df["qqq_trend_20"] = (qqq_prices > df["qqq_ma_20"]).astype(int)
    df["qqq_dist_ma20"] = (qqq_prices / df["qqq_ma_20"] - 1).clip(-0.2, 0.2)
    df["qqq_roc_10"] = (qqq_prices / qqq_prices.shift(10) - 1).clip(-0.3, 0.3)

    # --- VIX / Fear ---
    if vix is not None and len(vix) > 0:
        df["vix"] = vix.reindex(df.index).ffill().bfill()
        df["vix_level"] = pd.cut(df["vix"], bins=[0, 15, 20, 25, 100], labels=[0, 1, 2, 3]).astype(int).fillna(1)
        df["vix_chg"] = df["vix"].diff(5).clip(-10, 10)
    else:
        df["vix_level"] = 1
        df["vix_chg"] = 0.0

    # --- Account relative (if available) ---
    if account_equity is not None and len(account_equity) > 0:
        df["acct_ret"] = account_equity.pct_change().reindex(df.index).ffill().fillna(0)
        df["acct_alpha"] = df["acct_ret"] - df["qqq_ret"]
    else:
        df["acct_alpha"] = 0.0

    # --- Clean ---
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.interpolate(limit_direction="both").ffill().bfill()
    # Keep only the most reliable columns for HMM (avoid too many NaNs at start)
    core_cols = [c for c in df.columns if c in [
        "qqq_ret", "qqq_alpha", "qqq_alpha_5", "qqq_alpha_20", "alpha_ma_5", "alpha_vol_20",
        "qqq_vol_20", "vol_ratio", "qqq_trend_20", "qqq_dist_ma20", "qqq_roc_10",
        "vix_level", "vix_chg", "acct_alpha"
    ]]
    df = df[core_cols].dropna(thresh=max(3, int(len(core_cols)*0.6)))

    return df


# ------------------------------------------------------------------
# HMM Model
# ------------------------------------------------------------------
def train_hmm(
    features: pd.DataFrame,
    n_states: int = 5,
    random_state: int = 42,
) -> GaussianHMM:
    """Train a Gaussian HMM on the feature set. Very defensive for financial data."""
    if GaussianHMM is None:
        raise ImportError("hmmlearn is required. Run: pip install hmmlearn")

    # Force a small, high-variance feature set if input is problematic
    X = features.select_dtypes(include=[np.number]).values
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    X = np.clip(X, -5, 5)

    if X.shape[0] < 50 or X.shape[1] < 2:
        print("[HMM] Too little data — using synthetic fallback features")
        rng = np.random.default_rng(random_state)
        X = rng.normal(0, 0.02, size=(200, 5))
        X[:, 0] += rng.normal(0, 0.01, 200)  # simulate alpha

    # Add jitter
    X = X + np.random.normal(0, 5e-4, X.shape)

    # Try full model
    for cov in ["diag", "spherical", "tied"]:
        try:
            model = GaussianHMM(
                n_components=n_states,
                covariance_type=cov,
                n_iter=250,
                random_state=random_state,
                tol=1e-4,
                min_covar=1e-2,
            )
            model.fit(X)
            # Validate
            _ = model.predict(X[:5])
            print(f"[HMM] Trained successfully with covariance_type={cov}")
            return model
        except Exception as e:
            print(f"[HMM] {cov} failed: {str(e)[:80]}")
            continue

    # Last resort: return a dummy model that won't crash later
    print("[HMM] All fits failed — creating minimal stable model on synthetic data")
    rng = np.random.default_rng(42)
    X = rng.normal(0, 0.03, size=(300, 4))
    model = GaussianHMM(n_components=n_states, covariance_type="spherical", n_iter=100, random_state=42)
    model.fit(X)
    return model


def predict_regime(
    model: GaussianHMM,
    features: pd.DataFrame,
) -> Tuple[int, np.ndarray]:
    """Return the most likely regime and the probability distribution."""
    X = features.select_dtypes(include=[np.number]).iloc[-1:].values
    state = model.predict(X)[0]
    probs = model.predict_proba(X)[0]
    return int(state), probs


# ------------------------------------------------------------------
# Convenience: Get current regime with QQQ benchmark context
# ------------------------------------------------------------------
def get_current_regime(
    spy: pd.Series,
    qqq: pd.Series,
    vix: Optional[pd.Series] = None,
    account_equity: Optional[pd.Series] = None,
    model: Optional[GaussianHMM] = None,
) -> Dict:
    """
    High-level function the Research Agent will call.
    Returns regime + benchmark context.
    """
    features = compute_features(spy, qqq, vix, account_equity)

    if model is None:
        model = load_model()
    if model is None:
        return {
            "regime_id": 2,
            "regime_name": REGIME_LABELS[2],
            "bias": REGIME_BIAS[2],
            "qqq_alpha_20d": features["qqq_alpha"].tail(20).mean() if "qqq_alpha" in features else 0.0,
            "note": "Model not yet trained — using tightened QQQ-alpha features",
        }

    state, probs = predict_regime(model, features)
    return {
        "regime_id": state,
        "regime_name": REGIME_LABELS[state],
        "bias": REGIME_BIAS[state],
        "confidence": float(probs[state]),
        "probabilities": dict(enumerate(probs.round(3))),
    }


if __name__ == "__main__":
    print("HMM Regime module loaded. Ready for integration with Research Agent.")