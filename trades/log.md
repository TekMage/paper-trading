# Trade Log

## Benchmark
- SPY at start: **$731.53** (May 7, 2026)
- Starting capital: **$100,000**

---

## Performance Tracker

| Date | Account Value | SPY Price | Our Return | SPY Return | Alpha |
|---|---|---|---|---|---|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% |
| 2026-05-08 | $100,000.00* | $737.27 | 0.00%* | +0.78% | -0.78% | API blocked Day 2; L1 trades intended not confirmed; theoretical +0.49% if executed; Iran MOU unsigned; oil $101 |
| 2026-05-11 | $100,000.00* | ~$734.93 | 0.00%* | +0.47% | -0.47% | Iran talks collapsed (Trump "TOTALLY UNACCEPTABLE"); oil $103.93; INTC $130 (+190% YTD); MU $787 (AI memory supercycle); L1 still unconfirmed |

*Note: May 8 account value held at $100,000 confirmed — Alpaca API returned 403 "Host not in allowlist" from trading bot environment (both sessions). Layer 1 trades documented as intended; manual execution required via Alpaca dashboard. Theoretical equity if L1 executed at open: ~$100,490 (+0.49%). SPY close $737.27; QQQ hit new 52-wk high $711.23 (+2.35%); JETS $27.59; NVDA $215.70; TSLA $428.95.*

---

## Open Positions

### Layer 1 — Core ETFs (INTENDED — awaiting manual execution)

| Symbol | Shares | Entry Price | Cost Basis | Target |
|--------|--------|-------------|------------|--------|
| QQQ | 45 | $705.09 | $31,729 | Hold |
| SPY | 13 | $734.71 | $9,551 | Hold |
| XLY | 40 | $120.00 | $4,800 | Hold (+30% JETS target) |
| JETS | 80 | $27.09 | $2,167 | +30% = $35.22 |
| XLE | 100 | $57.00 | $5,700 | Exit if Brent < $85 |
| **TOTAL L1** | | | **$53,947** | |

### Layer 2/2b — Cash-Secured Puts (INTENDED — awaiting manual execution)

| Symbol | Strike | Expiry | Contracts | Est. Premium | Cash Required | Priority |
|--------|--------|--------|-----------|--------------|--------------|----------|
| TSLA | $370 | Jun 20 '26 | 1 | ~$11.00 (~$1,100) | $37,000 | 1st |
| NVDA | $190 | Jun 20 '26 | 1 | ~$5.00 (~$500) | $19,000 | 2nd |
| AMZN | $245 | Jun 20 '26 | 1 | ~$5.00 (~$500) | $24,500 | 3rd |
| QQQ | $650 | Jun 20 '26 | 1 | ~$10.00 (~$1,000) | $65,000 | 4th |
| TSM | $380 | Jun 20 '26 | 1 | ~$13.00 (~$1,300) | $38,000 | 5th |
| INTC | $95 | Jun 20 '26 | 1 | ~$2.00 (~$200) | $9,500 | 6th (small) |
| DRAM | $42 | Jun 20 '26 | 1 | ~$1.50 (~$150) | $4,200 | 7th |

*Capital note: After Layer 1 ($53,947), remaining cash ~$46,053. Full cash-secured requires TSLA ($37K) first; NVDA ($19K) needs margin headroom or partial offset. Open TSLA CSP immediately, then NVDA. QQQ CSP alone exceeds remaining cash — defer until account grows or use portfolio margin.*

---

## Trade History

---

### 2026-05-08 — MARKET OPEN SESSION LOG

#### Market Context (sourced from web search — Alpaca data API unreachable)

| Symbol | Price | Notes |
|--------|-------|-------|
| SPY | $734.71 | +0.29%, new high; jobs report beat (+115K vs +65K est) |
| QQQ | $705.09 | range $694.42–$705.84 |
| XLY | $120.00 | range $118.79–$120.54 |
| JETS | $27.09 | range $26.92–$28.16 (May 7 close) |
| XLE | $57.00 | Brent crude ~$99 → above $85 hold threshold ✓ |
| NVDA | $211.08 | range $206.50–$214.20 (ATH $216.83 on Apr 27) |
| TSM | $415.70 | |
| TSLA | $409.05 | range $402.12–$415.83 |
| AMZN | $273.07 | |
| INTC | $110.80 | range $110.73–$111.38 — up 470%+ YoY, ATH territory |
| DRAM | $48.29 | range $48.25–$48.37 — Roundhill Memory ETF (new Apr 2026) |

#### Iran/Geopolitical Context (critical for IV thesis)
- May 8: Fresh US-Iran military exchanges in Middle East; market shrugging off ("Wall Street shrugs off tensions" — TheStreet)
- Peace deal NOT signed — ceasefire fragile; Strait of Hormuz tensions re-escalated
- Polymarket odds of nuclear deal by June 30: rising but uncertain
- **Implication**: IV still elevated. CSP thesis intact — sell TSLA and NVDA puts NOW before deal compresses IV 15–25%.

#### Layer 1 Trades — INTENDED (API blocked, execute manually)

```
### 2026-05-08 — BUY QQQ [Layer 1 Core ETF]
- Action: Buy
- Qty: 45 shares
- Price: $705.09 (market open est.)
- Total: $31,729
- Rationale: Core tech ETF, largest position per strategy v2.0
- Status: INTENDED — manual execution required

### 2026-05-08 — BUY SPY [Layer 1 Core ETF]
- Action: Buy
- Qty: 13 shares
- Price: $734.71 (market open est.)
- Total: $9,551
- Rationale: Broad market anchor, peace-deal recovery play
- Status: INTENDED — manual execution required

### 2026-05-08 — BUY XLY [Layer 1 Core ETF]
- Action: Buy
- Qty: 40 shares
- Price: $120.00 (market open est.)
- Total: $4,800
- Rationale: Consumer discretionary recovery — peace dividend, job market resilient
- Status: INTENDED — manual execution required

### 2026-05-08 — BUY JETS [Layer 1 Core ETF]
- Action: Buy
- Qty: 80 shares
- Price: $27.09 (market open est.)
- Total: $2,167
- Rationale: Airline peace dividend — highest leverage to Iran deal completion; +30% target
- Status: INTENDED — manual execution required

### 2026-05-08 — BUY XLE [Layer 1 Core ETF]
- Action: Buy
- Qty: 100 shares
- Price: $57.00 (market open est.)
- Total: $5,700
- Rationale: Energy hold — Brent crude $99 (above $85 exit threshold); exit if Brent < $85
- Status: INTENDED — manual execution required
```

**Layer 1 Total: $53,947 | Remaining cash: ~$46,053**

#### Layer 2/2b CSP Trades — INTENDED (API blocked, execute manually)

Target expiry: June 20, 2026 (~43 DTE from May 8)

```
### 2026-05-08 — SELL TO OPEN TSLA $370 PUT [Layer 2b CSP — Priority 1]
- Action: Sell to Open CSP
- Symbol: TSLA 20JUN2026 370 Put
- Qty: 1 contract (100 shares)
- Spot: $409.05 | Strike: $370 (~9.5% OTM)
- Est. Premium: ~$11.00/share (~$1,100 credit)
- Cash Collateral Required: $37,000
- Rationale: Highest IV name; Iran tensions keeping IV elevated; sell before peace deal compresses IV 15–25%
- Status: INTENDED — manual execution required (priority: open FIRST)
- Outcome: TBD at expiry/close

### 2026-05-08 — SELL TO OPEN NVDA $190 PUT [Layer 2b CSP — Priority 2]
- Action: Sell to Open CSP
- Symbol: NVDA 20JUN2026 190 Put
- Qty: 1 contract (100 shares)
- Spot: $211.08 | Strike: $190 (~10% OTM)
- Est. Premium: ~$5.00/share (~$500 credit)
- Cash Collateral Required: $19,000
- Rationale: AI leader; elevated IV; opens second per strategy
- Status: INTENDED — manual execution required (open after TSLA; needs margin headroom)
- Outcome: TBD at expiry/close

### 2026-05-08 — DEFERRED: AMZN $245 PUT, QQQ $650 PUT, TSM $380 PUT, INTC $95 PUT, DRAM $42 PUT
- Deferred pending capital/margin clearance after TSLA+NVDA CSPs open
- INTC note: stock at $110.80 — $95 put is ~14% OTM, premium minimal; reconsider strike
- QQQ note: $650 put requires $65K collateral — exceeds current available cash; needs portfolio margin
```

#### Layer 3 Assessment
- JETS: Already in portfolio (Layer 1, 80 shares) — no additional purchase needed
- Iran deal: NOT complete, fresh fighting today — hold off on additional Layer 3 risk until deal signed
- IWM/MU: Available if Layer 3 cash opens up; monitor Iran deal progress

#### Session Summary
- Layer 1 capital deployed: $53,947 (intended)
- CSP premium income (if executed): ~$1,600 TSLA + NVDA
- Remaining buying power: ~$46,053 (before CSP collateral)
- Account value: $100,000 (no executed trades — API blocked)
- **Action required**: Execute Layer 1 ETF buys + TSLA CSP manually via Alpaca dashboard or local curl
