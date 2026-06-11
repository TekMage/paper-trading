# CLAUDE.md — Paper Trading Bot

**GitHub repo:** https://github.com/TekMage/paper-trading  
**Stack:** Python / Alpaca paper trading API / GitHub Actions (3x daily)  
**Repo root:** `/Users/tekmage/DevProjects/paper/`

---

## Quick Account Check

Use the Alpaca MCP tools available in this session:
- `mcp__alpaca__get_account_info` — equity, buying power, cash
- `mcp__alpaca__get_all_positions` — all open positions (equity + options)
- `mcp__alpaca__get_orders` — open or recent orders

Or run the bot locally (no manual env export needed — `.env` auto-loads):
```bash
cd /Users/tekmage/DevProjects/paper
.venv/bin/python scripts/trading_agent.py --session eod --dry-run
```

If `.venv` doesn't exist:
```bash
python3 -m venv .venv && .venv/bin/pip install requests
```

---

## GitHub Actions (automated — runs on GitHub's runners)

| Workflow | Schedule | What it does |
|---|---|---|
| `trading-open.yml` | 9:30 AM ET Mon–Fri | Layer 1 rebalance, open new CSPs |
| `trading-midday.yml` | 12:00 PM ET Mon–Fri | Profit-take checks, 50% CSP closes |
| `trading-eod.yml` | 4:00 PM ET Mon–Fri | EOD summary + regenerates dashboard.html |

All workflows write `trades/exec_{session}_{date}.md` and commit to main.

---

## Key Files

| File | Purpose |
|---|---|
| `scripts/trading_agent.py` | Main bot — all strategy logic |
| `trades/exec_eod_*.md` | Confirmed EOD account state (equity, SPY, options BP) |
| `trades/dashboard.html` | Auto-generated HTML chart dashboard (updates every EOD) |
| `trades/log.md` | Manual performance tracker and benchmark |
| `.env` | Alpaca paper API credentials (auto-loaded by script) |
| `PLAN.md` | Full v2.0 strategy document |

---

## Strategy State (v2.1 — June Sprint, updated 2026-06-11)

**Layer 1 — Core ETFs (targets):**
- QQQ: 50 shares, SPY: 13, JETS: 80, XLE: 100
- XLY REMOVED: closing position via `FORCE_CLOSE_EQUITY` — June sprint exit

**Layer 2 — Cash-Secured Puts (The Wheel):**
- `CSP_TARGETS` in `trading_agent.py` — current targets: NVDA ($190P Jul18), AMZN ($215P)
- AMZN re-added at $215P (~14% OTM) — previous $250P Jun26 closed at a loss (too close)
- TSLA removed from targets (re-enter only when IV > 40, manually)
- INTC removed from targets (v2.0 strategy does not target INTC)
- `CSP_MIN_PREMIUM = 1.50` — bot skips contracts below this limit price
- `CSP_CLOSE_PCT = 0.50` — auto-closes at 50% profit
- `OPT_DTE_MIN = 25`, `OPT_DTE_MAX = 60`

**Layer 2b — Call Buying (June Alpha):**
- `CALL_TARGETS` — QQQ: 1 contract, 2% OTM, `CALL_DTE_MIN=10`, `CALL_DTE_MAX=20`
- Buys at open if no long QQQ options already held
- Objective: leveraged upside exposure for June sprint vs SPY

**IPO Watchlist (auto-buy on first available day):**
- SPCX (SpaceX): 15 shares — pricing June 11, debut June 12
- ANTHROPIC: 10 shares — ~Oct 23, 2026 IPO (post June reset)
- OPENAI: 8 shares — Sept-Nov 2026 IPO (post June reset)
- Bot checks Alpaca asset status at each open session; buys on first available day

**Key discovery:** Alpaca paper cancels options GTC orders at session end. Orders that don't fill intraday are gone by next morning. BP appears reduced midday (reservation) but recovers by EOD if unfilled.

---

## Account Basics

- Starting capital: $100,000 (May 7, 2026)
- Benchmark: SPY at $731.53
- Account floor: $87,500 (bot halts new positions below this)
- Alpaca paper API: `paper-api.alpaca.markets/v2` — accessible locally AND from GitHub Actions
- Credentials: `.env` in repo root (auto-loaded)

---

## XLE Trigger Rules (Iran/Oil thesis)

| Trigger | Action |
|---|---|
| Brent ≤ $90 | Sell 30 XLE at market |
| Brent ≤ $85 | Sell all remaining XLE |
| Iran MOU signed | Sell 60 XLE at market immediately |
| JETS ≥ $35.69 (+30%) | Close all 80 JETS shares |

These are **manual** — the bot does not execute them automatically.

---

## Common Tasks

| Task | What to do |
|---|---|
| Check account state | Use Alpaca MCP or `--dry-run` locally |
| Review today's trades | Read `trades/exec_open_{today}.md`, `exec_eod_{today}.md` |
| View performance chart | Open `trades/dashboard.html` in browser |
| Add/remove CSP target | Edit `CSP_TARGETS` in `scripts/trading_agent.py` |
| Force a dry-run locally | `.venv/bin/python scripts/trading_agent.py --session open --dry-run` |
