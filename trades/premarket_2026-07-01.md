# Premarket Summary — Wednesday, July 1, 2026 (Q3 Opens)

> **🔴🔴🔴 CRITICAL: (1) GitHub Actions DOWN — Day 17; 24 confirmed missed sessions + 3 more today. Bot offline since June 18. (2) XLE exit: ALL 3 triggers active for Day 17 — UNCONFIRMED if sold. SELL 100 XLE AT OPEN if still held (~$53–54). (3) Iran rejected direct US face-to-face talks today — diplomatic setback; MOU intact but momentum stalling. (4) Brent ~$72.25–$73.20/bbl — all exit triggers deeply breached. (5) Markets: S&P futures -0.38% after best Q2 since 2020 (+14.9% Q2).**

---

## Header

| Item | Value |
|---|---|
| **API status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **Last confirmed equity** | $102,108.69 (exec_eod_2026-06-18 — **9 trading sessions stale**) |
| **Market context** | Q3 open — S&P futures -0.38% giving back some Q2 gains; best Q2 (S&P +14.9%) since Q2 2020; caution on open |
| **Authoritative source** | exec_eod_2026-06-18 (no exec files since; GitHub Actions down) |

---

## Account Snapshot

> ⚠️ All confirmed figures from exec_eod_2026-06-18 — 9 trading sessions stale. GitHub Actions has not committed a bot run since June 18. API unavailable. True equity unknown.

| Metric | Value | Source |
|---|---|---|
| Equity | **$102,108.69** | exec_eod_2026-06-18 — stale |
| Our return (inception) | **+2.11%** | June 18 baseline |
| SPY at last confirmed | $748.46 | June 18 EOD |
| Options BP remaining | **$73,470.00** | June 18 EOD — no Layer 2 moves since |
| API status | UNAVAILABLE | Alpaca unreachable from this environment |

---

## Current Positions

> ⚠️ No exec files after June 18. All positions reflect last confirmed bot state. No live API to verify.

**Layer 1 — Core ETFs (last confirmed June 18; bot offline 9 sessions):**

| Symbol | Shares | Target | Est. Close Jun 30 | Status |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$721 | At target |
| SPY | 13 | 13 | ~$745 | At target |
| JETS | 80 | 80 | ~$33.00 | At target — ~$2.69 gap to $35.69 trigger |
| **XLE** | **100 (unconfirmed)** | **EXIT** | **~$53.50** | 🔴🔴🔴 **ALL 3 EXIT TRIGGERS ACTIVE DAY 17 — XLE SALE UNCONFIRMED ACROSS 16 DAILY SUMMARIES. SELL AT OPEN.** |
| SPCX | 15 | 15 | — | SpaceX IPO hold |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY queued — bot offline |

**Layer 2 — Open CSPs:**

**FLAT.** No confirmed open options since June 18. Bot offline.

| Target | Strike | Expiry | DTE Today | Underlying Premarket | OTM % | Status |
|---|---|---|---|---|---|---|
| **NVDA** | **$185P*** | **Aug 21** | **51 DTE** | **~$200 (+2.58%)** | **~7.5% OTM** | ⚠️ **Approaching entry zone — need $200–205 SUSTAINED. Update bot target to $185P before resumption.** |
| AMZN | $215P | Aug 21 | 51 DTE | ~$239 (est.) | ~10.2% OTM | ✅ Strong cushion — await bot resumption |

*Note: NVDA target in `CSP_TARGETS` must be changed from $190P to $185P before bot resumes. Jul18 window (17 DTE) is permanently closed below OPT_DTE_MIN=25.*

**Layer 2b — QQQ Calls:** FLAT. PCE 4.1% + NFP Thursday = hold off until post-NFP.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran MOU (signed June 17) | ✅ **INTACT** — 60-day clock running; expires ~Aug 16 |
| Today's development | 🔴 **Iran rejected direct face-to-face talks with US envoys on July 1** — diplomatic setback |
| US delegation | Kushner/Witkoff in Doha; Iran declined to meet directly |
| Strait of Hormuz | ✅ Vessels moving freely — MOU obligates safe passage for 60 days |
| Switzerland technical talks | ❌ Postponed as of June 18; not rescheduled |
| **Brent crude today** | **~$72.25–$73.20/bbl** (Iran talk rejection caused slight upward pressure; baseline still bearish) |
| vs $90 trigger | ~$17–18 below — 🔴 **TRIGGERED (Day 17)** |
| vs $85 trigger | ~$12–13 below — 🔴 **TRIGGERED (Day 17)** |
| Iran MOU trigger | Signed June 17 — 🔴 **TRIGGERED (Day 17)** |

**Interpretation:** Iran's refusal of direct talks is a diplomatic setback but does not void the MOU — the ceasefire framework and Hormuz passage obligations remain in force. Brent ticked up slightly on the news but remains ~$17+ below the top exit threshold. The structural bear case for oil is intact: Hormuz is open, Iranian crude is flowing, and the MOU provides 60-day runway. **All 3 XLE exit triggers are deeply and unambiguously active — 17 days overdue.**

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | ~$72.50 | 🔴 **TRIGGERED — Day 17** |
| Brent ≤ $85 → exit all XLE | $85 | ~$72.50 | 🔴 **TRIGGERED — Day 17** |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED — Day 17** |
| JETS ≥ $35.69 (+30% from $27.45) → close all 80 | $35.69 | ~$33.00 (Jun 30) | 🟢 Clear — ~$2.69 gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102K (stale) | 🟢 Estimated clear |

---

## Morning Priority Actions

1. **🔴 SELL 100 XLE AT MARKET OPEN — Day 17 overdue**
   Every morning summary for 17 sessions has flagged this. If XLE is still held: sell 100 XLE at market at 9:30 AM ET today. Jun 30 range: $53.41–$54.28. Estimated proceeds at ~$53.50: **~$5,350**. Note: S&P futures are -0.38% premarket; a soft open may push XLE slightly lower — market order still appropriate given 17-day overdue status.

2. **🔴 FIX GITHUB ACTIONS — Day 17 (27 sessions missed by end of today)**
   Go to `github.com/TekMage/paper-trading/actions`. Check `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`. When bot resumes: (a) **first** update NVDA target in `CSP_TARGETS` to $185P Aug21, (b) XLY FORCE_CLOSE runs automatically, (c) verify equity floor before any new Layer 2 entries.

3. **⚠️ NVDA approaching CSP entry zone — update target first**
   NVDA premarket ~$200 (+2.58%) — first touch of the $200 level. Still need $200–205 **sustained** before CSP entry. Update `CSP_TARGETS` NVDA from `$190P` to `$185P Aug21` in `scripts/trading_agent.py` **before** bot resumes. At $200, a $185P is ~7.5% OTM — good cushion. Do not let bot enter $190P at $200 (only 5% OTM).

---

## Overnight Market Intel

| Topic | Summary |
|---|---|
| S&P 500 futures | **-0.38%** — slight pullback after strongest Q2 since 2020 (S&P +14.9% Q2, YTD +9.6%) |
| NVDA | **+2.58% premarket (~$200)** — 35 NVIDIA AI supercomputers in development across Europe (ISC 2026); Palantir sovereign AI collaboration announced |
| NVDA risk | SMCI Taiwan office raided in connection to Nvidia chip smuggling operation — sector watch |
| Marvell (MRVL) | Up 247% YTD; UBS raised PT to $340; added to S&P 500 June 22; $1B CXL revenue projected 2027 |
| AMD | Disclosed 65,516 share stake in Marvell — AI infrastructure positioning |
| Q2 retrospective | S&P +14.9% Q2 (best since Q2 2020); Nasdaq-100 tech outperformance intact; July 4 holiday Friday = short week |
| NFP Thursday Jul 3 | Hot print = rate-cut delayed (headwind for QQQ/NVDA); soft print = September cut back on table; critical for July CSP timing |
| Fed Chair Warsh | ECB Symposium panel today — watch for hawkish signal post-PCE 4.1% |

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions offline — Day 17 | 🔴 CRITICAL | 24+ missed sessions; equity 9 trading sessions stale; no Layer 2 entries or auto-closes |
| XLE exit still unconfirmed | 🔴 CRITICAL | 17 days overdue; ~$5,350 trapped; soft futures open may pressure XLE slightly at open |
| NVDA $190P target in bot — too close | 🔴 HIGH | At $200 premarket, $190P is only 5% OTM. Update to $185P before bot resumes or bot will enter a dangerously close CSP on first run |
| Iran diplomatic setback (talk rejection) | 🟡 MEDIUM | Slight upward Brent pressure; MOU structurally intact but 60-day window eroding; watch for July talks failure |
| Iran MOU expiry ~Aug 16 | 🟡 MEDIUM | ~46 days remaining; if not renewed, Hormuz risk re-emerges; watch Swiss technical talks rescheduling |
| SMCI chip smuggling / NVDA exposure | 🟡 MEDIUM | Taiwan raid in connection to Nvidia chips — regulatory/supply chain risk; monitor if DOJ expands scope to NVDA |
| NFP Thursday macro risk | 🟡 MEDIUM | Hot jobs print = September rate cut delayed; QQQ/NVDA vulnerable; avoid new CSPs before print |
| Account figures 9 sessions stale | 🟡 MEDIUM | Actual equity unknown; no live API; rough estimate ~$105–107K (QQQ/SPY up ~5% from Jun 18, offset by XLE drag if held) |
| XLY FORCE_CLOSE pending | 🟡 LOW | Queued in bot; position status unknown since June 18 |

---

*Sources: [Brent crude Jul 1 — HDFCSky](https://hdfcsky.com/news/brent-crude-oil-price-today-july-1-2026-oil-prices-rise-as-iran-rejects-face-to-face-talks-with-u-s-in-fresh-middle-east-setback) · [S&P 500 futures Jul 1 — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-july-1-2026-nasdaq-futures-slip-after-strongest-quarter-since-2020) · [Iran MOU — Al Jazeera](https://www.aljazeera.com/news/2026/6/17/iran-confirms-that-mou-has-been-signed-electronically-by-both-sides) · [NVIDIA Newsroom ISC 2026](https://nvidianews.nvidia.com/news/latest) · [Marvell 247% YTD — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/marvell-technology-soared-247-2026-192800362.html) · exec_eod_2026-06-18 (last authoritative bot file) · eod_2026-06-30*
