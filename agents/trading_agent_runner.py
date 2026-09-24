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
                        start_equity: float = 100000.0, start_qqq: float = 694.94) -> float:
    """Secondary benchmark alpha vs QQQ (real start close 2026-05-07). Prefer calculate_dual_alpha."""
    try:
        from strategy_lib import calculate_benchmark_alphas, load_benchmarks
        b = load_benchmarks()
        # spy unused here — pass qqq as both if only one price available
        return calculate_benchmark_alphas(equity, float(b.get("spy_start", 731.53)), qqq_price)["qqq_alpha"]
    except Exception:
        acct_ret = (equity - start_equity) / start_equity * 100
        qqq_ret = (qqq_price - start_qqq) / start_qqq * 100
        return round(acct_ret - qqq_ret, 2)


def calculate_dual_alpha(equity: float, spy_price: float, qqq_price: float) -> Dict[str, float]:
    from strategy_lib import calculate_benchmark_alphas
    return calculate_benchmark_alphas(equity, spy_price, qqq_price)


def get_current_spy_price() -> float:
    bars = get_bars("SPY", limit=1)
    if bars:
        return float(bars[-1].get("c", 750.0))
    return 750.0

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
                         max_candidates: int = 12, high_vol: bool = False) -> Optional[Dict]:
    """Dynamically pick the best option contract from chain (robust to quote 404s).
    Falls back to chain close_price. Scores on premium/yield/OI/DTE/strike distance.
    high_vol: prefer richer premium / slightly wider search for income harvest.
    """
    from datetime import date, timedelta
    spot = get_underlying_price(underlying)
    if spot <= 0:
        spot = 740.0 if underlying == "QQQ" else 200.0
    target_strike = spot * (1 - otm_pct) if opt_type == "put" else spot * (1 + otm_pct)

    chain = get_option_chain(underlying, dte_min=dte_min, dte_max=dte_max,
                             opt_type=opt_type, strike_gte=target_strike*0.65, strike_lte=target_strike*1.35, limit=80)
    if not chain:
        chain = get_option_chain(underlying, dte_min=dte_min, dte_max=dte_max, opt_type=opt_type, limit=50)

    # Prefer liquid names first so we don't score dead contracts only
    try:
        chain = sorted(chain, key=lambda c: int(c.get("open_interest") or 0), reverse=True)
    except Exception:
        pass

    candidates = []
    today = date.today()
    min_floor = min_premium * (0.5 if high_vol else 0.6)
    for c in chain[: max(max_candidates * 4, 40)]:
        try:
            strike = float(c.get("strike_price", 0))
            exp_date = c.get("expiration_date")
            if not exp_date: continue
            exp = date.fromisoformat(exp_date)
            dte = (exp - today).days
            if dte < dte_min or dte > dte_max: continue

            # Never sell ITM premium as a "CSP" / long call — require OTM cushion
            if opt_type == "put":
                min_otm = max(otm_pct * 0.5, 0.05)   # at least ~5% OTM
                max_otm = max(otm_pct * 2.0, 0.22)  # not absurdly far
                if strike >= spot * (1.0 - min_otm):
                    continue
                if strike < spot * (1.0 - max_otm):
                    continue
            else:
                min_otm = max(otm_pct * 0.5, 0.01)
                max_otm = max(otm_pct * 2.5, 0.08)
                if strike <= spot * (1.0 + min_otm):
                    continue
                if strike > spot * (1.0 + max_otm):
                    continue

            contract = c.get("symbol")
            # Try live quote, fallback to chain close_price
            bid, ask = get_option_quote(contract)
            mid = (bid + ask) / 2 if bid and ask else (bid or ask or 0)
            if mid < 0.01:
                # fallback
                cp = c.get("close_price")
                mid = float(cp) if cp and float(cp) > 0 else 0.0
            if mid < min_floor:
                continue
            # Cap absurd premiums (likely mis-marked ITM leakage)
            if opt_type == "put" and mid > max(min_premium * 8, spot * 0.08):
                continue

            collateral = strike * 100
            yield_pct = (mid * 100 / collateral) * 100 if collateral > 0 else 0
            oi = int(c.get("open_interest", 0) or 0)
            strike_dist = abs(strike - target_strike) / max(spot, 1)
            dte_score = 1 - abs(dte - (dte_min + dte_max)/2) / max((dte_max - dte_min), 1)

            # High-vol: overweight premium/yield so we actually monetize IV — but still OTM
            if high_vol:
                score = (yield_pct * 0.40 + min(mid, 6) * 0.12 + min(oi / 50, 8) * 0.22
                         + (1 - min(strike_dist, 0.3)) * 0.16 + dte_score * 0.10)
            else:
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
                    + (" [high-vol harvest]" if high_vol else ""),
                "high_vol": high_vol,
                "spot": round(spot, 2),
            })
        except Exception:
            continue

    if not candidates:
        return None
    best = max(candidates, key=lambda x: x.get("score", 0))
    logger.info(f"Selected best {opt_type} {underlying}: {best['contract']} score={best.get('score')}")
    return best

def propose_csp_trades(positions: List[Dict], regime: Dict, min_premium: float = 1.50,
                       account: Optional[Dict] = None) -> tuple:
    """Propose CSPs using config universe. Holding equity does NOT block CSPs.
    Returns (proposals, skips).
    """
    from strategy_lib import (
        load_strategy_config, short_put_underlyings, otm_for_regime,
        can_afford_csp_cash_secured, regime_is_elevated_vol,
    )
    cfg = load_strategy_config()
    proposals: List[Dict] = []
    skips: List[Dict] = []
    min_premium = float(cfg.get("csp_min_premium", min_premium))
    dte_min = int(cfg.get("csp_dte_min", 21))
    dte_max = int(cfg.get("csp_dte_max", 45))
    max_new = int(cfg.get("csp_max_new_contracts_per_day", 2))
    universe = list(cfg.get("csp_universe") or ["NVDA", "AMZN", "QQQ", "SPY"])
    already_short = short_put_underlyings(positions)
    regime_name = regime.get("regime_name", "")
    high_vol = regime_is_elevated_vol(regime_name)
    if high_vol:
        # Harvest elevated IV: slightly wider DTE band + softer min premium
        dte_min = max(14, dte_min - 7)
        dte_max = min(60, dte_max + 10)
        min_premium = max(0.5, min_premium * float(cfg.get("csp_high_vol_min_premium_scale", 0.85)))
    otm = otm_for_regime(regime_name)

    for sym in universe:
        if sym in already_short:
            skips.append({"code": "MAX_POSITION", "detail": f"Already short put on {sym}"})
            continue
        best = select_best_contract(
            sym, opt_type="put", otm_pct=otm, dte_min=dte_min, dte_max=dte_max,
            min_premium=min_premium, high_vol=high_vol,
        )
        if not best:
            skips.append({"code": "NO_CHAIN", "detail": f"No viable put chain for {sym}"})
            continue
        if account is not None:
            ok, reason, need = can_afford_csp_cash_secured(
                account, best["strike"], qty=1, positions=positions,
            )
            if not ok:
                skips.append({
                    "code": reason,
                    "detail": f"{sym} strike {best['strike']} needs ~${need:,.0f} cash-secured "
                              f"(after existing short collateral)",
                })
                continue
            best["affordability"] = reason
        best["regime"] = regime_name
        best["high_vol"] = high_vol
        proposals.append(best)
        if len(proposals) >= max_new:
            break
    return proposals[:max_new], skips

def propose_qqq_calls(positions: List[Dict], regime: Dict) -> tuple:
    """Propose QQQ call using OCC call detection (equity shares do not block)."""
    from strategy_lib import has_long_qqq_call, regime_is_bull, regime_is_elevated_vol, load_strategy_config
    skips: List[Dict] = []
    cfg = load_strategy_config()
    yolo = bool(cfg.get("yolo_max_value"))
    if has_long_qqq_call(positions):
        skips.append({"code": "MAX_POSITION", "detail": "Already long QQQ call option"})
        return [], skips
    regime_name = regime.get("regime_name", "")
    # Test window: chase account value, not the bear-regime call ban.
    if not yolo and regime_is_elevated_vol(regime_name):
        skips.append({
            "code": "REGIME_BLOCK",
            "detail": f"No QQQ long calls in elevated/stress regime {regime_name} — harvest CSPs instead",
        })
        return [], skips
    rec = get_regime_recommendation(regime_name)
    if not yolo and not (regime_is_bull(regime_name) or "Growth" in rec.get("posture", "")):
        skips.append({"code": "REGIME_BLOCK", "detail": f"No QQQ calls in regime {regime_name}"})
        return [], skips
    best = select_best_contract("QQQ", opt_type="call", otm_pct=0.02, dte_min=10, dte_max=20, min_premium=0.5)
    if best:
        best["qty"] = QQQ_CALL_TARGET.get("qty", 1)
        return [best], skips
    skips.append({"code": "NO_CHAIN", "detail": "No viable QQQ call"})
    return [], skips


def propose_manage_actions(positions: List[Dict]) -> List[Dict]:
    """Profit-take / defensive loss cut / expiry manage for short options.

    Critical: underwater shorts must not sit unmanaged until DTE force while
    capital is frozen and vol is elevated. DEFENSIVE_CLOSE frees collateral
    so the same cycle can re-sell richer premium.
    """
    from strategy_lib import (
        load_strategy_config, is_option_symbol, option_profit_pct_short,
        option_adverse_multiple, dte_from_occ, parse_occ,
    )
    cfg = load_strategy_config()
    pt = float(cfg.get("profit_take_pct", 0.50))
    dte_force = int(cfg.get("manage_dte_force", 7))
    dte_hard = int(cfg.get("manage_dte_hard", 2))
    loss_cut = float(cfg.get("manage_loss_cut_pct", 0.75))  # close if profit <= -loss_cut
    adv_mult = float(cfg.get("manage_adverse_multiple", 1.6))  # close if mark >= mult * credit
    defensive_on = bool(cfg.get("manage_defensive_enabled", True))
    actions: List[Dict] = []
    for p in positions:
        sym = str(p.get("symbol", ""))
        if not is_option_symbol(sym):
            continue
        qty = float(p.get("qty", 0) or 0)
        side = (p.get("side") or "").lower()
        is_short = qty < 0 or side == "short"
        if not is_short:
            continue
        close_qty = abs(int(qty))
        profit = option_profit_pct_short(p)
        adverse = option_adverse_multiple(p)
        dte = dte_from_occ(sym)
        cur = float(p.get("current_price") or 0)
        entry = float(p.get("avg_entry_price") or 0)
        # Buy-to-close: slightly above mark for fill (more aggressive when losing)
        if cur > 0:
            if profit is not None and profit < 0:
                limit = round(max(cur * 1.08, cur + 0.10), 2)  # pay up to exit damaged short
            else:
                limit = round(max(cur * 1.05, cur + 0.05), 2)
        else:
            limit = None

        if profit is not None and profit >= pt:
            actions.append({
                "action": "PROFIT_TAKE",
                "type": "MANAGE",
                "contract": sym,
                "qty": close_qty,
                "side": "buy",
                "position_intent": "buy_to_close",
                "limit_price": limit,
                "profit_pct": round(profit * 100, 1),
                "entry": entry,
                "current": cur,
                "rationale": f"Short option +{profit*100:.0f}% >= {pt*100:.0f}% profit-take",
            })
            continue

        # Defensive: cut when vol/underlying moved hard against short premium
        if defensive_on:
            hit_loss = profit is not None and profit <= -abs(loss_cut)
            hit_adv = adverse is not None and adverse >= adv_mult
            if hit_loss or hit_adv:
                adv_s = f"{adverse:.2f}" if adverse is not None else "n/a"
                pnl_s = f"{((profit or 0) * 100):.0f}"
                actions.append({
                    "action": "DEFENSIVE_CLOSE",
                    "type": "MANAGE",
                    "contract": sym,
                    "qty": close_qty,
                    "side": "buy",
                    "position_intent": "buy_to_close",
                    "limit_price": limit,
                    "profit_pct": round((profit or 0) * 100, 1),
                    "adverse_multiple": round(adverse, 2) if adverse is not None else None,
                    "entry": entry,
                    "current": cur,
                    "dte": dte,
                    "rationale": (
                        f"DEFENSIVE: mark {cur:.2f} vs credit {entry:.2f} "
                        f"(mult={adv_s}, pnl={pnl_s}%) "
                        f"— free collateral / stop premium bleed in high vol"
                    ),
                })
                continue

        if dte is not None and dte <= dte_hard:
            actions.append({
                "action": "EXPIRY_CLOSE",
                "type": "MANAGE",
                "contract": sym,
                "qty": close_qty,
                "side": "buy",
                "position_intent": "buy_to_close",
                "limit_price": limit,
                "dte": dte,
                "rationale": f"DTE={dte} <= hard {dte_hard} — close",
            })
        elif dte is not None and dte <= dte_force:
            actions.append({
                "action": "EXPIRY_REVIEW",
                "type": "MANAGE",
                "contract": sym,
                "qty": close_qty,
                "side": "buy",
                "position_intent": "buy_to_close",
                "limit_price": limit,
                "dte": dte,
                "profit_pct": round((profit or 0) * 100, 1),
                "rationale": f"DTE={dte} <= force {dte_force} — close to free capital for wheel",
            })
    return actions

def csp_sell_limit(proposal: Dict, cfg: Dict) -> float:
    """Limit for sell-to-open: slightly below mid in high vol to improve fill rate
    while still harvesting elevated premium (passive mid limits often day-expire).
    """
    mid = float(proposal.get("current_premium") or proposal.get("mid") or 0)
    bid = proposal.get("bid")
    high_vol = bool(proposal.get("high_vol"))
    yld = float(proposal.get("yield_pct") or 0)
    if yld >= float(cfg.get("csp_high_vol_yield_pct", 0.6)):
        high_vol = True
    frac = float(cfg.get("csp_high_vol_sell_limit_frac" if high_vol else "csp_sell_limit_frac", 0.92))
    if mid <= 0 and bid:
        mid = float(bid)
    limit = mid * frac
    if bid is not None:
        try:
            # Never go below bid for a sell (would be marketable worse than necessary)
            # Actually for faster fill we WANT near bid: clamp between bid and mid
            b = float(bid)
            if b > 0:
                limit = max(b, min(limit, mid) if mid > 0 else b)
        except Exception:
            pass
    return round(max(limit, 0.05), 2)

def pre_close_review(context: Dict) -> List[Dict]:
    """~3:15 PM ET pre-close review. Expanded for institutional flows, positions, regime."""
    logger.info("=== Pre-Close Review (~3:15 PM ET) ===")
    actions = []
    alpha = context.get("qqq_alpha", 0)
    spy_alpha = context.get("spy_alpha", 0)
    regime = context.get("regime", {}).get("regime_name", "")
    positions = context.get("positions", []) or []
    news = context.get("news", []) or []

    # Core logic — account-value goal, not SPY lag
    actions.append({"action": "MONITOR", "note": "Test goal is $110k by 2026-11-30. SPCX is blocked. Deploy recovered cash."})
    for p in positions:
        if not isinstance(p, dict):
            continue
        sym = str(p.get("symbol", ""))
        from strategy_lib import is_option_symbol, option_profit_pct_short, option_adverse_multiple
        if is_option_symbol(sym):
            pr = option_profit_pct_short(p)
            adv = option_adverse_multiple(p)
            if (pr is not None and pr < -0.4) or (adv is not None and adv >= 1.4):
                actions.append({
                    "action": "SHORT_OPTION_STRESS",
                    "note": f"{sym} underwater pnl={((pr or 0)*100):.0f}% mult={adv} — defensive manage priority",
                })
    for p in positions[:3]:
        sym = p.get("symbol") if isinstance(p, dict) else str(p)[:4]
        if sym:
            actions.append({"action": "FLOW_CHECK", "note": f"Monitor {sym} volume/flows into close"})

    # News tie-in
    geo_keywords = ["Iran", "Middle East", "geopolitical", "war", "truce"]
    if any(any(kw.lower() in str(n).lower() for kw in geo_keywords) for n in news):
        actions.append({"action": "GEO_MONITOR", "note": "Geopolitical news active — watch energy/defense names and oil"})

    # Always log
    logger.info(f"Pre-close actions generated: {len(actions)}")
    return actions

def run_trading_cycle(context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Main trading cycle. Manage open options first (incl defensive), refresh, then CSPs."""
    context = context or {}
    logger.info("=== Trading Agent Started (PAPER TRADING ONLY) | Cycle: %s ===", context.get("cycle", "unknown"))
    logger.info("DRY_RUN=%s", DRY_RUN)

    if not PAPER_TRADING_ONLY:
        return {"status": "blocked", "reason": "LIVE_TRADING_DISABLED"}

    market_status = {"is_open": False, "note": "unknown"}
    orders_submitted = 0
    skips: List[Dict] = []
    actions_log: List[str] = []
    notes: List[str] = []
    manage_actions: List[Dict] = []
    csp_proposals: List[Dict] = []
    call_proposals: List[Dict] = []
    priced_csps: List[Dict] = []
    priced_calls: List[Dict] = []
    preclose_actions: List[Dict] = []

    try:
        from strategy_lib import load_strategy_config, reserved_short_put_collateral
        from cycle_logger import write_cycle_log

        cfg = load_strategy_config()
        if get_market_status:
            market_status = get_market_status()
            logger.info("Market: %s", market_status.get("note"))

        account = get_account()
        equity = float(account.get("equity", 0))
        bp = float(account.get("buying_power", 0))
        opt_bp = float(account.get("options_buying_power", 0) or 0)
        cash = float(account.get("cash", 0) or 0)
        logger.info(f"Equity: ${equity:,.2f} | Cash: ${cash:,.2f} | Total BP: ${bp:,.2f} | Options BP: ${opt_bp:,.2f}")

        if equity < float(cfg.get("account_floor", ACCOUNT_FLOOR)):
            logger.warning("Below $80k floor — pausing new positions (manage still allowed)")
            notes.append("FLOOR: new risk paused; manage-only")

        positions = get_positions()
        reserved = reserved_short_put_collateral(positions)
        notes.append(f"Reserved short-put collateral ~${reserved:,.0f}")
        pos_summary = analyze_positions(positions)
        logger.info(f"Managing {pos_summary['total_positions']} positions | reserved CSP collateral ~${reserved:,.0f}")

        qqq_price = get_current_qqq_price()
        spy_price = get_current_spy_price()
        dual = calculate_dual_alpha(equity, spy_price, qqq_price)
        spy_alpha = dual["spy_alpha"]
        qqq_alpha = dual["qqq_alpha"]
        logger.info(
            "Alphas — SPY(primary)=%s%% QQQ(secondary)=%s%% | acct=%s%%",
            spy_alpha, qqq_alpha, dual["account_return_pct"],
        )

        regime = context.get("regime", {"regime_name": "Unknown"})
        rec = get_regime_recommendation(regime.get("regime_name", "Unknown"))
        logger.info(f"Regime: {regime.get('regime_name')} → Posture: {rec['posture']}")

        market_open = bool(market_status.get("is_open", False))
        floor_hit = equity < float(cfg.get("account_floor", ACCOUNT_FLOOR))

        # ------------------------------------------------------------------
        # 1) MANAGE FIRST — profit-take, defensive loss, expiry
        # ------------------------------------------------------------------
        manage_actions = propose_manage_actions(positions)
        logger.info("Manage actions: %d", len(manage_actions))

        MANAGE_EXECUTE = ("PROFIT_TAKE", "EXPIRY_CLOSE", "EXPIRY_REVIEW", "DEFENSIVE_CLOSE")
        if manage_actions and not DRY_RUN and market_open:
            for m in manage_actions:
                if m.get("action") not in MANAGE_EXECUTE:
                    continue
                contract = m["contract"]
                qty = m["qty"]
                limit = m.get("limit_price")
                order = enhanced_submit_order(
                    contract, qty, "buy", type_="limit" if limit else "market",
                    limit_price=limit, position_intent="buy_to_close",
                )
                if order:
                    orders_submitted += 1
                    actions_log.append(
                        f"buy_to_close {contract} x{qty} @ {limit} [{m.get('action')}] id={order.get('id')}"
                    )
                    logger.info("Submitted manage %s %s", m.get("action"), contract)
                else:
                    skips.append({"code": "SUBMIT_FAIL", "detail": f"manage {contract} {m.get('action')}"})
        elif manage_actions and DRY_RUN:
            for m in manage_actions:
                actions_log.append(f"[DRY_RUN] {m.get('action')} {m.get('contract')} x{m.get('qty')} @ {m.get('limit_price')}")
        elif manage_actions and not market_open:
            for m in manage_actions:
                notes.append(f"MANAGE_QUEUED (market closed): {m.get('action')} {m.get('contract')} — {m.get('rationale')}")

        # Refresh book after manage so CSP can use freed names + collateral
        MANAGE_EXECUTE = ("PROFIT_TAKE", "EXPIRY_CLOSE", "EXPIRY_REVIEW", "DEFENSIVE_CLOSE")
        managed_contracts = {
            m.get("contract") for m in manage_actions if m.get("action") in MANAGE_EXECUTE and m.get("contract")
        }
        if managed_contracts and (orders_submitted > 0 or DRY_RUN):
            try:
                if DRY_RUN and orders_submitted == 0:
                    # Simulate closes so CSP phase sees freed underlyings/collateral
                    positions = [p for p in positions if str(p.get("symbol")) not in managed_contracts]
                    notes.append(f"Simulated close after manage: {sorted(managed_contracts)}")
                else:
                    positions = get_positions()
                    account = get_account()
                    cash = float(account.get("cash", 0) or 0)
                    equity = float(account.get("equity", 0) or equity)
                    opt_bp = float(account.get("options_buying_power", 0) or 0)
                    notes.append("Refreshed positions/account after manage phase")
            except Exception as e:
                logger.warning("Post-manage refresh failed: %s", e)

        # ------------------------------------------------------------------
        # 2) CSPs — cash secured, collateral-aware, high-vol aggressive limits
        # ------------------------------------------------------------------
        if floor_hit:
            csp_proposals, csp_skips = [], [{"code": "FLOOR", "detail": "Equity below floor — no new CSPs"}]
        else:
            csp_proposals, csp_skips = propose_csp_trades(positions, regime, account=account)
        skips.extend(csp_skips)

        # 3) QQQ calls
        call_proposals, call_skips = propose_qqq_calls(positions, regime)
        skips.extend(call_skips)

        preclose_actions = pre_close_review({**context, "positions": positions, "qqq_alpha": qqq_alpha, "spy_alpha": spy_alpha}) if context.get("cycle") == "pre_close" else []

        logger.info(
            "Proposals — Manage: %d, CSPs: %d, QQQ Calls: %d, PreClose: %d",
            len(manage_actions), len(csp_proposals), len(call_proposals), len(preclose_actions),
        )

        priced_csps = [price_proposal(p) for p in csp_proposals]
        priced_calls = [price_proposal(p) for p in call_proposals]

        # Execute CSPs with fill-friendly limits in high vol
        if priced_csps and not DRY_RUN and market_open and not floor_hit:
            min_prem = float(cfg.get("csp_min_premium", 1.0))
            for p in priced_csps:
                prem = p.get("current_premium") or p.get("mid") or p.get("bid") or 0
                contract = p.get("contract")
                gate = min_prem * (0.5 if p.get("high_vol") else 0.6)
                if contract and prem >= gate:
                    limit = csp_sell_limit(p, cfg)
                    order = enhanced_submit_order(
                        contract, 1, "sell", limit_price=limit, position_intent="sell_to_open"
                    )
                    if order:
                        orders_submitted += 1
                        actions_log.append(
                            f"sell_csp {contract} @ {limit} (mid={p.get('mid')}, hv={p.get('high_vol')}) id={order.get('id')}"
                        )
                        logger.info(f"Submitted dynamic CSP: {contract} @ {limit}")
                    else:
                        skips.append({"code": "SUBMIT_FAIL", "detail": f"csp {contract}"})
                else:
                    skips.append({"code": "PREMIUM_LOW", "detail": f"{contract} prem={prem}"})
        elif priced_csps and DRY_RUN:
            for p in priced_csps:
                lim = csp_sell_limit(p, cfg)
                actions_log.append(f"[DRY_RUN] sell_csp {p.get('contract')} @ {lim}")
        elif priced_csps and not market_open:
            for p in priced_csps:
                notes.append(f"CSP_QUEUED (market closed): {p.get('contract')} mid={p.get('mid')}")

        # Execute calls (bull only already gated)
        if priced_calls and not DRY_RUN and market_open and not floor_hit:
            for p in priced_calls:
                prem = p.get("current_premium") or p.get("ask") or p.get("mid") or 0
                contract = p.get("contract")
                if contract and prem > 0.3:
                    order = enhanced_submit_order(
                        contract, p.get("qty", 1), "buy", limit_price=prem, position_intent="buy_to_open"
                    )
                    if order:
                        orders_submitted += 1
                        actions_log.append(f"buy_call {contract} id={order.get('id')}")
        elif priced_calls and DRY_RUN:
            for p in priced_calls:
                actions_log.append(f"[DRY_RUN] buy_call {p.get('contract')}")

        for act in preclose_actions:
            logger.info(f"Pre-close action: {act}")
            notes.append(str(act))

        # SPCX sold 2026-09-24. Do not rebuy.

        result = {
            "status": "success",
            "equity": equity,
            "cash": cash,
            "options_buying_power": opt_bp,
            "spy_alpha": spy_alpha,
            "qqq_alpha": qqq_alpha,
            "account_return_pct": dual["account_return_pct"],
            "spy_return_pct": dual["spy_return_pct"],
            "qqq_return_pct": dual["qqq_return_pct"],
            "positions_count": len(positions),
            "regime": regime.get("regime_name"),
            "posture": rec["posture"],
            "proposals": {
                "manage": manage_actions,
                "csps": priced_csps,
                "qqq_calls": priced_calls,
                "pre_close": preclose_actions,
            },
            "skips": skips,
            "actions": actions_log,
            "orders_submitted": orders_submitted,
            "market_open": market_open,
            "notes": notes,
        }

        try:
            paths = write_cycle_log(context.get("cycle", "open"), result)
            result["cycle_log"] = paths
            logger.info("Cycle log written: %s", paths)
        except Exception as e:
            logger.warning("Cycle log failed: %s", e)

        logger.info("Trading cycle completed (paper only) orders=%s", orders_submitted)
        return result

    except Exception as e:
        logger.error(f"Trading error: {e}")
        try:
            from cycle_logger import write_cycle_log
            write_cycle_log(context.get("cycle", "open"), {"status": "error", "error": str(e), "orders_submitted": 0})
        except Exception:
            pass
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
        if "404" not in str(e):
            logger.warning(f"Option quote failed for {contract_symbol}: {e}")
        else:
            logger.debug(f"Option quote 404 (inactive/expired) for {contract_symbol}")
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
            logger.info(f"Order accepted: {order.get('id')}")
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
