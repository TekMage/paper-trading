# Premarket Summary — Monday, July 6, 2026 (Q3 Day 4)

> **🔴🔴🔴 CRITICAL: (1) GitHub Actions STILL DOWN — Day 21; 33+ total missed sessions since June 18. (2) XLE exit: ALL 3 TRIGGERS ACTIVE Day 21 — unknown if sold over holiday weekend; verify and sell immediately at 9:30 AM open if still held. (3) NFP 57K miss carries forward — Nasdaq futures +1.1% premarket; September rate cut firmly in play; QQQ call entry viable today. (4) Brent $71.88/bbl — OPEC+ approved August output hike; structural oil bear thesis intact and reinforced. (5) Iran MOU intact — diplomatic round post-Khamenei funeral (Jul 4–9) expected this week. (6) NVDA AH ~$197 Thursday + Nasdaq premarket surge: may open $199–203 — $200 CSP entry threshold watch.**

---

## Header

| Item | Value |
|---|---|
| **API status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **Last confirmed equity** | $102,108.69 (exec_eod_2026-06-18 — **12 trading sessions stale**) |
| **Market status** | OPEN — 9:30 AM ET normal session. First day back from 3-day holiday weekend. |
| **Authoritative source** | exec_eod_2026-06-18 (no exec files since; GitHub Actions offline since June 18) |
| **GitHub Actions** | 🔴 DOWN — Day 21; last trading bot run June 18, 2026 |

---

## Account Snapshot

> ⚠️ All confirmed figures from exec_eod_2026-06-18 — 12 trading sessions stale. No API. Actual equity unknown.

| Metric | Value | Source |
|---|---|---|
| Equity | **$102,108.69** | exec_eod_2026-06-18 — stale |
| Our return (inception) | **+2.11%** | June 18 baseline |
| SPY at last confirmed | $748.46 | June 18 EOD |
| Options BP remaining | **$73,470.00** | June 18 EOD — Layer 2 FLAT since |
| API status | UNAVAILABLE | Alpaca unreachable from this environment |

> Rough equity estimate (unconfirmed): ~$104–110K based on QQQ +~3.5% and SPY +~0–1% from June 18 baseline, partially offset by XLE drag (~-7% if still held). Do not trade on estimate.

---

## Current Positions (from exec_eod_2026-06-18; unconfirmed 12 sessions)

> ⚠️ GitHub Actions offline. XLE exit status unknown. No bot rebalancing for 12 trading sessions.

**Layer 1 — Core ETFs (last confirmed June 18):**

| Symbol | Shares | Target | Status |
|---|---|---|---|
| QQQ | 50 | 50 | At target — unconfirmed 12 sessions |
| SPY | 13 | 13 | At target — unconfirmed 12 sessions |
| JETS | 80 | 80 | At target — ~$2.69 gap to $35.69 trigger (est.) |
| **XLE** | **100 or 0 (UNKNOWN)** | **EXIT** | 🔴🔴🔴 **CRITICAL — ALL 3 EXIT TRIGGERS ACTIVE DAY 21. Must verify at open; sell immediately if still held.** |
| SPCX | 15 | 15 | SpaceX IPO hold — unconfirmed |
| XLY | Closing | 0 | FORCE_CLOSE_EQUITY queued — bot offline; unexecuted |

**Layer 2 — Open CSPs:**

FLAT. No confirmed open options since June 18.

| Target | Strike | Expiry | DTE (Jul 6) | Est. Underlying | OTM% | Status |
|---|---|---|---|---|---|---|
| NVDA | $185P Aug21 | Aug 21 | 46 DTE | ~$199–203 (est.) | ~8–9% | ⚠️ Config still shows old $190P Jul18 — update before bot runs. Entry only if NVDA holds $200+ at open. |
| AMZN | $215P | Aug 21 | 46 DTE | ~$243–247 (est.) | ~11–13% | ✅ Strong cushion — solid candidate on bot resumption |

**Layer 2b — QQQ Calls:** FLAT. Rate-cut tailwind (NFP miss) + Nasdaq +1.1% premarket = viable entry today if QQQ opens above $730 and holds. Do not pre-commit; reassess after first 30 min.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| **Iran MOU ("Islamabad Memorandum," signed Jun 17)** | ✅ **INTACT** — 60-day clock running; expires ~Aug 16 |
| Doha talks (July 1–2) | Concluded — "positive progress" on Hormuz mechanics; nuclear issues unresolved |
| Current diplomatic status | **PAUSED** — Khamenei funeral ceremonies July 4–9 (burial Mashhad July 9) |
| Next round | Post-funeral this week; both sides committed; JD Vance Qatar meeting being arranged |
| Hormuz Strait | 35+ commercial vessels/day; toll-free per MOU; MOU structurally intact |
| **Brent crude (July 6)** | **~$71.88/bbl** — slipped below $72, easing 0.33%; OPEC+ approved August output hike |
| OPEC+ August hike | Approved — additional supply headwind for oil; reinforces structural bear thesis |
| vs $90 trigger | ~$18.12 below — 🔴 **TRIGGERED (Day 21)** |
| vs $85 trigger | ~$13.12 below — 🔴 **TRIGGERED (Day 21)** |
| Iran MOU trigger | Signed June 17 — 🔴 **TRIGGERED (Day 21)** |

**Interpretation:** Brent easing to $71.88 on OPEC+ August hike approval. Iranian + Russian barrels flowing freely. No Hormuz re-closure risk through at least late July. Diplomatic talks resume post-funeral this week — watch for any indication of deal breakdown that could spike oil. Otherwise the structural XLE exit thesis is fully intact and further deteriorating.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | $71.88 | 🔴 **TRIGGERED (Day 21)** |
| Brent ≤ $85 → exit ALL XLE | $85 | $71.88 | 🔴 **TRIGGERED (Day 21)** |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED (Day 21)** |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 | $35.69 | ~$33 est. | 🟢 Clear — ~$2.69 gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102K+ (stale) | 🟢 Estimated clear |

---

## Morning Priority Actions

**1. 🔴 IMMEDIATE AT 9:30 AM ET — VERIFY AND EXIT XLE**
Open Alpaca dashboard or paper-api.alpaca.markets. If XLE is still held (100 shares), submit market sell immediately. All 3 exit triggers have been active for 21 trading days. No further delay justified. Estimated proceeds: ~100 × $52–54 ≈ $5,200–$5,400. Realized loss: ~-$300 to -$500 vs $57.00 avg cost — acceptable given thesis is fully confirmed.

**2. 🔴 FIX GITHUB ACTIONS TODAY**
Go to github.com/TekMage/paper-trading/actions and re-enable `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`. Day 21 of outage = 33+ missed sessions, zero premium collected since June 18, undetected position drift. Before bot's first run: (a) change `CSP_TARGETS` NVDA strike from `$190P Jul18` → `$185P Aug21`, (b) confirm XLY FORCE_CLOSE is queued, (c) verify equity floor.

**3. ⚠️ NFP FOLLOW-THROUGH — QQQ CALL ENTRY WATCH**
Nasdaq-100 futures +1.1% premarket driven by NFP rate-cut thesis and Morgan Stanley chip sector upgrades (LARC, AMAT, KLAC price targets hiked). If QQQ opens above $730 and holds after the first 30 minutes, 2% OTM 10–20 DTE calls are viable. Do not chase momentum at open — wait for stabilization.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| XLE exit status UNKNOWN | 🔴 CRITICAL | All 3 exit triggers active Day 21. Unknown if sold over holiday. Verify and act immediately at open. |
| GitHub Actions DOWN — Day 21 | 🔴 CRITICAL | No trading bot since June 18; 33+ missed sessions; no Layer 2 premium collected; XLY FORCE_CLOSE unexecuted |
| NVDA $190P Jul18 still in config | 🔴 HIGH | Jul18 expiry permanently below OPT_DTE_MIN=25. Must update to $185P Aug21 before bot resumes. At ~$200, even $185P may be too close — wait for $200+ hold before entry. |
| Iran MOU expiry ~Aug 16 | 🟡 MEDIUM | ~41 days remaining; nuclear talks unresolved; single breakdown could spike Brent and reverse XLE thesis |
| Post-funeral diplomacy this week | 🟡 MEDIUM | Khamenei funeral concludes July 9; next Iran/US round expected shortly after; oil catalyst watch |
| NVDA CSP entry timing | 🟡 MEDIUM | NVDA AH ~$197 Thursday + Nasdaq +1.1% premarket = may open ~$200. $185P at $200 = 7.5% OTM — acceptable if confirmed. Do not enter below $200. |
| Account figures 12 sessions stale | 🟡 MEDIUM | Last confirmed equity June 18; rough est. ~$104–110K unverified. Bot fix is prerequisite for accurate tracking. |
| XLY FORCE_CLOSE pending | 🟡 LOW | Queued in bot; executes automatically on bot resumption |

---

## Overnight Market Intel

| Topic | Summary |
|---|---|
| **S&P 500 futures** | +0.4% premarket — constructive open expected |
| **Nasdaq-100 futures** | **+1.1%** — chip stocks leading; Morgan Stanley price target hikes on Lam Research, Applied Materials, KLA |
| **Brent crude** | **$71.88/bbl** (-0.33%) — OPEC+ approved August output hike; Brent slips below $72 |
| WTI crude | ~$68.5/bbl — parallel move to Brent |
| **NFP June** | 57K vs 110K expected — big miss; September rate cut firmly on table; QQQ +1.73% on July 2 close |
| **NVDA** | ~$193–194 July 2 close; AH +1.9% to ~$197; premarket estimate ~$199–203 with Nasdaq surge |
| **AMZN** | ~$243–247 est. — strong cushion vs $215P CSP target (~11–13% OTM) |
| **Iran / MOU** | Intact — Khamenei funeral July 4–9; next diplomatic round expected this week post-funeral |
| **OPEC+** | Approved August production output hike — additional downward pressure on Brent/WTI |
| **GitHub Actions** | STILL DOWN — Day 21 confirmed via GitHub API; last trading run: exec_eod_2026-06-18 |

---

*Sources: exec_eod_2026-06-18 (authoritative) · eod_2026-07-02.md · [Sunday Guardian — Brent $71.88 Jul 6](https://sundayguardianlive.com/business/brent-crude-oil-price-today-july-6-brent-slips-below-72-wti-falls-near-685-as-opec-approves-august-output-hike-check-latest-brent-crude-wti-oil-rates-today-228673/) · [HDFCSky — Brent Jul 6](https://hdfcsky.com/news/url-brent-crude-oil-price-today-july-6-2026-oil-prices-ease-as-opec-aims-to-bump-up-output-from-august-brent-below-72) · [CNBC — Nasdaq futures Jul 6](https://www.cnbc.com/2026/07/05/stock-market-today-live-updates.html) · [FXStreet — NFP 57K miss](https://www.fxstreet.com/news/nonfarm-payrolls-set-to-grow-by-over-100k-in-june-reinforcing-bets-of-upcoming-fed-rate-hikes-202607020500) · [NBC News — Iran MOU](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513) · [Axios — Iran ceasefire extended](https://www.axios.com/2026/06/14/us-iran-ceasefire-extended-hormuz-reopen-trump) · GitHub Actions API (confirmed last run: 2026-06-18T22:28:52Z)*
