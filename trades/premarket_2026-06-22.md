# Premarket Summary — 2026-06-22 (Monday)

> **⚠️ URGENT: XLE exit triggers remain active — sell 100 XLE at open. GitHub Actions did NOT run Friday June 20 — verify bot resumes today.**

---

## Header

- **API status:** UNAVAILABLE (Alpaca paper API unreachable from this environment)
- **Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18 — most recent authoritative source; no exec files exist for June 19 [Juneteenth] or June 20 [bot did not run])
- **Market context:** S&P 500 futures -0.19% premarket; oil sinking (-2.1%) on Iran supply ramp; AI/chip names positive (NVDA +3.08%, AMD +5.27%). PCE inflation print due Thursday — main macro event this week.

---

## Account Snapshot (exec_eod_2026-06-18 — last confirmed)

| Metric | Value |
|---|---|
| Equity | $102,108.69 |
| Our return (inception) | +2.11% |
| SPY return | +2.31% ($748.46) |
| Alpha | -0.21% vs SPY |
| Options BP remaining | $73,470.00 |
| Account floor | $87,500 (bot halts new positions below this) |

> Note: No exec files for June 20. Equity estimate is unchanged from June 18 close (market was open June 20 but bot did not run). Actual equity will be confirmed by today's exec_open file after GitHub Actions runs at 9:30 AM ET.

---

## Current Positions

**Layer 1 — Core ETFs** *(from eod_2026-06-19 narrative — no bot-confirmed June 20 update)*

| Symbol | Shares | Target | Status |
|---|---|---|---|
| QQQ | 50 | 50 | At target |
| SPY | 13 | 13 | At target |
| JETS | 80 | 80 | At target — $30.87 today, trigger at $35.69 |
| **XLE** | **100** | **EXIT** | 🔴 **ALL 3 EXIT TRIGGERS ACTIVE — 6+ sessions overdue** |
| SPCX | 15 | 15 | SpaceX IPO position, held since Jun 17 |
| XLY | Closing | 0 | FORCE_CLOSE_EQUITY in progress (June sprint exit) |

**Layer 2 — Open CSPs** *(Layer 2 entered weekend FLAT — all orders canceled by Alpaca at June 18 close)*

| Position | Strike | Expiry | Status |
|---|---|---|---|
| NVDA CSP | $190P | Jul 18 | FLAT — bot will re-attempt at today's open (26 DTE, barely within OPT_DTE_MIN=25) |
| AMZN CSP | $220P | Jul 17 | FLAT — June 18 attempt at $2.20 limit did not fill (closed ~$2.32); bot re-attempts today |

**Layer 2b — QQQ Calls**
- FLAT. Bot evaluates at open: targets ~$740 strike (2% OTM on QQQ ~$724), DTE 10–20. Buys if no long QQQ options held.

---

## ⚠️ IRAN / OIL STATUS — CRITICAL

| Item | Status |
|---|---|
| Iran MOU signed? | ✅ **YES — signed June 15 (digital) / June 18 (Versailles ceremony)** |
| Strait of Hormuz | ✅ **OPEN** — shipping fully resumed; Iranian crude tankers transiting |
| Brent crude today | **$78.41/bbl (-2.1%)** — down from $80.59 Jun 19 |
| vs $90 trim trigger | **$11.59 below — TRIGGERED** |
| vs $85 exit trigger | **$6.59 below — TRIGGERED** |
| Iran MOU trigger | **TRIGGERED (Day 6+)** |
| Structural outlook | Hormuz supply supply ramp accelerating; Brent likely continues lower toward $70s as Iranian crude reaches markets |

**All three XLE exit rules are simultaneously breached.** XLE is trading ~$53.77 today (down from ~$54.67 prior close). The longer the position is held, the more exposure to continued oil price decline.

---

## Manual Triggers — Status as of 2026-06-22

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90.00 | $78.41 | 🔴 **TRIGGERED — $11.59 below** |
| Brent ≤ $85 → exit ALL XLE | $85.00 | $78.41 | 🔴 **TRIGGERED — $6.59 below** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed Jun 15/18 | 🔴 **TRIGGERED — Day 6+** |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 | ~$30.87 | 🟢 Clear — $4.82 gap (~15.6%) |
| Equity < $87,500 → halt | $87,500 | $102,108.69 | 🟢 Clear — $14,608 headroom |

---

## ⚠️ GITHUB ACTIONS GAP — Friday June 20

No exec_open, exec_midday, or exec_eod files exist for June 20, 2026 (Friday — a regular trading day). GitHub Actions did not appear to run. Possible causes:
- Workflow failure (check GitHub Actions run history in the repo)
- Scheduled trigger skipped due to holiday-adjacent timing
- Repo/workflow configuration issue

**Action needed:** Verify GitHub Actions ran (or failed) on June 20. Confirm today's 9:30 AM run fires correctly. If the June 20 gap resulted in missed CSP placement, that's acceptable (Layer 2 was flat anyway). More importantly, if the XLE position moved while the bot was offline, today's exec_open will be the first confirmation of actual account state.

---

## Morning Priority Actions

1. **🔴 CRITICAL: Sell ALL 100 XLE shares at market open** — All three manual triggers are active simultaneously. XLE is ~$53.77, down from $55+ before the Iran deal. Delay costs money in a confirmed structural oil downtrend. At 100 shares × $53.77 ≈ $5,377 in proceeds. Do this manually — the bot does not auto-execute manual triggers.

2. **⚠️ Verify GitHub Actions resumes today** — No exec files from June 20. Confirm the 9:30 AM trading-open workflow fires and creates exec_open_2026-06-22.md. If it doesn't fire, manually trigger or investigate the workflow.

3. **ℹ️ Watch JETS today** — Iran peace dividend + lower jet fuel costs is a structural tailwind for airlines. JETS at ~$30.87 is 15.6% below the $35.69 exit trigger. A strong risk-on open could accelerate the move. Have a sell order ready if it approaches $35.69.

---

## Risk Flags

- **XLE exit overdue:** Structural oil bear (Iran supply ramp) + all 3 triggers active + Brent now $78.41 and falling. Each session of inaction increases realized loss potential. The $90 trigger was first breached ~June 11–12; Brent has since fallen further.
- **Bot gap June 20:** Unknown whether positions changed on June 20 without bot monitoring. Layer 2 was flat entering the weekend, so no options exposure risk. Today's exec_open will confirm actual account state.
- **NVDA CSP window tightening:** Jul18 expiry = 26 DTE from today — within OPT_DTE_MIN=25 window but barely. If bot doesn't fill today, the window closes. Watch exec_open for fill confirmation.
- **AMZN CSP limit:** $220P Jul17 unfilled at $2.20 limit on June 18 (market was $2.32). Bot retries today; if AMZN has moved further, limit may need manual adjustment.
- **PCE Thursday:** Core PCE print is the week's key macro risk. A hot print could revive rate-hike fears and pressure equities. Both CSP positions and QQQ call are exposed to a volatility spike.
- **AI/Chip sector positive today:** NVDA +3.08%, AMD +5.27% premarket — helps NVDA CSP stay OTM and benefits Layer 2b. AMD announced a 6-GW multi-year deal with Meta for MI450 GPUs, boosting sector sentiment broadly.

---

## Sources

- Iran MOU / Hormuz: [NPR — Trump-Iran agreement](https://www.npr.org/2026/06/19/nx-s1-5863544/trump-us-iran-agreement) · [Al Jazeera — 14-point plan details](https://www.aljazeera.com/news/2026/6/18/what-the-trump-iran-14-point-plan-says-about-lebanon-hormuz-and-uranium)
- Brent crude $78.41 (-2.1%): [Trading Economics — Brent crude](https://tradingeconomics.com/commodity/brent-crude-oil) · [ICE Brent Futures](https://www.ice.com/products/219/Brent-Crude-Futures/data)
- XLE $53.77: [Investing.com XLE](https://www.investing.com/etfs/spdr-energy-select-sector-fund)
- JETS ~$30.87: [Yahoo Finance JETS](https://finance.yahoo.com/quote/JETS/)
- S&P 500 futures -0.19%: [CNBC live updates](https://www.cnbc.com/2026/06/21/stock-market-today-live-updates.html)
- NVDA/AMD news: [Investing.com AMD Meta deal](https://www.investing.com/analysis/amd-breaks-nvidias-ai-monopoly-5-chip-stocks-to-own-200675586) · [BofA chip outlook](https://seekingalpha.com/news/4592277-nvidia-amd-still-among-bofas-top-chip-stocks-as-ai-likely-to-stay-stronger-for-longer)
