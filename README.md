# Paper Trading Test — $110k by 2026-11-30

**Account:** PA37YW74AICR (Alpaca paper only)
**Starting capital:** $100,000 on 2026-05-07
**Hard end:** close of 2026-11-30, the last full NYSE session of November (2026-11-27 is a half day)
**Score:** account equity, not SPY alpha
**Floor:** pause new risk below $80,000. Still manage open options.

**Goal:** $110,000 account value by the hard end. That is the end of this test. Beating the S&P is no longer the mandate.

Live marks move. As of the 2026-09-24 redeploy: equity about $103,349, cash about $52,093. Gap to the goal was about $6,651.

---

## What changed on 2026-09-24

The old plan (beat SPY by ≥5%, hold SPCX for recovery) is retired for this test.

- Sold 15 SPCX at market, fill $147.41 ($2,211.15). Order `f8354b6b-e3e4-4002-9778-db31ba68b07f`. Do not rebuy. `spcx_blocked` is true in `agents/config/strategy_config.json`.
- Put the proceeds into 1 QQQ Nov 20 2026 750 call, fill $21.43 ($2,143). Order `71a2197d-b8a5-45bc-a8c2-39496f44f768`.
- The harness may buy QQQ calls even when the HMM says Normal Bear (`yolo_max_value`). The $80k floor still stops new risk.
- Short options still take profit at ≥50%. Cash-secured CSPs stay the income leg. Paper only.

Older PLAN.md sections (Iran pivot, June sprint, SPCX hold) are history. Do not restore them.

---

## Harness

Config is `agents/config/strategy_config.json`. Runners:

- `agents/research_agent_runner.py` — brief, headline filter, bounded self-correct
- `agents/trading_agent_runner.py` — manage shorts, cash-secured CSPs, QQQ call slot
- `agents/news_relevance.py` — TypeSafe headline filter (cutoff 0.60, fail-open)

`TYPESAFE_API_KEY` and Alpaca keys stay in `~/.hermes/.env`. Do not commit them.

Daily research briefs and `trades/exec_*` / `trades/cycles/` are run logs. They are not the code backup and stay untracked on purpose.

---

## Rules that still bind

- Paper API only (`https://paper-api.alpaca.markets`). No live orders.
- New risk pauses if equity is under $80,000.
- One short put per underlying. Size the sum of proposed 1-lots against cash, not each name alone.
- Do not rebuy SPCX.
