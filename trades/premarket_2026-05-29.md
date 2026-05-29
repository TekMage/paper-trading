# Pre-Market Summary — Friday, May 29, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment — Day 27.
> Equity confirmed via exec_eod: **$102,138.36** (SPY $755.36). Options BP: **$56,297.67**.
> NVDA R2+R3 confirmed closed (BP evidence). AMZN $250P Jun26 status uncertain — verify at broker.
> Verify all positions at https://app.alpaca.markets/paper-trading before trading.

---

## ACCOUNT SNAPSHOT

| Metric | Value | vs Baseline |
|--------|-------|-------------|
| Equity (exec_eod May 28, confirmed) | **$102,138.36** | +$2,138.36 |
| Our total return | **+2.14%** | vs $100,000 May 7 start |
| SPY close (May 28) | **$755.36** | +3.26% from $731.53 |
| Alpha vs SPY | **-1.12%** | Widened from -0.84% |
| Options BP (exec_eod May 28) | **$56,297.67** | Healthy — NVDA R2/R3 freed |
| Account vs $87,500 floor | **✅ OK — $14,638 cushion** | No halt triggered |

**Alpha context:** SPY had a strong May 28 (+0.54%) while our portfolio held gains. Alpha widened to -1.12% because our energy position (XLE) didn't keep pace with the broad market. Dell's massive AI blowout AH (+38%) is today's major positive catalyst for the QQQ-heavy portfolio — this is the day to close the gap.

---

## CURRENT POSITIONS (estimated closes, May 28)

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | Est. Close (May 28) | Unreal P&L | Unreal % | Today's Signal |
|--------|-----|----------|---------------------|------------|----------|----------------|
| QQQ | 45 | $710.93 | **$735.42** (all-time high) | **+$1,102** | **+3.44%** | 🟢 **Dell AI +38% AH — NVDA/QQQ sympathy rally expected; tech leadership** |
| SPY | 13 | $736.39 | **$755.36** | **+$247** | **+2.57%** | 🟢 S&P 500 futures +0.1% on tentative Iran deal |
| XLY | 40 | $117.00 | **~$122.80** | **~+$232** | **+4.96%** | 🟢 Lower oil = consumer recovery thesis intact; Dell sympathy |
| JETS | 80 | $27.45 | **$29.14** | **+$135** | **+6.16%** | 🟢 **Tentative Iran deal — Hormuz opening timeline accelerating; hold for $35** |
| XLE | 100 | $56.70 | **~$58.80** | **~+$210** | **+3.70%** | 🔴 **WTI $87.66 premarket (below $90 again) — EXIT DECISION TODAY** |
| **Total L1** | | **~$53,947 cost** | **~$55,873** | **~+$1,926** | **+3.57%** | |

*QQQ $735.42 confirmed (MacroTrends/Robinhood all-time high May 28). SPY $755.36 confirmed (exec_eod). JETS $29.14 confirmed (Barchart range $28.25–$29.32). XLE ~$58.80 estimated from Brent $96.57 (+2.41%) on May 28 vs $57.26 prior. XLY ~$122.80 estimated from SPY +0.54% × consumer disc. Verify at app.alpaca.markets.*

### Layer 2/2b — Cash-Secured Puts

| Symbol | Strike | Expiry | DTE | Underlying Est. | OTM% | Sold For | Est. Mark | Action |
|--------|--------|--------|-----|-----------------|------|----------|-----------|--------|
| TSLA $330P | $330P | Jun 26 '26 | **28** | ~$441 | **25.2%** | $1.29 | ~$0.25–0.40 | ✅ Hold — extremely safe; good theta decay |
| TSLA $335P | $335P | Jun 26 '26 | **28** | ~$441 | **24.1%** | $1.19 | ~$0.30–0.45 | ✅ Hold — extremely safe |
| AMZN $250P | $250P | Jun 26 '26 | **28** | ~$268 | **6.7%** | $2.14 | ~$1.20–1.50 | ⚠️ **STATUS UNCERTAIN — submitted limit May 28; confirm at broker** |
| NVDA R2 | $180P | Jun 18 '26 | — | — | — | $0.78 | ~$0 | ✅ **CLOSED** (BP evidence confirms) |
| NVDA R3 | $180P | Jun 18 '26 | — | — | — | $0.66 | ~$0 | ✅ **CLOSED** (BP evidence confirms) |
| TSLA $370P | $370P | Jun 20 '26 | — | — | — | ~$11 | ~$0 | ✅ **GTC filled** (confirmed by BP May 28 open) |
| AMZN $245P | $245P | Jun 20 '26 | — | — | — | ~$5 | ~$0 | ✅ **GTC filled** (confirmed by BP May 28 open) |

**BP Logic May 28:** exec_open $56,323 (NVDA R2/R3 BTC'd overnight) → exec_midday $6,544 (AMZN $250P likely filled, consuming ~$25K + TSLA recalculation) → exec_eod $56,297 (TSLA/AMZN rallied, reducing collateral requirements). **AMZN $250P most likely filled at midday.**

**Cumulative Options P&L (estimated):**

| Position | Sold | Status | P&L |
|----------|------|--------|-----|
| NVDA R1 $180P Jun18 | $1.67 | ✅ Closed | **+$91 confirmed** |
| INTC $90P Jun18 | $2.61 | ✅ Closed | **+$143 confirmed** |
| TSLA $370P Jun20 | ~$11 | ✅ GTC closed | **~+$550** |
| AMZN $245P Jun20 | ~$5 | ✅ GTC closed | **~+$250** |
| NVDA R2 $180P | $0.78 | ✅ Closed | **~+$74** |
| NVDA R3 $180P | $0.66 | ✅ Closed | **~+$62** |
| TSLA $330P Jun26 | $1.29 | ⚠️ Open | **+$129 credit** |
| TSLA $335P Jun26 | $1.19 | ⚠️ Open | **+$119 credit** |
| AMZN $250P Jun26 | $2.14 | ❓ Uncertain | **+$214 credit if filled** |
| **Total est.** | | | **~+$1,418–1,632** |

---

## MARKET SNAPSHOT — Premarket May 29

| Indicator | Level | Change | Signal |
|-----------|-------|--------|--------|
| S&P 500 futures | **+0.1%** | ↑ slight | 🟢 Iran tentative deal + Dell AI boom |
| **Dell (DELL)** | **+38–39% AH** | ↑ massive | 🟢 **AI server revenue +757%; FY guidance $167B; NVDA/QQQ catalyst** |
| HPE | +16% AH | ↑ sympathy | 🟢 AI infrastructure wave |
| Brent crude | **~$95–96** | → flat/↓ est. | 🟡 May bounce; Iran deal will push down |
| WTI crude | **$87.66** | -1.4% | 🔴 Below $90 again — XLE exit trigger active |
| Gold | little changed | → | Neutral — Iran uncertainty but optimism |
| NVDA | ~$215–225 est. | ↑ on Dell AI | 🟢 Dell buys NVDA GPUs — CSP thesis validated; $180P extremely safe |
| QQQ | ~$737–745 est. | ↑ from $735.42 | 🟢 All-time high extended — AI wave |

**Dell AI Story Impact on Portfolio:**
Dell reported AI server revenue **+757%** to $16.1B, total Q1 revenue $43.8B (+88%), EPS $4.86 (vs $2.95 est.), FY guidance raised to $167B including $60B AI servers. Every GPU in those servers is NVDA's. Impact:
- **QQQ** (largest holding): Direct winner. NVDA ~8-9% of QQQ; AVGO, MSFT also benefit. QQQ at all-time high; today should extend that.
- **NVDA CSPs**: Our $180 strikes become even safer as NVDA moves up on AI confirmation. Window to open NVDA Jul18 $195-200P is opening.
- **TSLA/AMZN CSPs**: Indirect positive — AI narrative supports entire tech sector; puts move further OTM.
- **Alpha gap**: This is the day QQQ outperforms SPY. Our 45-share QQQ position is the portfolio's engine.

---

## IRAN DEAL STATUS

| Item | Status |
|------|--------|
| Formal MOU signed? | ❌ **NO — Still pending Trump + Khamenei approval** |
| Negotiator status | 🟢 **Deal text agreed by US/Iran negotiators as of May 28** |
| Trump status | 🟡 **CNN: Trump "weighing whether to back memo" — asked for a few days; "not satisfied but will be"** |
| JD Vance | 🟡 **"Couple of language points" remain** |
| Khamenei | 🔴 **Has not publicly confirmed deal** |
| Iranian parliament | 🟢 **"Large part of Iran's proposals accepted"** |
| Hormuz terms | 🟢 **Unrestricted traffic immediately upon signing; mines removed within 30 days** |
| Deal probability estimate | **65–75%** ↑ (Negotiators have text; both sides want it; Trump just needs final language) |
| Brent crude (May 28 close) | **$96.57** (+2.41% on May 28; May 29 premarket ~$95) |
| WTI crude (premarket May 29) | **$87.66** (-1.4%; below $90) |
| XLE trigger status (Brent ≤ $90) | ⚠️ **Brent ~$95 — not yet; but WTI is below $90** |

**Iran analysis:** The deal is essentially done at the negotiator level. Trump is delaying for maximum leverage on a few final terms (likely nuclear enrichment timeline or Hezbollah). JD Vance's "couple of language points" framing signals days, not weeks. WTI's premarket drop to $87.66 (below $90) reflects market pricing of imminent deal. When Trump signs (likely today or over the weekend):
- **Oil drops $5-10 immediately** → Brent toward $85-90
- **JETS surges toward $31-33** (another +7-13% from $29.14 close)
- **XLE exits our portfolio** at current prices (~$58.80; protect the ~$210 gain)
- **IV compresses** — close existing TSLA CSPs at 50% profit; pause new CSP openings

**CRITICAL — XLE EXIT DECISION:**
| Trigger | Level | Gap | Recommendation |
|---------|-------|-----|----------------|
| WTI ≤ $90 | $90 | ✅ **FIRED ($87.66)** | 🔴 **Exit TODAY at open — WTI trigger active** |
| Iran MOU signed | N/A | Imminent | 🔴 Exit ALL 100 XLE at market immediately |
| Brent ≤ $90 | $90 | ~$5 away ($95) | 🟡 Exit staged |

**Recommendation: EXIT all 100 shares of XLE at market open today.** WTI is at $87.66 (below $90); the Iran deal will push Brent below $90 when signed; XLE's unrealized gain of ~$210 will evaporate quickly when deal is confirmed. Lock in the gain now.

---

## IV ENVIRONMENT

| Context | Assessment |
|---------|------------|
| War-era IV status | 🟡 **Transitioning** — deal tentative but unsigned; some war premium remains |
| Dell AI boom effect | 🟢 **AI names IV elevated slightly** — sell premium into this spike if possible |
| TSLA IV estimate | ~35–45% (elevated; $330P/$335P at 24–25% OTM are very safe) |
| NVDA IV post-Dell | ~45–55% est. (Dell AI blowout reignites AI IV temporarily) |
| New CSP window | 🟢 **OPEN NOW** — Dell AI + pre-deal IV = best remaining window before peace compresses premiums |
| NVDA Jul18 $195–200P | 🟢 **Target if BP and NVDA open confirms** — Dell = structural demand; want to own NVDA below $195 |

**IV timing:** This is likely the LAST good window to sell elevated CSPs. Once Trump signs the Iran MOU, IV drops 15-25% and the war-era premium is gone permanently. If opening new CSPs today: NVDA Jul18 $195P or $200P on any opening strength confirmation.

---

## TOP 3 PRIORITY ACTIONS — Friday, May 29

### Priority 1 — EXIT XLE 100 Shares at Market Open
**Via app.alpaca.markets at 9:30 AM ET:**
- Sell ALL 100 shares of XLE at market
- Rationale: WTI at $87.66 (trigger fired); Iran deal imminent (final oil drop catalyst); unrealized gain ~+$210 is at risk
- Expected execution: ~$58-60/share → ~$5,800-6,000 proceeds; locks in ~$130-330 gain vs cost $56.70
- This cash (~$5,800) frees buying power for new options or Layer 3 positions
- **Do not wait for Brent to confirm** — WTI is the forward indicator and it's well below $90

### Priority 2 — Confirm AMZN $250P Status + NVDA CSP Decision
**At app.alpaca.markets (Positions/Orders tab):**
- If AMZN $250P **is open** (filled): Good position — hold; AMZN ~$268 with $250P is 6.7% OTM; reasonable yield
- If AMZN $250P **did not fill**: Re-evaluate whether to submit again (limit $2.14 may need adjustment to $1.80-2.00 if AMZN moved)
- After confirming AMZN status: Evaluate NVDA Jul18 $195P or $200P CSP if NVDA opens above $215
  - With Dell's AI blowout, NVDA is bullish — $200P at 10 DTE from $215+ is appropriate
  - Check BP availability first (need $19,500-20,000 collateral per contract)

### Priority 3 — Monitor for Iran MOU Signing (Weekend Risk)
**Today is a Friday before a weekend — Trump may sign or reject:**
- **If MOU signed today**: Exit XLE immediately (if not already done), hold JETS, check IV compression pace
- **If MOU rejected/collapses**: Buy 50 JETS at current prices (thesis disrupted); XLE may bounce — DO NOT add XLE
- **Weekend gap risk**: Position for peace — the deal is done at negotiator level; risk is to the upside (JETS), not downside
- JETS target: **$35.69** (+30% from $27.45 cost) — currently $29.14 (+6.2%). Deal signing is worth +$3-4 in a single session.

---

## RISK FLAGS

| Risk | Level | Detail |
|------|-------|--------|
| XLE exit urgency | 🔴 **ACT NOW** | WTI $87.66 (below $90); Iran deal imminent → oil will fall further; lock in $210 gain |
| Alpha gap -1.12% | 🟡 **ELEVATED** | Dell AI boom is today's catalyst to close the gap via QQQ surge |
| TSLA dual CSP inefficiency | 🟡 **WATCH** | $330P+$335P = $248 premium on $66.5K collateral (0.37% yield); safe but capital is locked poorly; consider BTC one at 50% profit |
| AMZN $250P status unknown | 🟡 **WATCH** | If filled: fine (6.7% OTM, $214 premium). If not filled: decide whether to re-submit |
| Iran deal not yet signed | 🟡 **WATCH** | Trump "weighing" — weekend risk of rejection. Portfolio is positioned correctly (bullish for deal); no hedge needed unless deal collapses |
| IV compression coming | 🟡 **WATCH** | Once MOU is signed, IV drops 15-25%. BTC open CSPs at 50% profit; don't open new CSPs post-signing |
| Bot CSP logic | 🟢 **MONITOR** | Bot submitted AMZN $250P May 28; verify it isn't targeting new positions today |
| Account vs $87,500 floor | ✅ **OK** | $102,138 — $14,638 cushion |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-14 | $100,950.97 | $747.80 | +0.95% | +2.22% | -1.27% | Confirmed |
| 2026-05-21 | $100,893.34 | $742.91 | +0.89% | +1.56% | -0.66% | Confirmed |
| 2026-05-22 | $101,184.27 | $745.92 | +1.18% | +1.97% | -0.78% | Confirmed |
| 2026-05-26 | $101,779.23 | $750.46 | +1.78% | +2.59% | -0.81% | Confirmed |
| 2026-05-27 | $101,869.20 | $751.32 | +1.87% | +2.71% | -0.84% | ✅ exec_eod confirmed |
| 2026-05-28 | **$102,138.36** | **$755.36** | **+2.14%** | **+3.26%** | **-1.12%** | ✅ exec_eod confirmed; NVDA R2/R3 closed; bot submitted AMZN $250P; Dell +38% AH; Iran tentative deal; WTI $89.53 |
| **2026-05-29** | **TBD** | **TBD** | **TBD** | **TBD** | **TBD** | Dell AI boom; WTI $87.66 premarket; Iran deal imminent; alpha gap close opportunity |

---

## WATCHLIST PRICES (May 28 close / May 29 premarket est.)

| Symbol | May 28 Close | May 29 Premarket Est. | Notes |
|--------|-------------|----------------------|-------|
| SPY | $755.36 | ↑ ~$756–758 | Futures +0.1%; Iran optimism |
| QQQ | $735.42 | ↑ **~$740–748** | **All-time high; Dell AI +38% AH — strong open expected** |
| XLY | ~$122.80 | ↑ ~$123–124 | Lower oil + consumer recovery; TSLA/AMZN in index |
| JETS | $29.14 | ↑ ~$29.50–30.50 | **Iran tentative deal — peace dividend pricing; hold for $35** |
| XLE | ~$58.80 | ↓ ~$57.50–58 | WTI $87.66 premarket — **EXIT AT OPEN** |
| IWM | — | ↑ slight | Iran = rate cut hope revival; small caps watch |
| NVDA | ~$212–218 | ↑ **~$218–228** | **Dell AI server demand confirmed; $180P strikes totally safe** |
| TSM | ~$414 | ↑ ~$416–420 | AI foundry thesis; NVDA order flow benefits TSM |
| TSLA | ~$441 | → ~$440–448 | $330P/$335P at 24–25% OTM — extremely safe |
| AMZN | ~$268 | ↑ ~$269–272 | AWS + AI; $250P strike safe (6.7% OTM) |
| MU | — | ↑ | AI HBM memory; Dell = HBM demand confirmation; Layer 3 watch |
| AVGO | — | ↑ | AI networking; Dell + NVDA tailwind |
| DELL | — | ↑ **+38%** | AH earnings blowout; not in portfolio but signals AI theme strength |

---

## SESSION OUTLOOK

**Theme: AI Infrastructure Boom + Iran Deal Finale — Portfolio's Best Aligned Day**

Today is the most favorable premarket setup of the v2.0 campaign. Two major tailwinds converge:

1. **Dell's AI blowout** validates the entire AI infrastructure thesis. AI server revenue +757%, guidance raised to $167B, $9.7B Pentagon AI contract. Every layer of the portfolio benefits: QQQ (NVDA is ~9% of QQQ), NVDA CSP strikes become even safer, XLY (AMZN/TSLA in index), and the narrative reinforces the "AI capex cycle is intact" thesis from the plan.

2. **Iran tentative deal** — Negotiators agreed text, leaders deciding. JD Vance says "couple of language points." WTI at $87.66 premarket reflects this. JETS at $29.14 is positioned for a move to $32-35 on signing.

**The alpha gap (-1.12%) can close today** if:
- QQQ surges 1.5-2%+ on Dell/AI momentum (our $31K position gains $500-1,000)
- JETS adds another $0.50-1 on Iran progress
- XLE exit locks in gains before oil drops further

**Today's primary mechanical action: EXIT XLE.** This is the clean, unambiguous, textbook execution. WTI is at $87.66, well below the $90 trigger. The Iran deal is essentially done. XLE's unrealized gain of ~$210 can become a loss within days if the deal is signed and oil drops $10. Exit at open, lock the gain, redeploy capital.

**Green path:** XLE exits at $58-59, JETS gaps up to $30+ on Iran news, QQQ extends all-time high on Dell AI, NVDA CSP opened at $195-200P Jul18. Alpha gap narrows toward -0.5%.

**Bear path:** Iran talks collapse (Trump rejects terms), oil spikes to $100+, JETS falls to $28, XLE recovers. But: NVDA/QQQ still rally on Dell AI regardless. Downside is contained; upside (deal signed) is asymmetric.

---

*Pre-market report — Friday, May 29, 2026.*
*Confirmed EOD equity: $102,138.36 (exec_eod May 28, SPY $755.36). API blocked Day 27.*
*Key data: WTI $87.66 premarket (-1.4%); Brent ~$95-96; Dell +38% AH; S&P futures +0.1%; Iran MOU tentative — Trump weighing.*
*Top action: EXIT XLE 100 shares at market open (WTI trigger fired at $87.66).*

Sources:
- [S&P 500 Futures Edge Up on Tentative U.S.-Iran Deal — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-may-29-2026)
- [US and Iran reach tentative deal, pending Trump's approval — Euronews](https://www.euronews.com/2026/05/28/us-and-iran-reach-tentative-deal-pending-trumps-approval)
- [Live updates: Trump weighing whether to back Iran memo — CNN](https://www.cnn.com/2026/05/29/world/live-news/iran-trump-war-news)
- [US-Iran ceasefire deal agreed upon, hangs on Trump, Khamenei — Jerusalem Post](https://www.jpost.com/middle-east/article-897679)
- [Dell AI server revenue +757%; stock +38% AH — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-28/dell-boosts-outlook-to-60-billion-in-ai-server-sales-this-year)
- [DELL Soars 39% After AI Server Revenue Rockets 757% — FX Leaders](https://www.fxleaders.com/news/2026/05/29/dell-soars-39-after-ai-server-revenue-rockets-757-and-pentagon-deal-boosts-outlook/)
- [Brent crude oil price — Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)
- [US Premarket Movers May 29, 2026 — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-29/us-stock-futures-today-dell-gap-netapp-nextpower-sentinelone)
- [Nvidia Q1 FY2027 Record $81.6B Revenue — Intellectia AI](https://intellectia.ai/blog/nvda-stock-earnings-analysis-may-2026)
- [QQQ all-time high May 28 — MacroTrends](https://www.macrotrends.net/stocks/charts/QQQ/invesco-qqq/stock-price-history)
