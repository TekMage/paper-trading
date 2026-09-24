# Premarket Summary — 2026-06-25 (Thursday)

> **🔴🔴 CRITICAL: (1) XLE exit triggers ALL active — Day 12, Brent collapsed further to $73.43 (↓ from $76.40 yesterday) — widening gap below all three thresholds. (2) GitHub Actions STILL DOWN — 7th consecutive trading session without exec files. (3) Layer 2 FLAT; no options positions open.**

> **✅ UPSIDE: Micron crushed Q3 earnings (+17–18% premarket) — Nasdaq futures +2.4%; semiconductor sentiment reversal could improve NVDA CSP entry on bot resume.**

---

## Header

- **API status:** UNAVAILABLE (Alpaca paper API unreachable from this environment; confirmed via live test this session)
- **Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18 — 5 trading sessions stale; no exec files since)
- **Market context:** Nasdaq futures +2.4% on Micron earnings beat; S&P 500 futures +0.8%; PCE inflation 4.1% (highest since April 2023) providing macro headwind; Brent crude $73.43 continuing decline

---

## Account Snapshot (exec_eod_2026-06-18 — last confirmed)

| Metric | Value | Note |
|---|---|---|
| Equity | $102,108.69 | Last confirmed — 5 trading sessions stale |
| Our return (inception) | +2.11% | As of June 18 |
| SPY price at that date | $748.46 | SPY return +2.31% |
| Alpha | -0.21% vs SPY | As of June 18 |
| Options BP remaining | $73,470.00 | Layer 2 FLAT |
| Account floor | $87,500 | Bot halts new positions below this |

> **Note:** No exec files exist for Jun 20, 22, 23, or 24. Equity has NOT been bot-confirmed since June 18. Today is Thursday June 25. Nasdaq's recovery today (Micron-led) may partially offset the June 23 selloff (Nasdaq -2.6%). Estimated equity still well above $87,500 floor.

---

## Current Positions (exec_eod_2026-06-18 + narrative updates)

**Layer 1 — Core ETFs** *(target from exec_eod 2026-06-18; no bot rebalance since; prices estimated)*

| Symbol | Shares | Target | ~Est. Price (Jun 25 pre) | Notes |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$745–750 | Micron-driven bounce; +2.4% NQ futures |
| SPY | 13 | 13 | ~$750–755 | Broad market +0.8% premarket |
| JETS | 80 | 80 | ~$31.10 | ~$4.59 gap to $35.69 trigger; clear |
| **XLE** | **100** | **EXIT** | **~$53–54** | 🔴🔴🔴 **ALL 3 TRIGGERS ACTIVE — Day 12** |
| SPCX | 15 | 15 | — | SpaceX IPO; held since Jun 17 re-buy |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY in progress (bot offline) |

**Layer 2 — Open CSPs** *(FLAT — bot offline since June 18)*

| Target | Strike | Expiry | DTE Today | Status |
|---|---|---|---|---|
| NVDA $190P | Aug 21 | ~57 DTE | Within range (25–60) | FLAT — no open position; bot must run to open |
| AMZN $215P | Aug 21 | ~57 DTE | Within range (25–60) | FLAT — no open position; bot must run to open |

**Note on NVDA proximity:** NVDA at ~$199 premarket — $190P strike is ~4.5% OTM. This is within acceptable range, but closer than ideal. Micron's strong print may boost NVDA higher today, improving entry risk/reward if bot runs. Monitor NVDA response to Micron news at open.

**Layer 2b — QQQ Calls:** FLAT. Bot not running. QQQ likely to rally with NQ +2.4% — favorable setup if bot resumes today.

---

## Iran / Oil Status — June 25

| Item | Status |
|---|---|
| Iran-US MOU signed? | ✅ YES — MOU signed ~June 15–17; 60-day ceasefire + Hormuz open |
| Final nuclear deal? | ❌ NOT YET — Switzerland talks ongoing; IAEA inspections disputed; frozen assets unresolved |
| Strait of Hormuz | ✅ OPEN — traffic increasing; US 60-day Iran oil licence active |
| Brent crude (Jun 25 premarket) | **$73.43** — down $0.44 (−0.6%) from $73.87 close; intraday range $72.43–$73.72 |
| vs $90 trim trigger | **~$16.57 below — TRIGGERED Day 12** |
| vs $85 exit trigger | **~$11.57 below — TRIGGERED Day 12** |
| Iran MOU trigger | **TRIGGERED Day 12** |

**Interpretation:** Brent fell further overnight — now $73.43, down from $76.40 yesterday. The Middle East risk premium continues to fade as Hormuz traffic increases and Iran sanctions relief takes hold. 60-day nuclear talks are ongoing but unresolved. The structural bear case for XLE is fully intact and worsening. No reversal catalyst in sight.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90.00 | $73.43 | 🔴 **TRIGGERED — Day 12** |
| Brent ≤ $85 → exit ALL XLE | $85.00 | $73.43 | 🔴 **TRIGGERED — Day 12** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed ~Jun 15 | 🔴 **TRIGGERED — Day 12** |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 | ~$31.10 | 🟢 Clear — ~14.6% gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102,108 (est.) | 🟢 Clear (estimated; stale) |

---

## Morning Priority Actions

1. **🔴 CRITICAL: Sell ALL 100 XLE shares at market open (9:30 AM ET)**
   All 3 manual exit rules have been simultaneously active for 12 days. Brent fell another $0.44 overnight to $73.43, continuing to worsen. At 100 shares × ~$53 ≈ **$5,300 in proceeds**. Every additional day of inaction is realized loss on a structurally declining position. Execute manually via Alpaca paper trading UI — the bot does not run manual triggers.

2. **🔴 CRITICAL: Investigate & restart GitHub Actions**
   Bot has not run since June 18 EOD — 7 consecutive trading sessions offline (missed: Jun 20, 22, 23, 24, and today if not fixed). Both CSP targets (NVDA $190P Aug21, AMZN $215P Aug21) remain within 25–60 DTE window — today ~57 DTE. Go to github.com/TekMage/paper-trading/actions and diagnose why trading-open.yml is not triggering. Every day of delay reduces DTE and narrows the premium collection window.

3. **✅ OPPORTUNITY: Micron earnings beat — monitor NVDA response at open**
   Micron surged +17–18% on Q3 earnings that beat AI revenue expectations. Nasdaq futures +2.4%. If NVDA rallies from $199 toward $205–210 on the coattails, the $190P Aug21 CSP moves further OTM and improves risk/reward. If bot resumes today, this is the best entry context for NVDA CSP in ~2 weeks. Watch NVDA price action in first 30 minutes.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions outage | 🔴 CRITICAL | 7 missed bot sessions; exec files absent since June 18; account unconfirmed |
| XLE exit Day 12 | 🔴 CRITICAL | All 3 triggers active; Brent at $73.43 (new low); worsening daily |
| XLY FORCE_CLOSE status | ⚠️ HIGH | Bot offline; XLY close in progress; confirm bot resumes this task |
| PCE inflation 4.1% | ⚠️ HIGH | Highest since April 2023; macro headwind even on a rally day |
| NVDA proximity to $190P | ⚠️ MEDIUM | $199 premarket = 4.5% OTM on $190P; acceptable but closer than ideal |
| Equity staleness | ℹ️ INFO | 5 sessions stale; estimated well above $87,500 floor given Nasdaq recovery today |
| AMZN CSP path | ℹ️ INFO | AMZN ~$234–236 est.; $215P Aug21 = ~8.5–9% OTM; solid cushion on bot resume |

---

## GitHub Actions Outage — Session Tally

| Date | Session | Status |
|---|---|---|
| Jun 18 | Open / Midday / EOD | ✅ All 3 ran — last confirmed |
| Jun 19 | All | ✅ Juneteenth — NYSE closed |
| Jun 20 | Open / Midday / EOD | ❌ 0 exec files committed |
| Jun 22 | Open / Midday / EOD | ❌ 0 exec files committed |
| Jun 23 | Open / Midday / EOD | ❌ 0 exec files committed |
| Jun 24 | Open / Midday / EOD | ❌ 0 exec files committed |
| **Jun 25** | **Open (due 9:30 AM ET)** | **❓ TBD — fix required** |

**Total missed bot sessions: 12.** Layer 2 FLAT 7 trading days. Jul18 NVDA and Jul17 AMZN windows permanently closed. Both CSP targets now on Aug21 (~57 DTE today).

---

*Sources: Trading Economics (Brent $73.43 Jun 25) · Gulf News (Brent risk premium fading) · Bloomberg Oil (Jun 25 premarket) · Wikipedia / CSIS / Time / Al Jazeera (Iran-US MOU framework, 60-day ceasefire, Switzerland talks ongoing) · TheStreet (Stock Market Today Jun 25, Micron earnings, PCE 4.1%) · Yahoo Finance (NVDA ~$199, Micron +17–18% premarket)*
