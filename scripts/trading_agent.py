#!/usr/bin/env python3
"""
trading_agent.py — Rule-based trading agent for GitHub Actions.
No AI API required — executes strategy rules mechanically.

Sessions:
  open   — Layer 1 rebalance + open new CSPs
  midday — Profit takes, 50% CSP closes, stop checks
  eod    — Summary log only (market already closed)

Usage:
  python3 trading_agent.py --session open
  python3 trading_agent.py --session open --dry-run
"""

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import requests

# Auto-load .env if present (local development). GitHub Actions uses secrets directly.
_env_file = Path(__file__).parent.parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _, _v = _line.partition("=")
            os.environ.setdefault(_k.strip(), _v.strip())

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
ALPACA_KEY    = os.environ["ALPACA_API_KEY"]
ALPACA_SECRET = os.environ["ALPACA_SECRET_KEY"]
ALPACA_BASE   = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")
ALPACA_DATA   = os.environ.get("ALPACA_DATA_URL",  "https://data.alpaca.markets/v2")

HEADERS = {
    "APCA-API-KEY-ID":    ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

REPO_ROOT  = Path(__file__).parent.parent
TRADES_DIR = REPO_ROOT / "trades"
TODAY      = date.today().isoformat()

STARTING_CAPITAL = 100_000.00
SPY_START        = 731.53
ACCOUNT_FLOOR    = 87_500.00

# Layer 1 share targets
# XLY removed 2026-06-11: June sprint exit — position closed via FORCE_CLOSE_EQUITY.
# QQQ increased 45→50 to absorb freed capital.
LAYER1 = {"QQQ": 50, "SPY": 13, "JETS": 80, "XLE": 100}

# Layer 1 positions to force-exit: bot sells full position then never rebuys.
# Add symbols here when exiting a Layer 1 name — remove entry once position is flat.
FORCE_CLOSE_EQUITY = {"XLY"}

# IPO watchlist — buy a starter position the first open session the symbol is tradeable.
# Bot checks Alpaca asset status daily; buys on first available day.
# IMPORTANT: remove a symbol once the position has been opened AND exited — the "already
# owned" check only prevents re-entry while the position is live. After a profit-take the
# symbol is no longer in eq_positions and the bot will re-buy on the next session.
# SPCX: removed — IPO play complete. Bought Jun 12 @ ~$135, profit-taken Jun 16 at +21%.
#   Re-entry at $201 (49% above IPO price) is not the intended play.
IPO_WATCHLIST = [
    {"symbol": "ANTHROPIC", "qty": 10, "note": "Anthropic IPO — AI frontier, long-term DCA target"},
    {"symbol": "OPENAI",    "qty": 8,  "note": "OpenAI IPO — brand momentum, watch unit economics"},
]

# CSP targets: (underlying, strike, max_contracts)
# Priority order matters — most IV-sensitive first
# INTC removed: v2.0 strategy does not target INTC; Jun18 position was unintended bot action
# TSLA removed: $350P Jun18 closed at 50% profit (good exit). Re-enter only when IV > 40.
# NVDA: Jul18 expiry, OPT_DTE_MAX extended to 60 to cover ~57 DTE
# AMZN: re-added at $215P (~14% OTM at ~$250 spot). Previous $250P Jun26 closed at a loss
#   (5.7% OTM too close). New strike provides adequate downside buffer.
CSP_TARGETS = [
    ("NVDA", 190, 1),
    ("AMZN", 215, 1),
]

# QQQ calls — buy 1 contract 2% OTM for June alpha leverage.
# Short-dated (CALL_DTE_MAX=20) to stay within June expiry cycle.
CALL_TARGETS = [
    {"underlying": "QQQ", "otm_pct": 0.02, "qty": 1, "note": "June sprint leverage"},
]
CALL_DTE_MIN = 10
CALL_DTE_MAX = 20

# Layer 3 profit-take thresholds (unrealized %)
PROFIT_TAKE    = {"JETS": 0.30, "IWM": 0.20, "MU": 0.20, "XLY": 0.20}
STOP_REVIEW    = 0.10   # flag for review if L3 down >10%

# CSP close-early threshold: buy back when current premium <= this fraction of entry
CSP_CLOSE_PCT  = 0.50

# CSP stop-loss: buy back when current premium >= this multiple of entry.
# 2.0 = stop when the put costs 2× what we received (premium has doubled against us).
# This caps the maximum loss on any single CSP at roughly the premium received.
CSP_STOP_MULT  = 2.0

# Option chain search window — extended to 60 to reach Jul18 expiry (~57 DTE)
OPT_DTE_MIN = 25
OPT_DTE_MAX = 60

# Minimum premium to accept when opening a new CSP.
# Prevents entering contracts with negligible yield relative to collateral.
# At $1.50/contract minimum: $150 credit on $19K-35K collateral = ~0.4-0.8% floor.
# Raise this in low-IV environments; lower it only when IV > 40 and strike is close.
CSP_MIN_PREMIUM = 1.50

# ---------------------------------------------------------------------------
# Alpaca REST
# ---------------------------------------------------------------------------
def _get(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

def _post(url, body):
    r = requests.post(url, headers=HEADERS, json=body, timeout=15)
    r.raise_for_status()
    return r.json()

def _delete(url):
    r = requests.delete(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.json() if r.content else {}

def get_account():
    return _get(f"{ALPACA_BASE}/account")

def get_positions():
    return _get(f"{ALPACA_BASE}/positions")

def get_orders(status="open"):
    return _get(f"{ALPACA_BASE}/orders", {"status": status, "limit": 100})

def get_clock():
    return _get(f"{ALPACA_BASE}/clock")

def get_snapshots(symbols):
    return _get(f"{ALPACA_DATA}/stocks/snapshots",
                {"symbols": ",".join(symbols), "feed": "iex"})

def get_option_quote(symbol):
    """Fetch live bid/ask for a single option contract.
    Returns (bid, ask) floats, or (None, None) on failure.
    Used to price CSP limit orders at the current market bid so orders fill immediately.
    """
    try:
        data = _get(f"{ALPACA_DATA}/options/quotes/latest", {"symbols": symbol})
        q = data.get("quotes", {}).get(symbol, {})
        bid = q.get("bp")
        ask = q.get("ap")
        return (float(bid) if bid is not None else None,
                float(ask) if ask is not None else None)
    except Exception as e:
        print(f"    Option quote fetch failed for {symbol}: {e}")
        return None, None

def asset_is_tradeable(symbol):
    """Return True if symbol exists on Alpaca and is currently tradeable."""
    try:
        data = _get(f"{ALPACA_BASE}/assets/{symbol}")
        return data.get("status") == "active" and bool(data.get("tradable", False))
    except requests.HTTPError as e:
        if e.response is not None and e.response.status_code == 404:
            return False
        raise

def get_option_chain(underlying, strike_target):
    gte = (date.today() + timedelta(days=OPT_DTE_MIN)).isoformat()
    lte = (date.today() + timedelta(days=OPT_DTE_MAX)).isoformat()
    return _get(f"{ALPACA_BASE}/options/contracts", {
        "underlying_symbols": underlying,
        "type": "put",
        "expiration_date_gte": gte,
        "expiration_date_lte": lte,
        "strike_price_gte":    strike_target * 0.90,
        "strike_price_lte":    strike_target * 1.05,
        "limit": 20,
    })

def place_stock_order(symbol, side, qty):
    return _post(f"{ALPACA_BASE}/orders", {
        "symbol": symbol, "qty": str(qty),
        "side": side, "type": "market", "time_in_force": "day",
    })

def place_option_order(symbol, side, qty, limit_price, position_intent):
    return _post(f"{ALPACA_BASE}/orders", {
        "symbol": symbol, "qty": str(qty), "side": side,
        "type": "limit", "limit_price": str(round(limit_price, 2)),
        "time_in_force": "day", "position_intent": position_intent,
    })

def close_position(symbol):
    return _delete(f"{ALPACA_BASE}/positions/{symbol}")

# ---------------------------------------------------------------------------
# Strategy helpers
# ---------------------------------------------------------------------------
def equity_positions(positions):
    return {p["symbol"]: p for p in positions
            if p.get("asset_class") == "us_equity"}

def option_positions(positions):
    return {p["symbol"]: p for p in positions
            if p.get("asset_class") == "us_option"}

def pending_option_orders(orders, underlying):
    """Return True if there's already an open/pending option order for this underlying."""
    for o in orders:
        sym = o.get("symbol", "")
        if sym.startswith(underlying) and o.get("asset_class") == "us_option":
            return True
    return False

def _is_monthly_expiry(expiry_str):
    """Return True if expiry_str (YYYY-MM-DD) is a standard monthly (3rd Friday)."""
    try:
        d = date.fromisoformat(expiry_str)
        if d.weekday() != 4:  # not a Friday
            return False
        # 3rd Friday: day is between 15 and 21
        return 15 <= d.day <= 21
    except ValueError:
        return False


def find_best_contract(underlying, strike_target):
    """
    Find the most liquid tradeable put contract closest to strike_target
    within the DTE window. Prefers monthly expiries over weeklies.
    Returns contract dict or None.
    """
    try:
        data = get_option_chain(underlying, strike_target)
    except Exception as e:
        print(f"    Option chain fetch failed for {underlying}: {e}")
        return None

    contracts = [c for c in data.get("option_contracts", [])
                 if c.get("tradable") and c.get("close_price")]

    if not contracts:
        return None

    # Monthly first (0), then weekly (1); within each tier sort by OI desc, then strike proximity
    contracts.sort(key=lambda c: (
        0 if _is_monthly_expiry(c.get("expiration_date", "")) else 1,
        -int(c.get("open_interest") or 0),
        abs(float(c["strike_price"]) - strike_target),
    ))
    return contracts[0]


def find_call_contract(underlying, strike_target):
    """Find the best OTM call contract within the short CALL_DTE window."""
    try:
        gte = (date.today() + timedelta(days=CALL_DTE_MIN)).isoformat()
        lte = (date.today() + timedelta(days=CALL_DTE_MAX)).isoformat()
        data = _get(f"{ALPACA_BASE}/options/contracts", {
            "underlying_symbols": underlying,
            "type": "call",
            "expiration_date_gte": gte,
            "expiration_date_lte": lte,
            "strike_price_gte": strike_target * 0.98,
            "strike_price_lte": strike_target * 1.04,
            "limit": 20,
        })
    except Exception as e:
        print(f"    Call chain fetch failed for {underlying}: {e}")
        return None

    contracts = [c for c in data.get("option_contracts", [])
                 if c.get("tradable") and c.get("close_price")]
    if not contracts:
        return None

    contracts.sort(key=lambda c: (
        0 if _is_monthly_expiry(c.get("expiration_date", "")) else 1,
        -int(c.get("open_interest") or 0),
        abs(float(c["strike_price"]) - strike_target),
    ))
    return contracts[0]


# ---------------------------------------------------------------------------
# Rule engine
# ---------------------------------------------------------------------------
def layer1_actions(eq_positions):
    """Buy any Layer 1 ETF that is below its target share count."""
    actions = []
    for sym, target in LAYER1.items():
        current = int(float(eq_positions.get(sym, {}).get("qty", 0)))
        shortfall = target - current
        if shortfall > 0:
            actions.append({
                "type": "buy_stock",
                "symbol": sym,
                "qty": shortfall,
                "note": f"Layer 1 rebalance: have {current}, need {target}",
            })
    return actions


def ipo_watchlist_actions(eq_positions):
    """Buy IPO watchlist symbols the first session they are tradeable on Alpaca."""
    actions = []
    for item in IPO_WATCHLIST:
        symbol = item["symbol"]
        if symbol in eq_positions:
            print(f"    IPO watch: {symbol} already owned — skip")
            continue
        if not asset_is_tradeable(symbol):
            print(f"    IPO watch: {symbol} not yet on Alpaca — skip")
            continue
        actions.append({
            "type": "buy_stock",
            "symbol": symbol,
            "qty": item["qty"],
            "note": f"IPO buy: {item['note']}",
        })
    return actions


def call_buy_actions(eq_positions, opt_positions, orders, snapshots, options_bp):
    """Buy short-dated OTM calls on CALL_TARGETS for June alpha leverage."""
    actions = []
    for target in CALL_TARGETS:
        underlying = target["underlying"]

        # Skip if we already have a long option position on this underlying
        already_long = any(
            sym.startswith(underlying) and float(pos.get("qty", 0)) > 0
            for sym, pos in opt_positions.items()
        )
        if already_long or pending_option_orders(orders, underlying):
            print(f"    {underlying} call: already open or pending — skip")
            continue

        snap = snapshots.get(underlying, {})
        current_px = snap.get("latestTrade", {}).get("p", 0)
        if not current_px:
            print(f"    {underlying} call: no price data — skip")
            continue

        # Round to nearest $0.50 strike
        raw_strike = current_px * (1 + target["otm_pct"])
        strike_target = round(raw_strike * 2) / 2

        contract = find_call_contract(underlying, strike_target)
        if not contract:
            print(f"    {underlying} call: no contract found near ${strike_target:.0f} — skip")
            continue

        bid, ask = get_option_quote(contract["symbol"])
        if bid is None or ask is None or ask < 0.10:
            print(f"    {underlying} call: quote unavailable or ask too low — skip")
            continue

        # Buy at ask × 1.02 to ensure fill (buying, not selling)
        limit_price = round(ask * 1.02, 2)
        cost = limit_price * 100 * target["qty"]

        if options_bp < cost:
            print(f"    {underlying} call: need ${cost:,.0f}, have ${options_bp:,.0f} — skip")
            continue

        print(f"    {underlying} call: live bid=${bid:.2f} ask=${ask:.2f} strike=${contract['strike_price']} exp={contract['expiration_date']}")
        actions.append({
            "type": "buy_call",
            "symbol": contract["symbol"],
            "underlying": underlying,
            "strike": contract["strike_price"],
            "expiry": contract["expiration_date"],
            "limit_price": limit_price,
            "qty": target["qty"],
            "note": (f"{underlying} {contract['strike_price']}C {contract['expiration_date']} "
                     f"@ ${limit_price} ({target['note']})"),
        })
    return actions


def csp_open_actions(eq_positions, opt_positions, orders, options_bp):
    """Open new CSPs for any target name that doesn't already have one."""
    actions = []
    for underlying, strike, max_contracts in CSP_TARGETS:
        # Skip if already have a position or a pending order
        already_open = any(sym.startswith(underlying) for sym in opt_positions)
        if already_open or pending_option_orders(orders, underlying):
            print(f"    {underlying} CSP: already open or pending — skip")
            continue

        # Check buying power (rough check: strike × 100 per contract)
        required_bp = strike * 100
        if options_bp < required_bp:
            print(f"    {underlying} CSP: need ${required_bp:,}, have ${options_bp:,.0f} — skip")
            continue

        contract = find_best_contract(underlying, strike)
        if not contract:
            print(f"    {underlying} CSP: no tradeable contract found — skip")
            continue

        # Fetch live bid so the limit order fills immediately at open.
        # Selling at close×0.95 caused GTC loops when the close was above the
        # actual market bid — the order would sit unfilled and expire daily.
        bid, ask = get_option_quote(contract["symbol"])
        close_px = float(contract["close_price"])

        if bid is None:
            # Quote fetch failed — fall back to close×0.95 with a warning
            print(f"    {underlying} CSP: live quote unavailable, using close×0.95 fallback")
            limit_price = round(close_px * 0.95, 2)
        else:
            limit_price = round(bid, 2)
            print(f"    {underlying} CSP: live bid=${bid:.2f} ask=${ask:.2f} close=${close_px:.2f}")

        if limit_price < CSP_MIN_PREMIUM:
            print(f"    {underlying} CSP: bid ${limit_price:.2f} below minimum ${CSP_MIN_PREMIUM:.2f} — skip (low IV)")
            continue

        actions.append({
            "type": "sell_csp",
            "symbol": contract["symbol"],
            "underlying": underlying,
            "strike": contract["strike_price"],
            "expiry": contract["expiration_date"],
            "limit_price": limit_price,
            "close_price": close_px,
            "note": (f"{underlying} {contract['strike_price']}P {contract['expiration_date']} "
                     f"@ ${limit_price}"
                     + (f" (bid ${bid:.2f}, close was ${close_px})" if bid is not None
                        else f" (close was ${close_px})")),
        })
        # Deduct from available BP so we don't over-commit in the same session
        options_bp -= required_bp

    return actions


def management_actions(eq_positions, opt_positions):
    """
    Check open positions for:
    - Layer 3 profit takes / stop flags
    - CSP 50% profit closes
    """
    actions = []
    flags   = []

    # --- Force-close Layer 1 exits ---
    for sym in FORCE_CLOSE_EQUITY:
        if sym in eq_positions:
            actions.append({
                "type": "close_position",
                "symbol": sym,
                "note": f"Layer 1 exit: {sym} removed from strategy — closing full position",
            })

    # --- Layer 3 equity profit/stop checks ---
    for sym, pos in eq_positions.items():
        if sym in LAYER1 or sym in FORCE_CLOSE_EQUITY:
            continue  # Layer 1 / exiting — skip profit-take logic
        pct = float(pos.get("unrealized_plpc", 0))
        threshold = PROFIT_TAKE.get(sym, 0.20)
        if pct >= threshold:
            actions.append({
                "type": "close_position",
                "symbol": sym,
                "note": f"Profit take: +{pct*100:.1f}% >= {threshold*100:.0f}% target",
            })
        elif pct <= -STOP_REVIEW:
            flags.append(f"⚠️  {sym} down {pct*100:.1f}% — review stop")

    # --- CSP profit close and stop-loss ---
    for sym, pos in opt_positions.items():
        qty = float(pos.get("qty", 0))
        if qty >= 0:
            continue  # long options — not our CSPs
        avg_cost   = float(pos.get("avg_entry_price", 0))   # premium originally received
        current_px = float(pos.get("current_price", avg_cost))

        if avg_cost <= 0:
            continue

        if current_px <= avg_cost * CSP_CLOSE_PCT:
            # 50% profit — buy to close, lock in gain
            limit = round(current_px * 1.05, 2)
            actions.append({
                "type": "buy_to_close",
                "symbol": sym,
                "limit_price": limit,
                "note": (f"50% profit: sold @ ${avg_cost:.2f}, "
                         f"now ${current_px:.2f} — locking in gain"),
            })
        elif current_px >= avg_cost * CSP_STOP_MULT:
            # Stop-loss: premium has multiplied beyond acceptable loss
            # Buy to close at 5% above current to ensure fill
            limit = round(current_px * 1.05, 2)
            actions.append({
                "type": "buy_to_close",
                "symbol": sym,
                "limit_price": limit,
                "note": (f"stop-loss: sold @ ${avg_cost:.2f}, "
                         f"now ${current_px:.2f} ({current_px/avg_cost:.1f}x) — "
                         f"exceeds {CSP_STOP_MULT}x threshold"),
            })
            flags.append(f"🛑 CSP stop triggered on {sym}: "
                         f"${avg_cost:.2f} → ${current_px:.2f} "
                         f"({current_px/avg_cost:.1f}× premium)")

    return actions, flags


# ---------------------------------------------------------------------------
# Execution
# ---------------------------------------------------------------------------
def execute(actions, dry_run=False):
    results = []
    for a in actions:
        atype  = a["type"]
        symbol = a.get("symbol", "")
        note   = a.get("note", "")
        print(f"  {'[DRY RUN] ' if dry_run else ''}→ {atype} {symbol}: {note}")

        if dry_run:
            results.append({**a, "status": "dry_run"})
            continue

        try:
            if atype == "buy_stock":
                r = place_stock_order(symbol, "buy", a["qty"])
                results.append({**a, "status": "submitted", "order_id": r["id"]})

            elif atype == "close_position":
                close_position(symbol)
                results.append({**a, "status": "closed"})

            elif atype == "sell_csp":
                r = place_option_order(symbol, "sell", 1,
                                        a["limit_price"], "sell_to_open")
                results.append({**a, "status": "submitted", "order_id": r["id"]})

            elif atype == "buy_to_close":
                r = place_option_order(symbol, "buy", 1,
                                        a["limit_price"], "buy_to_close")
                results.append({**a, "status": "submitted", "order_id": r["id"]})

            elif atype == "buy_call":
                r = place_option_order(symbol, "buy", a.get("qty", 1),
                                        a["limit_price"], "buy_to_open")
                results.append({**a, "status": "submitted", "order_id": r["id"]})

        except requests.HTTPError as e:
            err = e.response.text if e.response else str(e)
            print(f"    ERROR: {err}")
            results.append({**a, "status": "error", "error": err})
        except Exception as e:
            print(f"    ERROR: {e}")
            results.append({**a, "status": "error", "error": str(e)})

    return results


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
def write_log(session, account, actions, results, flags, snapshots):
    equity      = float(account.get("equity", 0))
    options_bp  = float(account.get("options_buying_power", 0))
    our_ret     = (equity - STARTING_CAPITAL) / STARTING_CAPITAL * 100
    spy_px      = snapshots.get("SPY", {}).get("latestTrade", {}).get("p", 0)
    spy_ret     = (spy_px - SPY_START) / SPY_START * 100 if spy_px else 0
    alpha       = our_ret - spy_ret

    lines = [
        f"# exec_{session} — {TODAY}\n\n",
        f"| | |\n|---|---|\n",
        f"| Equity | ${equity:,.2f} |\n",
        f"| Our return | {our_ret:+.2f}% |\n",
        f"| SPY return | {spy_ret:+.2f}% (${spy_px:.2f}) |\n",
        f"| Alpha | {alpha:+.2f}% |\n",
        f"| Options BP remaining | ${options_bp:,.2f} |\n\n",
    ]

    if flags:
        lines.append("## Flags\n" + "".join(f"- {f}\n" for f in flags) + "\n")

    if actions:
        lines.append("## Actions\n")
        for r in results:
            st  = r.get("status", "?")
            oid = r.get("order_id", "")
            err = r.get("error", "")
            lines.append(
                f"- `{r['type']} {r.get('symbol','')}` — {r.get('note','')} "
                f"**[{st}]**" + (f" `{oid}`" if oid else "")
                + (f"\n  - error: `{err}`" if err else "") + "\n"
            )
    else:
        lines.append("## Actions\nNo actions needed.\n")

    TRADES_DIR.mkdir(exist_ok=True)
    outfile = TRADES_DIR / f"exec_{session}_{TODAY}.md"
    outfile.write_text("".join(lines))
    print(f"Wrote {outfile}")
    return str(outfile)


# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------
def _parse_eod_files():
    """Read all exec_eod_*.md files and return sorted list of dicts."""
    rows = []
    pat_equity  = re.compile(r'\| Equity\s*\|\s*\$([0-9,]+\.\d+)')
    pat_our     = re.compile(r'\| Our return\s*\|\s*([+-]?\d+\.\d+)%')
    pat_spy_ret = re.compile(r'\| SPY return\s*\|\s*([+-]?\d+\.\d+)%\s*\(\$([0-9.]+)\)')
    pat_bp      = re.compile(r'\| Options BP remaining\s*\|\s*\$([0-9,]+\.\d+)')

    for f in sorted((TRADES_DIR).glob("exec_eod_*.md")):
        m_date = re.search(r'exec_eod_(\d{4}-\d{2}-\d{2})\.md', f.name)
        if not m_date:
            continue
        text = f.read_text()
        m_eq   = pat_equity.search(text)
        m_our  = pat_our.search(text)
        m_spy  = pat_spy_ret.search(text)
        m_bp   = pat_bp.search(text)
        if not (m_eq and m_our and m_spy and m_bp):
            continue
        rows.append({
            "date":     m_date.group(1),
            "equity":   float(m_eq.group(1).replace(",", "")),
            "our_ret":  float(m_our.group(1)),
            "spy_ret":  float(m_spy.group(1)),
            "spy_px":   float(m_spy.group(2)),
            "opt_bp":   float(m_bp.group(1).replace(",", "")),
        })
    return rows


def generate_dashboard():
    rows = _parse_eod_files()
    if not rows:
        print("No exec_eod files found — skipping dashboard.")
        return

    # Prepend day-0 row (starting capital)
    all_rows = [{"date": "2026-05-07", "equity": 100000.0, "our_ret": 0.0,
                 "spy_ret": 0.0, "spy_px": SPY_START, "opt_bp": 100000.0}] + rows

    dates      = [r["date"]                                    for r in all_rows]
    equities   = [r["equity"]                                  for r in all_rows]
    spy_vals   = [round(100000 * (1 + r["spy_ret"] / 100), 2) for r in all_rows]
    our_rets   = [r["our_ret"]                                 for r in all_rows]
    spy_rets   = [r["spy_ret"]                                 for r in all_rows]
    alphas     = [round(r["our_ret"] - r["spy_ret"], 2)        for r in all_rows]
    opt_bps    = [r["opt_bp"]                                  for r in all_rows]

    # Daily P&L in dollars
    daily_pnl = [0.0]
    for i in range(1, len(all_rows)):
        daily_pnl.append(round(all_rows[i]["equity"] - all_rows[i-1]["equity"], 2))

    last = all_rows[-1]
    last_equity  = last["equity"]
    last_our_ret = last["our_ret"]
    last_spy_ret = last["spy_ret"]
    last_alpha   = round(last["our_ret"] - last["spy_ret"], 2)
    last_bp      = last["opt_bp"]
    last_date    = last["date"]
    total_pnl    = round(last_equity - 100000, 2)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Paper Trading Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: #0d1117;
    color: #e6edf3;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", monospace;
    padding: 1.5rem;
  }}
  h1 {{ font-size: 1.4rem; color: #58a6ff; margin-bottom: 0.25rem; }}
  .subtitle {{ color: #8b949e; font-size: 0.8rem; margin-bottom: 1.5rem; }}
  .stats {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0.75rem;
    margin-bottom: 1.5rem;
  }}
  .stat {{
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 0.75rem 1rem;
  }}
  .stat-label {{ color: #8b949e; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.05em; }}
  .stat-value {{ font-size: 1.25rem; font-weight: 600; margin-top: 0.2rem; }}
  .pos {{ color: #3fb950; }}
  .neg {{ color: #f85149; }}
  .neu {{ color: #e6edf3; }}
  .chart-wrap {{
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 1rem;
  }}
  .chart-title {{ color: #8b949e; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.75rem; }}
  canvas {{ max-height: 280px; }}
</style>
</head>
<body>

<h1>Paper Trading Dashboard</h1>
<p class="subtitle">Updated {last_date} &nbsp;·&nbsp; Started 2026-05-07 &nbsp;·&nbsp; $100,000 starting capital</p>

<div class="stats">
  <div class="stat">
    <div class="stat-label">Account Value</div>
    <div class="stat-value neu">${last_equity:,.2f}</div>
  </div>
  <div class="stat">
    <div class="stat-label">Total P&amp;L</div>
    <div class="stat-value {'pos' if total_pnl >= 0 else 'neg'}">{'+' if total_pnl >= 0 else ''}${total_pnl:,.2f}</div>
  </div>
  <div class="stat">
    <div class="stat-label">Our Return</div>
    <div class="stat-value {'pos' if last_our_ret >= 0 else 'neg'}">{last_our_ret:+.2f}%</div>
  </div>
  <div class="stat">
    <div class="stat-label">SPY Return</div>
    <div class="stat-value {'pos' if last_spy_ret >= 0 else 'neg'}">{last_spy_ret:+.2f}%</div>
  </div>
  <div class="stat">
    <div class="stat-label">Alpha</div>
    <div class="stat-value {'pos' if last_alpha >= 0 else 'neg'}">{last_alpha:+.2f}%</div>
  </div>
  <div class="stat">
    <div class="stat-label">Options BP Available</div>
    <div class="stat-value neu">${last_bp:,.0f}</div>
  </div>
</div>

<div class="chart-wrap">
  <div class="chart-title">Account Value vs SPY Benchmark</div>
  <canvas id="equityChart"></canvas>
</div>

<div class="chart-wrap">
  <div class="chart-title">Daily P&amp;L ($)</div>
  <canvas id="pnlChart"></canvas>
</div>

<div class="chart-wrap">
  <div class="chart-title">Cumulative Return: Us vs SPY (%)</div>
  <canvas id="retChart"></canvas>
</div>

<div class="chart-wrap">
  <div class="chart-title">Options Buying Power Remaining ($)</div>
  <canvas id="bpChart"></canvas>
</div>

<script>
const DATES    = {json.dumps(dates)};
const EQUITIES = {json.dumps(equities)};
const SPY_VALS = {json.dumps(spy_vals)};
const OUR_RETS = {json.dumps(our_rets)};
const SPY_RETS = {json.dumps(spy_rets)};
const ALPHAS   = {json.dumps(alphas)};
const DAILY_PNL= {json.dumps(daily_pnl)};
const OPT_BPS  = {json.dumps(opt_bps)};

const GRID = {{ color: 'rgba(48,54,61,0.8)' }};
const TICK = {{ color: '#8b949e', font: {{ size: 11 }} }};

// Chart 1 — Equity vs SPY
new Chart(document.getElementById('equityChart'), {{
  type: 'line',
  data: {{
    labels: DATES,
    datasets: [
      {{ label: 'Account Value', data: EQUITIES, borderColor: '#58a6ff', backgroundColor: 'rgba(88,166,255,0.08)', tension: 0.3, fill: true, pointRadius: 3 }},
      {{ label: 'SPY ($100K)', data: SPY_VALS,  borderColor: '#3fb950', backgroundColor: 'rgba(63,185,80,0.06)',  tension: 0.3, fill: true, pointRadius: 3 }},
    ]
  }},
  options: {{
    responsive: true, interaction: {{ mode: 'index', intersect: false }},
    plugins: {{ legend: {{ labels: {{ color: '#e6edf3', font: {{ size: 12 }} }} }} }},
    scales: {{
      x: {{ grid: GRID, ticks: TICK }},
      y: {{ grid: GRID, ticks: {{ ...TICK, callback: v => '$' + v.toLocaleString() }} }}
    }}
  }}
}});

// Chart 2 — Daily P&L bars
new Chart(document.getElementById('pnlChart'), {{
  type: 'bar',
  data: {{
    labels: DATES.slice(1),
    datasets: [{{ label: 'Daily P&L', data: DAILY_PNL.slice(1),
      backgroundColor: DAILY_PNL.slice(1).map(v => v >= 0 ? 'rgba(63,185,80,0.7)' : 'rgba(248,81,73,0.7)'),
      borderRadius: 3
    }}]
  }},
  options: {{
    responsive: true,
    plugins: {{ legend: {{ labels: {{ color: '#e6edf3', font: {{ size: 12 }} }} }} }},
    scales: {{
      x: {{ grid: GRID, ticks: TICK }},
      y: {{ grid: GRID, ticks: {{ ...TICK, callback: v => '$' + v.toLocaleString() }} }}
    }}
  }}
}});

// Chart 3 — Cumulative return %
new Chart(document.getElementById('retChart'), {{
  type: 'line',
  data: {{
    labels: DATES,
    datasets: [
      {{ label: 'Us', data: OUR_RETS, borderColor: '#58a6ff', tension: 0.3, pointRadius: 3 }},
      {{ label: 'SPY', data: SPY_RETS, borderColor: '#3fb950', tension: 0.3, pointRadius: 3 }},
      {{ label: 'Alpha', data: ALPHAS, borderColor: '#d2a8ff', tension: 0.3, pointRadius: 3, borderDash: [4,4] }},
    ]
  }},
  options: {{
    responsive: true, interaction: {{ mode: 'index', intersect: false }},
    plugins: {{ legend: {{ labels: {{ color: '#e6edf3', font: {{ size: 12 }} }} }} }},
    scales: {{
      x: {{ grid: GRID, ticks: TICK }},
      y: {{ grid: GRID, ticks: {{ ...TICK, callback: v => v.toFixed(2) + '%' }} }}
    }}
  }}
}});

// Chart 4 — Options BP
new Chart(document.getElementById('bpChart'), {{
  type: 'bar',
  data: {{
    labels: DATES,
    datasets: [{{ label: 'Options BP Remaining', data: OPT_BPS,
      backgroundColor: 'rgba(88,166,255,0.55)', borderRadius: 3
    }}]
  }},
  options: {{
    responsive: true,
    plugins: {{ legend: {{ labels: {{ color: '#e6edf3', font: {{ size: 12 }} }} }} }},
    scales: {{
      x: {{ grid: GRID, ticks: TICK }},
      y: {{ grid: GRID, ticks: {{ ...TICK, callback: v => '$' + v.toLocaleString() }} }}
    }}
  }}
}});
</script>
</body>
</html>"""

    out = TRADES_DIR / "dashboard.html"
    out.write_text(html)
    print(f"Wrote {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", required=True, choices=["open", "midday", "eod"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"=== Trading Agent [{args.session.upper()}] {TODAY} ===")
    if args.dry_run:
        print("DRY RUN — no orders will be placed")

    # ── Market clock check ─────────────────────────────────────────────────
    clock = get_clock()
    is_open = clock.get("is_open", False)

    if not is_open and args.session in ("open", "midday"):
        next_open = clock.get("next_open", "unknown")
        print(f"Market closed. Next open: {next_open}. Exiting.")
        TRADES_DIR.mkdir(exist_ok=True)
        (TRADES_DIR / f"exec_{args.session}_{TODAY}.md").write_text(
            f"# exec_{args.session} — {TODAY}\nMarket closed — no action.\n"
        )
        sys.exit(0)

    # ── Gather state ───────────────────────────────────────────────────────
    print("Fetching account state...")
    account   = get_account()
    positions = get_positions()
    orders    = get_orders(status="open")
    equity    = float(account.get("equity", 0))
    options_bp = float(account.get("options_buying_power", 0))
    print(f"  Equity: ${equity:,.2f} | Options BP: ${options_bp:,.2f} | "
          f"Positions: {len(positions)} | Open orders: {len(orders)}")

    # ── Hard stop ──────────────────────────────────────────────────────────
    below_floor = equity < ACCOUNT_FLOOR
    if below_floor:
        print(f"⚠️  BELOW FLOOR ${ACCOUNT_FLOOR:,.0f} — blocking new positions")

    eq_pos  = equity_positions(positions)
    opt_pos = option_positions(positions)

    # ── Market snapshots ───────────────────────────────────────────────────
    watchlist = list(LAYER1.keys()) + ["NVDA", "TSLA", "AMZN", "INTC", "IWM", "MU", "XLY"]
    print("Fetching snapshots...")
    snapshots = get_snapshots(watchlist)

    # ── Build action list by session ───────────────────────────────────────
    all_actions = []
    all_flags   = []

    if args.session == "open":
        # Management first — catches FORCE_CLOSE_EQUITY exits and CSP profit/stops
        mgmt, flags = management_actions(eq_pos, opt_pos)
        all_actions += mgmt
        all_flags   += flags
        if not below_floor:
            print("Checking Layer 1 targets...")
            all_actions += layer1_actions(eq_pos)
            print("Checking CSP targets...")
            all_actions += csp_open_actions(eq_pos, opt_pos, orders, options_bp)
            print("Checking call targets...")
            all_actions += call_buy_actions(eq_pos, opt_pos, orders, snapshots, options_bp)
        print("Checking IPO watchlist...")
        all_actions += ipo_watchlist_actions(eq_pos)

    elif args.session == "midday":
        print("Running midday management checks...")
        mgmt, flags = management_actions(eq_pos, opt_pos)
        all_actions += mgmt
        all_flags   += flags

    elif args.session == "eod":
        print("EOD — summary log only.")
        mgmt, flags = management_actions(eq_pos, opt_pos)
        all_actions += mgmt   # close any positions that hit targets late in day
        all_flags   += flags
        if below_floor:
            all_flags.append(f"🚨 Account ${equity:,.2f} below floor ${ACCOUNT_FLOOR:,.0f}!")
        spy_px = snapshots.get("SPY", {}).get("latestTrade", {}).get("p", 0)
        if spy_px:
            spy_ret = (spy_px - SPY_START) / SPY_START * 100
            our_ret = (equity - STARTING_CAPITAL) / STARTING_CAPITAL * 100
            print(f"  SPY: ${spy_px:.2f} ({spy_ret:+.2f}%) | "
                  f"Us: ${equity:,.2f} ({our_ret:+.2f}%) | "
                  f"Alpha: {our_ret-spy_ret:+.2f}%")

    # ── Execute ────────────────────────────────────────────────────────────
    if all_actions:
        print(f"Executing {len(all_actions)} action(s)...")
    results = execute(all_actions, dry_run=args.dry_run)

    # ── Write log ──────────────────────────────────────────────────────────
    write_log(args.session, account, all_actions, results, all_flags, snapshots)

    if args.session == "eod":
        generate_dashboard()

    print("Done.")


if __name__ == "__main__":
    main()
