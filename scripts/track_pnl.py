#!/usr/bin/env python3
"""
Quick P&L tracker — compares account value to SPY benchmark.
Loads credentials from .env if present.
Usage: python3 track_pnl.py <current_account_value> <spy_price>
       python3 track_pnl.py --live   (fetches live values from Alpaca)
"""

import sys
import os
from datetime import date
from pathlib import Path

STARTING_CAPITAL = 100_000.00
SPY_START = 731.53
START_DATE = date(2026, 5, 7)


def load_env():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def calc_return(current, start):
    return (current - start) / start * 100


def fetch_live():
    import urllib.request, json
    key = os.environ["ALPACA_API_KEY"]
    secret = os.environ["ALPACA_SECRET_KEY"]
    base = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")
    data = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets/v2")
    headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret}

    def get(url):
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())

    account = get(f"{base}/account")
    spy = get(f"{data}/stocks/snapshots?symbols=SPY&feed=iex")
    return float(account["equity"]), float(spy["SPY"]["dailyBar"]["c"])


def print_report(account_value, spy_price):
    our_return = calc_return(account_value, STARTING_CAPITAL)
    spy_return = calc_return(spy_price, SPY_START)
    alpha = our_return - spy_return
    days_elapsed = (date.today() - START_DATE).days

    print(f"\n{'='*45}")
    print(f"  Paper Trading P&L — {date.today()}")
    print(f"  Day {days_elapsed} of test period")
    print(f"{'='*45}")
    print(f"  Account value:  ${account_value:>12,.2f}")
    print(f"  Starting cap:   ${STARTING_CAPITAL:>12,.2f}")
    print(f"  P&L:            ${account_value - STARTING_CAPITAL:>+12,.2f}")
    print(f"{'─'*45}")
    print(f"  Our return:     {our_return:>+10.2f}%")
    print(f"  SPY return:     {spy_return:>+10.2f}%")
    print(f"  Alpha:          {alpha:>+10.2f}%")
    print(f"{'='*45}")
    print(f"  {'✓ Beating' if alpha > 0 else '✗ Lagging'} SPY by {abs(alpha):.2f}%")

    if account_value < STARTING_CAPITAL * 0.875:
        print(f"\n  ⚠️  WARNING: Account below $87,500 stop threshold!")
        print(f"  ⚠️  Pause new positions and reassess strategy.")
    print()


def main():
    load_env()

    if len(sys.argv) == 2 and sys.argv[1] == "--live":
        print("Fetching live data from Alpaca...")
        account_value, spy_price = fetch_live()
    elif len(sys.argv) == 3:
        account_value = float(sys.argv[1])
        spy_price = float(sys.argv[2])
    else:
        print("Usage: python3 track_pnl.py <account_value> <spy_price>")
        print("       python3 track_pnl.py --live")
        sys.exit(1)

    print_report(account_value, spy_price)


if __name__ == "__main__":
    main()
