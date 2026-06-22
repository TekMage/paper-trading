"""trading_agent_runner.py — Real Trading Agent (Paper Trading Only)

WARNING: STRICTLY paper trading only.
Real money execution is explicitly blocked.
Primary goal: consistent significant positive alpha vs QQQ.

Fleshed out with:
- Regime-aware posture
- Position analysis
- Sample decisions for CSPs, QQQ calls, rebalances (per trading_agent.md + PLAN.md)
- Pre-close review hook
- Controlled paper execution via submit_order
- Context from Research Agent
"""

import os
import logging
from datetime import datetime
from typing import Dict, Any, Optional, List

import requests

try:
    from market_status import get_market_status, is_market_open
except ImportError:
    get_market_status = None
    is_market_open = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("trading_agent")

# SAFETY
PAPER_TRADING_ONLY = True
ACCOUNT_FLOOR = 80000.0
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"  # extra safety during dev

ALPACA_BASE = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")
ALPACA_DATA_BASE = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets/v2")
ALPACA_KEY = os.environ.get("ALPACA_API_KEY")
ALPACA_SECRET = os.environ.get("ALPACA_SECRET_KEY")
HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

# Example targets from PLAN.md / current state (update as strategy evolves)
CSP_TARGETS = [
    {"symbol": "NVDA", "strike": 190, "expiry": "2026-07-18", "min_premium": 1.50},
    {"symbol": "AMZN", "strike": 215, "expiry": "2026-07-18", "min_premium": 1.50},
]
QQQ_CALL_TARGET = {"symbol": "QQQ", "otm_pct": 0.02, "dte_min": 10, "dte_max": 20, "qty": 1}

def get_account() -> Dict[str, Any]:
    if not ALPACA_KEY or not ALPACA_SECRET:
        raise ValueError("Alpaca credentials not set")
    resp = requests.get(f"{ALPACA_BASE}/account", headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_positions() -> List[Dict[str, Any]]:
    resp = requests.get(f"{ALPACA_BASE}/positions", headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_bars(symbol: str, timeframe: str = "1Day", limit: int = 5) -> List[Dict]:
    """Fetch recent bars via Alpaca data API."""
    url = f"{ALPACA_DATA_BASE}/stocks/bars"
    params = {"symbols": symbol, "timeframe": timeframe, "limit": limit}
    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get("bars", {}).get(symbol, [])
    except Exception as e:
        logger.warning(f"Failed to fetch bars for {symbol}: {e}")
        return []


def fetch_historical_bars(symbol: str, days_back: int = 400, timeframe: str = "1Day") -> List[Dict]:
    """Fetch up to days_back of daily bars using pagination (next_page_token)."""
    from datetime import datetime, timedelta
    url = f"{ALPACA_DATA_BASE}/stocks/bars"
    end = datetime.now()
    start = (end - timedelta(days=days_back)).date().isoformat()
    all_bars = []
    params = {
        "symbols": symbol,
        "timeframe": timeframe,
        "start": start,
        "limit": 1000,
        "adjustment": "all",
    }
    page_token = None
    for _ in range(10):  # safety cap
        if page_token:
            params["page_token"] = page_token
        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            bars = data.get("bars", {}).get(symbol, [])
            all_bars.extend(bars)
            page_token = data.get("next_page_token")
            if not page_token or len(bars) == 0:
                break
        except Exception as e:
            logger.warning(f"Historical bars fetch error for {symbol}: {e}")
            break
    # Dedup + sort
    seen = set()
    unique = []
    for b in sorted(all_bars, key=lambda x: x.get("t", "")):
        if b.get("t") not in seen:
            seen.add(b.get("t"))
            unique.append(b)
    logger.info(f"Fetched {len(unique)} historical bars for {symbol}")
    return unique

def get_current_qqq_price() -> float:
    bars = get_bars("QQQ", limit=1)
    if bars:
        return float(bars[-1].get("c", 740.0))
    return 740.0

def submit_order(symbol: str, qty: float, side: str, type_: str = "market",
                 time_in_force: str = "day", limit_price: Optional[float] = None) -> Optional[Dict]:
    if not PAPER_TRADING_ONLY:
        logger.critical("LIVE TRADING ATTEMPT BLOCKED")
        return None
    if DRY_RUN:
        logger.info(f"[DRY_RUN] Would submit {side} {qty} {symbol}")
        return {"id": "dry-run", "symbol": symbol, "side": side, "qty": qty}

    payload = {
        "symbol": symbol, "qty": str(qty), "side": side,
        "type": type_, "time_in_force": time_in_force
    }
    if limit_price:
        payload["limit_price"] = str(limit_price)
        payload["type"] = "limit"

    logger.info(f"Submitting PAPER order: {side} {qty} {symbol}")
    resp = requests.post(f"{ALPACA_BASE}/orders", headers=HEADERS, json=payload, timeout=10)
    if resp.status_code in (200, 201):
        order = resp.json()
        logger.info(f"Order accepted: {order.get('id')}")
        return order
    else:
        logger.error(f"Order failed: {resp.text}")
        return None

def calculate_qqq_alpha(equity: float, qqq_price: float,
                        start_equity: float = 100000.0, start_qqq: float = 731.53) -> float:
    acct_ret = (equity - start_equity) / start_equity * 100
    qqq_ret = (qqq_price - start_qqq) / start_qqq * 100
    return round(acct_ret - qqq_ret, 2)

def analyze_positions(positions: List[Dict]) -> Dict[str, Any]:
    """Basic position summary."""
    summary = {"total_positions": len(positions), "symbols": []}
    for p in positions:
        sym = p.get("symbol")
        qty = p.get("qty")
        side = p.get("side", "long")
        market_value = float(p.get("market_value", 0))
        summary["symbols"].append({"symbol": sym, "qty": qty, "side": side, "market_value": market_value})
    return summary

def get_regime_recommendation(regime_name: str) -> Dict[str, Any]:
    """Map HMM regime to posture (from trading_agent.md)."""
    mapping = {
        "Normal Bull": {"posture": "Growth + Wheel", "risk": "medium-high", "focus": "Maximize QQQ alpha via CSPs and calls"},
        "Elevated Risk + Bull Trend": {"posture": "Selective long gamma + income", "risk": "medium", "focus": "Tilt to QQQ outperformance"},
        "High Geo Stress": {"posture": "Defensive", "risk": "low", "focus": "Credit spreads, reduce size"},
        "Normal Bear": {"posture": "Defensive income", "risk": "low", "focus": "Protect vs QQQ downside"},
        "Transition / Uncertainty": {"posture": "Reduce new risk", "risk": "very low", "focus": "Wait for clarity"},
    }
    return mapping.get(regime_name, {"posture": "Neutral", "risk": "medium", "focus": "Monitor and align to QQQ alpha"})


def get_underlying_price(symbol: str) -> float:
    bars = get_bars(symbol, limit=1) or fetch_historical_bars(symbol, days_back=5)
    if bars:
        return float(bars[-1].get("c", 0))
    return 0.0


def select_best_contract(underlying: str, opt_type: str = "put", otm_pct: float = 0.12,
                         dte_min: int = 25, dte_max: int = 60, min_premium: float = 1.0,
                         max_candidates: int = 5) -> Optional[Dict]:
    """Dynamically pick the best option contract from chain (robust to quote 404s).
    Falls back to chain close_price. Scores on premium/yield/OI/DTE/strike distance.
    """
    from datetime import date, timedelta
    spot = get_underlying_price(underlying)
    if spot <= 0:
        spot = 740.0 if underlying == "QQQ" else 200.0
    target_strike = spot * (1 - otm_pct) if opt_type == "put" else spot * (1 + otm_pct)

    chain = get_option_chain(underlying, dte_min=dte_min, dte_max=dte_max,
                             opt_type=opt_type, strike_gte=target_strike*0.65, strike_lte=target_strike*1.35, limit=50)
    if not chain:
        chain = get_option_chain(underlying, dte_min=dte_min, dte_max=dte_max, opt_type=opt_type, limit=30)

    candidates = []
    today = date.today()
    for c in chain[:max_candidates*3]:
        try:
            strike = float(c.get("strike_price", 0))
            exp_date = c.get("expiration_date")
            if not exp_date: continue
            exp = date.fromisoformat(exp_date)
            dte = (exp - today).days
            if dte < dte_min or dte > dte_max: continue

            contract = c.get("symbol")
            # Try live quote, fallback to chain close_price
            bid, ask = get_option_quote(contract)
            mid = (bid + ask) / 2 if bid and ask else (bid or ask or 0)
            if mid < 0.01:
                # fallback
                cp = c.get("close_price")
                mid = float(cp) if cp and float(cp) > 0 else 0.0
            if mid < min_premium * 0.6:  # relax a bit for fallback
                continue

            collateral = strike * 100
            yield_pct = (mid * 100 / collateral) * 100 if collateral > 0 else 0
            oi = int(c.get("open_interest", 0) or 0)
            strike_dist = abs(strike - target_strike) / max(spot, 1)
            dte_score = 1 - abs(dte - (dte_min + dte_max)/2) / max((dte_max - dte_min), 1)

            score = (yield_pct * 0.35 + min(oi / 50, 8) * 0.25 + (1 - min(strike_dist, 0.3)) * 0.25 + dte_score * 0.15)
            candidates.append({
                "contract": contract,
                "underlying": underlying,
                "strike": strike,
                "expiry": exp_date,
                "dte": dte,
                "bid": bid,
                "ask": ask,
                "mid": round(mid, 2),
                "current_premium": round(mid, 2),
                "open_interest": oi,
                "yield_pct": round(yield_pct, 3),
                "score": round(score, 3),
                "type": "CSP" if opt_type == "put" else "CALL",
                "rationale": f"Dynamic: ~{otm_pct*100:.0f}% OTM, {dte}d, prem ${mid:.2f} (y {yield_pct:.2f}%)"
            })
        except Exception:
            continue

    if not candidates:
        return None
    best = max(candidates, key=lambda x: x.get("score", 0))
    logger.info(f"Selected best {opt_type} {underlying}: {best['contract']} score={best.get('score')}")
    return best

def propose_csp_trades(positions: List[Dict], regime: Dict, min_premium: float = 1.50) -> List[Dict]:
    """Propose CSPs using dynamic best-contract selection (no fixed strikes)."""
    proposals = []
    held = {p["symbol"] for p in positions}
    # Dynamic targets based on regime — focus on high-conviction underlyings or wheel names
    targets = ["QQQ", "NVDA", "AMZN", "SPY"] if "Bull" in regime.get("regime_name", "") else ["QQQ", "SPY"]
    for sym in targets:
        if sym in held:
            continue
        otm = 0.10 if "Bull" in regime.get("regime_name", "") else 0.15
        best = select_best_contract(sym, opt_type="put", otm_pct=otm, min_premium=min_premium)
        if best:
            best["regime"] = regime.get("regime_name")
            proposals.append(best)
    return proposals[:3]

def propose_qqq_calls(positions: List[Dict], regime: Dict) -> List[Dict]:
    """Propose QQQ call using dynamic selection."""
    has_qqq_call = any("QQQ" in str(p.get("symbol", "")) and p.get("side") == "long" for p in positions)
    if has_qqq_call:
        return []
    rec = get_regime_recommendation(regime.get("regime_name", ""))
    if "Growth" in rec.get("posture", "") or "Bull" in rec.get("posture", ""):
        best = select_best_contract("QQQ", opt_type="call", otm_pct=0.02, dte_min=10, dte_max=20, min_premium=0.5)
        if best:
            best["qty"] = QQQ_CALL_TARGET.get("qty", 1)
            return [best]
    return []

def pre_close_review(context: Dict) -> List[Dict]:
    """~3:15 PM ET pre-close logic stub."""
    logger.info("=== Pre-Close Review (~3:15 PM ET) ===")
    actions = []
    alpha = context.get("qqq_alpha", 0)
    if alpha < -0.5:
        actions.append({"action": "HEDGE_REVIEW", "note": "Consider reducing size or adding hedge before close"})
    else:
        actions.append({"action": "MONITOR", "note": "Watch institutional flows in final hour"})
    return actions

def run_trading_cycle(context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main trading cycle. Accepts optional research context."""
    context = context or {}
    logger.info("=== Trading Agent Started (PAPER TRADING ONLY) | Cycle: %s ===", context.get("cycle", "unknown"))
    logger.info("DRY_RUN=%s", DRY_RUN)

    if not PAPER_TRADING_ONLY:
        return {"status": "blocked", "reason": "LIVE_TRADING_DISABLED"}

    market_status = {"is_open": False, "note": "unknown"}
    orders_submitted = 0

    try:
        if get_market_status:
            market_status = get_market_status()
            logger.info("Market: %s", market_status.get("note"))

        account = get_account()
        equity = float(account.get("equity", 0))
        bp = float(account.get("buying_power", 0))
        logger.info(f"Equity: ${equity:,.2f} | BP: ${bp:,.2f}")

        if equity < ACCOUNT_FLOOR:
            logger.warning("Below $80k floor — pausing new positions")
            return {"status": "paused", "reason": "Below floor", "equity": equity}

        positions = get_positions()
        pos_summary = analyze_positions(positions)
        logger.info(f"Managing {pos_summary['total_positions']} positions")

        qqq_price = get_current_qqq_price()
        qqq_alpha = calculate_qqq_alpha(equity, qqq_price)
        logger.info(f"QQQ Alpha: {qqq_alpha}%")

        regime = context.get("regime", {"regime_name": "Unknown"})
        rec = get_regime_recommendation(regime.get("regime_name", "Unknown"))
        logger.info(f"Regime: {regime.get('regime_name')} → Posture: {rec['posture']}")

        # Propose actions
        csp_proposals = propose_csp_trades(positions, regime)
        call_proposals = propose_qqq_calls(positions, regime)
        preclose_actions = pre_close_review(context) if context.get("cycle") == "pre_close" else []

        logger.info("Proposals — CSPs: %d, QQQ Calls: %d, PreClose: %d",
                    len(csp_proposals), len(call_proposals), len(preclose_actions))

        # === Real dynamic pricing + controlled paper execution ===
        priced_csps = [price_proposal(p) for p in csp_proposals]
        priced_calls = [price_proposal(p) for p in call_proposals]

        for p in priced_csps + priced_calls:
            prem = p.get("current_premium", p.get("mid", 0)) or 0
            logger.info(f"Proposal {p.get('type', p.get('contract'))} prem~${prem:.2f} (score {p.get('score', '?')})")

        if priced_csps and not DRY_RUN and market_status.get("is_open", False):
            for p in priced_csps:
                prem = p.get("current_premium") or p.get("mid") or p.get("bid") or 0
                contract = p.get("contract")
                if contract and prem >= 1.0:
                    order = enhanced_submit_order(contract, 1, "sell", limit_price=prem, position_intent="sell_to_open")
                    if order:
                        orders_submitted += 1
                        logger.info(f"Submitted dynamic CSP: {contract}")

        if priced_calls and not DRY_RUN and market_status.get("is_open", False):
            for p in priced_calls:
                prem = p.get("current_premium") or p.get("ask") or p.get("mid") or 0
                contract = p.get("contract")
                if contract and prem > 0.3:
                    order = enhanced_submit_order(contract, p.get("qty", 1), "buy", limit_price=prem, position_intent="buy_to_open")
                    if order:
                        orders_submitted += 1
                        logger.info(f"Submitted dynamic call: {contract}")

        # Pre-close specific
        for act in preclose_actions:
            logger.info(f"Pre-close action: {act}")

        result = {
            "status": "success",
            "equity": equity,
            "qqq_alpha": qqq_alpha,
            "positions_count": len(positions),
            "regime": regime.get("regime_name"),
            "posture": rec["posture"],
            "proposals": {"csps": csp_proposals, "qqq_calls": call_proposals, "pre_close": preclose_actions},
            "orders_submitted": orders_submitted,
            "market_open": market_status.get("is_open"),
        }

        logger.info("Trading cycle completed (paper only)")
        return result

    except Exception as e:
        logger.error(f"Trading error: {e}")
        return {"status": "error", "error": str(e)}


# ------------------------------------------------------------------
# Option Pricing & Chain Helpers (ported/adapted from legacy)
# ------------------------------------------------------------------

def get_option_quote(contract_symbol: str):
    """Return (bid, ask) for an option contract or (None, None)."""
    try:
        url = f"{ALPACA_DATA_BASE}/options/quotes/latest"
        resp = requests.get(url, headers=HEADERS, params={"symbols": contract_symbol}, timeout=10)
        resp.raise_for_status()
        q = resp.json().get("quotes", {}).get(contract_symbol, {})
        bid = q.get("bp")
        ask = q.get("ap")
        return (float(bid) if bid is not None else None, float(ask) if ask is not None else None)
    except Exception as e:
        logger.warning(f"Option quote failed for {contract_symbol}: {e}")
        return None, None

def build_contract_symbol(underlying: str, expiry: str, strike: float, opt_type: str = "P") -> str:
    """Build OCC-style contract symbol e.g. NVDA260718P00190000"""
    # expiry YYYY-MM-DD -> YYMMDD
    exp = expiry.replace("-", "")[2:]  # 260718
    strike_str = f"{int(strike * 1000):08d}"
    return f"{underlying}{exp}{opt_type}{strike_str}"

def get_option_chain(underlying: str, dte_min: int = 25, dte_max: int = 60, opt_type: str = "put", strike_gte: float = None, strike_lte: float = None, limit: int = 20):
    """Fetch option contracts for underlying."""
    from datetime import date, timedelta
    today = date.today()
    gte = (today + timedelta(days=dte_min)).isoformat()
    lte = (today + timedelta(days=dte_max)).isoformat()
    params = {
        "underlying_symbols": underlying,
        "type": opt_type,
        "expiration_date_gte": gte,
        "expiration_date_lte": lte,
        "limit": limit,
    }
    if strike_gte:
        params["strike_price_gte"] = strike_gte
    if strike_lte:
        params["strike_price_lte"] = strike_lte
    try:
        resp = requests.get(f"{ALPACA_BASE}/options/contracts", headers=HEADERS, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json().get("option_contracts", [])
    except Exception as e:
        logger.warning(f"Chain fetch failed for {underlying}: {e}")
        return []

def price_proposal(proposal: Dict) -> Dict:
    """Enhance proposal with latest quote if not already priced by dynamic selector."""
    if proposal.get("mid") is None or proposal.get("current_premium", 0) == 0:
        contract = proposal.get("contract")
        if not contract and proposal.get("symbol") and proposal.get("strike") and proposal.get("expiry"):
            opt_type = "P" if proposal.get("type") == "CSP" else "C"
            contract = build_contract_symbol(proposal["symbol"], proposal["expiry"], float(proposal["strike"]), opt_type)
            proposal["contract"] = contract
        if contract:
            bid, ask = get_option_quote(contract)
            mid = (bid + ask)/2 if bid and ask else (bid or ask or 0)
            proposal["bid"] = bid
            proposal["ask"] = ask
            proposal["mid"] = mid
            proposal["current_premium"] = mid
    return proposal

def enhanced_submit_order(symbol: str, qty: float, side: str, type_: str = "limit", 
                          limit_price: Optional[float] = None, position_intent: Optional[str] = None) -> Optional[Dict]:
    """Extended submit for stocks and options (paper only)."""
    if not PAPER_TRADING_ONLY:
        logger.critical("LIVE TRADING ATTEMPT BLOCKED")
        return None
    if DRY_RUN:
        logger.info(f"[DRY_RUN] Would submit {side} {qty} {symbol} @ {limit_price}")
        return {"id": "dry-run", "symbol": symbol, "side": side, "qty": qty, "limit_price": limit_price}

    payload = {
        "symbol": symbol,
        "qty": str(qty),
        "side": side,
        "type": type_,
        "time_in_force": "day",
    }
    if limit_price:
        payload["limit_price"] = str(round(limit_price, 2))
    if position_intent:
        payload["position_intent"] = position_intent

    logger.info(f"Submitting PAPER order: {side} {qty} {symbol} limit {limit_price} intent {position_intent}")
    try:
        resp = requests.post(f"{ALPACA_BASE}/orders", headers=HEADERS, json=payload, timeout=10)
        if resp.status_code in (200, 201):
            order = resp.json()
            logger.info(f"Order accepted: {order.get("id")}")
            return order
        else:
            logger.error(f"Order failed {resp.status_code}: {resp.text[:200]}")
            return None
    except Exception as e:
        logger.error(f"Submit error: {e}")
        return None


if __name__ == "__main__":
    result = run_trading_cycle({"cycle": "open", "regime": {"regime_name": "Normal Bull"}})
    print("Result:", result)
