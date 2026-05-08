#!/usr/bin/env python3
"""
trading_agent.py — GitHub Actions trading agent
Calls Claude API for decisions, executes via Alpaca REST.

Usage: python3 trading_agent.py --session {open|midday|eod}
       python3 trading_agent.py --session open --dry-run
"""

import argparse
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

import anthropic
import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
ALPACA_KEY    = os.environ["ALPACA_API_KEY"]
ALPACA_SECRET = os.environ["ALPACA_SECRET_KEY"]
ALPACA_BASE   = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")
ALPACA_DATA   = os.environ.get("ALPACA_DATA_URL", "https://data.alpaca.markets/v2")

ALPACA_HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

REPO_ROOT  = Path(__file__).parent.parent
TRADES_DIR = REPO_ROOT / "trades"
TODAY      = date.today().isoformat()

STARTING_CAPITAL = 100_000.00
SPY_START        = 731.53
ACCOUNT_FLOOR    = 87_500.00

# Layer 1 targets
LAYER1_TARGETS = {"QQQ": 45, "SPY": 13, "XLY": 40, "JETS": 80, "XLE": 100}

# CSP targets: symbol → (strike, max_contracts)
CSP_TARGETS = {
    "TSLA": (370, 1),
    "NVDA": (190, 1),
    "AMZN": (245, 1),
    "INTC": (95,  1),
}

WATCHLIST = ["SPY", "QQQ", "XLY", "JETS", "XLE", "NVDA", "TSLA", "AMZN", "INTC", "IWM", "MU"]

# ---------------------------------------------------------------------------
# Alpaca REST helpers
# ---------------------------------------------------------------------------
def _get(url, params=None):
    r = requests.get(url, headers=ALPACA_HEADERS, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

def _post(url, body):
    r = requests.post(url, headers=ALPACA_HEADERS, json=body, timeout=15)
    r.raise_for_status()
    return r.json()

def _delete(url):
    r = requests.delete(url, headers=ALPACA_HEADERS, timeout=15)
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
    return _get(f"{ALPACA_DATA}/stocks/snapshots", {"symbols": ",".join(symbols), "feed": "iex"})

def get_option_contracts(underlying, strike_gte, strike_lte):
    today = date.today()
    expiry_gte = (today + timedelta(days=25)).isoformat()
    expiry_lte = (today + timedelta(days=50)).isoformat()
    return _get(f"{ALPACA_BASE}/options/contracts", {
        "underlying_symbols": underlying,
        "type": "put",
        "expiration_date_gte": expiry_gte,
        "expiration_date_lte": expiry_lte,
        "strike_price_gte": strike_gte,
        "strike_price_lte": strike_lte,
        "limit": 20,
    })

def place_stock_order(symbol, side, qty, order_type="market", limit_price=None):
    body = {"symbol": symbol, "qty": str(qty), "side": side,
            "type": order_type, "time_in_force": "day"}
    if limit_price:
        body["limit_price"] = str(limit_price)
    return _post(f"{ALPACA_BASE}/orders", body)

def place_option_order(symbol, side, qty, limit_price, position_intent):
    body = {"symbol": symbol, "qty": str(qty), "side": side,
            "type": "limit", "limit_price": str(limit_price),
            "time_in_force": "day", "position_intent": position_intent}
    return _post(f"{ALPACA_BASE}/orders", body)

def close_position(symbol):
    return _delete(f"{ALPACA_BASE}/positions/{symbol}")

# ---------------------------------------------------------------------------
# Context helpers
# ---------------------------------------------------------------------------
def load_plan():
    p = REPO_ROOT / "PLAN.md"
    return p.read_text() if p.exists() else "No PLAN.md found."

def load_recent(prefix):
    files = sorted(TRADES_DIR.glob(f"{prefix}_*.md"), reverse=True)
    return files[0].read_text() if files else f"No {prefix} file found."

def gather_option_chains():
    chains = {}
    for sym, (strike, _) in CSP_TARGETS.items():
        try:
            data = get_option_contracts(sym, strike * 0.85, strike * 1.10)
            contracts = data.get("option_contracts", [])
            # Keep only contracts with open interest or close price
            liquid = [c for c in contracts if c.get("close_price") or c.get("open_interest")]
            chains[sym] = liquid[:10]  # top 10 per name
        except Exception as e:
            chains[sym] = [{"error": str(e)}]
    return chains

# ---------------------------------------------------------------------------
# Claude decision engine
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are an automated trading agent managing a paper trading account.
You receive account state and market data, then return a JSON action plan.
Be conservative: only trade when the strategy clearly calls for it.
Never exceed buying power. Always verify positions before placing orders."""

def build_user_prompt(session, account, positions, orders, snapshots, option_chains, plan, context):
    equity = float(account.get("equity", 0))
    options_bp = float(account.get("options_buying_power", 0))
    cash = float(account.get("cash", 0))

    pos_summary = {p["symbol"]: {"qty": p["qty"], "avg_cost": p["avg_entry_price"],
                                  "market_value": p["market_value"],
                                  "unrealized_pl": p["unrealized_pl"],
                                  "unrealized_plpc": p["unrealized_plpc"]}
                   for p in positions}

    open_option_orders = [o for o in orders if o.get("asset_class") == "us_option"]
    price_summary = {sym: snap["latestTrade"]["p"]
                     for sym, snap in snapshots.items() if "latestTrade" in snap}

    return f"""SESSION: {session.upper()} | DATE: {TODAY}

## ACCOUNT
- Equity: ${equity:,.2f} (start: $100,000 | return: {(equity-100000)/100000*100:+.2f}%)
- Cash: ${cash:,.2f}
- Options buying power: ${options_bp:,.2f}
- Floor trigger: ${ACCOUNT_FLOOR:,.0f} (pause new positions if below)

## CURRENT POSITIONS
{json.dumps(pos_summary, indent=2)}

## OPEN OPTION ORDERS (pending fills)
{json.dumps(open_option_orders, indent=2)}

## MARKET PRICES
{json.dumps(price_summary, indent=2)}

## OPTION CHAINS (30-50 DTE puts, near target strikes)
{json.dumps(option_chains, indent=2)}

## STRATEGY (PLAN.md excerpt)
Layer 1 targets: QQQ×45, SPY×13, XLY×40, JETS×80, XLE×100
CSP priority: TSLA $370 strike, NVDA $190, AMZN $245, INTC $95
- Open CSPs with 30-45 DTE when IV is elevated (war-era IV still elevated)
- Close CSPs at 50% profit (buy to close)
- Roll if premium doubles (50% loss)
- Exit XLE if Brent crude < $85
- Layer 3 profit at +20%, JETS at +30%
- STOP new positions if equity < $87,500

## TODAY'S RESEARCH CONTEXT
{context}

---

Return a JSON object with this exact structure:

```json
{{
  "reasoning": "brief explanation of your decisions",
  "risk_flags": ["any warnings or stops triggered"],
  "actions": [
    {{
      "type": "buy_stock",
      "symbol": "QQQ",
      "qty": 45,
      "note": "Layer 1: at 0 of 45 target"
    }}
  ]
}}
```

Valid action types:
- "buy_stock": {{"symbol", "qty", "note"}}
- "sell_csp": {{"symbol": "OCC_SYMBOL", "limit_price": float, "note"}} — use exact OCC symbol from option_chains
- "buy_to_close": {{"symbol": "OCC_SYMBOL", "limit_price": float, "note"}}
- "close_position": {{"symbol": "TICKER", "note"}}
- "no_action": {{"note": "reason"}}

Rules:
1. Only buy Layer 1 stocks that are SHORT of their target qty in current positions
2. Only sell_csp if options_buying_power >= strike × 100 AND no existing open order for that name
3. For sell_csp limit_price: use close_price from option_chains, subtract 5-10% to improve fill odds
4. If equity < ${ACCOUNT_FLOOR:,.0f}: no new buy_stock or sell_csp actions
5. Return "no_action" if nothing needs to be done

Return ONLY the JSON block."""

def ask_claude(session, account, positions, orders, snapshots, option_chains, plan, context):
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
    prompt = build_user_prompt(session, account, positions, orders, snapshots,
                                option_chains, plan, context)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text

def parse_decision(raw):
    m = re.search(r'```json\s*(.*?)\s*```', raw, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    return json.loads(raw)

# ---------------------------------------------------------------------------
# Execution
# ---------------------------------------------------------------------------
def execute_actions(actions, dry_run=False):
    results = []
    for action in actions:
        atype  = action.get("type", "no_action")
        symbol = action.get("symbol", "")
        note   = action.get("note", "")
        tag    = f"{atype} {symbol}".strip()

        print(f"  → {tag}: {note}")

        if dry_run or atype == "no_action":
            results.append({"action": action, "status": "dry_run" if dry_run else "no_action"})
            continue

        try:
            if atype == "buy_stock":
                r = place_stock_order(symbol, "buy", action["qty"])
                results.append({"action": action, "status": "submitted", "order_id": r["id"]})

            elif atype == "close_position":
                r = close_position(symbol)
                results.append({"action": action, "status": "closed"})

            elif atype == "sell_csp":
                r = place_option_order(symbol, "sell", 1,
                                        action["limit_price"], "sell_to_open")
                results.append({"action": action, "status": "submitted", "order_id": r["id"]})

            elif atype == "buy_to_close":
                r = place_option_order(symbol, "buy", 1,
                                        action["limit_price"], "buy_to_close")
                results.append({"action": action, "status": "submitted", "order_id": r["id"]})

        except requests.HTTPError as e:
            msg = e.response.text if e.response else str(e)
            print(f"    ERROR: {msg}")
            results.append({"action": action, "status": "error", "error": msg})
        except Exception as e:
            print(f"    ERROR: {e}")
            results.append({"action": action, "status": "error", "error": str(e)})

    return results

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
def write_log(session, reasoning, risk_flags, actions, results, account):
    equity = float(account.get("equity", 0))
    our_ret = (equity - STARTING_CAPITAL) / STARTING_CAPITAL * 100

    lines = [
        f"# exec_{session} — {TODAY}\n",
        f"**Equity:** ${equity:,.2f} | **Return:** {our_ret:+.2f}%\n",
        f"\n## Reasoning\n{reasoning}\n",
    ]
    if risk_flags:
        lines.append("\n## Risk Flags\n" + "\n".join(f"- {f}" for f in risk_flags) + "\n")

    lines.append("\n## Actions\n")
    for r in results:
        a   = r["action"]
        st  = r["status"]
        oid = r.get("order_id", "")
        lines.append(f"- `{a.get('type')} {a.get('symbol','')}` — {a.get('note','')} **[{st}]**"
                      + (f" `{oid}`" if oid else "") + "\n")

    TRADES_DIR.mkdir(exist_ok=True)
    outfile = TRADES_DIR / f"exec_{session}_{TODAY}.md"
    outfile.write_text("".join(lines))
    print(f"Wrote {outfile}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", required=True, choices=["open", "midday", "eod"])
    parser.add_argument("--dry-run", action="store_true", help="Plan only, no orders placed")
    args = parser.parse_args()

    print(f"=== Trading Agent — {args.session.upper()} — {TODAY} ===")
    if args.dry_run:
        print("DRY RUN — no orders will be placed")

    # 1. Market clock check
    clock = get_clock()
    if not clock.get("is_open") and args.session in ("open", "midday"):
        print(f"Market is closed (next open: {clock.get('next_open')}). Skipping execution.")
        # Still write a log so the cron is visible in git history
        TRADES_DIR.mkdir(exist_ok=True)
        (TRADES_DIR / f"exec_{args.session}_{TODAY}.md").write_text(
            f"# exec_{args.session} — {TODAY}\nMarket closed — no action.\n"
        )
        sys.exit(0)

    # 2. Gather state
    print("Fetching account state...")
    account   = get_account()
    positions = get_positions()
    orders    = get_orders(status="open")
    equity    = float(account.get("equity", 0))
    print(f"  Equity: ${equity:,.2f} | Positions: {len(positions)} | Open orders: {len(orders)}")

    # 3. Market data
    print("Fetching market snapshots...")
    snapshots = get_snapshots(WATCHLIST)

    # 4. Option chains (skip for EOD)
    option_chains = {}
    if args.session != "eod":
        print("Fetching option chains...")
        option_chains = gather_option_chains()

    # 5. Context from repo
    plan = load_plan()
    context_map = {
        "open":   lambda: load_recent("premarket"),
        "midday": lambda: load_recent("exec_open") or load_recent("premarket"),
        "eod":    lambda: load_recent("exec_midday") or load_recent("exec_open"),
    }
    context = context_map[args.session]()

    # 6. Ask Claude
    print("Consulting Claude for decisions...")
    raw = ask_claude(args.session, account, positions, orders,
                      snapshots, option_chains, plan, context)
    print("Claude response received.")

    # 7. Parse
    decision   = parse_decision(raw)
    reasoning  = decision.get("reasoning", "")
    risk_flags = decision.get("risk_flags", [])
    actions    = decision.get("actions", [])
    print(f"Reasoning: {reasoning}")
    print(f"Actions planned: {len(actions)}")

    # 8. Hard stops
    if equity < ACCOUNT_FLOOR:
        print(f"⚠️  BELOW FLOOR ${ACCOUNT_FLOOR:,.0f} — blocking buy/sell_csp actions")
        actions = [a for a in actions if a["type"] not in ("buy_stock", "sell_csp")]
        risk_flags.append(f"Account ${equity:,.2f} below floor ${ACCOUNT_FLOOR:,.0f} — new positions blocked")

    # 9. Execute
    results = execute_actions(actions, dry_run=args.dry_run)

    # 10. Log
    write_log(args.session, reasoning, risk_flags, actions, results, account)
    print("Done.")

if __name__ == "__main__":
    main()
