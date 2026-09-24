# Premarket Summary — 2026-06-24 (Wednesday)

> **🔴🔴 CRITICAL: (1) XLE exit triggers ALL active — Day 11+, Brent collapsed to $74.73 (Aug futures) / $76.40 (spot) — lowest since pre-Iran-war Feb 2026. (2) GitHub Actions STILL DOWN — 6th consecutive trading session without exec files. (3) Layer 2 FLAT 6 days; CSP windows shifted to Aug21.**

---

## Header

- **API status:** UNAVAILABLE (Alpaca paper API unreachable from this environment; confirmed via live test this session)
- **Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18 — 4 trading sessions stale; no exec files committed Jun 20, 22, or 23)
- **Market context:** Equities mixed after June 23 chip selloff — TheStreet reports S&P 500 futures "edge higher" on June 24 with Micron earnings in focus; Nasdaq recouping some losses. Brent crude extended declines to $74.73, fresh low since before the Iran conflict.

---

## Account Snapshot (exec_eod_2026-06-18 — last confirmed)

| Metric | Value | Note |
|---|---|---|
| Equity | $102,108.69 | Last confirmed — 4 trading sessions stale |
| Our return (inception) | +2.11% | As of June 18 |
| SPY price at that date | $748.46 | SPY return +2.31% |
| Alpha | -0.21% vs SPY | As of June 18 |
| Options BP remaining | $73,470.00 | Layer 2 FLAT as of June 18 EOD |
| Account floor | $87,500 | Bot halts new positions below this |

> **Note:** No exec files exist for June 20, 22, or 23. Equity and positions have NOT been bot-confirmed since June 18. The June 23 selloff (Nasdaq -2.6%) has likely reduced equity from the June 18 figure; still estimated well above $87,500 floor.

---

## Current Positions (from exec_eod_2026-06-18 + midday_2026-06-23 narrative)

**Layer 1 — Core ETFs** *(target from exec_eod 2026-06-18; no bot rebalance since; prices estimated)*

| Symbol | Shares | Target | ~Closing Price (Jun 23) | Notes |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$736 | Chip selloff day; recovering slightly today |
| SPY | 13 | 13 | ~$746 | Broad market soft |
| JETS | 80 | 80 | ~$31.09 | ~$4.60 gap to $35.69 trigger; clear |
| **XLE** | **100** | **EXIT** | **~$53.50** | 🔴🔴🔴 **ALL 3 TRIGGERS ACTIVE — Day 11+** |
| SPCX | 15 | 15 | — | SpaceX IPO; held since Jun 17 re-buy |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY in progress |

**Layer 2 — Open CSPs** *(FLAT — bot offline since June 18)*

| Target | Strike | Expiry | DTE Today | Status |
|---|---|---|---|---|
| NVDA $190P | Aug 21 | ~58 DTE | Within range (25–60) | FLAT — Jul18 window closed Jun 23; target → Aug21 |
| AMZN $215P | Aug 21 | ~58 DTE | Within range (25–60) | FLAT — Jul17 window closed; target → Aug21 |

**No options positions are confirmed open.** The AMZN $220P Jul17 order submitted June 18 at $2.20 never filled — Alpaca cancels GTC options orders at session end. NVDA Jul18 window closed permanently as of June 23 open session.

**Layer 2b — QQQ Calls:** FLAT. Bot not running. QQQ futures slightly positive today; evaluate on bot resume.

---

## Iran / Oil Status — June 24

| Item | Status |
|---|---|
| Iran-US MOU signed? | ✅ YES — signed June 17 (Versailles/Tehran); 60-day ceasefire + Hormuz open |
| Switzerland nuclear talks | ✅ UNDERWAY — Vance called first day "very, very good"; Iran FM hedging |
| Strait of Hormuz | ✅ OPEN — 25 vessels/day (record since mid-April); US 60-day Iran oil licence active |
| Brent crude (premarket Jun 24) | **$74.73 (Aug futures) / $76.40 (spot)** — lowest since pre-Iran-war (Feb 2026) |
| vs $90 trim trigger | **~$15.27 below — TRIGGERED Day 11+** |
| vs $85 exit trigger | **~$10.27 below — TRIGGERED Day 11+** |
| Iran MOU trigger | **TRIGGERED Day 11+** |

**Interpretation:** Brent fell again on June 24 as Hormuz optimism accelerated oil supply expectations. August futures at $74.73 are below spot ($76.40), indicating near-term supply glut pricing. This is the lowest Brent has been since before the US-Iran conflict began in February 2026. The structural bear thesis (Iranian crude formally entering global markets within 60 days) is fully priced in and then some. No catalyst to reverse the XLE exit decision.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90.00 | $76.40 | 🔴 **TRIGGERED — Day 11+** |
| Brent ≤ $85 → exit ALL XLE | $85.00 | $76.40 | 🔴 **TRIGGERED — Day 11+** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed Jun 17 | 🔴 **TRIGGERED — Day 11+** |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 | ~$31.09 | 🟢 Clear — ~14.7% gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102,108 (est.) | 🟢 Clear (estimated; stale) |

---

## Morning Priority Actions

1. **🔴 CRITICAL: Sell ALL 100 XLE shares at market open (9:30 AM ET)**
   All 3 manual exit rules have been simultaneously active for 11+ days. Brent is now at a post-conflict low ($74.73 Aug futures) — the situation has gotten worse, not better. At 100 shares × ~$53.50 ≈ **$5,350 in proceeds**. Execute manually via Alpaca paper trading UI. The bot does not run manual triggers. Do not wait for a bounce.

2. **🔴 CRITICAL: Investigate & restart GitHub Actions**
   Bot has not run since June 18 EOD — 6 consecutive trading sessions dark (Jun 20: 3 sessions, Jun 22: 3 sessions, Jun 23: 2 sessions = 8 total missed). Check github.com/TekMage/paper-trading/actions — find why trading-open.yml, trading-midday.yml, trading-eod.yml are not firing. Today is the first viable session for NVDA $190P Aug21 (~58 DTE) and AMZN $215P Aug21 — both within OPT_DTE range. Bot must run at 9:30 AM ET to open these.

3. **⚠️ HIGH: Monitor Micron earnings for NVDA/semis signal**
   Micron earnings are in focus today (cited by TheStreet as the market driver for June 24). Micron missed Q3 AI revenue guides last week (-10%) triggering the chip selloff — today's data could clarify whether AI spending doubts are structural. NVDA ~$202–203 premarket. A constructive Micron print could help stabilize semis and improve NVDA CSP risk/reward on Aug21.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions outage | 🔴 CRITICAL | 8 missed bot sessions; exec files absent since June 18; account state unconfirmed |
| XLE exit Day 11+ | 🔴 CRITICAL | All 3 triggers active; Brent at post-conflict low $74.73; cost of inaction compounding daily |
| XLY FORCE_CLOSE status | ⚠️ HIGH | Bot offline; XLY close in progress; confirm bot resumes this task when Actions fixed |
| NVDA continued weakness | ⚠️ HIGH | $202–203 premarket; $190P Aug21 strike ~6% OTM; elevated IV from chip selloff |
| Micron earnings catalyst | ⚠️ HIGH | Could move NVDA/AMD/QQQ significantly in either direction today |
| Equity staleness | ℹ️ INFO | Jun 23 Nasdaq -2.6% has reduced equity from $102,108; still estimated above $87,500 floor |
| AMZN CSP path | ℹ️ INFO | AMZN ~$234 (Jun 23 close); $215P Aug21 = ~8.4% OTM; solid cushion on bot resume |

---

## GitHub Actions Outage — Session Tally

| Date | Session | Status |
|---|---|---|
| Jun 18 | Open / Midday / EOD | ✅ All 3 ran — last confirmed |
| Jun 19 | All | ✅ Juneteenth — NYSE closed |
| Jun 20 | Open / Midday / EOD | ❌ 0 exec files committed |
| Jun 22 | Open / Midday / EOD | ❌ 0 exec files committed |
| Jun 23 | Open / Midday / EOD | ❌ 0 exec files committed |
| **Jun 24** | **Open (due 9:30 AM ET)** | **❓ TBD — fix required** |

**Total missed bot sessions: 9 (including today's open if not fixed).** Layer 2 FLAT 6 trading days. NVDA Jul18 window permanently closed. AMZN Jul17 window permanently closed. Both CSP targets now on Aug21 expiry.

---

*Sources: [CNBC — Brent falls below $75, lowest since pre-Iran-war](https://www.cnbc.com/2026/06/24/oil-prices-wti-brent-crude-trump-doj-gasoline-prices-strait-of-hormuz.html) · [HDFCSky — Brent $74.73 June 24](https://hdfcsky.com/news/brent-crude-oil-price-today-june-24-2026-crude-oil-price-continue-slide-as-us-iran-peace-progress-sparks-hormuz-optimism) · [TheStreet — Stock Market Today June 24 (futures edge higher, Micron focus)](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-24-2026) · [NPR — US-Iran MOU signed June 17](https://www.npr.org/2026/06/19/nx-s1-5863544/trump-us-iran-agreement) · [CBS News — Switzerland nuclear talks underway](https://www.cbsnews.com/live-updates/iran-us-deal-trump-war-negotiations/) · [Yahoo Finance — NVDA $202.84 premarket](https://finance.yahoo.com/markets/stocks/articles/3-semiconductor-stocks-buy-while-143037327.html)*
