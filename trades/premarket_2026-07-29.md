# Premarket Summary — Wednesday, July 29, 2026

> **Generated: ~9:00 AM ET** | Market opens in ~30 minutes

---

## Header

- **API status:** UNAVAILABLE — curl to paper-api.alpaca.markets returned no data (consistent since June 19)
- **Last confirmed equity:** $102,108.69 (June 18 EOD — authoritative; ~29 unconfirmed trading sessions)
- **Market context:** Chip sell-off extends Day 3 — NVDA, AMD, MU, SNDK all lower premarket; Brent rebounds to $89.53 (relief from yesterday's $84.99 lows); AMZN/MSFT/META earnings tomorrow AH — peak volatility ahead

---

## Account Snapshot

> All figures from `exec_eod_2026-06-18.md` — last authoritative confirmed state. GitHub Actions DOWN — **Day 42**.

| Metric | Value | Source |
|---|---|---|
| **Equity** | $102,108.69 | exec_eod_2026-06-18.md (confirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026 |
| **Options BP remaining** | $73,470.00 | exec_eod_2026-06-18.md |
| **Account floor** | $87,500.00 | Bot halts new positions below this |
| **GitHub Actions** | ❌ DOWN — **Day 42** | All 3 workflows disabled since June 19 |
| **API status** | ❌ UNAVAILABLE | Consistent since June 19 |

> Actual current equity is unknown. ~29 unconfirmed trading sessions since June 18.

---

## Current Positions (from exec_eod_2026-06-18 + prior premarket context)

### Layer 1 — Core ETFs (GitHub Actions maintains these — but Actions DOWN Day 42)

| Symbol | Shares (Est.) | Target | Status |
|---|---|---|---|
| **QQQ** | 50 (est.) | 50 | At target; Nasdaq chip pressure premarket |
| **SPY** | 13 (est.) | 13 | At target |
| **JETS** | 80 (est.) | 80 | At target; $31.86 today; trigger at $35.69 (+$3.83 = +12%) |
| **XLE** | 100 (est.) | EXIT | 🔴 FORCE_CLOSE unexecuted — Day 42; $90 Brent trim trigger still active |
| **SPCX** | 15 (est.) | 15 | SpaceX ETF held |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 42; strategy violation ongoing |

### Layer 2 — Open CSPs

**No confirmed open options positions.** Bot offline Day 42; NVDA $190P Jul18 confirmed expired worthless.

| Target | Strike / Expiry | Price Today | Status |
|---|---|---|---|
| **NVDA CSP** | $190P Aug21 | $197.15 premarket (+0.07%) | ⚠️ DTE = 23 days — BELOW OPT_DTE_MIN=25; Aug21 window CLOSED for new entry today; next valid: Sep expiry |
| **AMZN CSP** | $215P (post-earnings) | ~$240 est. | ⛔ Hard block — AMZN earnings July 30 AH (tomorrow); reassess strike Thursday morning |

---

## Iran / Oil Status

| Item | Status |
|---|---|
| **June 17 MOU framework** | ⚠️ Under stress — conflict resumed July 6–7; informal ceasefire holds; Oman mediating Hormuz transit talks |
| **New formal MOU (July 29)** | ❌ NOT signed — informal ceasefire and ongoing negotiations only |
| **XLE MOU trigger** | ❌ NOT newly triggered — June 17 MOU was the prior trigger event (already flagged) |
| **Hormuz shipping** | 🔴 RESTRICTED — ~10 ships/day vs 88/day normal (as of July 23); effectively closed to commercial shipping |
| **Brent crude (Jul 29, ~8:30 AM ET)** | **$89.53/bbl** — up $0.45 from yesterday's close; rebounded sharply from yesterday's premarket lows of $84.99 |
| **vs $90 XLE trim trigger** | 🔴 **ACTIVE** — Brent clearly below $90; sell 30 XLE required (unexecuted) |
| **vs $85 XLE exit trigger** | 🟡 WATCH — $4.53 cushion at $89.53; not triggered today; yesterday's $84.99 low was the scare |

**Oil context:** Brent has recovered significantly from yesterday's alarming sub-$85 premarket prints back to $89.53 today. The $85 all-out trigger is not actively threatened. However, the $90 trim trigger (sell 30 XLE) has been active since Brent breached $88.81 intraday July 27 and remains unexecuted — manual action is required. The Hormuz strait remains effectively closed despite the June 17 MOU, with the second conflict cycle (July 6–7) having re-restricted traffic.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE** — Brent $89.53; sell 30 XLE MANUAL ACTION REQUIRED |
| **Brent ≤ $85 → exit ALL XLE at market** | $85/bbl | 🟡 WATCH — $4.53 cushion; not triggered today; monitor intraday |
| **Iran MOU signed → sell 60 XLE immediately** | New formal MOU | ❌ NOT triggered — informal ceasefire only |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69/share | ❌ NOT triggered — JETS $31.86; $3.83 (+12%) away |

---

## Morning Priority Actions

**1. 🔴 SELL 30 XLE AT MARKET — $90 BRENT TRIGGER ACTIVE**
> Brent at $89.53, clearly below $90 threshold. The trim trigger has been active since July 27 (intraday low $88.81) and remains unexecuted. Open Alpaca paper dashboard at 9:30 AM → sell 30 XLE at market. Manual action required — bot offline Day 42.

**2. 🔴 RE-ENABLE GITHUB ACTIONS — DAY 42 CRITICAL**
> Navigate to github.com/TekMage/paper-trading/actions and re-enable all 3 workflows before or at the 9:30 AM ET open. 42 days offline = $0 Layer 2 premium collected, XLY FORCE_CLOSE unexecuted, and NVDA Aug21 DTE window has now expired (DTE=23 < OPT_DTE_MIN=25). Single highest-leverage action available.

**3. 🟡 HOLD ON NVDA CSP — WINDOW CLOSED FOR AUG21**
> NVDA $190P Aug21 DTE = 23 days today, below OPT_DTE_MIN=25. Do NOT enter this position. If bot re-enabled, it will target Sep expiry (~DTE 50+). NVDA at $197.15 premarket ($7.15 OTM from $190P) with chip sell-off continuing — no manual entry appropriate today.

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **$90 Brent trim trigger active** | Brent $89.53 — sell 30 XLE required today (manual, bot offline) |
| 🔴 **GitHub Actions Day 42** | ~29 missed sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted |
| 🔴 **XLY FORCE_CLOSE Day 42** | Strategy violation ongoing; manual close or bot resumption required |
| ⚠️ **NVDA Aug21 window expired for entry** | DTE = 23, below OPT_DTE_MIN=25; Sep expiry is next valid window |
| ⚠️ **Chip sell-off Day 3** | NVDA, AMD, MU, SNDK all lower premarket; SK Hynix record results failed to impress; China chipmaking progress fears; AI financing sustainability concerns narrowing the trade to NVDA alone |
| ⚠️ **Big Tech earnings tomorrow AH (Jul 30)** | AMZN + MSFT + META all reporting after close; QQQ maximum volatility event; hard block on AMZN CSP until post-earnings |
| ⚠️ **Hormuz effectively closed** | Despite June 17 MOU, ~10 ships/day vs 88 normal; oil supply restriction ongoing; Brent volatility risk elevated |
| ⚠️ **$85 trigger yesterday scare** | Yesterday's premarket Brent lows hit $84.99; today's $89.53 rebound provides cushion but volatility remains |
| 🟢 **Brent recovered from $84.99 lows** | $89.53 today — $85 all-out exit trigger not actively threatened |
| 🟢 **Options BP preserved ($73,470)** | Dry powder intact since June 18; ready to deploy Layer 2 when Actions re-enabled |
| 🟢 **AMZN CSP hard block appropriate** | AMZN ~$240 est.; $215P ~10.4% OTM; reassess Thursday post-earnings |
| 🟢 **JETS healthy gap from trigger** | $31.86 vs $35.69 trigger; $3.83 (+12%) away; Brent-driven fuel relief a structural tailwind |

---

## Market Context — Premarket July 29

| Asset | Premarket | Note |
|---|---|---|
| **Brent crude** | **$89.53/bbl** | Recovered from yesterday's $84.99 lows; $90 trim still active |
| **NVDA** | $197.15 (+0.07%) | Slight recovery from $197.01 close; chip sector broadly under pressure |
| **AMD** | Down est. ~5–8% | Extending yesterday's -8% decline; AI chip trade narrowing to NVDA |
| **JETS** | $31.86 (range $30.89–$31.96) | Trigger at $35.69 — $3.83 away |
| **S&P 500 futures** | Data unavailable | Chip sell-off likely weighing on Nasdaq; Big Tech earnings tomorrow key catalyst |

---

*Sources: exec_eod_2026-06-18.md · premarket_2026-07-28.md · [Fortune — Brent Jul 29](https://fortune.com/article/price-of-oil-07-29-2026/) · [TipRanks — Chip sell-off Jul 29](https://www.tipranks.com/news/semiconductor-stocks-nvda-amd-micron-and-sndk-extend-their-sell-off-in-pre-market-today-july-29-what-triggered-the-latest-slide) · [247 Wall St — AMD/chip rout Jul 28](https://247wallst.com/investing/2026/07/28/amd-sinks-8-marvell-sinks-7-intel-fall-6-as-ai-chip-trade-narrows-to-nvidia/) · [Al Jazeera — Hormuz glut Jul 2](https://www.aljazeera.com/news/2026/7/2/with-hormuz-reopened-has-the-oil-shortage-turned-into-a-glut) · [CNN — Iran MOU Jun 18](https://www.cnn.com/2026/06/18/world/live-news/iran-war-trump-israel-lebanon) · NVDA/JETS prices via web search · Alpaca API UNAVAILABLE · ~9:00 AM ET*
