# Premarket Summary — 2026-06-05

| | |
|---|---|
| **API Status** | UNAVAILABLE (confirmed test failure this morning) |
| **Last Confirmed Equity** | $101,749.56 (exec_eod_2026-06-04) |
| **Options BP Remaining** | $73,805.20 |
| **Market Context** | S&P futures -0.61% premarket; chip weakness + May Jobs Report at 8:30 AM ET |

---

## Account Snapshot

| Metric | Value |
|--------|-------|
| Equity | $101,749.56 |
| Our return (since inception) | +1.75% |
| SPY benchmark return | +3.37% |
| Alpha | -1.62% |
| Options BP remaining | $73,805.20 |

*All figures from exec_eod_2026-06-04 — authoritative GitHub Actions data.*

---

## Current Positions

### Layer 1 — Core ETFs (GitHub Actions maintains these)

| Symbol | Shares | Notes |
|--------|--------|-------|
| QQQ | 45 | Chip weakness dragging Nasdaq premarket |
| SPY | 13 | S&P futures -0.61% |
| XLY | 40 | Negative open expected; consumer discretionary |
| JETS | 80 | Monitor vs. $35.69 exit trigger |
| XLE | 100 | **Active watch — Iran/oil triggers below** |

### Layer 2 — Open CSPs

**Likely no open CSPs as of EOD June 4:**

- **AMZN $250P Jun26**: Closed — BTC confirmed at open June 4
- **NVDA $180P Jul17**: Submitted June 4 at $1.79 limit — **fill unconfirmed, likely did NOT fill**. Options BP was essentially unchanged from midday ($73,876) to EOD ($73,805); a filled $180P would have consumed ~$18K in margin and driven BP down to ~$55,805. Order may have expired unfilled at session close.

Confirm status via Alpaca dashboard. GitHub Actions may re-queue the NVDA CSP today. Strategy targets per plan: NVDA $190P and AMZN $245P — bot handles execution, no manual entry.

---

## Iran / Oil Status

### MOU Signed? **NO**

No signing announcement overnight. As of June 1 (Soufan Center), "U.S.-Iran Distrust Holds Up an Agreement." A tentative 60-day ceasefire framework exists — Hormuz open, no tolls, Iran mines cleared — but VP Vance indicated late May it was unclear whether Trump would approve. Negotiations remain active; no breakthrough confirmed.

**A signed MOU triggers: sell 60 XLE immediately (manual action required)**

### Brent Crude

| | |
|---|---|
| **Price (June 5)** | **$95.25/bbl** (+0.23% from June 4) |
| **$90 trim trigger distance** | $5.25 away (~5.5% drop needed) — **NOT triggered** |
| **$85 exit trigger distance** | $10.25 away (~10.8% drop needed) — **NOT triggered** |

Brent has declined from ~$101 (June 3) → ~$97 (June 4) → $95.25 today. Three consecutive sessions lower, driven by Iran diplomacy hopes. A signed MOU could push Brent toward or through $90 in a single session.

---

## Manual Triggers to Monitor Today

| Trigger | Action Required |
|---------|----------------|
| Brent ≤ **$90.00** | Sell 30 XLE at market (manual) |
| Brent ≤ **$85.00** | Exit all 100 XLE at market (manual) |
| Iran MOU **signed** | Sell 60 XLE immediately (manual) |
| JETS ≥ **$35.69** (+30% from $27.45 cost) | Close all 80 JETS at market (manual) |

---

## Morning Priority Actions

1. **Iran MOU watch — elevated risk today**: Brent is now only $5.25 from the $90 trim trigger and trending lower for three straight sessions. Keep Axios/Reuters open through the session. A signing announcement could push Brent through $90 in a single move, triggering manual XLE action before the algo catches it at EOD.

2. **May Jobs Report at 8:30 AM ET**: S&P futures -0.61% is partly jobs-driven. A strong NFP = yields up, tech under pressure (negative QQQ/SPY); soft NFP = possible relief rally. Assess whether the print changes conditions for NVDA CSP re-entry today — higher IV from morning volatility improves premium.

3. **Confirm NVDA CSP status on Alpaca dashboard**: The June 4 $180P limit order at $1.79 likely expired unfilled. Strategy target is $190P Jul18. With chip sector weak this morning (NVDA may open lower on post-COMPUTEX mean reversion), IV may be elevated — good conditions for new CSP entry once the open volatility settles. Let GitHub Actions handle execution.

---

## Risk Flags

- **Brent declining trend — $90 trigger approaching**: $101 (Jun 3) → $97 (Jun 4) → $95.25 (Jun 5). The $90 XLE trim trigger is now only 5.5% away. Iran deal risk is asymmetric: no progress = oil stable; deal = sharp drop.
- **Chip sector weakness today**: S&P futures down on chip names after a big COMPUTEX week (Jensen Huang called Marvell "the next trillion-dollar company" on June 2; MRVL +32%). Mean reversion in AI semis is possible — watch NVDA direction before any CSP decisions.
- **NVDA CSP gap**: No confirmed open CSP after AMZN closed. Account is undeployed in Layer 2, leaving premium income on the table. GitHub Actions should re-queue today.
- **Alpha lag**: -1.62% vs. SPY since inception. Core ETF portfolio is not capturing full AI/semiconductor upside that's driven recent SPY outperformance.
- **API unavailable**: Cannot verify live position values, option marks, or pending order status. All figures are T-1 from exec_eod. Check Alpaca dashboard directly for real-time data.
- **Jobs report opening volatility**: Wide bid-ask spreads at the open are expected; avoid limit orders in the first 5–10 minutes if acting manually.

---

*Sources: exec_eod_2026-06-04 (authoritative equity/BP), midday_2026-06-04 (CSP fill context), [Axios](https://www.axios.com/2026/05/24/iran-deal-strait-hormuz-sanctions-nuclear) / [Al Jazeera](https://www.aljazeera.com/news/2026/5/29/us-iran-60-day-proposal-what-we-know) / [Soufan Center](https://thesoufancenter.org/intelbrief-2026-june-1/) (Iran deal), [Fortune](https://fortune.com/article/price-of-oil-06-04-2026/) / [TradingEconomics](https://tradingeconomics.com/commodity/brent-crude-oil) (Brent crude), [TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-05-2026) / [Stocktwits](https://stocktwits.com/news-articles/markets/equity/stock-market-today-nasdaq-sp500-futures-jobs-data-lulu-celh-mrln-keel-nvidia/cZ0FgcjRezy) (S&P futures), [CNBC](https://www.cnbc.com/2026/06/02/jensen-huang-nvidia-marvell-technology-trillion-dollar-ai.html) / [Motley Fool](https://www.fool.com/coverage/stock-market-today/2026/06/02/stock-market-today-june-2-marvell-technology-surges-after-nvidia-ceo-highlights-ai-infrastructure-role/) (semiconductor news)*
