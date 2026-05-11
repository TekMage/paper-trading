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
import sys
from datetime import date, timedelta
from pathlib import Path

import requests

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
LAYER1 = {"QQQ": 45, "SPY": 13, "XLY": 40, "JETS": 80, "XLE": 100}

# CSP targets: underlying -> (strike, max_contracts)
# Priority order matters — most IV-sensitive first
CSP_TARGETS = [
    ("TSLA", 370, 1),
    ("NVDA", 190, 1),
    ("AMZN", 245, 1),
    ("INTC",  95, 1),
]

# Layer 3 profit-take thresholds (unrealized %)
PROFIT_TAKE    = {"JETS": 0.30, "IWM": 0.20, "MU": 0.20, "XLY": 0.20}
STOP_REVIEW    = 0.10   # flag for review if L3 down >10%

# CSP close-early threshold: buy back when current premium <= this fraction of entry
CSP_CLOSE_PCT  = 0.50

# Option chain search window
OPT_DTE_MIN = 25
OPT_DTE_MAX = 50

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

        close_px = float(contract["close_price"])
        # Sell at 5% below yesterday's close to improve fill odds
        limit_price = round(close_px * 0.95, 2)

        actions.append({
            "type": "sell_csp",
            "symbol": contract["symbol"],
            "underlying": underlying,
            "strike": contract["strike_price"],
            "expiry": contract["expiration_date"],
            "limit_price": limit_price,
            "close_price": close_px,
            "note": (f"{underlying} {contract['strike_price']}P {contract['expiration_date']} "
                     f"@ ${limit_price} (close was ${close_px})"),
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

    # --- Layer 3 equity profit/stop checks ---
    for sym, pos in eq_positions.items():
        if sym in LAYER1:
            continue  # Layer 1 — hold forever per strategy
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

    # --- CSP 50% profit closes ---
    for sym, pos in opt_positions.items():
        qty = float(pos.get("qty", 0))
        if qty >= 0:
            continue  # long options — not our CSPs
        avg_cost    = float(pos.get("avg_entry_price", 0))   # premium originally received
        current_px  = float(pos.get("current_price", avg_cost))
        if avg_cost > 0 and current_px <= avg_cost * CSP_CLOSE_PCT:
            # Buy to close at 5% above current to ensure fill
            limit = round(current_px * 1.05, 2)
            actions.append({
                "type": "buy_to_close",
                "symbol": sym,
                "limit_price": limit,
                "note": (f"50% profit: sold @ ${avg_cost:.2f}, "
                         f"now ${current_px:.2f} — locking in gain"),
            })

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
    watchlist = list(LAYER1.keys()) + ["NVDA", "TSLA", "AMZN", "INTC", "IWM", "MU"]
    print("Fetching snapshots...")
    snapshots = get_snapshots(watchlist)

    # ── Build action list by session ───────────────────────────────────────
    all_actions = []
    all_flags   = []

    if args.session == "open":
        if not below_floor:
            print("Checking Layer 1 targets...")
            all_actions += layer1_actions(eq_pos)
            print("Checking CSP targets...")
            all_actions += csp_open_actions(eq_pos, opt_pos, orders, options_bp)
        # Management checks at open too
        mgmt, flags = management_actions(eq_pos, opt_pos)
        all_actions += mgmt
        all_flags   += flags

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
    print("Done.")


if __name__ == "__main__":
    main()
