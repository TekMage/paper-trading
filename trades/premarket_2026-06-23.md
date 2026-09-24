# Premarket Summary — 2026-06-23 (Tuesday)

> **🔴🔴 CRITICAL: (1) XLE exit triggers ALL active — Day 10+, sell 100 XLE at open. (2) GitHub Actions STILL DOWN — 5th consecutive session without exec files. (3) NVDA -6% premarket, approaching $190P strike.**

---

## Header

- **API status:** UNAVAILABLE (Alpaca paper API unreachable from this environment; confirmed via live test)
- **Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18 — no exec files have been committed for June 20, 22, or 23)
- **Market context:** S&P 500 futures -1.2%, Nasdaq -2.6% on a global chip selloff — Micron -10%, NVDA -6%, AMD -9% premarket. Markets opening sharply lower. XLE triggers are all active and Brent has bounced ~$3 overnight to ~$77-78 but remains well below both thresholds.

---

## Account Snapshot (exec_eod_2026-06-18 — last confirmed)

| Metric | Value | Note |
|---|---|---|
| Equity | $102,108.69 | Last confirmed — 3 trading sessions stale |
| Our return (inception) | +2.11% | As of June 18 |
| SPY price at that date | $748.46 | SPY return +2.31% |
| Alpha | -0.21% vs SPY | As of June 18 |
| Options BP remaining | $73,470.00 | Layer 2 was FLAT June 18 EOD |
| Account floor | $87,500 | Bot halts new positions below this |

> **Note:** No exec files exist for June 20 (Friday), June 22 (Monday), or June 23 (today). Equity and positions have NOT been bot-confirmed since June 18. Layer 1 ETF prices will have moved; the equity figure above is stale.

---

## Current Positions (from exec_eod_2026-06-18 + June 22 EOD narrative)

**Layer 1 — Core ETFs** *(target from exec_eod 2026-06-18; not bot-rebalanced since; prices estimated)*

| Symbol | Shares | Target | Status |
|---|---|---|---|
| QQQ | 50 | 50 | At target — was $739.83 at June 22 close |
| SPY | 13 | 13 | At target |
| JETS | 80 | 80 | At target — ~$31.16 (June 22); ~$4.53 gap to $35.69 trigger |
| **XLE** | **100** | **EXIT** | 🔴🔴🔴 **ALL 3 TRIGGERS ACTIVE — Day 10+ overdue** |
| SPCX | 15 | 15 | SpaceX IPO, held since Jun 17 re-buy ~$201.80 |
| XLY | Closing | 0 | FORCE_CLOSE_EQUITY in progress (June sprint exit) |

**Layer 2 — Open CSPs** *(Layer 2 is FLAT entering today)*

| Target | Strike | Expiry | Status |
|---|---|---|---|
| NVDA $190P | Jul 18 | **25 DTE today = OPT_DTE_MIN** | FLAT — TODAY IS LAST VIABLE DAY for Jul18 ⚠️ NVDA -6% premarket |
| AMZN CSP | — | — | Jul17 window CLOSED (<25 DTE). Retarget: AMZN $215P Aug21 (~60 DTE) |

**Layer 2b — QQQ Calls**
- FLAT. Bot targets 2% OTM QQQ. With QQQ likely opening sharply lower today on tech selloff, any call buy carries elevated downside risk. Skip or wait for price to stabilize.

---

## Iran / Oil Status — June 23

| Item | Status |
|---|---|
| Iran-US MOU signed? | ✅ **YES — signed June 15/17; 60-day ceasefire + Hormuz open** |
| Strait of Hormuz | ✅ OPEN — Iranian crude tankers transiting; US 60-day general oil licence issued June 22 |
| 60-day negotiation sprint | Active — US/Iranian officials in Switzerland |
| Brent crude (premarket) | **~$77.42–$78.15** — bounced ~$3 overnight from June 22's ~$74.30 collapse |
| vs $90 trim trigger | **~$12.58 below — TRIGGERED (Day 10+)** |
| vs $85 exit trigger | **~$7.58 below — TRIGGERED (Day 10+)** |
| Iran MOU trigger | **TRIGGERED (Day 10+)** |

**Interpretation:** Brent's bounce today is a technical rebound after a ~$5 intraday collapse on June 22 (US issued Iran oil licence). The structural bear case is intact — Iranian crude will formally reach markets within 60 days. All three XLE exit rules remain simultaneously breached by a wide margin. This is not a close call.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90.00 | ~$77–78 | 🔴 **TRIGGERED — Day 10+** |
| Brent ≤ $85 → exit ALL XLE | $85.00 | ~$77–78 | 🔴 **TRIGGERED — Day 10+** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed Jun 15/17 | 🔴 **TRIGGERED — Day 10+** |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 | ~$31.16 | 🟢 Clear — ~14.5% gap; likely wider today (markets -1.2%) |
| Equity < $87,500 → halt new positions | $87,500 | ~$102,108 (est.) | 🟢 Clear (estimated; tech selloff may reduce this) |

---

## Morning Priority Actions

1. **🔴 CRITICAL: Sell ALL 100 XLE shares at market open (9:30 AM ET)**
   All 3 manual exit rules active simultaneously, Day 10+ overdue. Brent ~$77 structurally: US-Iran oil licence issued June 22 means Iranian supply formally entering global markets in 60 days. At 100 shares × ~$53 ≈ $5,300 in proceeds. Do NOT wait for a Brent bounce — the $3 overnight pop is noise. Execute manually; the bot does not run manual triggers.

2. **🔴 CRITICAL: Investigate & restart GitHub Actions**
   Bot has not run since June 18. Check github.com/TekMage/paper-trading/actions — find why scheduled workflows (trading-open.yml, trading-midday.yml, trading-eod.yml) are not firing. Layer 1 has not been rebalanced in 3 trading sessions. Layer 2 has been unable to open CSPs. The NVDA $190P Jul18 window closes after today.

3. **⚠️ HIGH: NVDA CSP decision — TODAY is the last viable day for Jul18**
   NVDA is DOWN ~6% premarket (~$196–197 from $209 close). At $196, the $190P strike is only ~3% OTM — well inside normal NVDA daily range. If the bot resumes and attempts to open this CSP, the premium will be elevated but so is the risk. Consider whether $190P Jul18 is still appropriate at $196 NVDA, or whether to wait for Aug21 expiry at a lower strike. If bot does NOT run today, the Jul18 window closes and the default target shifts to NVDA $190P Aug21.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions outage | 🔴 CRITICAL | 3 trading sessions / 6 bot sessions missed; bot completely dark; account state unconfirmed |
| XLE exit Day 10+ | 🔴 CRITICAL | All 3 triggers active; Brent ~$74–78 range; structural oil bear (Iran supply ramp) ongoing |
| NVDA -6% premarket | 🔴 CRITICAL | NVDA ~$196–197 premarket vs $190P strike = ~3% OTM; approaching danger zone; CSP risk asymmetry has worsened significantly |
| Tech selloff today | ⚠️ HIGH | S&P -1.2%, Nasdaq -2.6%; driven by Micron (-10%) sparking AI doubts; QQQ call risky; Layer 1 equity value likely dropped overnight |
| NVDA Jul18 window closing | ⚠️ HIGH | 25 DTE = OPT_DTE_MIN; if bot misses today's open, shift NVDA target to Aug21 expiry |
| AMZN CSP path reset | ⚠️ HIGH | Jul17 window closed; AMZN ~$231 after -4.8% June 22; target retarget to $215P Aug21 on bot resume |
| PCE Thursday June 26 | ⚠️ HIGH | Core PCE is week's key macro risk — hot print could pressure equities and revive rate-hike fear |
| Equity floor risk | ℹ️ INFO | Tech selloff means actual equity may be below $102K; still estimated well above $87,500 floor but unconfirmed |

---

## Context — Why Markets Are Down Today

**Global chip selloff (Micron -10%):** Micron hit a record high on June 22, then faced a cascade of profit-taking that spread to all semis overnight. NVDA -6%, AMD -9%, South Korea's Kospi -10%. The trigger is AI spending doubts surfacing after multiple consecutive record-high closes in chip stocks. This is rotation/valuation-driven, not fundamentally driven by earnings or guidance cuts. NVDA's Q1 FY27 was up 85% YoY — the sell-off is multiple compression, not deteriorating fundamentals.

**JETS today:** Airlines face a dual headwind — tech-risk-off selloff plus lower oil prices (normally bullish for JETS) may not offset the broad market decline. JETS likely opens near or below $31. The $35.69 trigger remains ~15% away.

---

## GitHub Actions Status

No exec files have been committed since `exec_eod_2026-06-18`. Missing sessions:

| Date | Session | Status |
|---|---|---|
| 2026-06-19 | — | 🏛️ Juneteenth — NYSE closed |
| 2026-06-20 | Open / Midday / EOD | ❌ No exec files committed |
| 2026-06-22 | Open / Midday / EOD | ❌ No exec files committed |
| 2026-06-23 | Open (due 9:30 AM ET) | ❓ TBD — depends on fix |

---

*Sources: [CNBC — chip selloff premarket June 23](https://www.cnbc.com/2026/06/22/stock-market-today-live-updates.html) · [TheStreet — Dow futures June 23](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-23-2026) · [Sunday Guardian Live — Brent June 23](https://sundayguardianlive.com/business/brent-crude-oil-price-today-june-23-brent-climbs-above-78-on-us-iran-peace-deal-hopes-check-latest-brent-crude-wti-oil-rates-today-211696/) · [Yahoo Finance — NVDA -6%](https://finance.yahoo.com/sectors/technology/live/tech-stocks-today-nvidia-stock-drops-6-in-ugly-day-for-chip-stocks-100000734.html) · [NPR — US-Iran agreement](https://www.npr.org/2026/06/19/nx-s1-5863544/trump-us-iran-agreement) · [CNN — US-Iran MOU text](https://www.cnn.com/2026/06/17/middleeast/us-iran-war-mou-text-intl) · [Yahoo Finance JETS](https://finance.yahoo.com/quote/JETS/)*
