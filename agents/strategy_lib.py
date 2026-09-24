"""Shared strategy config, benchmarks, alpha, OCC helpers, affordability."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CONFIG_DIR = Path(__file__).parent / "config"
_STRATEGY_CACHE: Optional[Dict[str, Any]] = None
_BENCH_CACHE: Optional[Dict[str, Any]] = None

OCC_RE = re.compile(r"^([A-Z]{1,6})(\d{6})([CP])(\d{8})$")


def load_strategy_config() -> Dict[str, Any]:
    global _STRATEGY_CACHE
    if _STRATEGY_CACHE is not None:
        return _STRATEGY_CACHE
    path = CONFIG_DIR / "strategy_config.json"
    with open(path) as f:
        _STRATEGY_CACHE = json.load(f)
    return _STRATEGY_CACHE


def load_benchmarks() -> Dict[str, Any]:
    global _BENCH_CACHE
    if _BENCH_CACHE is not None:
        return _BENCH_CACHE
    path = CONFIG_DIR / "benchmarks.json"
    with open(path) as f:
        _BENCH_CACHE = json.load(f)
    return _BENCH_CACHE


def reload_configs() -> None:
    global _STRATEGY_CACHE, _BENCH_CACHE
    _STRATEGY_CACHE = None
    _BENCH_CACHE = None


def save_strategy_config(cfg: Dict[str, Any]) -> None:
    path = CONFIG_DIR / "strategy_config.json"
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")
    reload_configs()


def calculate_benchmark_alphas(
    equity: float,
    spy_price: float,
    qqq_price: float,
) -> Dict[str, float]:
    b = load_benchmarks()
    start_eq = float(b.get("account_start_equity", 100000.0))
    spy0 = float(b.get("spy_start", 731.53))
    qqq0 = float(b.get("qqq_start") or 694.94)
    acct_ret = (equity - start_eq) / start_eq * 100
    spy_ret = (spy_price - spy0) / spy0 * 100
    qqq_ret = (qqq_price - qqq0) / qqq0 * 100
    return {
        "account_return_pct": round(acct_ret, 2),
        "spy_return_pct": round(spy_ret, 2),
        "qqq_return_pct": round(qqq_ret, 2),
        "spy_alpha": round(acct_ret - spy_ret, 2),
        "qqq_alpha": round(acct_ret - qqq_ret, 2),
    }


def parse_occ(symbol: str) -> Optional[Dict[str, Any]]:
    m = OCC_RE.match(symbol or "")
    if not m:
        return None
    underlying, yymmdd, cp, strike_raw = m.groups()
    strike = int(strike_raw) / 1000.0
    return {
        "underlying": underlying,
        "yymmdd": yymmdd,
        "right": cp,
        "strike": strike,
        "is_put": cp == "P",
        "is_call": cp == "C",
    }


def is_option_symbol(symbol: str) -> bool:
    return parse_occ(symbol) is not None


def short_put_underlyings(positions: List[Dict]) -> set:
    out = set()
    for p in positions:
        occ = parse_occ(str(p.get("symbol", "")))
        if not occ or not occ["is_put"]:
            continue
        qty = float(p.get("qty", 0) or 0)
        side = (p.get("side") or "").lower()
        if qty < 0 or side == "short":
            out.add(occ["underlying"])
    return out


def has_long_qqq_call(positions: List[Dict]) -> bool:
    for p in positions:
        occ = parse_occ(str(p.get("symbol", "")))
        if not occ or occ["underlying"] != "QQQ" or not occ["is_call"]:
            continue
        qty = float(p.get("qty", 0) or 0)
        side = (p.get("side") or "").lower()
        if qty > 0 or side == "long":
            return True
    return False


def reserved_short_put_collateral(positions: List[Dict]) -> float:
    """Cash already earmarked for open short puts (strike * 100 * qty)."""
    reserved = 0.0
    for p in positions or []:
        occ = parse_occ(str(p.get("symbol", "")))
        if not occ or not occ["is_put"]:
            continue
        qty = float(p.get("qty", 0) or 0)
        side = (p.get("side") or "").lower()
        if qty < 0 or side == "short":
            reserved += float(occ["strike"]) * 100.0 * abs(qty)
    return reserved


def can_afford_csp_cash_secured(
    account: Dict[str, Any],
    strike: float,
    qty: int = 1,
    positions: Optional[List[Dict]] = None,
) -> Tuple[bool, str, float]:
    """Cash-secured only: strike*100*qty <= (cash - reserved_shorts) * haircut.

    Existing short-put collateral must be subtracted or broker rejects with
    SUBMIT_FAIL while cash still looks ample (classic META-after-NVDA failure).
    """
    cfg = load_strategy_config()
    haircut = float(cfg.get("cash_secure_haircut", 0.90))
    cash = float(account.get("cash", 0) or 0)
    reserved = reserved_short_put_collateral(positions or [])
    free_cash = max(cash - reserved, 0.0)
    need = float(strike) * 100.0 * qty
    available = free_cash * haircut
    if available >= need:
        return True, "CASH_SECURED", need
    return False, "LOW_CASH_SECURED", need


def regime_is_bull(regime_name: str) -> bool:
    name = regime_name or ""
    return "Bull" in name and "Bear" not in name


def regime_is_elevated_vol(regime_name: str) -> bool:
    """True when HMM label implies stress / elevated risk (harvest premium)."""
    name = (regime_name or "").lower()
    keys = ("elevated", "risk", "stress", "bear", "uncertainty", "transition", "geo")
    return any(k in name for k in keys)


def otm_for_regime(regime_name: str) -> float:
    cfg = load_strategy_config()
    if regime_is_bull(regime_name) and not regime_is_elevated_vol(regime_name):
        return float(cfg.get("csp_otm_bull", 0.10))
    # Elevated Risk + Bull Trend should still use wider OTM (defensive income)
    if regime_is_elevated_vol(regime_name):
        return float(cfg.get("csp_otm_elevated", cfg.get("csp_otm_bear", 0.14)))
    return float(cfg.get("csp_otm_bear", 0.14))


def option_profit_pct_short(position: Dict) -> Optional[float]:
    """Fraction of credit captured for short option. Positive = winning.

    Prefer mark vs entry: (entry - mark) / entry. Alpaca unrealized_plpc is used
    only as fallback — it can disagree slightly with marks.
    """
    try:
        entry = float(position.get("avg_entry_price") or 0)
        cur = float(position.get("current_price") or 0)
        if entry > 0 and cur > 0:
            return (entry - cur) / entry
        up = position.get("unrealized_plpc")
        if up is not None:
            return float(up)
        return None
    except Exception:
        return None


def option_adverse_multiple(position: Dict) -> Optional[float]:
    """mark / credit for short option. >1 means underwater."""
    try:
        entry = float(position.get("avg_entry_price") or 0)
        cur = float(position.get("current_price") or 0)
        if entry <= 0 or cur <= 0:
            return None
        return cur / entry
    except Exception:
        return None


def dte_from_occ(symbol: str):
    from datetime import date

    occ = parse_occ(symbol)
    if not occ:
        return None
    yymmdd = occ["yymmdd"]
    try:
        exp = date(2000 + int(yymmdd[0:2]), int(yymmdd[2:4]), int(yymmdd[4:6]))
        return (exp - date.today()).days
    except Exception:
        return None
