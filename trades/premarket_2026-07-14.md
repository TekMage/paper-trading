# Premarket Summary — Tuesday, July 14, 2026 (~9:00 AM ET)

> **CRITICAL HEADER: (1) GitHub Actions STILL DOWN — Day 29; no bot execution since June 18; ~18 missed trading sessions. (2) US NAVAL BLOCKADE TAKES EFFECT TODAY AT 4 PM ET (20:00 GMT) — highest-risk afternoon binary event; XLE/Brent highly volatile into close. (3) NEW CEASEFIRE EXTENSION DEAL: PBS/NBC/Axios report US-Iran reached new agreement to extend ceasefire and reopen Strait of Hormuz — "ships beginning to cross through the Strait" but challenges remain; deal fragile. (4) Brent surged overnight to $86.35–$86.99 (+~10% from Jul 13 close $78.85) on blockade announcement — $85 XLE exit trigger CLEARED; $90 trim trigger still active. (5) CPI 3.5% vs 3.8% expected — cooler inflation; Nasdaq slightly positive premarket. (6) Alpaca API UNAVAILABLE.**

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **GitHub Actions** | 🔴 DOWN — Day 29; no exec_open, exec_midday, or exec_eod since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — ~18 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD) |
| **Jul 13 confirmed closes** | QQQ $717.80 · SPY $754.90 · S&P 500 -0.79% · Nasdaq -1.55% · Brent $78.85/bbl (from eod_2026-07-13.md) |
| **Market context** | S&P futures -0.2%, Nasdaq +0.2–0.5%; CPI June 3.5% (below 3.8% est.); new US-Iran ceasefire extension deal reported but fragile; Brent jumped to $86.35–$86.99 overnight (+~10%) on US naval blockade announcement; blockade takes effect 4 PM ET today |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| Equity | **$102,108.69** | ~18 trading sessions stale; actual equity unknown |
| Return (inception) | **+2.11%** | vs $100K starting capital May 7 |
| vs Benchmark | **-0.21% alpha** | SPY was $748.46 on June 18 |
| Options BP remaining | **$73,470.00** | Layer 2 flat — no CSPs open since June 18 |

> Actual current equity is unknown. Nasdaq slightly positive today (CPI beat); XLE likely up on Brent surge (+3.66%). Cannot confirm without live API or Actions resume. Verify via Alpaca dashboard.

---

## Current Positions (Last Confirmed — June 18 EOD; ~18 Sessions Unconfirmed)

**Layer 1 — Core ETFs:**

| Symbol | Shares (Confirmed Jun 18) | Target | Est. Price (Jul 14 PM) | Status |
|---|---|---|---|---|
| QQQ | 50 | 50 | **$717.80** (Jul 13) → ~$718–726 est. today | Confirmed Jul 13 close $717.80; Nasdaq +0.2–0.5% premarket today — slight tailwind |
| SPY | 13 | 13 | **$754.90** (Jul 13) → ~$752–758 est. today | Confirmed Jul 13 close $754.90; S&P -0.2% premarket; CPI beat may soften intraday |
| JETS | 80 | 80 | ~$32.09–32.41 est. | Unconfirmed; Jul 12–13 data ~$32.09–$32.41; Hormuz partial reopen may ease fuel cost headwind |
| **XLE** | **100 or 0 (UNKNOWN)** | **EXIT** | **~$55–58 est.** | 🔴 **Position unconfirmed ~18 sessions. $90 trim trigger active (Brent $86.35 < $90). $85 exit trigger CLEARED (Brent rose above $85). XLE likely UP today on Brent +3.66%.** |
| SPCX | 15 | 15 | ~$150–165 est. | Unconfirmed; memory chip/IPO adjacent names mentioned positive today; hold |
| XLY | Unknown | 0 (FORCE_CLOSE) | ~$116+ est. | 🔴 FORCE_CLOSE unexecuted ~18 sessions; manual close needed or wait for Actions restoration |

**Layer 2 — Open CSPs:**

FLAT. No confirmed open options positions since June 18.

| Target | Strike / Expiry | DTE (Jul 14) | Underlying Est. | OTM% | Status |
|---|---|---|---|---|---|
| NVDA | $190P Jul18 (disqualified) | **4 DTE — EFFECTIVELY EXPIRED** | ~$195–200 est. | ~3–5% | ⛔ Disqualified and near-expiry. On Actions restore: target Aug/Sep expiry, ≥8% OTM. NVDA fundamentals strong — data center revenue $193.7B FY2026; 80% AI accelerator market share. |
| AMZN | $215P Aug 21 | ~38 DTE | ~$240–250 est. | ~12–14% | ✅ Viable on bot resumption. ⚠️ AMZN Q2 earnings ~Jul 30 — do NOT enter new CSP until post-earnings. |

**Layer 2b — QQQ Calls:**
Slightly favorable today — Nasdaq +0.2-0.5% premarket, CPI beat. If Actions restore today, 1x QQQ call (2% OTM, 10–20 DTE) would be viable if no long QQQ options already held.

---

## Iran / Oil Status

| Item | Status (July 14 AM) |
|---|---|
| **Iran / Hormuz — NEW DEAL** | 🟡 **NEW CEASEFIRE EXTENSION REPORTED** — PBS, NBC, CSIS reporting US-Iran reached agreement to extend ceasefire and reopen Strait of Hormuz; "ships beginning to cross through the Strait of Hormuz." Deal described as fragile; challenges remain over transit terms and pace of negotiations. |
| **Original MOU (Jun 17)** | Dead since Jul 8 (Trump: "over"); this is a reported extension/new agreement, not the original Islamabad Memorandum |
| **Market reaction to deal** | Oil RISING +3.66% to $86.35 — market is NOT pricing in a durable Hormuz resolution; skeptical the deal will hold |
| **US naval blockade** | 🔴🔴🔴 **TAKES EFFECT TODAY at 20:00 GMT = 4:00 PM ET** — US declared "Guardian of Hormuz Strait"; 20% toll on cargo value for safe passage; enforcement starts this afternoon |
| **US military** | 4th wave of US strikes on Iran reported Jul 13; Iranian retaliation on Bahrain/Kuwait/Jordan bases |
| **MOU signed?** | Not a signed MOU — described as "initial deal" and "extended ceasefire"; not the formal trigger event |
| **Brent crude (Jul 14 AM)** | **$86.35–$86.99/bbl** (+3.66% from Jul 13's $79.16; +15.5% from pre-conflict ~$75 baseline) |
| **vs $90 Brent trigger** | **$3.01–3.65 below $90 — TRIGGER ACTIVE** (Brent ≤ $90 → sell 30 XLE; manual action required IF XLE is held) |
| **vs $85 Brent trigger** | **$0.35–$1.99 ABOVE $85 — TRIGGER CLEARED** (Brent rose above $85; exit-all rule no longer triggered — rules apply when Brent FALLS below threshold) |
| **Iran MOU formal signing** | No signed formal MOU — "initial deal" reports only; formal MOU signing would trigger sell-60-XLE rule |

**Strategic note on XLE/Brent:** The XLE exit rules were designed for a peace-deal scenario (oil falls). The inverse is occurring — Brent at $86.35 is UP 15%+ from pre-conflict levels. If XLE is still held, the position is likely performing well. The $85 trigger is no longer active (Brent above it). The $90 trim rule (sell 30) remains technically active. A formal MOU signing that holds and truly reopens Hormuz would send oil back down — that's when the exit rules would be most relevant. Watch for whether today's reported ceasefire extension shows signs of durability.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE at market | $90/bbl | **🔴 ACTIVE** — Brent $86.35–$86.99; sell-30-XLE rule technically active (IF XLE held) |
| Brent ≤ $85 → exit all XLE | $85/bbl | **✅ CLEARED** — Brent rose above $85; exit-all rule no longer active |
| Iran MOU signed → sell 60 XLE immediately | Formal MOU signed | **🟡 WATCH** — "Initial deal" to extend ceasefire reported but NOT a formal signed MOU; no trigger yet; watch for formal signing event |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 JETS | $35.69 | Not triggered — JETS ~$32.09–$32.41; ~$3.28–$3.60 below trigger |

---

## Morning Priority Actions

1. **🔴 FIX GITHUB ACTIONS (Most Urgent — Day 29):** Go to [github.com/TekMage/paper-trading/actions](https://github.com/TekMage/paper-trading/actions) and re-enable all 3 workflows. ~18 trading sessions missed — $0 Layer 2 premium collected, XLY FORCE_CLOSE unexecuted, NVDA Jul18 CSP now 4 DTE and effectively expired. Every additional day compounds strategy drift. With cool CPI data and Nasdaq slightly positive, today is a favorable day to restore execution.

2. **🔴 XLE DECISION BEFORE 4 PM ET BLOCKADE DEADLINE:** The US naval blockade of Iranian shipping begins at 4 PM ET today — a high-stakes binary event. Brent jumped from $78.85 (Jul 13 close) to $86.35+ overnight on this announcement. If XLE is held, you're exposed to: (a) spike to $90+ if Iran retaliates at blockade implementation → both XLE triggers deactivated (oil above $90 = rules inactive); (b) crash if ceasefire extension news takes hold and markets price in Hormuz reopening. Recommend: verify XLE position via Alpaca dashboard, decide on a plan before 4 PM. The $85 trigger is now cleared (Brent above $85). $90 is the next threshold — $3–4 away.

3. **🟢 CPI BEAT CREATES OPENING SESSION:** June CPI 3.5% vs 3.8% expected is a positive catalyst. Nasdaq +0.2–0.5% premarket. If Actions resume today, the bot can open positions in a relatively favorable equity environment. QQQ call (Layer 2b) and AMZN CSP (after Jul 30 earnings) are the best near-term Layer 2 opportunities.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions offline — Day 29 | 🔴 CRITICAL | ~18 missed sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted; NVDA Jul18 CSP effectively expired |
| US blockade effective 4 PM ET today | 🔴 CRITICAL | Blockade begins 20:00 GMT; Iranian response (mine-laying, tanker attack, missile strike) would spike Brent toward $90+; XLE becomes a high-volatility hold into close |
| Ceasefire extension fragile | 🔴 HIGH | PBS/NBC report new deal but "challenges remain"; Brent +$7.50 overnight signals market skepticism; formal MOU signing not confirmed |
| XLE / XLY position status unknown | 🔴 HIGH | Both positions unconfirmed ~18 sessions; XLE trigger status has CHANGED (see above); XLY FORCE_CLOSE still unexecuted |
| Brent approaching $90 threshold | 🟡 MEDIUM | Brent $86.35–$86.99 — only $3–4 below $90; if Hormuz deal collapses or new escalation event, $90 trim trigger could be cleared (deactivated) rapidly |
| Account equity ~18 sessions stale | 🟡 MEDIUM | $102K confirmed June 18; CPI beat + Nasdaq positive today = modest tailwind for QQQ/SPY; cannot confirm net without live data |
| AMZN Q2 earnings risk | 🟡 MEDIUM | AMZN earnings ~Jul 30; do NOT open new AMZN CSP until post-earnings; 38 DTE $215P is viable but wait |
| NVDA Jul18 CSP target expired | 🟡 MEDIUM | 4 DTE — disqualified by DTE_MIN=25; select new Aug/Sep expiry when Actions resume |
| SPCX (SpaceX) position | 🟢 LOW | SPCX referenced in today's memory chip/IPO news roundup; 15 shares target; hold |

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · [Fortune — Brent $86.35–$86.99 Jul 14](https://fortune.com/article/price-of-oil-07-14-2026/) · [PBS — Iran-US ceasefire extension deal](https://www.pbs.org/newshour/world/iran-and-u-s-reach-an-initial-deal-to-extend-the-ceasefire-and-open-the-strait-of-hormuz-but-challenges-remain) · [NBC — Trump-Iran initial deal to end war, open Hormuz](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513) · [CSIS — US-Iran Deal to End the War](https://www.csis.org/analysis/united-states-and-iran-announce-deal-end-war-state-play) · [Yahoo Finance — Futures slip, Iran tensions, CPI Jul 14](https://finance.yahoo.com/markets/stocks/live/stock-market-today-tuesday-july-14-231302282.html) · [TheStreet — S&P futures fall Middle East Jul 14](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-14-2026) · [TradingKey — Memory chips rebound, IBM -22%, CPI Jul 14](https://www.tradingkey.com/analysis/stocks/us-stocks/262029081-nvda-ibm-skhynix-dram-mu-spcx-sndk-tradingkey) · [NPR — US strikes Iran, Hormuz blockade renewed](https://www.npr.org/2026/07/13/nx-s1-5891746/us-iran-strait-of-hormuz-updates) · [AMD AI chip surge, Zen 6 launch](https://www.interactivecrypto.com/amd-s-ai-chip-surge-and-zen-6-launch-drive-stock-higher-amid-sector-rally-jul-2026)*
