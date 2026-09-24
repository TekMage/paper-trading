# Premarket Summary — Monday, July 20, 2026 (~9:00 AM ET)

> **CRITICAL HEADER:** (1) GitHub Actions DOWN — **Day 35** (calendar); all 3 trading workflows `disabled_manually` since June 19; no exec files since June 18. (2) **Brent crude ~$86–88/bbl** — ABOVE $85 exit-all trigger; BELOW $90 trim trigger; $90 trim (sell 30 XLE) remains unexecuted. (3) Iran: June 17 Islamabad MOU signed; 60-day negotiating window through mid-August; technical talks continuing as of July 17; no final comprehensive nuclear deal as of this morning; July 15 US airstrikes disrupted deal briefly but talks resumed. (4) Market futures POSITIVE today: S&P 500 +0.5%, Nasdaq-100 +1.0%, Dow +0.1% — semis recovering from 3-day July 13–17 slide. (5) **NVDA $190P Jul18 expired Friday (July 18)** — was never confirmed open; new CSP window opens (Aug/Sep strike ≤$185). (6) **AMZN Q2 earnings ~July 30** — do NOT enter new AMZN CSP before then. (7) Alpaca API UNAVAILABLE from this environment.

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable from this remote environment |
| **GitHub Actions** | 🔴 DOWN — Day 35 (calendar since June 19); all 3 workflows `disabled_manually`; no trades or EOD files since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — ~23 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD — Layer 2 flat since then) |
| **Iran/Hormuz** | ⚠️ NEGOTIATIONS ACTIVE — June 17 MOU signed (60-day window through mid-Aug); July 15 US airstrikes disrupted; technical talks resumed as of July 17; no final comprehensive deal yet |
| **Brent crude** | **~$86–88/bbl est.** (July 17 close ~$86.09–$88.10) — ✅ ABOVE $85 exit trigger; 🔴 BELOW $90 trim trigger (trim still unexecuted) |
| **Market context** | Futures POSITIVE: S&P 500 +0.5%, Nasdaq-100 +1.0% — semis recovering after 3-day slide; chip stocks likely to open green |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Stale — ~23 trading sessions unconfirmed since GitHub Actions went down |
| **Return (inception)** | **+2.11%** | vs $100,000 starting capital May 7, 2026 |
| **Options BP remaining** | **$73,470.00** | Layer 2 flat since June 18; no new CSPs in 35 days |
| **SPY benchmark (Jun 18)** | **$748.46** (+2.32%) | SPY has rallied since; alpha gap likely wider now |
| **Alpha (stale)** | **⚠️ ~-1.5% to -2.0% est.** | Bot outage + SPY rally since June 18 widening the gap |

> Actual equity is unknown. S&P futures +0.5% and Nasdaq +1.0% today suggests a green open for QQQ/SPY holdings, partially recovering the July 13–17 selloff. Real equity could be slightly above or below June 18 figure depending on total position drift over 5 weeks.

---

## Current Positions (Last Confirmed June 18 + Context)

### Layer 1 — Core ETFs (Unconfirmed — ~23 Sessions Stale)

| Symbol | Shares | Target | Today's Context | Notes |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | Nasdaq-100 +1.0% premarket | Semis recovering; QQQ likely opens green today |
| **SPY** | 13 | 13 | S&P 500 +0.5% premarket | Broad market recovery; position on target |
| **JETS** | 80 | 80 | ~$31–33 est. | Brent ~$87 is mild headwind; $35.69 exit trigger ~$3–4 away; not close |
| **XLE** | **100 (unconfirmed)** | **EXIT (per CLAUDE.md)** | Brent ~$87, XLE ~$57 est. | 🔴 FORCE_CLOSE + $90 trim both unexecuted; see triggers below |
| **SPCX** | 15 est. | 15 | ~$131–135 range est. | At/near cost basis; Nasdaq recovery today may help; Nasdaq-100 forced inclusion buy still pending |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | — | 🔴 FORCE_CLOSE unexecuted ~23 sessions; manual close or bot resumption required |

### Layer 2 — Open CSPs

**FLAT** — No confirmed open options positions since June 18.

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA** | $190P Jul18 | **EXPIRED Friday July 18** — was never confirmed open. New entry window: Aug21 or Sep19, strike ≤$185. Nasdaq +1% today; semis recovery = less premium but better timing. Evaluate post-Actions resumption. |
| **AMZN** | $215P Aug21 | **HOLD — do NOT enter before July 30 earnings.** $215P target remains; underlying est. ~$245–255; strong OTM cushion. Enter post-earnings once Actions re-enabled. |

**Layer 2b — QQQ Calls:** Nasdaq +1% today is favorable. No manual action; evaluate on bot resumption.

---

## Iran / Oil Status

| Item | Status (July 20 Premarket) |
|---|---|
| **June 17 Islamabad MOU** | ✅ SIGNED — 14-point agreement; reopened Strait of Hormuz; set 60-day negotiating window through ~mid-August |
| **60-day window** | Active through ~August 15, 2026 — technical talks on uranium enrichment, HEU stockpile ongoing |
| **July 15 disruption** | US airstrikes briefly put deal "in collapse"; Iran agreed to nuclear inspectors and Treasury waived crude sanctions through Aug 21 as talks resumed |
| **As of July 20** | No final comprehensive nuclear agreement signed; deal in active negotiating phase; geopolitical risk remains elevated |
| **Brent crude (est.)** | **~$86–88/bbl** — July 17 premarket $86.09, closed ~$88 per sources; today's est. in same range |
| **vs $90 trim trigger** | 🔴 **ACTIVE** — Brent ~$3–4 below $90; sell-30-XLE rule unexecuted for weeks; manual action required |
| **vs $85 exit-all trigger** | ✅ **NOT triggered** — Brent above $85; monitor intraday; $85 was briefly hit July 16 ($84.63) |
| **MOU trigger** | ⚠️ June 17 MOU = trigger technically fired but deal in subsequent flux; no clean "signed and finalized" state; monitor for final agreement or breakdown |

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE** — Brent ~$87; rule firing; 30-share trim unexecuted for weeks; **manual action on Alpaca dashboard** |
| **Brent ≤ $85 → exit all XLE at market** | $85/bbl | ⚠️ NOT triggered today (~$87); was triggered briefly July 16; monitor intraday |
| **Iran MOU signed → sell 60 XLE immediately** | Formal final agreement | ⚠️ June 17 MOU signed but deal still in negotiating phase; no final comprehensive agreement yet; monitor |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69 | ✅ NOT triggered — JETS ~$31–33 est.; ~$3–4 below trigger; not imminent |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Re-enable GitHub Actions** — Day 35 of outage. Go to `github.com/TekMage/paper-trading/actions` and re-enable all 3 workflows. Trading-open.yml will run today at 9:30 AM ET if re-enabled in the next ~30 minutes. This is the highest-leverage action: Layer 1 rebalance, XLY FORCE_CLOSE, and CSP evaluation all automated once resumed. |
| 🔴 2 | **Execute XLE trim (sell 30 shares manually)** — The $90 trim rule has been active for weeks; Brent ~$87, well below $90. Sell 30 XLE at market via Alpaca paper dashboard. The exit-all trigger ($85) was briefly active July 16; with Brent bouncing to $87–88, trim is the appropriate action today unless Brent drops to $85 again. |
| 🟡 3 | **Monitor Brent intraday and Iran news** — Iran technical talks are active this week (60-day window through mid-August). Any formal final agreement triggers sell-60-XLE immediately. Also watch if Brent dips below $85 intraday — exit-all rule re-activates. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 35** | ~23 missed trading sessions; no Layer 2 premium generated; XLY FORCE_CLOSE unexecuted; strategy paralyzed. Re-enabling today (before 9:30 AM ET) lets bot auto-handle all open session tasks. |
| 🔴 **$90 XLE trim unexecuted** | Brent ~$87 — trigger has been firing for weeks. 30-share trim unexecuted. Execute manually on Alpaca dashboard. |
| 🟡 **$85 exit-all near-miss July 16** | Brent hit $84.63 on July 16 (trigger activated), then bounced. Monitor for re-test; set alert at $85. |
| 🟡 **Iran deal in negotiating phase** | June 17 MOU signed, but July 15 airstrikes tested stability. Talks resumed. Final agreement could come any day in the 60-day window (through ~Aug 15). MOU trigger technically fired June 17; monitor for clean finalization. |
| 🟡 **AMZN Q2 earnings ~July 30** | Do NOT enter new AMZN CSP before July 30 earnings. $215P Aug21 remains on deck post-earnings. |
| 🟡 **NVDA CSP window opens** | $190P Jul18 expired Friday (July 18). New target: Aug21 or Sep19, strike ≤$185. Nasdaq recovery today improves entry context post-Actions resumption. |
| 🟡 **XLY FORCE_CLOSE unexecuted** | Position force-close flag has been pending ~23 sessions. Will auto-execute when GitHub Actions re-enabled. |
| 🟢 **Options BP intact** | $73,470 options BP confirmed June 18; no positions opened since. Capital preserved and ready to deploy once bot re-enabled. |
| 🟢 **Market positive today** | S&P +0.5%, Nasdaq +1.0%; semis recovering from 3-day slide. Green open benefits QQQ, SPY, SPCX positions. |

---

## Overnight News Summary

**Iran/Hormuz:** The June 17 Islamabad MOU (14-point agreement) remains the governing framework. The deal reopened the Strait of Hormuz and set a 60-day window (~through August 15) for follow-on nuclear negotiations covering uranium enrichment and HEU stockpile levels. July 15 US airstrikes created instability; Iran agreed to allow nuclear inspectors to resume and Treasury waived crude oil sanctions through August 21 as confidence-building measures. Technical talks were expected to continue through this week (week of July 20). No final comprehensive nuclear agreement has been signed as of this morning. Brent crude's ~$86–88 level reflects a "deal progressing but not finalized" premium environment.

**Brent crude:** Estimated ~$86–88/bbl this morning. July 17 premarket was $86.09 (+2% from July 16's $84.63 low). Research suggests a possible close around $88.10 on July 17. The $90 sell-30-XLE trigger remains active and unexecuted. The $85 exit-all trigger was nearly activated July 16 but Brent bounced — monitor today.

**Market (July 20 premarket):** S&P 500 +0.5%, Nasdaq-100 +1.0%, Dow slightly positive. Semiconductors recovering after the July 13–17 multi-day slide. AI capex cycle intact: hyperscalers committed to ~$1.8T AI spend 2026–27; NVDA still holds ~80% of AI accelerator market. AMD $60B Meta MI400 deal confirmed. NVDA/MRVL strategic partnership (NVLink Fusion, optical interconnects) active. Broadly risk-on tone heading into the week; mega-cap tech earnings season begins shortly.

**SPCX/SpaceX:** Was at $131.11 on July 17 (below $135 IPO price), pressured by Starship test abort + Nasdaq selloff. Today's Nasdaq recovery may provide partial support. Nasdaq-100 forced inclusion buy (~$4.3B) may serve as a floor.

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · premarket_2026-07-17 (most recent prior) · CNN / NBC News (June 17 MOU) · Axios (60-day ceasefire/MOU) · CNBC live updates July 19–20 · Yahoo Finance / NAI500 semiconductor analysis · Alpaca paper API (UNAVAILABLE)*
