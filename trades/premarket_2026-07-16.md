# Premarket Summary — Thursday, July 16, 2026 (~9:00 AM ET)

> **CRITICAL HEADER:** (1) GitHub Actions DOWN — **Day 31**; all 3 trading workflows `disabled_manually` since June 19; no exec files since June 18. (2) **Brent crude $84.63–$84.80/bbl — BELOW the $85 exit-all-XLE trigger. Exit-all-XLE rule is ACTIVE and requires manual action.** (3) Iran: no new MOU overnight; US launched fresh airstrikes on Iran on July 15 (Wednesday); Strait of Hormuz still under tension; June 17 MOU effectively in collapse. (4) Market futures MIXED-DOWN: Dow +0.2%, S&P 500 -0.2%, Nasdaq-100 -0.7% as chip stocks slide on TSMC earnings (record beat but warning of higher prices). (5) SPCX (SpaceX) fell below its $135 IPO price for the first time July 15 — lockup expiration fears; our 15-share position is roughly at cost or slightly underwater. (6) Alpaca API UNAVAILABLE from this environment.

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **GitHub Actions** | 🔴 DOWN — Day 31; all 3 workflows `disabled_manually` since June 19; no trades since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — 20 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD) |
| **Iran MOU** | 🔴 COLLAPSED — June 17 MOU in effective failure; US struck Iran July 15; Hormuz monitoring continues; no new formal MOU signed overnight July 15–16 |
| **Brent crude** | **~$84.63–$84.80/bbl** 🔴 **BELOW $85 exit-all-XLE trigger — MANUAL ACTION REQUIRED** |
| **Market context** | Futures mixed-down: Dow +0.2%, S&P -0.2%, Nasdaq -0.7% on chip stock selloff (TSMC earnings) |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Stale — 20 trading sessions unconfirmed |
| **Return (inception)** | **+2.11%** | vs $100K starting capital May 7, 2026 |
| **Options BP remaining** | **$73,470.00** | Layer 2 flat since June 18; no new CSPs opened |
| **SPY benchmark (Jun 18)** | **$748.46** (+2.32%) | SPY ~$754–756 range recently; inception ~+3.1–3.3% |
| **Alpha (stale)** | **⚠️ ~-1.0% to -1.2%** | Stale +2.11% vs SPY inception ~+3.1–3.3% |

> Actual equity is unknown. Nasdaq -0.7% premarket on chip selloff; SPCX down from peak; oil headwind on XLE. Real-time equity likely slightly below June 18 on tech weakness today.

---

## Current Positions (Last Confirmed June 18 + Context)

### Layer 1 — Core ETFs (Unconfirmed — 20 Sessions Stale)

| Symbol | Shares | Target | Context | Notes |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | Nasdaq -0.7% futures | Chip selloff on TSMC; QQQ likely weak at open |
| **SPY** | 13 | 13 | S&P -0.2% futures | Mixed session expected |
| **JETS** | 80 | 80 | ~$32 est. | Brent headwind; $35.69 trigger ~$3.69 away; not close |
| **XLE** | **100 (UNCONFIRMED)** | **EXIT (per CLAUDE.md)** | **🔴 Brent ~$84.7 — exit-all trigger ACTIVE** | **Manual sell of all 100 XLE required per rules** |
| **SPCX** | 15 | 15 | ~$132–136 (below $135 IPO price) | ⚠️ First close below IPO; lockup expiration pressure; not a rule trigger but monitor |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | ~$116+ est. | 🔴 FORCE_CLOSE unexecuted 20 sessions; manual close or bot resumption required |

### Layer 2 — Open CSPs

**FLAT** — No confirmed open options positions since June 18.

| Target | Strike / Expiry | DTE (Jul 16) | Underlying | Status |
|---|---|---|---|---|
| **NVDA** | $190P Jul18 | **2 DTE — EXPIRES TOMORROW** | Weak today on chip selloff | ✅ NOT held (never confirmed open). NVDA new target: Aug21 or Sep19, strike ≤$185 (≥8% OTM). Bot can enter post-Jul-18. |
| **AMZN** | $215P Aug21 | ~36 DTE | ~$248+ est. | ✅ Strong 13%+ OTM cushion. ⚠️ Do NOT enter before AMZN Q2 earnings (~Jul 30). Ready for bot post-resumption + post-earnings. |

**Layer 2b — QQQ Calls:** Nasdaq -0.7% is a headwind; hold for bot resumption. No manual action needed.

---

## Iran / Oil Status

| Item | Status (July 16 Premarket) |
|---|---|
| **June 17 MOU** | 🔴 **IN EFFECTIVE COLLAPSE** — Implementation failed; US continued strikes July 15; Hormuz still contested |
| **New MOU overnight** | ❌ **NONE** — No new formal MOU signed July 15–16 overnight |
| **US military action** | 🔴 **ACTIVE** — US launched fresh airstrikes on Iran on Wednesday July 15; monitoring Hormuz |
| **Brent crude (Jul 16)** | **~$84.63–$84.80/bbl** — down 0.37% from prior day; gave up early session gains |
| **vs $90 trim trigger** | 🔴 **ACTIVE** (Brent ~$5–6 below $90) |
| **vs $85 exit-all trigger** | 🔴🔴 **TRIGGERED** — Brent at $84.63–$84.80; **BELOW $85 threshold; exit-all-XLE rule is active** |
| **vs MOU trigger** | ⚠️ **AMBIGUOUS** — June 17 MOU WAS signed (trigger technically fired) but deal collapsed; bot never executed (Actions down); no new MOU today |

**Oil context:** Brent down 0.37% to ~$84.7 today after four consecutive sessions of gains. Oil gave up early gains as profit-taking hit, but Iran tensions keep supply disruption risk elevated. At current price, both the $90 trim AND the $85 exit-all triggers are simultaneously active. The rules call for exiting ALL 100 XLE shares if Brent ≤ $85.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $85 → exit ALL XLE at market** | $85/bbl | 🔴🔴 **TRIGGERED** — Brent $84.63–$84.80; **execute manually via Alpaca paper dashboard** |
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE** (superseded by $85 rule) |
| **Iran MOU signed → sell 60 XLE immediately** | Formal new MOU | ❌ Not triggered overnight — no new deal; blockade ongoing |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69 | ✅ NOT triggered — JETS ~$32; ~$3.69 below; Brent headwind is a drag on JETS too |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **EXIT ALL XLE** — Brent confirmed at $84.63–$84.80/bbl, below the $85 exit-all threshold. Log into Alpaca paper dashboard and **sell all 100 XLE shares at market open** (9:30 AM ET). This rule has been active since at least July 15 and is unambiguously triggered today. Every session this goes unexecuted is a rules violation. |
| 🔴 2 | **Re-enable GitHub Actions** — Go to `github.com/TekMage/paper-trading/actions` and re-enable all 3 trading workflows. Day 31 = ~60 missed sessions. Bot will auto-handle XLY FORCE_CLOSE, Layer 1 rebalance, and evaluate new CSPs at 9:30 AM if re-enabled. |
| 🟡 3 | **Monitor SPCX** — SpaceX (SPCX) closed below its $135 IPO price July 15 for the first time, driven by lockup expiration concerns. Our 15-share position at ~$135 cost is roughly breakeven or slightly underwater. No strategy rule governs this; hold per plan unless manual review suggests otherwise. Watch for lockup expiration date for potential further pressure. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **$85 XLE exit-all TRIGGERED** | Brent $84.63–$84.80 — both XLE triggers active simultaneously. Every session without action is a rules violation. XLE likely faces continued pressure if Iran escalation persists. |
| 🔴 **GitHub Actions Day 31** | ~60 missed sessions; Layer 2 generating $0 premium; XLY FORCE_CLOSE unexecuted; all CSP and call opportunities missed; strategy paralyzed. |
| 🔴 **Iran escalation ongoing** | US struck Iran July 15; no diplomatic resolution visible; Hormuz supply route at risk; oil remains elevated relative to pre-war levels. No near-term off-ramp. |
| 🟡 **Chip stock selloff** | Nasdaq -0.7% premarket; TSMC beat on earnings but warned of higher prices and stocks fell. NVDA and QQQ likely to open lower today. Blackwell ramp starting H2 2026. |
| 🟡 **SPCX below IPO price** | First close below $135 IPO price on July 15; all-time high was $225.64 on Jun 16; down ~40% from peak. Lockup expiration a known near-term risk. No rule trigger, but position is at/below cost. |
| 🟡 **NVDA $190P Jul18 — expires tomorrow** | Expires in 1 trading session (July 18 Friday). NOT held (never confirmed open since Actions down). New CSP window opens post-expiry; target Aug21 strike ≤$185. |
| 🟡 **AMZN Q2 earnings ~Jul 30** | No new AMZN CSP until post-earnings. $215P Aug21 remains on deck. |
| 🟡 **XLY FORCE_CLOSE unexecuted** | 20 sessions; if still held, close via Alpaca dashboard (sell at market). |
| 🟢 **Options BP intact** | $73,470 options BP confirmed June 18; no positions opened since. Capital preserved. |

---

## Overnight News Summary

**Iran/Hormuz:** US launched latest wave of airstrikes on Iranian targets on Wednesday July 15. Strait of Hormuz remains under active monitoring; investors watching oil supply disruption risk. June 17 MOU in effective collapse; no new formal agreement reached overnight July 15–16. No new MOU signed.

**Brent crude:** $84.63–$84.80/bbl — down 0.37% on July 16, gave up early gains after four consecutive up sessions. Iran tensions maintaining structural support but profit-taking pulling prices lower. **Both the $90 trim and $85 exit-all triggers for XLE are active simultaneously.**

**Market (July 16 premarket):** Dow futures +0.2%, S&P 500 futures -0.2%, Nasdaq-100 futures -0.7%. Chip stocks sliding for a second day. PPI inflation data and retail sales due this morning. Netflix Q2 earnings after close.

**TSMC Q2 2026 earnings (reporting July 16):** Record Q2 revenue $39.62B (+36% YoY), net profit +77% YoY — strong beat driven by AI chip demand (61% of sales). But: TSMC warned of higher prices and raised capex, which markets are reading negatively. Chip stocks falling in premarket despite the beat. Broader semiconductor sector has been under pressure since early July ($1.3–1.4T in market cap wiped in a few sessions on DeepSeek concerns, HBM inventory worries, and hawkish Fed signals). NVDA expected to be weak today.

**SPCX/SpaceX:** SPCX closed below its $135 IPO price for the first time on July 15, 2026, driven by lockup expiration concerns. The stock hit an all-time high of $225.64 on June 16 (IPO week peak) and has retraced ~40% since. Nasdaq-100 inclusion forces a buy of ~$4.3B of the 3% float, which may provide support near-term. Our 15-share position at ~$135 cost is at or slightly below cost.

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · premarket_2026-07-15 · [HDFCSky — Brent Jul 16](https://hdfcsky.com/news/brent-crude-oil-price-today-july-16-2026-us-iran-tensions) · [Yahoo Finance — Stock Market Today Jul 16](https://finance.yahoo.com/markets/live/stock-market-today-thursday-july-16-dow-sp-500-nasdaq-103116735.html) · [FX Leaders — TSMC slips Jul 15](https://www.fxleaders.com/news/2026/07/15/tsmc-tsm-stock-slips-despite-strong-ai-chip-demand-and-robust-revenue-growth/) · [TheStreet — SPCX below IPO Jul 15](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-15-2026) · [TradingKey — SPCX Nasdaq-100 forced buy](https://www.tradingkey.com/analysis/stocks/us-stocks/262011296-spacex-spcx-stock-forecast-july-2026-nasdaq-100-inclusion-tradingkey) · NBC News / CNN / Al Jazeera — June 17 MOU context · Alpaca paper API (UNAVAILABLE)*
