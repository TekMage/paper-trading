# Premarket Summary — Friday, July 17, 2026 (~9:00 AM ET)

> **CRITICAL HEADER:** (1) GitHub Actions DOWN — **Day 32**; all 3 trading workflows `disabled_manually` since June 19; no exec files since June 18. (2) **Brent crude $86.09/bbl — ABOVE $85 today** (was $84.63–$84.80 yesterday, BELOW trigger; bounced overnight +2.04%). $90 trim trigger remains active; $85 exit-all trigger NOT currently active. (3) Iran: overnight nuclear talks show renewed progress — Iran agreed to allow nuclear inspectors, Treasury waiving sanctions on Iranian crude through Aug 21; no new formal MOU; technical talks continue this week. Brent's bounce (+2%) may reflect optimism on deal progress. (4) Market futures sharply lower: S&P 500 -0.8%, Nasdaq-100 -1.6%, Dow -0.6% — Netflix -9% on Q3 revenue miss + semiconductors extending 3-day slide. (5) SPCX at $131.11 — below $135 IPO price; Starship test abort added pressure. (6) Alpaca API UNAVAILABLE from this environment.

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **GitHub Actions** | 🔴 DOWN — Day 32; all 3 workflows `disabled_manually` since June 19; no trades since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — 21 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD) |
| **Iran/Hormuz** | ⚠️ NEGOTIATIONS PROGRESSING — Iran agreed to nuclear inspectors; Treasury waiving crude sanctions through Aug 21; technical talks ongoing; no new formal MOU signed; Brent bounced +2% overnight on renewed optimism |
| **Brent crude** | **~$86.09/bbl** (+2.04%) — ✅ ABOVE $85 exit-all trigger today; 🔴 $90 trim trigger still active |
| **Market context** | Futures sharply lower: S&P 500 -0.8%, Nasdaq-100 -1.6%, Dow -0.6%; Netflix -9% premarket on Q3 miss; chip selloff extends to Day 3 |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Stale — 21 trading sessions unconfirmed |
| **Return (inception)** | **+2.11%** | vs $100K starting capital May 7, 2026 |
| **Options BP remaining** | **$73,470.00** | Layer 2 flat since June 18; no new CSPs opened in 32 days |
| **SPY benchmark (Jun 18)** | **$748.46** (+2.32%) | SPY has rallied since; inception benchmark likely ~+3–4% now |
| **Alpha (stale)** | **⚠️ ~-1.0% to -1.5% est.** | Bot outage + strong SPY rally widening gap |

> Actual equity is unknown. Nasdaq -1.6% premarket today, QQQ and NVDA likely to open lower; SPCX below IPO price; real equity likely below June 18 figure.

---

## Current Positions (Last Confirmed June 18 + Context)

### Layer 1 — Core ETFs (Unconfirmed — 21 Sessions Stale)

| Symbol | Shares | Target | Today's Context | Notes |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | Nasdaq-100 -1.6% premarket | Chip selloff + Netflix miss; QQQ opens lower today |
| **SPY** | 13 | 13 | S&P -0.8% premarket | Broad-based decline; futures down |
| **JETS** | 80 | 80 | ~$31–32 est. | Brent +2% is a headwind for airlines; $35.69 trigger ~$3.7–4.7 away; not close |
| **XLE** | **100 (UNCONFIRMED)** | **EXIT (per CLAUDE.md)** | **XLE $57.06; Brent +2% today** | ⚠️ See XLE trigger note below — $85 trigger NOT active today but WAS active yesterday |
| **SPCX** | 15 | 15 | **$131.11 (below $135 IPO price)** | Starship test abort + Nasdaq selloff; at ~$135 cost basis — slightly underwater |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | ~$116+ est. | 🔴 FORCE_CLOSE unexecuted 21 sessions; manual close or bot resumption required |

### Layer 2 — Open CSPs

**FLAT** — No confirmed open options positions since June 18.

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA** | $190P Jul18 | **EXPIRES TOMORROW (Jul 18)** — NOT held (never confirmed open). New window post-expiry: Aug21 strike ≤$185. Chip selloff today; NVDA likely weak; evaluate new CSP entry next week. |
| **AMZN** | $215P Aug21 | ~$248+ underlying est. — strong OTM cushion. ⚠️ Do NOT enter before AMZN Q2 earnings (~Jul 30). Bot target post-earnings + Actions resumption. |

**Layer 2b — QQQ Calls:** Nasdaq -1.6% is a significant headwind; no manual action needed; hold for bot resumption.

---

## Iran / Oil Status

| Item | Status (July 17 Premarket) |
|---|---|
| **June 17 MOU** | ⚠️ AMBIGUOUS — was "in collapse" after US airstrikes July 15; overnight talks show renewed diplomatic progress |
| **Overnight development** | 🟡 Iran agreed to allow international nuclear inspectors to resume. Treasury waiving all US sanctions on Iranian crude through Aug 21, 2026. Pakistan and Qatar: "high-level talks concluded; technical talks continue this week." VP Vance held White House briefing on progress. |
| **New formal MOU** | ❌ **NONE signed overnight** — but progress materially positive; deal could re-solidify this week |
| **Brent crude (Jul 17)** | **~$86.09/bbl** (+2.04% vs yesterday's $84.63–$84.80) — bouncing on Iran diplomacy optimism |
| **vs $90 trim trigger** | 🔴 **ACTIVE** — Brent still $3.91 below $90; trim-30-XLE rule applies |
| **vs $85 exit-all trigger** | ✅ **NOT triggered today** — Brent at $86.09, above $85. WAS triggered yesterday at $84.63–$84.80 (no action taken; price has since recovered). |
| **MOU trigger** | ⚠️ June 17 MOU was signed — trigger technically fired — but deal stalled; nuclear talks now re-progressing; monitor for formal confirmation |

> **XLE trigger note:** The $85 exit-all rule was active as recently as yesterday. Today's +2% Brent bounce means the trigger is not technically firing at this moment. However, the $90 trim rule (sell 30 XLE) remains active and has been active for weeks. If Brent dips below $85 again, the exit-all rule re-triggers. The "MOU signed" trigger from June 17 was never executed due to Actions outage.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE** — Brent $86.09; rule has been active for weeks; 30-share trim still unexecuted |
| **Brent ≤ $85 → exit all XLE at market** | $85/bbl | ⚠️ **NOT triggered today** (Brent $86.09) — WAS triggered yesterday; watch for re-test |
| **Iran MOU signed → sell 60 XLE immediately** | Formal new MOU | ⚠️ June 17 MOU = trigger technically fired; deal in flux; nuclear talks progressing; monitor |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69 | ✅ NOT triggered — JETS ~$31–32; ~$3.7–4.7 away; Brent rise is a JETS headwind |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Re-enable GitHub Actions** — Day 32 of outage. Go to `github.com/TekMage/paper-trading/actions` and re-enable all 3 workflows. The bot will handle XLY FORCE_CLOSE, Layer 1 rebalance, and CSP evaluation at open (9:30 AM ET today). This is the highest-leverage action: every further session it's down is missed income and unexecuted strategy. |
| 🔴 2 | **Decide on XLE trim (30 shares)** — The $90 trim rule has been active for weeks (Brent ~$86, well below $90). Execute manually via Alpaca paper dashboard: sell 30 XLE at market. Separately: if Brent dips below $85 again today, exit-all rule re-triggers — monitor. |
| 🟡 3 | **Watch Iran talks this week** — Nuclear inspectors approved, sanctions temporarily waived, technical talks continuing. A re-formalized deal this week could trigger the "MOU signed → sell 60 XLE" rule. Monitor news; if confirmed, sell XLE immediately via Alpaca dashboard. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 32** | ~62 missed sessions; no Layer 2 premium generated; XLY FORCE_CLOSE unexecuted; strategy paralyzed. Re-enabling today would let bot auto-handle at 9:30 AM. |
| 🔴 **$90 XLE trim rule unexecuted** | Brent has been below $90 for weeks; 30-share trim rule active and unexecuted. Manual action on Alpaca dashboard. |
| 🟡 **$85 exit-all — yesterday's trigger, today's bounce** | Brent dipped to $84.63 yesterday (trigger active) then bounced +2% to $86.09 today. If oil sells off again intraday, the exit-all rule re-fires. Watch Brent intraday; set mental alert for $85. |
| 🟡 **Iran diplomatic whipsaw risk** | Talks re-progressing overnight (inspectors, sanctions waiver) but full deal not signed. Oil is reacting to headlines; Brent could swing $3-5 on any formal announcement or breakdown. If MOU formalizes, sell 60 XLE immediately. |
| 🟡 **Broad market selloff today** | S&P -0.8%, Nasdaq -1.6%; Netflix -9% on Q3 miss; chip stocks extending 3-day slide. QQQ, SPY, SPCX all likely to open lower. Weakness may create CSP entry opportunities once bot is re-enabled. |
| 🟡 **SPCX at $131.11** | Below $135 IPO price for third consecutive session; Starship test abort added pressure today. Our 15-share position at ~$135 cost is ~$3/share underwater. No strategy rule triggers; hold per plan but monitor Nasdaq-100 inclusion buy flow (~$4.3B forced buy). |
| 🟡 **NVDA $190P Jul18 — expires tomorrow** | Expires in 1 session (tomorrow, Jul 18). NOT held (never confirmed open). New CSP window opens post-expiry; target Aug21 or Sep19, strike ≤$185. Chip weakness today may create better premium. Evaluate post-Actions resumption. |
| 🟡 **AMZN Q2 earnings ~Jul 30** | Do NOT enter new AMZN CSP before earnings. $215P Aug21 remains on deck post-earnings. |
| 🟢 **Options BP intact** | $73,470 options BP confirmed June 18; no positions opened since. Capital preserved and ready to deploy once bot re-enabled. |

---

## Overnight News Summary

**Iran/Hormuz (overnight July 16–17):** Positive diplomatic developments overnight: Iran agreed to allow international nuclear inspectors to resume operations inside Iran. The US Treasury confirmed it was waiving all existing US sanctions on Iranian crude oil and petrochemical products through August 21, 2026. VP Vance held a White House briefing on progress. Pakistan and Qatar issued a joint statement: "high-level talks have concluded; technical talks will continue through the week." No new formal MOU signed, but tone has shifted meaningfully from the collapse signaled by July 15 US airstrikes. Brent's +2% bounce likely reflects this optimism. If technical talks produce a signed agreement this week, the "MOU signed → sell 60 XLE immediately" rule fires.

**Brent crude:** $86.09/bbl (+2.04%) on July 17 premarket, bouncing from yesterday's $84.63–$84.80 low (which briefly triggered the exit-all rule). Iran diplomacy driving the bounce. Still ~$3.91 below the $90 trim trigger.

**Market (July 17 premarket):** Dow -0.6%, S&P 500 -0.8%, Nasdaq-100 -1.6%. Netflix shares -9% premarket after Q2 missed estimates on EPS ($0.80 vs $0.79 est.) and revenue ($12.56B vs $12.58B est.) but Q3 guidance was the real miss: $12.86B revenue guidance vs $13B expected. Chip stocks extending their slide for a third consecutive session. Broad risk-off tone heading into weekend.

**NVDA/Semiconductors:** Chip stocks have now fallen for three consecutive sessions. NVDA weak today on broader Nasdaq selloff; no company-specific negative news overnight. AI capex cycle remains intact (TSMC +36% YoY, hyperscalers spending $1.8T on AI 2026–27), but near-term price action remains negative. NVDA $190P Jul18 expires tomorrow — not a current position.

**SPCX/SpaceX:** $131.11 premarket (-3.1% from $135.27 prev close). An aborted Starship test flight adding pressure on top of Nasdaq-100 selloff. Stock at 52-week low ($130.74 intraday low). Nasdaq-100 forced inclusion buy of ~$4.3B may provide support; lockup expiration pressure remains.

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · premarket_2026-07-16 · [Fortune — Brent $86.09 Jul 17](https://fortune.com/article/price-of-oil-07-17-2026/) · [Yahoo Finance — Market Today Jul 17](https://finance.yahoo.com/markets/live/stock-market-today-friday-july-17-dow-sp-500-nasdaq-092345307.html) · [CBS News — Vance Iran nuclear inspectors](https://www.cbsnews.com/live-updates/iran-us-deal-trump-war-negotiations/) · [Al Jazeera — US-Iran talks Jun 23](https://www.aljazeera.com/news/2026/6/23/what-the-us-and-iran-agreed-and-disagreed-on-first-day-of-talks) · [Yahoo Finance — Netflix earnings miss Jul 17](https://finance.yahoo.com/markets/stocks/article/netflix-stock-tanks-after-q3-revenue-falls-short-co-ceo-says-not-all-views-are-created-equal-201022485.html) · [TradingView — Netflix -9% premarket](https://www.tradingview.com/news/moneycontrol:a6c0bfef4094b:0-netflix-shares-drop-9-in-pre-market-trade-as-q3-revenue-guidance-misses-estimates/) · [TradingEconomics — SPCX $131.11](https://tradingeconomics.com/spcx:us) · [StockAnalysis — XLE $57.06](https://stockanalysis.com/etf/xle/) · Alpaca paper API (UNAVAILABLE)*
