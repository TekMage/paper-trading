# Trading Plan — Full Strategy

## Revision History
- **v1.0 — May 7, 2026:** Initial plan. Energy/defense tilt (Iran war).
- **v2.0 — May 7, 2026:** Post-backtest + Iran peace pivot. Rotate out of energy/defense into tech/growth/recovery.
- **v2.1 — June 11, 2026:** June sprint. XLY exit, QQQ bumped to 50, AMZN CSP re-entry, QQQ calls for leveraged beta, IPO watchlist (SPCX/ANTHROPIC/OPENAI). Target: max alpha vs SPY before June 30 reset.
- **v2.2 — June 17, 2026:** Long weekend brief. Iran war formally ending (formal signing June 19). XLE full exit Thursday open. SPCX hold at underwater entry. CSP open window critical Thursday. Monday deep reset.

---

---

## Long Weekend Brief — June 18–22, 2026 (v2.2)

### Calendar Correction
- **Thursday June 18** — Normal trading day. Full open/midday/EOD bot sessions run.
- **Friday June 19** — **Juneteenth Federal Holiday. NYSE CLOSED.** No bot sessions.
- **Saturday June 20 / Sunday June 21** — Weekend. No trading.
- **Monday June 22** — Markets reopen. First full session after the peace deal formal signing.

> Note: The EOD report on June 17 incorrectly stated "NYSE closed Thursday June 19." June 19 is
> a Friday this year and is the Juneteenth holiday. Thursday June 18 is a full trading day.

---

### Thursday June 18 — Action Plan

#### 🔴 CRITICAL — MANUAL: Sell all 100 XLE at market open (9:30 AM ET)
The bot does NOT execute XLE trigger exits automatically. This must be done manually via Alpaca.
- Brent ≤$85 trigger: ACTIVE since June 15 (Brent ~$79.45, $5.55 below threshold)
- Iran MOU trigger: ACTIVE since June 15
- This is Day 4 since both triggers fired. Every day of delay adds downside risk.
- Proceeds: ~$5,467 at $54.67/share — redeploy into CSPs and/or JETS

**How to execute:** Alpaca paper account → Sell 100 XLE → Market order → Confirm fill.

#### Bot Actions at Thursday Open (automatic)
The bot will run its normal open session. With FOMC IV spike in effect, expect:
- **CSP open attempts:** NVDA $190P Jul18 and AMZN $215P Jul18 should finally clear the
  $1.50 minimum premium threshold that has been blocking them all week. Jul18 is 28 DTE from
  Thursday — last day this expiry is within OPT_DTE_MIN=25. If they don't fill Thursday,
  the bot shifts to Aug15 expiry (~53 DTE) the following week.
- **No SPCX re-buy:** Fixed (removed from IPO watchlist June 17).
- **QQQ calls:** Bot will try to open 1 QQQ call 2% OTM if none held.

#### SPCX — Hold Decision
Current position: 15 shares @ $199.39 avg entry, ~$195 (-2.2%, -$65 unrealized).
Strategy: hold for recovery to break-even (~$199-201). This was an off-strategy re-entry
after the IPO profit-take; it's a small position ($2,925) and SPCX has strong fundamentals.
Do not add to this position — wait for break-even, then reassess.

---

### Friday June 19 — Market Closed (Juneteenth + Iran Formal Signing)

**No trading. Bot will not run.**

This is the day of the formal US–Iran war agreement signing ceremony in Switzerland. Even
though markets are closed, this is a major macro event to monitor:
- Full text of the formal peace agreement may differ from the June 15 MOU (14-point framework)
- Iranian crude tankers are physically in transit through Hormuz — formal signing confirms supply
- Watch for: any complications at the signing, last-minute conditions, congressional reaction
- Watch for: Brent crude futures reaction (markets don't close for futures)
- Watch for: geopolitical reaction from Saudi Arabia, Israel, Russia on the formal signing

**Key signals to track over the weekend:**
| Signal | Implication |
|---|---|
| Brent futures drop further from ~$79 | Confirms supply restoration; XLE exit was right call |
| Brent bounces toward $85 | Partial supply disruption; monitor JETS and XLE residual |
| Iran complications at signing | Risk-off; consider hedging Monday open |
| Congressional pushback / sanctions hold | Deal uncertainty; oil may retrace |
| Economic data releases (if any) | Note anything that moves rate expectations |
| JETS price action in pre-market Monday | Airlines are the direct peace dividend play |

---

### Monday June 22 — Pre-Market Research Reset

**Do a full research session before market open.** The formal peace deal changes the
strategic calculus significantly. Key questions to answer Monday morning:

#### 1. Oil and Energy
- Where did Brent close Friday (futures)? Where is it Sunday night?
- Is XLE stabilizing or continuing to fall? (Confirms exit thesis)
- Any resumption of Middle East energy contracts or refinery activity?

#### 2. Peace Dividend Assessment
- JETS: Airlines are the highest-conviction peace-dividend play. Fuel costs drop directly.
  Current: $30.25, exit trigger $35.69 (+18% to go). Is acceleration happening?
- Consumer discretionary: Lower fuel/inflation → consumer spending recovery. XLY was exited
  but this thesis was correct — monitor IWM (small caps, Fed-rate-sensitive) as potential add.
- Defense: ITA/RTX will underperform post-deal. Confirm no exposure.

#### 3. FOMC vs Peace Deal — Conflicting IV Signals
The June 17 FOMC hawkish hold (rate hike probability 77% by Dec 2026) spiked IV just as
the peace deal compresses it. These are opposing forces. Assess by Monday:
- Did IV compress over the weekend despite the hawkish FOMC?
- Are NVDA/AMZN CSP premiums still above $1.50 minimum?
- If IV has already collapsed, the original "wait 2-3 weeks post-deal" CSP rule applies.
  If IV is still elevated (FOMC win), open CSPs at Monday open aggressively.

#### 4. June Sprint Score
With ~8 trading days left in June (June 22-30, excluding June 22+), assess:
- Current alpha: +0.18% (EOD June 17). This is the best reading in weeks — PROTECT IT.
- SPY June 17 close: ~$742.43. Benchmark to beat by June 30.
- XLE exit proceeds ($5,467) redeployed into CSPs + potentially more JETS could accelerate.
- QQQ/NVDA/AMZN benefit from peace dividend + lower energy costs → tech cost compression.

#### 5. v2.3 Strategy Adjustments (if warranted)
After reviewing the above, decide whether a full strategy update is needed. Likely candidates:
- Add IWM or JETS to Layer 1 if peace dividend acceleration is confirmed
- Adjust CSP strikes/minimums based on post-deal IV environment
- Consider whether SPCX should be held beyond break-even (SpaceX unaffected by peace deal)
- Remove FOMC rate hike scenario weighting if deal overshadows monetary policy

---

## June Sprint Strategy (v2.1 — June 11–30, 2026)

**Goal:** Maximize alpha vs S&P 500 before June 30 reset. Currently -0.07% alpha. Need aggressive
stance — conservative wheel income will not close the gap in 19 trading days.

### June Sprint Changes (already implemented in bot)

| Change | Action | Reason |
|---|---|---|
| XLY removed from Layer 1 | Close full position | -5.44% loss, consumer thesis stale, capital better deployed elsewhere |
| QQQ bumped 45 → 50 shares | Buy 5 more QQQ at open | Absorb XLY capital into best-performing Layer 1 |
| AMZN CSP re-entered | $215P strike (~14% OTM, Jul) | Previous $250P was too close (5.7% OTM); new strike has adequate buffer |
| QQQ long calls | 1 contract, 2% OTM, 10-20 DTE | Leveraged upside exposure; 5-10× beta vs holding shares |
| IPO watchlist | SPCX (15 shares), ANTHROPIC (10), OPENAI (8) | Auto-buy on first tradeable day; SPCX debuts June 12 |

### IPO Analysis (for real-money account — beyond June test)

| Company | Ticker | Date | Valuation | Why |
|---|---|---|---|---|
| **SpaceX** | SPCX | Jun 12, 2026 | $1.75T | Starlink natural monopoly, launch dominance, PROFITABLE. Best structural moat. **DCA target #1.** |
| **Anthropic** | ANTHROPIC | ~Oct 23, 2026 | ~$965B | $47B ARR (4.7× YoY growth), Google+Amazon distribution, Constitutional AI moat. **DCA target #2.** |
| **OpenAI** | OPENAI | Q4 2026 | $730-852B | ChatGPT brand unmatched but $27B cash burn > $25B revenue. Buy IPO pop; wait for unit econ improvement before DCA. |

### ETF Exposure (pre-IPO proxy)
QQQ already provides indirect exposure via MSFT (49% OpenAI economics), GOOG ($3B Anthropic),
NVDA (GPU backbone for all three). ARKX will add SPCX post-IPO.

### June Return Target
| Scenario | Return | Alpha needed |
|---|---|---|
| Base | Flat to +0.5% | Recover current -0.07% deficit |
| Stretch | +1.5% | Beat SPY by 1%+ if market cooperates |
| Aggressive | +3%+ | Requires QQQ calls to pay off on an upleg |

---

## Market Context (v2.0 — updated June 17, 2026)

### Macro Regime Change: Iran War Ending — NOW EXECUTING
~~Ceasefire April 7. MOU finalizing.~~ **Status as of June 17, 2026:**
- MOU signed June 15 electronically (14-point framework, text released publicly June 17)
- Formal signing ceremony: **Switzerland, Friday June 19** (Juneteenth — US markets closed)
- First Iranian crude tankers physically departed Strait of Hormuz June 17
- Brent crude: ~$79.45 — already well through the $85 exit trigger
- **The thesis has executed. The portfolio pivot is underway.**

### What changes when the deal is signed (now confirmed):
- **Oil: immediate -$10-20 drop**, then settles $80–90 range (infrastructure damage, mine clearing
  keeps supply constrained — so NOT back to $60, but well below $111 current)
- **XLE / XOP / USO: go short-side.** Energy stocks that ran 23–90% are now headwinds.
- **Inflation eases → Fed has room to cut.** Lower rates = tailwind for growth/tech/real estate.
- **Risk-on rotation:** Cyclicals, consumer discretionary, airlines, small caps lead the next leg.
- **Tech/AI continues:** S&P 500 and Nasdaq at all-time highs. AI capex cycle is unaffected.
- **IV compression incoming:** Peace deal = less uncertainty = lower options premiums. Sell CSPs NOW
  while war-era IV is still elevated; premiums shrink once the deal is official.

### Key themes for v2.0
1. **Tech/AI** (QQQ, NVDA, TSM) — record highs, AI capex cycle intact
2. **Recovery / risk-on** (XLY, JETS, IWM) — consumer, airlines, small caps
3. **Reduced energy** (keep small XLE, drop USO/XOP) — oil normalizes, don't fight the trend
4. **Options income** — sell CSPs NOW before IV compresses post-deal

---

## Portfolio Allocation (v2.0)

### Layer 1 — Core ETF Positions (~$53,000 / 53%)

| ETF | Ticker | Price | Shares | Allocation | Thesis |
|---|---|---|---|---|---|
| Nasdaq 100 | QQQ | $694.93 | 45 | $31,272 | AI/tech at record highs; primary growth engine |
| S&P 500 | SPY | $731.53 | 13 | $9,510 | Broad market anchor; liquidity for covered calls |
| Consumer Disc. | XLY | $119.85 | 40 | $4,794 | Iran war ends = inflation eases = consumer spending recovers |
| Airlines | JETS | $27.61 | 80 | $2,209 | Hormuz reopens = airspace normalizes; airlines crushed by war, now recover |
| Energy (reduced) | XLE | $55.96 | 100 | $5,596 | Trimmed 268→100 shares. Oil settles $80–90; keep small position, don't fight decline |

**Total Layer 1:** ~$53,381

**Covered call plan on Layer 1:**
- QQQ: Sell monthly calls ~5% OTM (~$730 strike). Target ~$8–14/contract/month.
- SPY: Sell monthly calls ~5% OTM (~$768 strike). Target ~$8–14/contract/month.
- XLY: Sell monthly calls ~5% OTM (~$126 strike). Target ~$1.50–3/contract/month.
- XLE: Sell monthly calls ~3% OTM (~$58 strike — tighter since it's likely declining). Target ~$0.50–0.80/contract/month.

**Dropped from Layer 1:**
- ~~ITA (Defense ETF)~~ — Backtest confirmed −7.9% drag. Iran war ending removes the thesis entirely.

---

### Layer 2 — Options Income / The Wheel ($30,000 / 30%)

Cash-secured puts on quality names. Sell NOW while war-era IV is still elevated.
Goal: collect 1.5–2.5% per month in premium before IV compresses post-deal.

| Ticker | Price | Target Put Strike | Target Premium | Why |
|---|---|---|---|---|
| NVDA | $211.56 | $190 (10% OTM) | $5–8/contract | AI GPU leader; IV still high; want to own on any dip |
| QQQ | $694.93 | $650 (6% OTM) | $10–15/contract | Core index; high liquidity; strong theta |
| TSM | $414.22 | $380 (8% OTM) | $8–12/contract | AI foundry; cheaper than NVDA; strong earnings |
| AMZN | $271.08 | $245 (9.5% OTM) | $5–9/contract | AWS AI backbone; recovery play too |

**Dropped from Layer 2 Wheel:**
- ~~XLE~~ — Oil trend is now down. Don't want to be assigned a declining ETF.

**Monthly income target from Layer 2:** $600–$900 (2–3% of $30k)

**Wheel rules:**
1. Only sell puts on stocks/ETFs you'd genuinely want to own at the strike price.
2. Never sell more puts than your cash can cover (cash-secured only).
3. If assigned, immediately sell covered calls at or above your cost basis.
4. Roll a put down/out if it goes 50% against you (avoid assignment at a bad price).
5. **IV timing rule:** Sell CSPs BEFORE the Iran deal is signed (high war-era IV). After deal,
   wait for the next volatility event before opening new CSPs.

---

### Layer 2b — Single-Stock Options ($15,000 / 15%)

| Ticker | Price | Strategy | Strike | Rationale |
|---|---|---|---|---|
| TSLA | $411.83 | CSP / Wheel | $370 (10% OTM) | High IV still. EV plays benefit from lower oil (cheaper to compete vs ICE) |
| AMZN | $271.08 | CSP / Wheel | $245 (9.5% OTM) | AWS + consumer recovery (Prime spending returns as inflation eases) |
| NVDA | $211.56 | CSP / Wheel | $190 (10% OTM) | AI GPU; overlap with Layer 2 reinforces conviction |
| INTC | $109.61 | CSP — contrarian | $95 (13% OTM) | 18A process node + US foundry narrative. Small size. |
| DRAM | $46.49 | CSP / Wheel | $42 (9.7% OTM) | AI memory basket; SK Hynix, Micron, Samsung HBM demand is structural |

**IV note on Layer 2b:** TSLA and NVDA carry the most IV. Open these FIRST before peace deal
officially closes and IV drops 15–25%. INTC and DRAM are lower IV — less time-sensitive.

**Monthly income target from Layer 2b:** $400–$700

---

### Layer 3 — Opportunistic / Recovery Plays ($10,000 / 10%)

**Full rotation: drop oil plays, add peace dividend plays.**

| Candidate | Price | Thesis | Trigger |
|---|---|---|---|
| JETS | $27.61 | Airlines recovery — Hormuz reopens, Middle East routes resume, fuel costs drop with oil | Peace deal signed or Hormuz traffic resumes |
| IWM | $282.28 | Small caps — most leveraged to Fed rate cut expectations; risk-on after peace | Sustained market rally confirmation |
| XLY | $119.85 | Consumer discretionary — lower inflation = more spending. Also holds AMZN, TSLA, HD | Inflation print below 3% or consumer confidence data |
| MU | ~$646 | Micron — AI HBM memory; separate from oil macro entirely | Any AI capex news or earnings beat |

**Dropped from Layer 3:**
- ~~USO~~ — Oil is declining. The trade is over.
- ~~XOP~~ — Same. Oil E&P stocks will underperform in $80–90 oil world.

**Layer 3 rules:**
- Max 2 positions simultaneously
- Take profits at +20%, stop review at −10%
- JETS is the highest-conviction peace-deal play; size it first

---

### Layer 4 — Cash Reserve ($5,000 / 5%)

Unchanged. Deploy if:
- Account drops 10%+ (buy the dip)
- Peace deal announcement causes a sudden volatility spike/drop (use it)

---

## Risk Management Rules

### Position limits
- No single position > 20% of portfolio (QQQ at 31% is an exception — intentional overweight)
- No single sector > 40% of portfolio
- Wheel assignments can push a position up; cap covered call positions at 25%

### Stop losses
- Individual ETF positions: Stop review if down 15% from entry
- XLE specifically: If oil breaks below $80, exit remaining 100-share position
- Wheel puts: Roll if premium doubles (50% loss on position)
- Portfolio-level: Pause all new positions if account falls below $87,500

### Profit taking
- Layer 3 positions: Take profits at +20%
- XLE: Consider closing entire position if oil drops below $90 (peace deal confirmed)
- JETS: Take profits at +30% (airlines are a leveraged peace-deal trade)

### Weekly review checklist
- [ ] Account value vs SPY benchmark
- [ ] Oil price — key signal for XLE exit and JETS entry trigger
- [ ] Iran deal status — watch for signing, Hormuz traffic reports
- [ ] Review options positions approaching expiry
- [ ] IV environment — has peace deal compressed IV? Adjust CSP sizing accordingly
- [ ] Fed signals — rate cut expectations moving?

---

## IV Strategy: The Peace Deal Window

**Right now (pre-deal):** War-era IV is elevated. This is the best time to sell premium.
- Open TSLA, NVDA, AMZN CSPs immediately
- Use 30–45 DTE to ride the last of high IV through expiry

**Post-deal signed:** IV will compress 15–25% in days.
- Do NOT open new CSPs immediately after — wait 2–3 weeks for next catalyst
- Consider closing existing CSPs early at 50% profit rather than holding to expiry
- IV will re-normalize; adjust monthly income targets down to 1–1.5% until next event

---

## Return Targets (v2.0 — Recovery Scenario)

| Timeframe | Conservative | Base Case | Stretch |
|---|---|---|---|
| 1 month | +3% | +5% | +9% |
| 3 months | +8% | +14% | +22% |
| 6 months | +12% | +20% | +30% |

**Why higher targets than v1.0:** The Iran war ending is a one-time macro tailwind. The combination
of a risk-on recovery rally, AI momentum, consumer recovery, and options premium income (before IV
compression) creates a rare window for outsized returns.

**SPY benchmark:** Analysts now project 8,100 year-end (10–11% from current 7,315). In a peace
deal scenario, that could accelerate to 8,500+ (+16% from here).

---

## Options Reference

### IV Environment (v2.0 — Transitioning)
- **Now:** High IV (war risk premium). Favorable for sellers. Act quickly.
- **Post-deal (2–4 weeks):** IV compression. Pivot to covered calls on appreciating Layer 1.
- **Post-normalization:** IV returns to pre-war baseline. Target 1–2% monthly from options.

### Key expiration dates
- **Weekly (0–7 DTE):** Layer 3 event-driven plays only.
- **Monthly (21–45 DTE):** Primary Wheel/CSP timeframe. Open NOW before IV drops.
- **Quarterly (60–90 DTE):** Large assigned positions only.

### Greeks targets
- Delta on CSPs: 0.20–0.30 (20–30% probability of assignment)
- Theta: Maximize — favor 30–45 DTE at open
- Vega: Sell when IV rank > 40% (use this now; won't last long after peace deal)

---

## Benchmark Tracking

| Date | Account Value | SPY Price | Our Return | SPY Return | Alpha | Notes |
|---|---|---|---|---|---|---|
| 2026-05-07 | $100,000 | $731.53 | 0% | 0% | 0% | v2.0 plan start |

*(Update weekly in trades/log.md)*

---

## Backtest Summary (v1.0 Strategy, March–May 2026)

The v1.0 strategy was backtested over the 2-month period before launch.
See `research/backtest_results.md` for full details.

| Metric | Result |
|---|---|
| Portfolio return | +5.77% |
| SPY return | +7.85% |
| Alpha | −2.08% |
| Max drawdown | −0.87% |
| Sharpe (approx) | 7.18 |

**Key finding:** ITA dragged −7.9% (dropped). XLE was flat (reduced). QQQ and options income
were the winners. v2.0 addresses both structural issues.
