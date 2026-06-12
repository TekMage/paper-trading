# Premarket Summary — 2026-06-12

| | |
|---|---|
| API status | UNAVAILABLE (curl returned no data) |
| Last confirmed equity | $100,513.74 (exec_eod 2026-06-11) |
| Market context | S&P futures +0.6% on Iran deal optimism; SpaceX SPCX IPO debut today |

---

## Account Snapshot (from exec_eod_2026-06-11.md)

| Metric | Value |
|---|---|
| Equity | $100,513.74 |
| Return vs start ($100k) | +0.51% |
| SPY benchmark return | +0.90% (SPY @ $738.15) |
| Alpha vs SPY | -0.39% |
| Options BP remaining | $55,459.24 |
| Account floor | $87,500 (bot halts below this) |

---

## Current Positions

**Layer 1 — Core ETFs (GitHub Actions maintains targets):**
- QQQ: 50 shares (target)
- SPY: 13 shares (target)
- JETS: 80 shares (target)
- XLE: 100 shares (target) — **SEE MANUAL TRIGGER BELOW**
- XLY: being closed via FORCE_CLOSE_EQUITY (June sprint exit)

**Layer 2 — Open CSPs:**
- NVDA $190P Jul 18 — NVDA trading ~$205.50 premarket, strike ~7.8% OTM, not at risk
- AMZN $215P — status per exec_eod (no close actions triggered overnight)

**Layer 2b — Call Buying:**
- QQQ: 1 contract, 2% OTM, DTE 10–20 — bot buys at open if no long QQQ options held

**IPO Watchlist:**
- **SPCX (SpaceX): TODAY is debut day (June 12).** Priced at $135/share ($75B IPO, Nasdaq). Bot should auto-buy 15 shares at open (~$2,025 cost). Verify execution in exec_open_2026-06-12.md after market open.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran MOU signed? | **NO** — "largely negotiated," still needs Trump final approval. Al Jazeera reports draft agreed but not yet executed. |
| Brent crude | **$87.43/bbl** (down 3.26% on the day) |
| Distance from $90 trim trigger | **TRIGGER HIT — $87.43 is below $90** |
| Distance from $85 exit trigger | $2.43 above $85 — not yet triggered |

**Iran context:** A 60-day ceasefire extension MOU is in final negotiation, with terms including reopening the Strait of Hormuz and Iran halting nuclear weapons development. No signature yet as of premarket. If signed this weekend, sell 60 XLE immediately.

---

## Manual Triggers to Monitor Today

| Trigger | Status | Action Required |
|---|---|---|
| Brent ≤ $90 | **ACTIVE — $87.43** | **Sell 30 XLE at market — manual action required NOW** |
| Brent ≤ $85 | Not yet ($2.43 away) | Sell all remaining XLE at market |
| Iran MOU signed | Not yet (imminent risk) | Sell 60 XLE immediately |
| JETS ≥ $35.69 (+30%) | Monitor — JETS cost ~$27.45 | Close all 80 JETS at market |

---

## Morning Priority Actions

1. **XLE SELL 30 SHARES — MANUAL ACTION REQUIRED:** Brent at $87.43 has crossed the $90 trigger. Bot does not execute this automatically. Sell 30 XLE at market open at 9:30 AM ET.

2. **Watch SPCX at open:** SpaceX (SPCX) begins trading on Nasdaq today at $135. The bot's IPO watchlist targets 15 shares (~$2,025). Confirm execution in exec_open file after 9:30 AM. If bot fails to fill, place manually.

3. **Iran deal watch:** A signed MOU today or this weekend would trigger an immediate sell of 60 XLE. With Brent already at $87.43 and falling on deal optimism, oil could approach $85 quickly if an MOU is announced. Stay alert through the weekend.

---

## Risk Flags

- **XLE/Oil risk (HIGH):** Brent at $87.43 has breached the first trim trigger. Iran deal chatter is actively pushing oil lower; a signed agreement this weekend could drive Brent to or through $85, triggering a full XLE exit.
- **NVDA CSP cushion:** NVDA at ~$205.50 keeps the $190P ~7.8% OTM with ~5 weeks of time value. No immediate risk, but semiconductor sector saw a $1.4T single-session selloff earlier in June — volatility is elevated.
- **SpaceX IPO liquidity:** SPCX at $135 is a record-breaking debut. First-day volatility expected; the bot will buy 15 shares at open, but price could move significantly. Not a strategic risk given the small position size (~$2,025).
- **Exec_eod shows no Layer 2 detail:** Options BP at $55,459 is healthy. No CSP close triggers were fired overnight.

---

*Sources:*
- [Axios — What's inside the Iran deal Trump is close to signing](https://www.axios.com/2026/05/24/iran-deal-strait-hormuz-sanctions-nuclear)
- [Al Jazeera — US-Iran 60-day proposal: What we know](https://www.aljazeera.com/news/2026/5/29/us-iran-60-day-proposal-what-we-know)
- [Trading Economics — Brent crude oil price](https://tradingeconomics.com/commodity/brent-crude-oil)
- [Bloomberg — US Premarket Movers June 12, 2026](https://www.bloomberg.com/news/articles/2026-06-12/us-stock-futures-today-adobe-amd-echostar-rocket-lab-travelers)
- [Benzinga — S&P 500 June 12 open prediction](https://www.benzinga.com/markets/prediction-markets/26/06/53160378/sp500-june-12-open-up-or-down-polymarket-spacex-ipo-iran-deal)
- [CNBC — SpaceX IPO live updates](https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html)
- [NPR — SpaceX $75B record-breaking IPO](https://www.npr.org/2026/06/11/nx-s1-5853199/spacex-ipo-price-elon-musk)
- [Seeking Alpha — Nvidia AMD BofA top chip stocks](https://seekingalpha.com/news/4592277-nvidia-amd-still-among-bofas-top-chip-stocks-as-ai-likely-to-stay-stronger-for-longer)
