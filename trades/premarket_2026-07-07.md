# Premarket Summary — Tuesday, July 7, 2026 (Q3 Day 5)

> **🔴🔴🔴 CRITICAL: (1) GitHub Actions STILL DOWN — Day 22; 36+ total missed sessions since June 18. (2) XLE exit: ALL 3 TRIGGERS ACTIVE Day 22 — verify and sell immediately at 9:30 AM open if still held. (3) GLOBAL CHIP SELLOFF: Nasdaq-100 futures -1%; Samsung earnings disappoint; Micron -5%, AMD -4% premarket — QQQ call entry NOT viable today. (4) NVDA ~$190.75 premarket (-2.45%): $185P CSP strike now ~3% OTM — growing risk on bot resumption. (5) SPCX Nasdaq-100 inclusion today (Jul 7): $4.3B passive inflows — positive catalyst for 15-share position. (6) Brent $72.89/bbl — all XLE exit triggers remain active; Iran MOU intact.**

---

## Header

| Item | Value |
|---|---|
| **API status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **Last confirmed equity** | $102,108.69 (exec_eod_2026-06-18 — **13 trading sessions stale**) |
| **Market status** | Pre-market — opens 9:30 AM ET. Global chip selloff overnight. |
| **Authoritative source** | exec_eod_2026-06-18 (no exec files since; GitHub Actions offline since June 18) |
| **GitHub Actions** | 🔴 DOWN — Day 22; last trading bot run June 18, 2026 |

---

## Account Snapshot

> ⚠️ All confirmed figures from exec_eod_2026-06-18 — 13 trading sessions stale. No API. Actual equity unknown.

| Metric | Value | Source |
|---|---|---|
| Equity | **$102,108.69** | exec_eod_2026-06-18 — stale |
| Our return (inception) | **+2.11%** | June 18 baseline |
| SPY at last confirmed | $748.46 | June 18 EOD |
| Options BP remaining | **$73,470.00** | June 18 EOD — Layer 2 FLAT since |
| API status | UNAVAILABLE | Alpaca unreachable from this environment |

> Rough equity estimate (unconfirmed): Range has widened with chip selloff. QQQ-heavy portfolio facing headwinds today. Do not trade on estimate — fix GitHub Actions first.

---

## Current Positions (from exec_eod_2026-06-18; unconfirmed 13 sessions)

> ⚠️ GitHub Actions offline. XLE exit status unknown. No bot rebalancing for 13 trading sessions.

**Layer 1 — Core ETFs (last confirmed June 18):**

| Symbol | Shares | Target | Status |
|---|---|---|---|
| QQQ | 50 | 50 | At target — unconfirmed 13 sessions; facing -1% Nasdaq headwind today |
| SPY | 13 | 13 | At target — unconfirmed 13 sessions |
| JETS | 80 | 80 | At target — ~$2.69 gap to $35.69 trigger (est.) |
| **XLE** | **100 or 0 (UNKNOWN)** | **EXIT** | 🔴🔴🔴 **CRITICAL — ALL 3 EXIT TRIGGERS ACTIVE DAY 22. Verify at open; sell immediately if still held.** |
| SPCX | 15 | 15 | ✅ **Nasdaq-100 inclusion TODAY (Jul 7) — $4.3B passive inflows; positive catalyst** |
| XLY | Closing | 0 | FORCE_CLOSE_EQUITY queued — bot offline; unexecuted |

**Layer 2 — Open CSPs:**

FLAT. No confirmed open options since June 18.

| Target | Strike | Expiry | DTE (Jul 7) | Est. Underlying | OTM% | Status |
|---|---|---|---|---|---|---|
| NVDA | $185P Aug21 | Aug 21 | 45 DTE | **~$190–195 (est.)** | **~0–3%** | 🔴 **RISK: $185P may be too close to current price. Do NOT enter until NVDA stabilizes above $195+. Confirm on bot resumption.** |
| AMZN | $215P | Aug 21 | 45 DTE | ~$243–247 (est.) | ~11–13% | ✅ Strong cushion — solid candidate on bot resumption |

**Layer 2b — QQQ Calls:** ⛔ NOT viable today. Nasdaq-100 futures -1% on global chip selloff. Wait for sector stabilization.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| **Iran MOU ("Islamabad Memorandum," signed Jun 17)** | ✅ **INTACT** — 60-day clock running; ~40 days remaining (~Aug 16 expiry) |
| Post-Khamenei funeral diplomatic round | Funeral concluded July 4–9; next Iran/US round expected imminently |
| Hormuz Strait | Open; vessel traffic recovering; no re-closure risk |
| **Brent crude (July 7)** | **$72.89/bbl** (+1.26% from July 6); above $72 but near 4-month lows |
| OPEC+ August hike | Approved — additional supply headwind for oil; structural bear thesis intact |
| vs $90 trigger | ~$17.11 below — 🔴 **TRIGGERED (Day 22)** |
| vs $85 trigger | ~$12.11 below — 🔴 **TRIGGERED (Day 22)** |
| Iran MOU trigger | Signed June 17 — 🔴 **TRIGGERED (Day 22)** |

**Interpretation:** Brent edging up to $72.89 on slight short-covering but remains structurally weak on OPEC+ supply hike and Hormuz re-opening. All three XLE exit triggers have been active for 22 days. Watch for Iran diplomatic developments post-funeral this week — any breakdown could spike Brent and reverse thesis, but current trajectory supports the exit.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | $72.89 | 🔴 **TRIGGERED (Day 22)** |
| Brent ≤ $85 → exit ALL XLE | $85 | $72.89 | 🔴 **TRIGGERED (Day 22)** |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED (Day 22)** |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 | $35.69 | ~$33 est. | 🟢 Clear — ~$2.69 gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102K+ (stale) | 🟢 Estimated clear |

---

## Morning Priority Actions

**1. 🔴 IMMEDIATE AT 9:30 AM ET — VERIFY AND EXIT XLE**
Open Alpaca dashboard. If XLE is still held (100 shares), submit market sell immediately. All 3 exit triggers have been active for 22 days. Estimated proceeds: ~100 × $52–54 ≈ $5,200–$5,400.

**2. 🔴 FIX GITHUB ACTIONS TODAY**
Go to github.com/TekMage/paper-trading/actions and re-enable `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`. Day 22 of outage = 36+ missed sessions, zero premium collected since June 18. Before bot's first run: (a) hold NVDA CSP entry — $185P too close at current ~$190–195 price; wait for $195+ stability, (b) confirm XLY FORCE_CLOSE is queued, (c) verify AMZN $215P Aug21 target is current.

**3. ⚠️ MONITOR SPCX AT OPEN**
SpaceX joins Nasdaq-100 today (July 7) — index funds must buy to track the index, with ~$4.3B in estimated passive inflows. SPCX IPO surged 50% on debut but has since fallen 28% from ATH. Inclusion-day bounce possible; do not add to position on hype — monitor and hold the existing 15 shares.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| XLE exit status UNKNOWN | 🔴 CRITICAL | All 3 exit triggers active Day 22. Unknown if sold. Verify and act immediately at open. |
| GitHub Actions DOWN — Day 22 | 🔴 CRITICAL | No trading bot since June 18; 36+ missed sessions; no Layer 2 premium collected; XLY FORCE_CLOSE unexecuted |
| NVDA $185P OTM collapsed | 🔴 HIGH | NVDA ~$190.75 premarket (-2.45% on chip selloff); $185P only ~3% OTM — far below safe CSP threshold (~8–10%). Do NOT enter NVDA CSP until price stabilizes above $195+. |
| Global chip selloff | 🔴 HIGH | Samsung earnings disappoint; Micron -5%, AMD -4%, KLA, Marvell, Broadcom all down premarket. Nasdaq-100 -1%. QQQ position at risk; no call entry today. |
| Iran MOU expiry ~Aug 16 | 🟡 MEDIUM | ~40 days remaining; nuclear talks unresolved; watch post-funeral diplomatic round |
| SPCX inclusion volatility | 🟡 MEDIUM | Inclusion-day bounces historically fade; do not add to position |
| Account figures 13 sessions stale | 🟡 MEDIUM | Last confirmed equity June 18; actual equity unknown. Fix GitHub Actions before placing new positions. |
| XLY FORCE_CLOSE pending | 🟡 LOW | Queued in bot; executes automatically on bot resumption |

---

## Overnight Market Intel

| Topic | Summary |
|---|---|
| **S&P 500 futures** | -0.1% premarket — flat/slight negative |
| **Nasdaq-100 futures** | **-1.0%** — chip stocks leading selloff; rotation out of AI names |
| **Dow futures** | +0.4% — Dow diverging positive (rotation to value) |
| **Global chip selloff** | Samsung Q2 earnings: record 89.4T won profit, but misses elevated expectations. Micron -5%, AMD -4%, KLA, Marvell, Broadcom, SK Hynix all down. Spreading from Asia to US. |
| **NVDA** | ~$190.75 premarket (-2.45% from $195.55 close Jul 6). Report: next-gen AI rack delayed ~1 year. Volatile; some recovery to ~$197 seen later in premarket per one source. |
| **Brent crude** | **$72.89/bbl** (+1.26%) — slight bounce from $71.88; still near 4-month lows; OPEC+ supply hike structural headwind |
| **Iran / MOU** | Intact — 60-day window running. Post-Khamenei funeral (burial Jul 9) diplomatic round expected this week. |
| **SPCX** | Nasdaq-100 inclusion TODAY (Jul 7). ~$4.3B passive inflows from QQQ, QQQM, index funds. Stock down 28% from IPO ATH. |
| **GitHub Actions** | STILL DOWN — confirmed via GitHub API. Last trading run: 2026-06-18T22:28:52Z |

---

*Sources: exec_eod_2026-06-18 (authoritative) · [TradingEconomics — Brent Jul 7](https://tradingeconomics.com/commodity/brent-crude-oil) · [CNBC — Stock futures chip selloff Jul 7](https://www.cnbc.com/2026/07/06/stock-market-today-live-updates.html) · [Yahoo Finance — NVDA premarket rack delay](https://finance.yahoo.com/markets/stocks/articles/nvda-stock-swings-premarket-report-095928388.html) · [Yahoo Finance — Samsung chip selloff](https://finance.yahoo.com/markets/stocks/articles/micron-shares-retreat-samsung-earnings-104306083.html) · [Yahoo Finance — SPCX Nasdaq-100](https://finance.yahoo.com/markets/stocks/articles/spacex-set-nasdaq-100-debut-195400738.html) · [Motley Fool — SPCX QQQ impact](https://www.fool.com/investing/2026/07/06/spacex-joins-the-nasdaq-100-on-july-7-here-is-what/) · [Wikipedia — Iran-US negotiations](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations) · GitHub Actions API (confirmed last run: 2026-06-18)*
