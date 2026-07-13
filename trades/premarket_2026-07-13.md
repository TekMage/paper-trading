# Premarket Summary — Monday, July 13, 2026 (~9:00 AM ET)

> **🔴🔴🔴 CRITICAL HEADER: (1) GitHub Actions STILL DOWN — Day 28; no bot execution since June 18; ~17 missed trading sessions. (2) Iran FORMALLY CLOSED Strait of Hormuz Sunday — new escalation level; Brent +4% to $79.16 today. (3) Both XLE manual sell triggers active (Brent well below $85 and $90); XLE position status UNKNOWN. (4) S&P futures -0.4%, Nasdaq -0.8% on Iran/chip fears. (5) Alpaca API UNAVAILABLE from this environment.**

---

## Header

| Item | Value |
|---|---|
| **API Status** | UNAVAILABLE — Alpaca paper API unreachable (HTTP connection failed) |
| **GitHub Actions** | 🔴 DOWN — Day 28; no exec_open, exec_midday, or exec_eod since June 18 |
| **Last confirmed equity** | **$102,108.69** (exec_eod_2026-06-18 — ~17 trading sessions stale) |
| **Last confirmed options BP** | **$73,470.00** (June 18 EOD) |
| **Market context** | S&P futures -0.4%, Nasdaq -0.8%; Iran formally closed Strait of Hormuz Sunday; Brent crude +4% to $79.16; chip sector under pressure |

---

## Account Snapshot (Last Confirmed — June 18 EOD)

| Metric | Value | Note |
|---|---|---|
| Equity | **$102,108.69** | ~17 trading sessions stale; actual equity unknown |
| Return (inception) | **+2.11%** | vs $100K starting capital May 7 |
| vs Benchmark | **-0.21% alpha** | SPY was $748.46 on June 18 |
| Options BP remaining | **$73,470.00** | Layer 2 flat — no CSPs open since June 18 |

> Actual current equity is unknown. QQQ/tech drag (Nasdaq -0.8% today) works against the account; XLE if still held may be benefiting from Hormuz closure oil spike. No estimate added — confirm via Alpaca dashboard.

---

## Current Positions (Last Confirmed — June 18 EOD; ~17 Sessions Unconfirmed)

**Layer 1 — Core ETFs:**

| Symbol | Shares (Confirmed Jun 18) | Target | Approx Price (Jul 13 PM) | Status |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$700–715 est. | Unconfirmed; Nasdaq -0.8% premarket on Iran/chip headwinds |
| SPY | 13 | 13 | ~$730–740 est. | Unconfirmed; S&P -0.4% premarket |
| JETS | 80 | 80 | ~$30–33 est. | Unconfirmed; Brent +$5 from pre-conflict levels = airline fuel headwind; well below $35.69 trigger |
| **XLE** | **100 or 0 (UNKNOWN)** | **EXIT** | **~$58–63 est.** | 🔴🔴🔴 **BOTH manual sell triggers active (Brent $79.16 < $85 and < $90). BUT oil is RISING due to Hormuz closure — XLE may be in a winning trade. Rules say sell; thesis says hold. Verify position and decide before open.** |
| SPCX | 15 | 15 | ~$150–160 est. | Unconfirmed; hold — no action needed |
| XLY | Unknown | 0 (FORCE_CLOSE) | ~$115+ est. | 🔴 FORCE_CLOSE unexecuted 17+ sessions; manual close needed or wait for Actions restoration |

**Layer 2 — Open CSPs:**

FLAT. No confirmed open options positions since June 18. No bot execution to open new positions.

| Target | Strike / Expiry | DTE (Jul 13) | Underlying Est. | OTM% | Status |
|---|---|---|---|---|---|
| NVDA | $190P Jul18 (disqualified) | **5 DTE — EXPIRED RISK** | ~$195–200 | ~3–5% | ⛔ Disqualified by DTE_MIN=25 and near-expiry. On Actions restore: target Aug/Sep expiry, ≥8% OTM |
| AMZN | $215P Aug 21 | ~39 DTE | ~$245–249 est. | ~13–14% | ✅ Solid cushion; viable on bot resumption. No position open |

**Layer 2b — QQQ Calls:**
Not viable today. Nasdaq -0.8% premarket + Hormuz escalation = unfavorable conditions.

---

## Iran / Oil Status

| Item | Status (July 13 AM) |
|---|---|
| **Iran Strait of Hormuz** | 🔴🔴🔴 **FORMALLY CLOSED** — Iran declared passage "not possible" Sunday; applies to all vessel traffic |
| **US military action** | 4th wave of US strikes on Iran over weekend, including one-way attack drones at sea for first time |
| **Iran retaliation** | Drone/missile attacks on US-linked sites in Bahrain, Kuwait, Jordan |
| **MOU/ceasefire** | Dead since July 8 (Trump: "over"); talks continue but ceasefire invalidated |
| **Brent crude (Jul 13 AM)** | **$79.16/bbl** (+4.14% today; up from ~$74 pre-conflict baseline) |
| **vs $85 Brent trigger** | **$5.84 below — TRIGGER ACTIVE** (Brent well below $85; sell-all-XLE rule triggered) |
| **vs $90 Brent trigger** | **$10.84 below — TRIGGER ACTIVE** (Brent well below $90; sell-30-XLE rule triggered) |
| **Hormuz closure risk** | Bloomberg: Goldman Sachs warns "serious re-escalation could reintensify upside risk to oil prices" |
| **Oil output gap** | Global output still 9.4 mbpd below pre-war levels (IEA) |

**Critical Strategic Conflict on XLE:**
The XLE exit rules (Brent ≤ $90/$85) were designed for a scenario where oil FALLS (peace deal = lower oil = XLE down). The inverse has occurred: active Hormuz closure is pushing oil UP and XLE likely UP with it. If XLE is held, it may be performing well despite the rule triggers being active. Decision is yours: (a) follow the rules and sell, (b) recognize thesis inversion and hold with a mental stop. Either choice is defensible — but the position must be confirmed first.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE at market | $90/bbl | **🔴 TRIGGERED** — Brent $79.16; sell-30 rule active (if XLE held) |
| Brent ≤ $85 → exit all XLE | $85/bbl | **🔴 TRIGGERED** — Brent $79.16; exit-all rule active (if XLE held) |
| Iran MOU signed → sell 60 XLE immediately | MOU signed | **🔴 TRIGGERED (DEAD)** — MOU signed Jun 17; now invalidated Jul 8; original trigger fired |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 JETS | $35.69 | Not triggered — JETS est. ~$30–33; ~$2.69–$5.69 below trigger |

---

## Morning Priority Actions

1. **🔴 FIX GITHUB ACTIONS (Most Urgent — Day 28):** Go to [github.com/TekMage/paper-trading/actions](https://github.com/TekMage/paper-trading/actions) and re-enable all 3 workflows (`trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`). The bot has been offline for 28 calendar days — ~17 trading sessions missed, $0 Layer 2 premium collected, XLY FORCE_CLOSE unexecuted, no Layer 1 rebalancing. This is the single highest-priority action; every additional session is compounding strategic drift.

2. **🔴 DECIDE ON XLE BEFORE OPEN — Hormuz Closure Is Live:** Iran formally closed the Strait of Hormuz Sunday. Brent is up 4%+ this morning. Log into the Alpaca paper dashboard and: (a) confirm whether 100 XLE shares are held, (b) decide: follow the sell rules (both triggers active for weeks) OR hold given thesis inversion (oil going UP, not down, on Hormuz closure). If choosing to hold, set a mental downside stop (suggest: close if Brent drops back below $74 or conflict de-escalates sharply).

3. **🟡 VERIFY OVERALL ACCOUNT STATE:** With ~17 sessions of no bot execution and Nasdaq under pressure (-0.8% today), confirm actual equity via the Alpaca web dashboard before assuming the June 18 figure of $102K is still valid. QQQ at 50 shares is the largest holding and most sensitive to today's tech/chip selloff.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions offline — Day 28 | 🔴 CRITICAL | ~17 missed sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted; all Layer 1 rebalancing suspended |
| Strait of Hormuz formally closed | 🔴 CRITICAL | Iran declared closure Sunday; 20% of global oil/gas transit at risk; oil up 4% today; further spikes possible if closure holds |
| XLE position status unknown | 🔴 CRITICAL | Both sell triggers have been active for weeks; position needs immediate manual verification before today's open |
| Nasdaq/chip selloff today | 🔴 HIGH | S&P -0.4%, Nasdaq -0.8% premarket; NVDA ~$200 fighting green but chip sector (SMH) -5% backdrop; QQQ position at risk |
| Brent approaching $85 trigger territory | 🟡 MEDIUM | Brent $79.16 — $5.84 from $85. A Hormuz escalation event could push past threshold rapidly; monitor intraday |
| Account equity ~17 sessions stale | 🟡 MEDIUM | Cannot estimate net equity direction with confidence; confirm via Alpaca dashboard |
| XLY FORCE_CLOSE unexecuted | 🟡 MEDIUM | Bot offline; XLY was slated for exit in June sprint; unclear if still held |
| NVDA CSP target expired | 🟡 MEDIUM | Jul18 contract now 5 DTE — disqualified; select new Aug/Sep expiry when bot resumes |
| Iran-US active military exchanges | 🟡 MEDIUM | 4th wave of strikes + Iranian retaliation; further escalation possible intraday; elevated VIX environment |

---

*Sources: exec_eod_2026-06-18 (authoritative confirmed account state) · [Fortune — Brent $78.31–$79.22 today](https://fortune.com/article/price-of-oil-07-13-2026/) · [TradingKey — Brent +4.06% Jul 13](https://www.tradingkey.com/news/market-movers/262025238-market-movers-ukoil-20260713) · [Al Jazeera — Oil prices jump, Hormuz attacks](https://www.aljazeera.com/economy/2026/7/13/oil-prices-jump-as-us-and-iran-trade-attacks-over-strait-of-hormuz) · [Yahoo Finance — Dow/S&P/Nasdaq futures slip Jul 13](https://finance.yahoo.com/markets/live/stock-market-today-monday-july-13-dow-sp-nasdaq-113249278.html) · [CNBC — Chipmakers drag futures lower](https://www.cnbc.com/2026/07/12/stock-market-today-live-updates.html) · [CNN — Iran mediators July 10](https://www.cnn.com/2026/07/10/world/live-news/iran-war-trump) · [Bloomberg — Hormuz closure oil shock](https://www.bloomberg.com/graphics/2026-iran-war-hormuz-closure-oil-shock/) · [The National — Oil jumps Hormuz fears](https://www.thenationalnews.com/business/energy/2026/07/13/oil-jumps-amid-fears-of-prolonged-disruption-in-strait-of-hormuz/)*
