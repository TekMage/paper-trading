# Premarket Summary — Wednesday, July 15, 2026 (~9:00 AM ET)

> **CRITICAL HEADER:** (1) GitHub Actions DOWN — **Day 30**; all 3 trading workflows `disabled_manually` since June 19; no exec files since June 18. (2) Iran ceasefire is DEAD — US reimposed naval blockade July 14; Trump declared the deal "over"; no new MOU signed overnight. (3) Brent crude ~$84.73–$85.84 — borderline on the $85 exit-all-XLE trigger; $90 trim trigger ACTIVE. (4) NVDA recovered +4.06% yesterday to $211.80 on China chip approval news; premarket flat ~$211.62. (5) Market futures green: S&P +0.2%, Nasdaq +0.5%, boosted by soft CPI and ASML raising guidance. (6) Alpaca API UNAVAILABLE from this environment.

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **GitHub Actions** | 🔴 DOWN — Day 30; all 3 workflows `disabled_manually` since June 19; no trades executed since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — 19 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD) |
| **Last bot action** | June 18 open — submitted close on AMZN 220P Jul17 @ $2.20 (unfilled; canceled at EOD) |
| **Iran MOU** | 🔴 DEAD — Blockade reimposed July 14; Trump declared deal "over"; no new MOU signed overnight |
| **Brent crude** | **~$84.73–$85.84/bbl** (sources diverge; borderline on $85 exit-all trigger — see Iran/Oil section) |
| **Market context** | Futures green: S&P +0.2%, Nasdaq +0.5% on soft CPI + ASML AI demand signal |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Stale — 19 trading sessions unconfirmed |
| **Return (inception)** | **+2.11%** | vs $100K starting capital May 7, 2026 |
| **Options BP remaining** | **$73,470.00** | Layer 2 flat since June 18; no new CSPs opened |
| **SPY benchmark (Jun 18)** | **$748.46** (+2.32%) | SPY closed ~$754.90 Jul 13; inception return ~+3.19% |
| **Alpha (stale)** | **⚠️ ~-1.08%** | Our stale +2.11% vs SPY ~+3.19% inception |

> Actual equity is unknown. NVDA +4% recovery July 14, QQQ up, SPY up — equity likely improved from June 18. Still unconfirmed.

---

## Current Positions (Last Confirmed June 18 + Context)

### Layer 1 — Core ETFs (Unconfirmed 19 Sessions)

| Symbol | Shares | Target | Premarket / Last Known | Notes |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | ~$722+ est. | Nasdaq +0.5% futures; QQQ closed $717.80 Jul 13, recovered on CPI beat Jul 14; +0.5% futures today |
| **SPY** | 13 | 13 | ~$756+ est. | S&P +0.2% futures; SPY closed ~$754.90 Jul 13 |
| **JETS** | 80 | 80 | ~$32 est. | Brent headwind; $35.69 trigger still ~$3.69 away; not close |
| **XLE** | **100 (UNCONFIRMED)** | **EXIT** | **~$56+ est.** | 🔴 $90 trim trigger ACTIVE; $85 exit-all BORDERLINE (see below) |
| **SPCX** | 15 | 15 | ~$154–165 est. | No action needed |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | ~$116+ est. | 🔴 FORCE_CLOSE unexecuted 19 sessions; manual action or wait for bot restore |

### Layer 2 — Open CSPs

**FLAT** — No confirmed open options positions since June 18.

| Target | Strike / Expiry | DTE (Jul 15) | Underlying | Status |
|---|---|---|---|---|
| **NVDA** | $190P Jul18 | **3 DTE — EXPIRING FRIDAY** | ~$211.62 premarket | ⛔ DISQUALIFIED (below DTE_MIN=25); NOT held. NVDA at $211.62 = 10.9% OTM at strike $190. New target: Aug21 or Sep19, strike ≤$185 (≥8% OTM). Bot can enter post-Jul-18. |
| **AMZN** | $215P Aug21 | ~37 DTE | ~$248+ est. | ✅ Strong 13%+ OTM cushion. ⚠️ Do NOT enter before AMZN Q2 earnings (~Jul 30). Ready for bot entry post-resumption + post-earnings. |

**Layer 2b — QQQ Calls:** Nasdaq +0.5% premarket is positive. If QQQ opens above $720, the 2% OTM call target would be ~$734 strike. Hold for bot execution on resumption.

---

## Iran / Oil Status

| Item | Status (July 15 Premarket) |
|---|---|
| **Iran MOU (Jun 17)** | 🔴🔴🔴 **DEAD** — Ceasefire collapsed; US reimposed naval blockade effective July 14 20:00 GMT; Trump declared deal "over" |
| **US blockade** | 🔴 **IN EFFECT** — Reinstated July 14; US launched another wave of strikes on Iran overnight; Iran struck Gulf State targets |
| **New MOU / deal** | ❌ **NONE** — No new formal MOU signed overnight July 14–15; Trump said attacks will intensify |
| **Brent crude (Jul 15)** | **~$84.73–$85.84/bbl** (sources diverge: Trading Economics $84.73; alternate source $85.84) |
| **vs $90 trim trigger** | 🔴 **ACTIVE** — Brent $5–6 below $90; sell-30-XLE rule applies IF XLE held |
| **vs $85 exit-all trigger** | ⚠️ **BORDERLINE** — One source puts Brent at $84.73 (exit-all triggered); another $85.84 (cleared). Treat as active until confirmed above $85 |
| **vs MOU trigger** | ❌ NOT triggered today — No new formal signed MOU |

**Oil context:** Brent is trading in the $84–86 range, down slightly from yesterday's high of $87.55. The US reimposed blockade + Trump escalation language is keeping upside pressure elevated. The divergence between $84.73 and $85.84 matters: at $84.73, the exit-all-XLE trigger is active.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE** — Brent ~$84–86; sell-30-XLE applies IF XLE held |
| **Brent ≤ $85 → exit all XLE at market** | $85/bbl | ⚠️ **BORDERLINE** — Verify live Brent; sources diverge at $84.73 vs $85.84 |
| **Iran MOU signed → sell 60 XLE immediately** | Formal MOU | ❌ Not triggered — no new deal; blockade in effect; watch Oman-mediated talks |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69 | ✅ NOT triggered — JETS ~$32; ~$3.69 below; Brent headwind on fuel costs |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Fix GitHub Actions** — Go to `github.com/TekMage/paper-trading/actions` and re-enable all 3 trading workflows. Day 30 = ~57 missed sessions (open + midday + EOD). Bot will auto-execute Layer 1 rebalance + XLY FORCE_CLOSE + evaluate new CSPs at 9:30 AM if re-enabled tonight. |
| 🔴 2 | **Verify live Brent price** — Check real-time Brent (Bloomberg, CNBC, oilprice.com). If Brent ≤ $85: exit-all-XLE trigger is active and requires manual action. If Brent $85–$90: only the 30-share trim applies. Confirm XLE position via Alpaca paper dashboard first. |
| 🔴 3 | **XLE decision today** — $90 trim trigger (sell 30 XLE) is active regardless of Brent source. Position unconfirmed since June 18. Log into Alpaca paper dashboard, confirm position, and execute per trigger rules. Iran situation has no near-term resolution — rules say sell. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 30** | 57 missed trading sessions; Layer 2 generating $0 premium; XLY FORCE_CLOSE unexecuted; NVDA CSP window missed; QQQ calls missed; ~6–8 weeks of strategy paralysis |
| 🔴 **XLE trigger compliance** | $90 trim + potentially $85 exit-all both active. Every day without action is a rules violation. With Iran ceasefire dead and blockade in force, oil direction is a binary. |
| 🔴 **Iran escalation** | Blockade reimposed July 14; Trump says attacks will intensify; no diplomatic off-ramp visible. Oil supply disruption risk is structural, not a short-term blip. |
| 🟡 **Brent source divergence** | $84.73 vs $85.84 — a $1.11 difference that determines which trigger applies. Verify live before acting on XLE. |
| 🟡 **NVDA $190P Jul18 expiry Friday** | Expires in 3 trading days; confirms new Aug/Sep CSP window. NOT held (never confirmed filled). New target: Aug21 strike ≤$185 when bot resumes. |
| 🟡 **AMZN Q2 earnings ~Jul 30** | No new AMZN CSP until post-earnings. $215P Aug21 remains on deck. |
| 🟡 **XLY FORCE_CLOSE** | 19 sessions unexecuted. If still held, closing via Alpaca dashboard (sell at market) removes the position cleanly. |
| 🟢 **NVDA recovery** | NVDA closed $211.80 Jul 14 (+4.06%) on China chip approvals (H200 cleared for ZTE, Maginfra). Premarket $211.62 = flat. No negative catalyst today. |
| 🟢 **Market tailwind** | Soft CPI data + ASML AI demand signal (+30% production capacity increase, raised guidance) boosting tech. Nasdaq +0.5% futures; good environment for QQQ position. |

---

## Overnight News Summary

**Iran/Hormuz:** US reimposed naval blockade on Iran effective July 14 at 20:00 GMT after ceasefire collapsed (Iran struck commercial vessels in Hormuz, triggering US retaliation). Trump declared the June 17 MOU deal "over." No new MOU signed overnight. US struck new Iranian targets overnight July 14–15. Iran struck targets in Gulf States (Bahrain, Kuwait). Oman-mediated talks ongoing but no formal agreement.

**Brent crude:** Trading ~$84.73–$85.84/bbl — third consecutive session of gains; down slightly from yesterday's high of $87.55. Iran escalation/blockade maintains upside pressure.

**AI/Semiconductors:** ASML raised annual sales forecast above Wall Street estimates, citing AI demand; plans 30% increase in chipmaking equipment production capacity. NVDA and AMD rose after China received US approval to purchase H200 chips (ZTE, Maginfra for NVDA; one firm for AMD). NVDA +4.06% July 14 to $211.80; AMD +6.05% to $566.73; BofA raised AMD price target to $620.

**Market:** Nasdaq +0.5%, S&P +0.2% futures. Cooler-than-expected CPI data from Tuesday July 14 is supporting risk-on sentiment. Oil price pressure is the main headwind.

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · eod_2026-07-13.md · midday_2026-07-14.md · [Fortune — Brent crude Jul 15](https://fortune.com/article/price-of-oil-07-15-2026/) · [Yahoo Finance — Premarket Jul 15](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-july-15-dow-sp-nasdaq-091813320.html) · [TheStreet — Stock Market Today Jul 15](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-15-2026) · [Al Jazeera — US reimposed blockade Jul 14](https://www.aljazeera.com/news/2026/7/14/us-strikes-new-targets-in-iran-as-tehran-hits-gulf-states-hormuz) · [ABC News — MOU ceasefire breakdown timeline](https://abcnews.com/Politics/us-iran-ceasefire-mou-broke-timeline/story?id=134622392) · [NPR — US blockade Hormuz Jul 13](https://www.npr.org/2026/07/13/nx-s1-5891746/us-iran-strait-of-hormuz-updates) · [TradingKey — NVDA/AMD Chinese chip approvals](https://www.tradingkey.com/analysis/stocks/us-stocks/262029542-amd-nvidia-ai-chip-zte-kingsoft-maginfra-h200-boa-620-cpu-tradingkey) · [TradingKey — ASML +3.04% Jul 14](https://www.tradingkey.com/news/market-movers/262029358-market-movers-asml-20260714) · Alpaca paper API (UNAVAILABLE)*
