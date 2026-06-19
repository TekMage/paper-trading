# Premarket Summary — 2026-06-19 (Juneteenth Holiday — Markets CLOSED)

> **CRITICAL ALERT: Iran MOU signed June 18. XLE exit triggers are LIVE. Next trading opportunity: Monday June 22 at open.**

---

## Header

- **API status:** UNAVAILABLE (Alpaca paper API unreachable from this environment)
- **Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18.md — authoritative)
- **Market context:** Markets CLOSED today (Juneteenth federal holiday). S&P 500 closed +1.08% Thursday June 18 — Iran deal rally. XLE fell Thursday as Iran deal compressed oil-risk premium.

---

## Account Snapshot (from exec_eod_2026-06-18)

| Metric | Value |
|---|---|
| Equity | $102,108.69 |
| Our return (MTD) | +2.11% |
| SPY return | +2.31% ($748.46) |
| Alpha | -0.21% vs SPY |
| Options BP remaining | $73,470.00 |
| Account floor | $87,500 (bot halts new positions below this) |

---

## Current Positions (exec_eod_2026-06-18 + strategy state)

**Layer 1 — Core ETFs:**

| Symbol | Shares | Status |
|---|---|---|
| QQQ | 45 | At target |
| SPY | 13 | At target |
| JETS | 80 | At target — monitor $35.69 trigger (~30.76 last known price, ~$31.33 52-wk high) |
| XLE | 100 | **⚠️ EXIT TRIGGERED — see below** |
| XLY | Closing | FORCE_CLOSE_EQUITY in progress (June sprint exit) |

**Layer 2 — Open CSPs:**

| Position | Strike | Expiry | Status |
|---|---|---|---|
| NVDA CSP | $190P | Jul 18 | Safe — NVDA ~$200.42, ~5% OTM |
| AMZN CSP | $215P | TBD | Monitor — AMZN target per strategy |

> Note: All options GTC orders placed Thursday were cancelled at session close per Alpaca paper behavior. Bot will re-open at Monday open session.

**Layer 2b — QQQ Calls:**
- Bot buys 1 contract (2% OTM, DTE 10–20) at open if no long QQQ options held. Will execute Monday.

---

## ⚠️ IRAN / OIL STATUS — CRITICAL

| Item | Status |
|---|---|
| Iran MOU signed? | **YES — signed June 18, 2026 in Versailles** |
| Deal details | 14-point MOU: Strait of Hormuz reopens, US lifts oil export sanctions, Iranian frozen assets released. Final deal negotiations ongoing. |
| Brent crude today | **$79.95/bbl** |
| vs. $90 trim trigger | **$10.05 below** — trigger ACTIVE |
| vs. $85 exit trigger | **$5.05 below** — trigger ACTIVE |

**Both Brent thresholds are breached AND the Iran MOU is signed.**

The Iran MOU trigger supersedes both Brent triggers. Per strategy rules:

- **Iran MOU signed → Sell 60 XLE at market immediately (MANUAL)**
- **Brent ≤ $85 → Exit ALL remaining XLE (MANUAL)**

Net result: **Full XLE exit (100 shares) is warranted.** Execute at Monday open (June 22).

XLE last price: ~$53.85–$54.59 (June 18). At 100 shares, full exit raises ~$5,400 in cash.

---

## Manual Triggers — Status as of 2026-06-19

| Trigger | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | $79.95 | **TRIGGERED** |
| Brent ≤ $85 → exit ALL XLE | $85 | $79.95 | **TRIGGERED** |
| Iran MOU signed → sell 60 XLE immediately | — | **SIGNED June 18** | **TRIGGERED** |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 | ~$30.76 (June 15) | Not triggered — watching |

---

## Morning Priority Actions (for Monday June 22 open)

1. **SELL 100 XLE at market — Monday June 22 open.** Iran MOU signed + Brent $79.95 = full exit warranted under all three triggered rules. Do not wait for further confirmation.

2. **Watch JETS on Monday.** Iran deal lowers jet fuel costs → airlines benefit → JETS may rally toward the $35.69 (+30%) exit trigger. Last known: $30.76, 52-wk high $31.33. Gap to trigger = ~$4.93 (~16%). Could move fast in a risk-on Monday open.

3. **Confirm NVDA and AMZN CSP status at Monday open.** Alpaca cancelled all options GTC orders at Thursday close. Bot will re-enter positions at Monday open session — verify fills by midday.

---

## Risk Flags

- **XLE exit timing risk:** Markets closed today. The Iran MOU was signed Thursday afternoon. Energy shares already fell Thursday (XLE ~$53.85 vs prior close ~$55.36). Monday open may gap down further on Iran/oil headlines — or may partially recover if final-deal optimism fades. Execute quickly at open.
- **Options BP reservation:** Midday BP appears lower due to order reservations; recovers by EOD if unfilled. Don't be alarmed by intraday BP compression on Monday.
- **JETS breakout watch:** A strong Iran/oil risk-off + airline tailwind on Monday could push JETS toward $35.69 trigger. Have sell order ready to place if it approaches.
- **NVDA $190P CSP safety margin is thin:** NVDA at ~$200, CSP at $190 = ~5% OTM. Any sharp NVDA drop on semiconductor news could threaten the position. Sector had volatile June (chip index -10% on June 5). Monitor.
- **Alpha lag:** Account +2.11% vs SPY +2.31% — slight underperformance. XLE has been a drag. Exiting XLE should improve alignment going forward.

---

## Sources

- Iran MOU: [CNN — US-Iran 14-point MOU text](https://www.cnn.com/2026/06/17/middleeast/us-iran-war-mou-text-intl) | [NBC News — Trump sealed Iran deal](https://www.nbcnews.com/world/iran/trump-finally-sealed-iran-deal-now-talks-final-deal-begin-rcna350663)
- Brent oil: [oilpriceapi.com](https://www.oilpriceapi.com/live/brent-crude-oil-price) | [Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)
- Markets closed Juneteenth: [Schwab market update](https://www.schwab.com/learn/story/stock-market-update-open)
- NVDA ~$200.42: [Yahoo Finance semiconductor roundup](https://finance.yahoo.com/markets/stocks/articles/3-semiconductor-stocks-buy-while-143037327.html)
- JETS ~$30.76 (June 15): [StockAnalysis](https://stockanalysis.com/etf/jets/)
- XLE ~$53.85: [StockAnalysis](https://stockanalysis.com/etf/xle/)
