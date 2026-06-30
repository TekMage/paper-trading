# Premarket Summary — Tuesday, June 30, 2026

> **🔴🔴 CRITICAL: (1) GitHub Actions DOWN — Day 16; 21+ missed bot sessions since June 18. (2) XLE exit: ALL 3 triggers active for 15+ days — DID YOU SELL YESTERDAY? No exec file confirms June 29 action. If still held, SELL 100 XLE AT OPEN TODAY. (3) Iran MOU intact (60-day clock running); US-Iran talks in Doha expected. (4) Brent ~$72.4 — all price thresholds still breached. (5) LAST DAY OF Q2 — markets near records: Dow 52K, S&P 7,440, Nasdaq 25,820.**

---

## Header

| Item | Value |
|---|---|
| **API status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **Last confirmed equity** | $102,108.69 (exec_eod_2026-06-18 — **12 calendar days / 8 trading sessions stale**) |
| **Market context** | Q2 final day — S&P futures +0.2%, Nasdaq flat after yesterday's record close (S&P 7,440 / Dow 52,182 / Nasdaq 25,820) |
| **Most recent authoritative file** | exec_eod_2026-06-18 (no exec files since; Actions down) |

---

## Account Snapshot

> ⚠️ All figures from exec_eod_2026-06-18. GitHub Actions has not committed a bot run since June 18 (Day 16). API unavailable. True equity unknown — likely moved with markets (S&P +~5% from June 18 SPY $748.46).

| Metric | Value | Source |
|---|---|---|
| Equity | **$102,108.69** | exec_eod_2026-06-18 — stale |
| Our return (inception) | **+2.11%** | vs. SPY +2.31% at June 18 |
| SPY at last confirmed | $748.46 | June 18 EOD |
| Options BP remaining | **$73,470.00** | June 18 EOD |
| Estimated current equity | **~$105–107K** | Rough estimate: QQQ/SPY markets +5% since June 18; XLE drag; unconfirmed |

---

## Current Positions

> ⚠️ No exec files exist after June 18. Bot has not run. Positions below are last confirmed state. Manual XLE action from June 29 is UNCONFIRMED — no exec file to verify.

**Layer 1 — Core ETFs (last confirmed June 18; bot offline):**

| Symbol | Shares | Target | Price (Jun 26 est.) | Status |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$510+ | At target — monitor for June 30 Q2 rebalancing flows |
| SPY | 13 | 13 | ~$755+ | At target |
| JETS | 80 | 80 | ~$33 | At target — $2.69 gap to $35.69 trigger |
| **XLE** | **100 (unconfirmed)** | **EXIT** | **~$53–54** | 🔴🔴🔴 **ALL 3 TRIGGERS ACTIVE 15+ DAYS — June 29 sell UNCONFIRMED. If still held, SELL AT OPEN TODAY.** |
| SPCX | 15 | 15 | — | SpaceX IPO position; hold |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY pending bot resumption |

**Layer 2 — Open CSPs:**

**FLAT.** No open options positions confirmed since June 18.

| Target | Status |
|---|---|
| NVDA $190P | 🔴 **DO NOT OPEN** — NVDA at ~$193.96 (Jun 26), only ~$3.96 OTM (~2%). Intraday swing can put this ITM. Wait for NVDA > $205. |
| AMZN $215P | ⚠️ Acceptable cushion (~6% OTM at ~$227) — await bot resumption before opening |

**Layer 2b — QQQ Calls:** FLAT. No open calls.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran MOU | ✅ **Signed June 17** (Islamabad Memorandum — 60-day ceasefire framework) |
| MOU status today | ✅ **INTACT** — US and Iran signaling engagement; talks in Doha being planned (Jun 30 headlines) |
| June 26 Drone Attack | 🟡 Trump called it "foolish violation" but did not void MOU — MOU structurally intact |
| Brent crude today | **~$72.4/bbl** (down ~1% today; fell from ~$73.85 Jun 26 close) |
| Distance from $90 trigger | ~$17.60 below — 🔴 TRIGGERED |
| Distance from $85 trigger | ~$12.60 below — 🔴 TRIGGERED |
| Iran MOU trigger | Signed June 17 — 🔴 TRIGGERED |

**Note:** Oil fell today on Doha talks optimism (markets pricing further de-escalation). Brent bear trend intact. No reversal of XLE exit thesis.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | ~$72.4 | 🔴 **TRIGGERED — Day 15+** |
| Brent ≤ $85 → exit all XLE | $85 | ~$72.4 | 🔴 **TRIGGERED — Day 15+** |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED — Day 15+** |
| JETS ≥ $35.69 (+30%) → close all 80 | $35.69 | ~$33 (Jun 26 est.) | 🟢 Clear — ~$2.69 gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102K (stale) | 🟢 Estimated clear |

---

## Morning Priority Actions

1. **🔴 CONFIRM XLE STATUS — Did you sell June 29?**
   Yesterday's premarket called for selling 100 XLE at open. No exec file was committed to confirm this. If XLE is still held:
   - **SELL 100 XLE AT MARKET AT OPEN TODAY (9:30 AM ET)**
   - All 3 exit rules have been active for 15+ days. Brent fell further overnight to $72.4. Estimated proceeds: 100 × ~$54 ≈ **~$5,400 cash**.
   - This is the last day of Q2; execution today avoids another weekend of unhedged oil/geopolitical risk.

2. **🔴 FIX GITHUB ACTIONS — Day 16 offline**
   Go to `github.com/TekMage/paper-trading/actions`. Check `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`. The bot has missed 21+ sessions (3 sessions × 7+ trading days). Without it: no CSP entries, no auto-closes, no rebalancing, no equity tracking. Every day down is missed Layer 2 premium income.
   - When bot resumes: verify NVDA $190P target — strike too close, manually override or adjust to $185P or $180P.
   - When bot resumes: XLY FORCE_CLOSE should execute automatically.

3. **⚠️ Q2 End — Window-Dressing / Rebalancing Flows Today**
   Today is the final session of Q2 2026. Expect elevated volume and potential volatility. Large funds may push winners (QQQ/tech names) higher into the close or rebalance out of laggards. Good context for any manual trades: prefer limit orders over market orders today, especially for options.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions offline — Day 16 | 🔴 CRITICAL | 21+ missed sessions; equity figure 8 trading sessions stale; no Layer 2 entries, no auto-closes |
| XLE exit UNCONFIRMED | 🔴 CRITICAL | June 29 sell may not have executed; all 3 triggers active 15+ days; $5,400 trapped in exiting position |
| NVDA $190P strike too close | 🔴 HIGH | NVDA at ~$193.96 (Jun 26) — only 2% OTM. If bot resumes without strike adjustment, CSP will be opened dangerously close to ITM |
| Iran 60-day clock running | 🟡 MEDIUM | MOU expires ~Aug 16. Doha talks upcoming — risk of breakdown or positive surprise. Watch for headlines |
| Q2 end volatility | 🟡 MEDIUM | Window-dressing can spike individual names both ways; options pricing elevated; avoid new positions at open |
| Account figures 8 sessions stale | 🟡 MEDIUM | Actual equity unknown; no live API access; rough estimate ~$105-107K based on market gains since June 18 |
| NVDA underperforming semiconductors | 🟡 MEDIUM | NVDA +7.3% YTD vs. SOX +90% YTD — relative underperformance; Vera Rubin shipments this fall could catalyze |
| XLY FORCE_CLOSE pending | 🟡 LOW | Queued in bot but bot offline; position status unknown since June 18 |

---

## Market Context (Q2 Close)

| Index | Jun 29 close | Status |
|---|---|---|
| Dow Jones | 52,182 | All-time record |
| S&P 500 | 7,440 | Near all-time high |
| Nasdaq Composite | 25,820 | Near all-time high |
| S&P 500 futures (Jun 30) | +0.2% premarket | Slight green — continuation |
| Nasdaq futures (Jun 30) | Flat | Consolidating near highs |

**NVDA:** ~$193.96 as of Jun 26 close; +7.3% YTD, underperforming SOX index. Vera Rubin GPU in full production, H2 catalyst expected. Q1 FY27 revenue $81.6B (+85% YoY).

---

*Sources: [Iran MOU — CNN](https://www.cnn.com/2026/06/18/world/live-news/iran-war-trump-israel-lebanon) · [Iran MOU terms — NPR](https://www.npr.org/2026/06/19/nx-s1-5863544/trump-us-iran-agreement) · [Brent crude Jun 30 — HDFCSky](https://hdfcsky.com/news/brent-crude-oil-price-today-june-30-2026-crude-oil-price-fall-1percent-to-72-4-as-markets-await-clarity-on-potential-us-iran-talks-in-doha) · [S&P 500 futures Jun 30 — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-30-2026) · [Dow record Jun 29 — Yahoo Finance](https://finance.yahoo.com/markets/stocks/live/stock-market-today-monday-june-29-224230573.html) · [NVDA semiconductor outlook — AOL/Yahoo](https://www.aol.com/articles/nvidia-stock-underperformed-semiconductor-sector-135900000.html) · exec_eod_2026-06-18 (last authoritative bot file)*
