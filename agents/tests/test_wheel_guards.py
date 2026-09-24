"""Unit tests for wheel guards / strategy_lib (no network)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from strategy_lib import (
    parse_occ,
    has_long_qqq_call,
    short_put_underlyings,
    can_afford_csp_cash_secured,
    calculate_benchmark_alphas,
)


def test_parse_occ_nvda_put():
    o = parse_occ("NVDA260724P00190000")
    assert o is not None
    assert o["underlying"] == "NVDA"
    assert o["is_put"]
    assert o["strike"] == 190.0


def test_qqq_shares_do_not_count_as_call():
    positions = [{"symbol": "QQQ", "qty": "50", "side": "long"}]
    assert has_long_qqq_call(positions) is False


def test_qqq_occ_call_detected():
    positions = [{"symbol": "QQQ260731C00700000", "qty": "1", "side": "long"}]
    assert has_long_qqq_call(positions) is True


def test_short_put_underlyings():
    positions = [
        {"symbol": "NVDA260724P00190000", "qty": "-4", "side": "short"},
        {"symbol": "QQQ", "qty": "50", "side": "long"},
    ]
    assert short_put_underlyings(positions) == {"NVDA"}


def test_cash_secured_afford():
    account = {"cash": 52000}
    ok, reason, need = can_afford_csp_cash_secured(account, 190, 1)
    assert ok is True
    assert reason == "CASH_SECURED"
    assert need == 19000


def test_cash_secured_reject():
    account = {"cash": 10000}
    ok, reason, need = can_afford_csp_cash_secured(account, 190, 1)
    assert ok is False
    assert reason == "LOW_CASH_SECURED"


def test_dual_alpha_spy_primary_math():
    # equity flat, SPY up → negative spy alpha
    r = calculate_benchmark_alphas(100000, spy_price=750, qqq_price=700)
    assert r["account_return_pct"] == 0.0
    assert r["spy_alpha"] < 0
