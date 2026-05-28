# Pre-Market Summary — Thursday, May 28, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment — Day 26.
> Equity confirmed via exec_eod: **$101,869.20** (SPY $751.32). Options BP: **$56,169.09**.
> Yesterday's TSLA $370P + AMZN $245P GTC fills likely explain BP recovery from midday $361 → EOD $56,169.
> Verify all positions at https://app.alpaca.markets/paper-trading before trading.

---

## ACCOUNT SNAPSHOT

| Metric | Value | vs Baseline |
|--------|-------|-------------|
| Equity (exec_eod May 27, confirmed) | **$101,869.20** | +$1,869.20 |
| Our total return | **+1.87%** | vs $100,000 May 7 start |
| SPY close (May 27) | **$751.32** | +2.71% from $731.53 |
| Alpha vs SPY | **-0.84%** | Widened from -0.77% midday |
| Options BP (exec_eod) | **$56,169.09** | Recovered from midday $361 |
| Account vs $87,500 floor | **✅ OK — $14,369 cushion** | No halt triggered |

**BP Recovery Explanation:** EOD BP jumped from midday $361 → $56,169. Most likely cause: the GTC BTC orders for TSLA $370P Jun20 and AMZN $245P Jun20 filled during the afternoon session, closing those positions and freeing ~$61K in collateral. If confirmed, this locks in ~+$550 (TSLA) and ~+$250 (AMZN) in options P&L. **Verify at broker first.**

---

## CURRENT POSITIONS (estimated closes, May 27)

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | Est. Close (May 27) | Unreal P&L | Unreal % | Premarket Signal |
|--------|-----|----------|---------------------|------------|----------|-----------------|
| QQQ | 45 | $710.93 | ~$726.51 | ~+$701 | +2.19% | ⚠️ Cautious — PCE 3.8% headwind; futures -0.3% |
| SPY | 13 | $736.39 | $751.32 (confirmed) | +$193 | +2.03% | ⚠️ Futures -0.3% — PCE inflation data drag |
| XLY | 40 | $117.00 | ~$122.21 | ~+$208 | +4.45% | 🟡 Watch — consumer hurt by sticky inflation |
| JETS | 80 | $27.45 | $28.95 (confirmed) | +$120 | +5.46% | 🟡 Watch — Iran military strikes cloud peace thesis |
| XLE | 100 | $56.70 | $57.26 (confirmed) | +$56 | +0.99% | 🟢 Brent $96.30 (+2.13%) — oil bouncing on Iran |

### Layer 2/2b — Cash-Secured Puts (estimated status)

| Symbol | Strike | Expiry | DTE | Underlying Est. | OTM% | Sold For | Est. Mark | Action |
|--------|--------|--------|-----|-----------------|------|----------|-----------|--------|
| NVDA R2 | $180P | Jun 18 '26 | **21** | ~$218+ | ~17% | $0.78 | ~$0.02–0.04 | 🔴 **BTC AT OPEN — Day 26 — market order if needed** |
| NVDA R3 | $180P | Jun 18 '26 | **21** | ~$218+ | ~17% | $0.66 | ~$0.02–0.04 | 🔴 **BTC WITH R2 — Day 26** |
| TSLA $330P | $330P | Jun 26 '26 | **28** | ~$443 | ~25% | $1.29 | ~$0.45–0.65 | ⚠️ Hold — very safe; bot position May 26 |
| TSLA $335P | $335P | Jun 26 '26 | **28** | ~$443 | ~24% | $1.19 | ~$0.50–0.65 | ⚠️ Hold — very safe; bot position May 27 |
| TSLA $370P | $370P | Jun 20 '26 | **23** | ~$443 | ~16% | ~$11 | ~$0 | 🟢 **Likely closed by GTC BTC (explains BP) — VERIFY** |
| AMZN $245P | $245P | Jun 20 '26 | **23** | ~$268 | ~9% | ~$5 | ~$0 | 🟢 **Likely closed by GTC BTC (explains BP) — VERIFY** |

**Cumulative Options P&L (estimated):**
| Position | Sold | Status | P&L |
|----------|------|--------|-----|
| NVDA R1 $180P Jun18 | $1.67 | ✅ Closed $0.76 | +$91 confirmed |
| INTC $90P Jun18 | $2.61 | ✅ Closed $1.18 | +$143 confirmed |
| TSLA $370P Jun20 | ~$11 | 🟢 Likely GTC filled | ~+$550 (unconfirmed) |
| AMZN $245P Jun20 | ~$5 | 🟢 Likely GTC filled | ~+$250 (unconfirmed) |
| NVDA R2 $180P | $0.78 | 🔴 Open — BTC today | ~+$74 at $0.04 mark |
| NVDA R3 $180P | $0.66 | 🔴 Open — BTC today | ~+$62 at $0.04 mark |
| TSLA $330P Jun26 | $1.29 | ⚠️ Open — hold | +$129 received |
| TSLA $335P Jun26 | $1.19 | ⚠️ Open — hold | +$119 received |
| **Total est.** | | | **~+$1,418 cumulative** |

---

## MARKET SNAPSHOT — Premarket May 28

| Indicator | Level | Change | Signal |
|-----------|-------|--------|--------|
| S&P 500 futures | ~-0.3% | ↓ | ⚠️ Modest weakness — PCE + Iran |
| Brent crude | **$96.30** | +2.13% | ⚠️ Bouncing on Iran retaliation fears — XLE positive, JETS risk |
| WTI crude | ~$90–92 est. | +2%+ est. | ⚠️ Recovering from $88.68 (no longer below $90) |
| PCE Inflation (released 8:30 AM today) | **3.8% annualized** | Above expectations | 🔴 Bad for rate cut hopes; QQQ/growth headwind |
| Dell (DELL) premarket | +4% | ↑ | ℹ️ $9.7B DoD contract — unrelated; market positive signal |
| Best Buy (BBY) premarket | +8.4% | ↑ | ℹ️ Earnings beat — consumer still spending |

**QQQ/NVDA context:** NVDA reported Q1 FY2027 earnings May 20 — record $81.6B revenue (+85% YoY), beat estimates. Stock dipped post-earnings on "sell the news" dynamics. AI capex cycle remains intact. Next NVDA earnings Aug 26, 2026. NVDA is still well above our $180 strikes.

---

## IRAN DEAL STATUS

| Item | Status |
|------|--------|
| Formal MOU signed? | ❌ **NO — Not signed** |
| US military strikes (May 25–26) | 🔴 **US struck Iranian missile sites + Hormuz boats — ceasefire violation allegations** |
| Iran retaliation threat | 🔴 **IRGC: "reciprocal response is legitimate and certain"** |
| Rubio (May 26) | 🟡 **"Disagreements over a word, a sentence"** — deal still in play but stalling |
| Trump | 🟡 **Deal "largely negotiated"** — still pushing for agreement |
| Hormuz commitment | 🟡 **Iran committed to restore traffic within 1 month** — but US strikes cloud timeline |
| Deal probability estimate | **45–55%** ↓ (reduced from 55–65%; military strikes complicate) |
| Brent crude today | **$96.30** (bounced +2.13% from ~$94 on Iran retaliation fears) |
| WTI crude today (est.) | **~$90–92** (recovering from $88.68 low) |

**Iran analysis:** The picture is significantly more complex than yesterday's bullish read. US conducted "self-defense strikes" on Iranian missile sites and Hormuz boats (May 25–26) during active ceasefire negotiations — Iran called it a ceasefire violation. Oil prices, which crashed -5.55% on May 27's Hormuz commitment news, have now bounced sharply (+2–3%) on Iran retaliation fears. As of premarket May 28: Brent $96.30. This has two portfolio implications:

1. **XLE**: The $90 Brent exit trigger is now ~$6.30 away (vs ~$4 yesterday). XLE position is SAFER near-term as oil bounces. Do NOT rush the exit — let Brent tell us where it goes.
2. **JETS**: Peace thesis is intact but delayed and riskier. $28.95 close yesterday; premarket may give back some gains on Iran strike news. Hold for now — the fundamental thesis (Hormuz reopening) is still alive.

---

## IV ENVIRONMENT

| Context | Assessment |
|---------|------------|
| War-era IV status | 🟡 **Partially elevated** — Military strikes reinjecting war premium |
| TSLA IV estimate | ~35–45% (still above normal; TSLA $330P/$335P at 24–25% OTM are safe) |
| NVDA IV post-earnings | ~40–50% (earnings IV spike on May 20 largely subsided) |
| CSP timing | 🟡 **Bot TSLA removed from targets (confirmed in code). No new NVDA CSPs until R2+R3 closed.** |
| New CSP candidates | ⚠️ After closing R2+R3: evaluate NVDA Jul18 $190P if IV > 40%; don't rush |

---

## TOP 3 PRIORITY ACTIONS — Thursday, May 28

### Priority 1 — BTC NVDA R2 + R3 at Open (Day 26 — Absolute)
**Via app.alpaca.markets at 9:30 AM ET:**
- Submit BTC limit $0.10 on BOTH R2 ($180P Jun18) and R3 ($180P Jun18) simultaneously
- If no fill within 3 minutes: **hit market order** — do not wait
- Expected P&L lock: R2 ~+$74, R3 ~+$62 = **~+$136 confirmed**
- Collateral freed: ~$36,000 → further improves BP
- NVDA is still ~$218 (17.4% OTM); these have zero assignment risk. There is no reason to hold longer.

### Priority 2 — Verify TSLA $370P + AMZN $245P Status
**At app.alpaca.markets (Order History tab):**
- If GTC BTC orders filled: record final P&L (+$550 TSLA, +$250 AMZN), update log.md
- If GTC BTC orders did NOT fill (Alpaca paper cancels options GTC at session end): Submit BTC market orders NOW — expiry Jun 20 approaching (23 DTE); marks near zero; free the collateral
- This explains the BP anomaly — **must confirm before any new positions**

### Priority 3 — Iran Watch + XLE / JETS Decision Framework
**Do NOT act preemptively — let price confirm:**

| Condition | Action |
|-----------|--------|
| Brent breaks below $90 during session | Sell ALL 100 XLE at market; lock the ~$56 gain |
| Brent holds above $92–93 all session | Hold XLE — oil bounce may continue |
| Formal MOU signed | Sell ALL 100 XLE at market; buy 20 more JETS if room |
| Iran escalates (retaliation strikes) | Sell 50 JETS; add to XLE if Brent spikes above $100 |
| JETS falls to $27.00 (near cost $27.45) | Stop review; consider trimming to 60 shares |

---

## RISK FLAGS

| Risk | Level | Detail |
|------|-------|--------|
| PCE inflation 3.8% | 🔴 **HIGH** | Fed rate cut in June unlikely; QQQ/tech growth stocks face headwind. Monitor QQQ for resistance. |
| Iran military strikes (ongoing) | 🔴 **HIGH** | Ceasefire violations by US forces; Iran retaliation "certain" per IRGC; peace deal at risk of collapse |
| Oil bouncing ($96.30 Brent) | 🟡 **ELEVATED** | Reverses yesterday's $90 trigger approach; XLE safe near-term but peace thesis oil downtrend disrupted |
| JETS thesis at risk | 🟡 **ELEVATED** | US strikes complicate Hormuz reopening timeline; JETS at $28.95 profitable but target of $35.69 further away |
| NVDA R2+R3 Day 26 overdue | 🔴 **ACT TODAY** | ~$136 locked gain + ~$36K collateral; no reason to hold |
| Dual TSLA CSPs (poor yield) | 🟡 **WATCH** | $330P+$335P Jun26 = $248 premium on $66.5K collateral (0.37%); very safe but inefficient; hold for now |
| Alpha gap -0.84% | ℹ️ **INFO** | Widened slightly; PCE + Iran strikes are short-term headwind for our recovery/growth tilt |
| Bot CSP logic | 🟢 **FIXED** | TSLA removed from CSP_TARGETS; INTC removed; min premium $1.50; NVDA target Jul18 $190 |
| Account vs $87,500 floor | ✅ **OK** | $101,869 — $14,369 cushion |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-14 | $100,950.97 | $747.80 | +0.95% | +2.22% | -1.27% | Confirmed |
| 2026-05-21 | $100,893.34 | $742.91 | +0.89% | +1.56% | -0.66% | Confirmed |
| 2026-05-22 | $101,184.27 | $745.92 | +1.18% | +1.97% | -0.78% | Confirmed |
| 2026-05-26 | $101,779.23 | $750.46 | +1.78% | +2.59% | -0.81% | Confirmed |
| 2026-05-27 | **$101,869.20** | **$751.32** | **+1.87%** | **+2.71%** | **-0.84%** | ✅ exec_eod confirmed; WTI -5.55% to $88.68; JETS $28.95; XLE $57.26; BP $56,169; bot TSLA $335P fixed |
| **2026-05-28** | **TBD** | **TBD** | **TBD** | **TBD** | **TBD** | PCE 3.8%; Brent $96.30; Iran strikes complicate deal; S&P futures -0.3% |

---

## WATCHLIST PRICES (May 27 close / premarket est.)

| Symbol | May 27 Close | Premarket Signal | Notes |
|--------|-------------|-----------------|-------|
| SPY | $751.32 | ↓ ~$748–749 | S&P futures -0.3% |
| QQQ | ~$726.51 | ↓ ~$723–725 | PCE headwind; tech cautious |
| XLY | ~$122.21 | ↓ slight | PCE sticky inflation = consumer watch |
| JETS | $28.95 | ↓ ~$28.50–29 | Iran strikes cloud Hormuz reopening |
| XLE | $57.26 | ↑ ~$58.50–59 | Brent $96.30 (+2.13%) — oil bounce |
| IWM | — | ↓ slight | Rate cut delay = small cap headwind |
| NVDA | ~$218 | → ~$217–219 | Post-earnings vol; $180 puts fully safe |
| TSM | ~$414 | → ~$412–415 | AI foundry thesis intact |
| TSLA | ~$443 | → ~$440–445 | EV stable; $330/$335 puts very safe |
| AMZN | ~$268 | ↓ slight | AWS strong; PCE = consumer caution |
| INTC | — | → | Not in current strategy |
| DRAM | — | → | Not in current strategy |
| MU | ~$646 | → ~$640–650 | AI HBM memory; Layer 3 candidate |
| AVGO | — | → | Monitoring |

---

## SESSION OUTLOOK

**Theme: Inflation Complication + Oil Volatility + Iran Uncertainty**

Today is a three-front challenge. The PCE print at 3.8% pushes the Fed further from cutting, which is a direct headwind for the QQQ-heavy portfolio. Brent's 2.13% bounce on Iran retaliation fears reverses yesterday's oil crash and complicates our XLE exit timing (good short-term for XLE, but bad for JETS and the peace thesis). And the formal Iran MOU remains unsigned with active US military operations ongoing.

**What this means operationally:**
- The "IV sell NOW before peace compresses premiums" urgency is LESS acute today — military action reinjected some war premium
- XLE hold decision validated — Brent at $96 makes the $90 exit trigger irrelevant today
- JETS thesis intact but patience required — formal deal still needed
- QQQ may face some pressure from rate cut repricing; this is a good day to let the portfolio breathe, not add risk
- NVDA R2+R3 BTC remains the single most important mechanical action — free the $36K collateral

**Green path for today:** Open closes R2+R3 cleanly (day 26), confirms TSLA $370P + AMZN $245P status, XLE holds on oil bounce, no Iran escalation. Alpha gap begins closing as SPY struggles with PCE data while our positions (XLE up on oil) hold steadier.

**Bear path:** Iran retaliates → oil spikes → Hormuz fears → JETS falls, Iran deal collapses. If Brent >$100, close JETS at breakeven, add XLE.

---

*Pre-market report — Thursday, May 28, 2026.*
*Confirmed EOD equity: $101,869.20 (exec_eod May 27, SPY $751.32). API blocked Day 26.*
*Key data: Brent $96.30 (+2.13%); PCE 3.8%; S&P futures -0.3%; Iran MOU not signed; US strikes May 25–26.*
*Top action: BTC NVDA R2+R3 at 9:30 AM open (Day 26 — market order if limit misses in 3 min).*

Sources:
- [S&P 500 futures fall after inflation data — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-may-28-2026)
- [US Premarket Movers May 28, 2026 — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-28/us-stock-futures-today-caesars-dollar-tree-photronics-red-cat)
- [Brent oil jumps on Iran retaliation threat — CNBC](https://www.cnbc.com/2026/05/26/oil-prices-today-brent-wti-iran-trump-hormuz.html)
- [US-Iran strikes and ceasefire violation — CNN](https://www.cnn.com/2026/05/25/world/live-news/iran-war-us-peace-deal)
- [Nvidia Q1 FY2027 earnings record $81.6B — Intellectia AI](https://intellectia.ai/blog/nvda-stock-earnings-analysis-may-2026)
- [Nvidia earnings live updates May 2026 — CNBC](https://www.cnbc.com/2026/05/20/nvidia-nvda-earnings-report-q1-2027.html)
- [Iran deal proposed terms — CNN](https://www.cnn.com/2026/05/24/middleeast/iran-us-proposed-deal-wwk-intl)
- [Iran deal "largely negotiated" — NPR](https://www.npr.org/2026/05/23/g-s1-124145/trump-iran-deal-strait-of-hormuz)
- [Brent crude historical data — Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)
- [PCE May 2026 preview — FXMacroData](https://fxmacrodata.com/articles/usd-pce-may-2026)
