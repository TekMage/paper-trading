# Pre-Market Summary — Wednesday, May 27, 2026

> **API Status:** 🔴 BLOCKED — Day 24. No bot-side execution. All trades via app.alpaca.markets.
> **Prior confirmed equity:** $101,779.23 (exec_eod_2026-05-26 ✅)
> **⚠️ BP ANOMALY:** exec_open $56,066 → exec_midday $1,290 → exec_eod $56,126. Requires broker verification.

---

## ACCOUNT SNAPSHOT

| Metric | Value | Note |
|--------|-------|------|
| Equity (confirmed, May 26 EOD) | **$101,779.23** | ✅ exec_eod confirmed |
| Equity (premarket est.) | **~$101,800–$102,100** | Flat premarket; TSLA +2.35% lifts XLY |
| Total return (vs $100K May 7) | **+1.78%** | Confirmed |
| SPY benchmark (May 26 close) | **$750.46** | SPY total return: +2.59% from $731.53 |
| SPY premarket (May 27) | **~$750.75** | +0.04% from close — flat |
| Alpha vs SPY | **-0.81%** | Confirmed EOD; JETS/QQQ closing the gap |
| Options BP (confirmed EOD May 26) | **$56,126.60** | ⚠️ Recovered from midday $1,290 — verify reason |
| Account vs $87,500 floor | **✅ OK** | ~$14,300 cushion |

**⚠️ CRITICAL BP ANOMALY NOTE:** exec_open showed $56,066 → exec_midday dropped to $1,290 (TSLA $330P CSP filled per plan, consuming ~$33K collateral) → exec_eod recovered to $56,126. The full recovery to $56,126 EOD is unexplained. Possible causes: (a) TSLA $330P was day order and lapsed/was auto-cancelled; (b) TSLA $330P was BTC'd by bot; (c) other positions closed. **VERIFY ALL OPTION POSITIONS AT BROKER BEFORE TAKING ANY ACTION.**

---

## POSITIONS — Premarket Estimates

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | May 26 Close | Premarket May 27 | Unreal P&L | P&L% | Status |
|--------|-----|----------|--------------|-----------------|------------|------|--------|
| QQQ | 45 | $710.93 | ~$726 | **~$725.25** | **+$645** | **+2.01%** | ✅ QQQ flat pm; tech leads |
| SPY | 13 | $736.39 | $750.46 | **~$750.75** | **+$187** | **+1.95%** | ✅ S&P at record; flat pm |
| XLY | 40 | $117.00 | ~$121 | **~$122.50** | **+$220** | **+4.70%** | 🟢 TSLA +2.35% pm lifts XLY |
| JETS | 80 | $27.45 | $28.28 | **~$28.30** | **+$68** | **+3.10%** | 🟢 Iran deal progress; hold |
| XLE | 100 | $56.70 | ~$58.75 | **~$58.52** | **+$182** | **+3.21%** | ✅ Brent $99.18; all triggers intact |
| **TOTAL L1** | | **~$53,947 cost** | | **~$55,249** | **~+$1,302** | **+2.41%** | |

*Sources: SPY $750.75 from Benzinga May 27 levels; QQQ $725.25 from Benzinga May 27 pivot; NVDA $218 pm; TSLA $443.79 pm (+2.35%, from Public.com premarket at 7:15 AM ET); Brent $99.18 (-0.41% from $99.58). XLE est. from Brent move. JETS est. flat from $28.28 close.*

### Layer 2/2b — Cash-Secured Puts

| Symbol | Strike | Expiry | DTE | Stock Premarket | OTM$ | OTM% | Sold For | Est. Mark | 50% BTC | Status |
|--------|--------|--------|-----|----------------|------|------|----------|-----------|---------|--------|
| NVDA R2 | $180 | Jun 18 '26 | **22** | **~$218** | $38 | **17.4%** | **$0.78** | ~$0.03–0.05 | $0.39 | 🔴 **BTC DAY 24 — ABSOLUTE PRIORITY** |
| NVDA R3 | $180 | Jun 18 '26 | **22** | **~$218** | $38 | **17.4%** | **$0.66** | ~$0.03–0.05 | $0.33 | 🔴 **BTC with R2 — near zero** |
| TSLA $330P | $330 | Jun 26 '26 | **30** | **~$443** | $113 | **25.5%** | **$1.29** | ~$0.30–0.50 | $0.65 | ⚠️ **VERIFY STATUS — BP anomaly** |
| TSLA $370P | $370 | Jun 20 '26 | **24** | **~$443** | $73 | **16.5%** | ~$11 | ~$0.02–0.05 | $5.50 | 🔴 **VERIFY STATUS — Day 24** |
| AMZN $245P | $245 | Jun 20 '26 | **24** | **~$268** | $23 | **8.6%** | ~$5 | ~$0.02–0.05 | $2.50 | 🔴 **VERIFY STATUS — Day 24** |

**Cumulative Options P&L (tracking):**
| Position | Sold | Status | P&L |
|----------|------|--------|-----|
| NVDA R1 $180P Jun18 | $1.67 | ✅ Closed $0.76 | **+$91 confirmed** |
| INTC $90P Jun18 | $2.61 | ✅ Closed $1.18 (May 22) | **+$143 confirmed** |
| TSLA $370P Jun20 | ~$11 | 🟡 Likely GTC closed (BP evidence) | **~+$550 unconfirmed** |
| AMZN $245P Jun20 | ~$5 | 🟡 Likely GTC closed (BP evidence) | **~+$250 unconfirmed** |
| NVDA R2 $180P | $0.78 | 🔴 Open (verify) — BTC today | **~+$73–75 unrealized** |
| NVDA R3 $180P | $0.66 | 🔴 Open (verify) — BTC today | **~+$61–63 unrealized** |
| TSLA $330P Jun26 | $1.29 | ⚠️ Status unknown — verify | **+$129 credit received (if open)** |
| **Total est.** | | | **~+$1,297–1,301 (if $330P open)** |

---

## WATCHLIST — Premarket Prices (May 27, 2026)

| Symbol | Premarket | vs Prior Close | Key Level | Note |
|--------|-----------|---------------|-----------|------|
| SPY | **~$750.75** | +0.04% | Pivot $750.75; target $756.25 | At record; flat pm |
| QQQ | **~$725.25** | ~-0.1% | Pivot $725.25; target $732 | Tech leader; slight pm pullback |
| XLY | **~$122.50** | ~+1.2% | — | TSLA +2.35% pm drives XLY up |
| JETS | **~$28.30** | ~flat | Cost $27.45; target $35.69 | Iran deal progress → hold |
| XLE | **~$58.52** | ~-0.4% | $90 Brent trim trigger (~$8 away) | Brent $99.18; hold |
| IWM | **~$284** | ~+0.7% | — | Small caps bid on Iran deal hopes |
| NVDA | **~$218.00** | ~flat/↓ from $228 est | Pivot $218; support $212 | Post-earnings stabilization; $180P deep OTM ✅ |
| TSM | **~$414** | ~flat | — | AI foundry; no position |
| TSLA | **$443.79** | **+2.35% ↑** | $330 strike $113 OTM | TSLA surging pm; TSLA $330P ultra-safe |
| AMZN | **~$268** | ~flat | $245 strike $23 OTM (8.6%) | AWS steady |
| INTC | **~$110** | ~flat | Position closed May 22 | No position |
| DRAM | **~$46** | ~flat | — | No position |
| MU | **~$912** | Prev: $912 (post +18%) | — | Don't chase; wait for $800 pullback |
| AVGO | **~$210** | ~flat | — | Watchlist only |

---

## IRAN DEAL STATUS

| Item | Status |
|------|--------|
| MOU signed today? | ❌ **NOT YET** |
| Rubio statement (May 27) | 🟢 **"Disagreements over a word, a sentence"** — deal essentially done |
| Trump | 🟡 Convening Cabinet meeting; Truth Social: talks "proceeding nicely" |
| IRGC | 🔴 **"Will turn area from Chabahar to Mahshahr into graveyard"** if US strikes resume |
| Iran FM Araghchi | 🟡 "Unsure if deal imminent" — Khamenei advisor calls Trump's nuclear demands a "fantasy" |
| Framework status | ✅ Islamabad Declaration: 60-day ceasefire + Hormuz reopening agreed in principle |
| Remaining obstacles | Lebanon/Hezbollah clause; Iranian asset release timeline; nuclear enrichment framing |
| Nuclear terms | ✅ No nukes committed; 60-day follow-on to negotiate enrichment suspension |
| Deal probability (today) | **65–70%** ↑ from 35–50% yesterday — Rubio "word/sentence" language = very close |
| Brent crude | **$99.18/bbl** (-0.41% from $99.58) |
| WTI crude | **~$92/bbl** |
| Oil vs $90 XLE trim trigger | ❌ NOT triggered — **$9.18 above threshold** |
| Oil vs $85 XLE exit trigger | ❌ NOT triggered — **$14.18 above threshold** |

**Iran analysis (May 27):** Today is the highest-probability day for an MOU signing since talks began. Rubio's "disagreements over a word, a sentence" language is the strongest "imminent" signal we've seen — compare to May 26's "a few more days." The IRGC threats are aggressive but appear to be a negotiating tactic (markets have learned to discount them — S&P hit a record yesterday despite identical rhetoric). The key variable is whether Khamenei endorses what Araghchi has negotiated. The Trump Cabinet meeting today could be to brief on the deal signing. **If deal signs today, execute: sell 60 XLE at market immediately; hold JETS for $35+ target.**

**Oil scenario analysis:**
| Scenario | Probability | Brent | XLE Action |
|----------|------------|-------|-----------|
| MOU signed today | 65–70% | -$8–15 immediate (→ $84–91) | Sell 60 XLE at market |
| Deal delayed, talks continue | 20–25% | Flat $97–102 | Hold all |
| Breakdown / IRGC strikes | 5–10% | +$8–15 spike (→ $107–114) | Hold all; JETS -10%, reassess if < $25 |

---

## IV ENVIRONMENT

| Symbol | IV Rank (est.) | Threshold | New CSPs? |
|--------|---------------|-----------|-----------|
| NVDA | ~30–32 | 40% required | ❌ No |
| TSLA | ~22 | 40% required | ❌ No |
| AMZN | ~25 | 40% required | ❌ No |
| Overall | Post-earnings compressed | | **Wait for next catalyst** |

**IV assessment:** War-era IV has deflated; NVDA's post-earnings IV crush is complete. NVDA at $218 vs $180P strike is 17.4% OTM — the puts are effectively worthless. No new CSPs until IV rank recovers above 40%, which may happen if: (a) Iran deal falls apart, (b) fresh earnings disappointment, or (c) new macro shock. The premium window is closed for now. If Iran MOU is signed today and IV spikes briefly on the market reaction, monitor for a 1-2 day IV bounce to sell into.

---

## KEY OVERNIGHT/PREMARKET NEWS

### Iran War (Primary Macro Theme)
- US struck Iranian missile sites and mine-laying boats May 25 overnight (self-defense framing)
- IRGC downed MQ-9 Reaper, fired on F-35 — escalation but market shrugged
- Today: Trump Cabinet meeting; Rubio "a word, a sentence" away from deal
- CNN live updates running: likely deal announcement today

### Market Premarket (May 27)
- S&P 500 futures: **+0.31%**
- Nasdaq 100 futures: **+0.69%**
- Russell 2000: **+0.74%**
- Asian markets: South Korea Kospi **+2%** (chipmaker surge); Taiwan strong
- Drivers: Iran deal hopes + AI momentum + Salesforce earnings tonight (after close)

### Individual Stocks
- **TSLA:** $443.79 premarket (+2.35%) — positive for XLY position; TSLA $330P ultra-safe
- **NVDA:** ~$218 premarket — stabilizing post-earnings; $180P still very safe
- **MU:** ~$912 (post +18% May 26) — no position; don't chase; monitor $800 pullback
- **Salesforce (CRM):** Reports today after close — could move Nasdaq significantly
- **Asia tech/chips:** SK Hynix, Samsung surging on HBM AI demand confirmation

### Oil
- Brent: **$99.18 (-0.41%)** — slight overnight pullback as Iran deal optimism holds
- Well above all XLE triggers ($90 trim, $85 exit)
- If Iran MOU signed intraday: expect immediate -$8–15 drop to $84–91 range

---

## TOP 3 PRIORITY ACTIONS

### 🔴 Priority 1 — VERIFY ALL OPTIONS POSITIONS FIRST (Critical — Before Anything Else)
**Open app.alpaca.markets; check Positions and Orders tabs:**
- **Why urgent:** EOD BP of $56,126 is nearly identical to open BP ($56,066), but midday showed $1,290 after TSLA $330P CSP filled. This BP recovery is unexplained — need to know exact open positions before trading.
- Confirm which of these are open: NVDA R2, NVDA R3, TSLA $330P Jun26, TSLA $370P Jun20, AMZN $245P Jun20
- Record all findings in log.md before placing any orders

### 🔴 Priority 2 — BTC NVDA R2 + R3 at Open (Day 24 — Absolute Priority)
**If confirmed open at broker:**
- NVDA ~$218; R2 mark ~$0.03–0.05; R3 mark ~$0.03–0.05 (both near zero)
- Submit limit BTC $0.10 on each; if no fill in 3 min → market order
- Expected P&L: R2 ~+$73–75, R3 ~+$61–63 = **~+$134–138 locked in**
- Frees ~$36K collateral for new opportunities when IV recovers

### 🟡 Priority 3 — Iran MOU Watch: XLE + JETS Standby Orders
**Load orders, do NOT submit until triggered:**
- **If Iran MOU signed today:** Submit 60-share XLE sell at market immediately → expected exit ~$58.50 area; P&L ~+$177 on those 60 shares; hold remaining 40 XLE
- **If Brent falls to $90:** Submit 30-share XLE sell at market
- **JETS:** Hold all 80 shares regardless; target $35.69 (+30% from cost $27.45); currently 80 × ($28.30 - $27.45) = **+$68** / +3.1%
- **Do NOT sell JETS on the signing news** — airlines benefit MOST from Hormuz reopening; let it run to $32–35

---

## RISK FLAGS

| Risk | Level | Detail | Action |
|------|-------|--------|--------|
| BP anomaly — EOD $56K vs midday $1.3K | 🔴 **VERIFY NOW** | Cannot trade safely without knowing exact positions | Check broker before any action |
| NVDA R2+R3 BTC overdue | 🔴 **Day 24** | Near zero value; $134-138 unrealized; daily theta decay tiny | BTC at market if limit misses |
| TSLA $370P + AMZN $245P status | 🔴 **Day 24** | Unconfirmed since Day 1 — GTC likely triggered | Check order history at broker |
| Iran IRGC retaliation risk (overnight) | 🟡 **ELEVATED** | Graveyard threat still standing; no strikes yet overnight | JETS stop-review if drops below $25 |
| NVDA estimate gap ($228 vs $218) | 🟡 **NOTE** | Yesterday's $228 estimate was wrong; actual ~$218. Recalibrate. | Use NVDA pivot levels $218/$212/$206 |
| Salesforce earnings after close | 🟡 **WATCH** | CRM miss = Nasdaq down tomorrow; beat = continuation | No position; monitor QQQ direction |
| TSLA $330P — $33K collateral for $129 | 🟡 **INEFFICIENT** | If verified open: hold until 50% target ($0.65 BTC) to free capital | BTC at $0.65 to free $33K for new CSPs when IV > 40% |
| IV below 40% threshold — no new CSPs | 🟡 **ACTIVE** | TSLA ~22, NVDA ~30–32; patience required | Wait for next vol event |
| JETS +3.1% vs cost — APPROACHING thesis | 🟢 **POSITIVE** | Iran deal signing = immediate gap to $32–35; +30% target = $35.69 | Hold; load XLE trim orders as proxy Iran hedge |
| Alpha gap -0.81% | ℹ️ **INFO** | SPY +2.59% vs us +1.78%; Iran MOU → JETS surge closes this gap | Path: MOU signed → JETS $32 → alpha positive |
| Account vs $87,500 floor | ✅ **OK** | ~$14,300 cushion | No halt |
| MU $912 — missed entry | ℹ️ **INFO** | Don't chase at +15.5% above original entry; monitor $800 pullback | No action |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | ✅ Confirmed |
| 2026-05-14 | $100,950.97 | $747.80 | +0.95% | +2.22% | -1.27% | ✅ Confirmed |
| 2026-05-19 | $99,744.04 | $733.42 | -0.26% | +0.26% | -0.51% | ✅ Confirmed |
| 2026-05-21 EOD | $100,893.34 | $742.91 | +0.89% | +1.56% | -0.66% | ✅ Confirmed |
| 2026-05-22 | $101,184.27 | $745.92 | +1.18% | +1.97% | -0.78% | ✅ Confirmed |
| 2026-05-26 | **$101,779.23** | **$750.46** | **+1.78%** | **+2.59%** | **-0.81%** | ✅ exec_eod confirmed; S&P record; MU $1T; US strikes Iran |
| **2026-05-27** | **~$101,800** | **~$750.75** | **~+1.80%** | **~+2.62%** | **~-0.82%** | Est. premarket; TSLA +2.35% pm; Iran "word/sentence" away |

**Alpha path to zero:** Iran MOU signed → JETS gaps to $32–35 (+14–24% from $28.30) → 80 shares × $5–7 gain = +$400–560 → alpha improves +0.4–0.6% → closes the entire gap.

---

## TODAY'S CATALYSTS TIMELINE

| Time (ET) | Event | Portfolio Impact |
|-----------|-------|-----------------|
| 9:00 AM | Pre-open: verify all options at broker | Structural — resolve BP anomaly |
| 9:30 AM | Market open | BTC NVDA R2+R3 immediately |
| 10:00 AM | Consumer Confidence data | Market direction signal; Benzinga noted volatility |
| Any time | Iran MOU announced | XLE sell 60 shares at market; JETS hold for $35 |
| After close | Salesforce (CRM) earnings | QQQ direction for tomorrow |
| All day | Brent crude watch | $90 trigger (currently $9.18 away) |

---

*Premarket report — Wednesday, May 27, 2026.*
*API blocked Day 24. Baseline: $101,779.23 (✅ exec_eod). SPY $750.75 premarket. TSLA $443.79 (+2.35%) pm. NVDA ~$218. Brent $99.18.*
*🔴 CRITICAL: Verify all options positions at broker — BP anomaly (midday $1,290 → EOD $56,126) unexplained.*
*🔴 BTC NVDA R2+R3 at open — Day 24, near zero, $134-138 locked in.*
*🟢 Iran deal: Rubio "disagreements over a word, a sentence" — HIGHEST probability signing day yet (65-70%). Have XLE 60-share sell order ready.*
*⚠️ TSLA $330P (if still open): now 25.5% OTM at $443 premarket — extremely safe; BTC at $0.65.*

Sources:
- [Benzinga: Trade Strategy SPY/QQQ/NVDA/TSLA May 27, 2026](https://www.benzinga.com/Opinion/26/05/52775533/trade-strategy-for-spy-qqq-aapl-msft-nvda-googl-meta-and-tsla-27)
- [CNN Live: Iran War / Trump Cabinet May 27, 2026](https://us.cnn.com/2026/05/27/world/live-news/iran-war-us-news)
- [Euronews: IRGC "graveyard" warning May 27, 2026](https://www.euronews.com/2026/05/27/irgc-warns-irans-coast-will-become-a-graveyard-if-us-strikes-resume)
- [Public.com: TSLA premarket $443.79 May 27](https://public.com/stocks/tsla/pre-market)
- [CNBC: Brent oil May 26 3% jump on Iran strikes](https://www.cnbc.com/2026/05/26/oil-prices-today-brent-wti-iran-trump-hormuz.html)
- [Trading Economics: Brent $99.18 May 27](https://tradingeconomics.com/commodity/brent-crude-oil)
- [Axios: What's inside the Iran deal](https://www.axios.com/2026/05/24/iran-deal-strait-hormuz-sanctions-nuclear)
- [NPR: Trump says deal with Iran "largely negotiated"](https://www.npr.org/2026/05/23/g-s1-124145/trump-iran-deal-strait-of-hormuz)
- [CNN: May 25-26 Iran war live updates](https://www.cnn.com/2026/05/25/world/live-news/iran-war-us-peace-deal)
- [Benzinga: SP500 may-27 open prediction](https://www.benzinga.com/markets/prediction-markets/26/05/52800148/sp500-may-27-open-up-or-down-polymarket-micron-ai-iran-talks)
