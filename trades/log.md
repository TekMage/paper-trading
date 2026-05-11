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
| 2026-05-11 | $100,000.00* | ~$736.39 | 0.00%* (+0.16% theoretical) | +0.66% | -0.66% (-0.50% theoretical) | Iran talks collapsed; S&P -0.12%; TSLA +4.02% $428.35; MU +5.8% $790.13; NVDA +1.75% $215.20; oil +3% $103.93; L1 unconfirmed Day 5 API blocked |

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

---

### 2026-05-11 — MARKET OPEN SESSION LOG

#### API Status
- Alpaca paper-api.alpaca.markets: **BLOCKED** (sandbox egress filter — "Host not in allowlist") — Day 5
- All prices sourced from web search. All trades remain INTENDED; manual execution via app.alpaca.markets required.

#### Market Context (sourced from web search)

| Symbol | Price | Change | Notes |
|--------|-------|--------|-------|
| SPY | ~$736.39 | -0.12% | S&P opened weak on Iran news; from $737.27 Friday close |
| QQQ | $710.93 | -0.34% | Range $708.91–$713.50; Nasdaq slight negative open |
| XLY | ~$117.00 | ~-2.5% | Estimated from pivot points $116.11–$118.30; consumer weakness |
| JETS | ~$27.45 | ~+1.3% | No May 11 data; last known May 8 close; Iran drone attacks = headwind |
| XLE | ~$56.70 | ~-0.5% | Estimated from pivot points $56.18–$57.23; oil up but energy stocks weak |
| TSLA | $428.35 | +4.02% | Range $422.25–$429.42; prev close $411.79; strong recovery vs $416 premarket est |
| NVDA | $215.20 | +1.75% | AI infrastructure demand intact |
| AMZN | $272.68 | +0.56% | Steady |
| TSM | $411.68 | -0.60% | Slight dip |
| INTC | $128.40 | +2.81% | Continued ATH momentum; up ~190% YTD; $95 CSP strike obsolete |
| MU | $790.13 | +5.80% | HBM memory supercycle; AI capex acceleration; Layer 3 candidate |
| Brent crude | $103.93 | +2.90% | Well above $85 XLE exit threshold ✓ |

#### Iran/Geopolitical Context
- Trump rejected Iran's counterproposal on May 10 as "TOTALLY UNACCEPTABLE" (NPR/CNN confirmed)
- Iran demands: immediate ceasefire + sanction relief + Hormuz sovereignty + reparations; deferred nuclear talks
- US demands: nuclear curbs integrated into deal — fundamental impasse
- Weekend drone attacks: UAE intercepted 2 Iranian drones; Qatar cargo ship struck; Kuwait airspace violated
- Brent crude +3% at open on escalation; Asian shares mixed
- **IV implication**: Talks collapsed = war-era IV EXTENDED. CSP window remains open. No rush from deal risk.
- **XLE**: Oil $103.93 >> $85 exit threshold → HOLD
- **JETS**: Thesis intact but delayed; Iran drone attacks on Gulf neighbors = airline route risk. HOLD.

#### Theoretical Layer 1 P&L (if May 8 fills confirmed)

| Symbol | Shares | Entry | Today | P&L$ | P&L% |
|--------|--------|-------|-------|------|------|
| QQQ | 45 | $705.09 | $710.93 | +$263 | +0.83% |
| SPY | 13 | $734.71 | $736.39 | +$22 | +0.23% |
| XLY | 40 | $120.00 | ~$117.00 | -$120 | -2.50% |
| JETS | 80 | $27.09 | ~$27.45 | +$29 | +1.33% |
| XLE | 100 | $57.00 | ~$56.70 | -$30 | -0.53% |
| **TOTAL** | | | | **+$164** | **+0.16%** |

Theoretical account value: ~$100,164 | SPY benchmark return: +0.66% | Theoretical alpha: **-0.50%**

#### Layer 1 Trades — STILL INTENDED (Day 5 — execute immediately via Alpaca dashboard)

```
### 2026-05-11 — BUY QQQ [Layer 1 Core ETF — OUTSTANDING]
- Action: Buy
- Qty: 45 shares
- Price: ~$710.93 (Monday open)
- Total: ~$31,992
- Status: INTENDED — API blocked; execute at app.alpaca.markets

### 2026-05-11 — BUY SPY [Layer 1 Core ETF — OUTSTANDING]
- Action: Buy
- Qty: 13 shares
- Price: ~$736.39
- Total: ~$9,573
- Status: INTENDED — API blocked; execute at app.alpaca.markets

### 2026-05-11 — BUY XLY [Layer 1 Core ETF — OUTSTANDING]
- Action: Buy
- Qty: 40 shares
- Price: ~$117.00
- Total: ~$4,680
- Status: INTENDED — API blocked; execute at app.alpaca.markets

### 2026-05-11 — BUY JETS [Layer 1 Core ETF — OUTSTANDING]
- Action: Buy
- Qty: 80 shares
- Price: ~$27.45
- Total: ~$2,196
- Status: INTENDED — API blocked; execute at app.alpaca.markets

### 2026-05-11 — BUY XLE [Layer 1 Core ETF — OUTSTANDING]
- Action: Buy
- Qty: 100 shares
- Price: ~$56.70
- Total: ~$5,670
- Status: INTENDED — API blocked; execute at app.alpaca.markets
```

**L1 Total at today's prices: ~$54,111 | Remaining cash after L1: ~$45,889**

#### Layer 2/2b CSP Trades — INTENDED (Priority: TSLA first, then NVDA)

Target expiry: June 20, 2026 (~40 DTE from today)

```
### 2026-05-11 — SELL TO OPEN TSLA $370 PUT [Layer 2b CSP — Priority 1]
- Action: Sell to Open CSP
- Symbol: TSLA 20JUN2026 370 Put
- Qty: 1 contract
- Spot: $428.35 | Strike: $370 (~13.6% OTM — more buffer than May 8)
- Est. Premium: ~$8–10/share (~$800–1,000 credit) [slightly lower vs $9–11 due to higher spot]
- Cash Collateral Required: $37,000
- Rationale: TSLA +4% today = more OTM buffer; IV still elevated (Iran talks dead); sell before any deal
- Status: INTENDED — execute FIRST via Alpaca dashboard
- Note: TSLA recovered from $416 premarket to $428 at open — great setup for CSP

### 2026-05-11 — SELL TO OPEN NVDA $190 PUT [Layer 2b CSP — Priority 2]
- Action: Sell to Open CSP
- Symbol: NVDA 20JUN2026 190 Put
- Qty: 1 contract
- Spot: $215.20 | Strike: $190 (~11.7% OTM)
- Est. Premium: ~$4–6/share (~$400–600 credit)
- Cash Collateral Required: $19,000
- Rationale: AI demand intact; IV elevated; standard delta ~0.20 position
- Status: INTENDED — open after TSLA CSP confirmed

### 2026-05-11 — DEFERRED: AMZN $245 PUT, QQQ $650 PUT, TSM $380 PUT, DRAM $42 PUT
- Deferred pending TSLA+NVDA fills and capital headroom

### 2026-05-11 — RECALIBRATE: INTC CSP STRIKE
- Original: $95 strike (INTC at $109.61 on May 7) — now 27% OTM at $128.40 → near-zero premium
- New suggested: $115 strike (~10% OTM); earns meaningful premium (~$2–3/contract)
- Or skip entirely — INTC has made its move; IV on a $130 stock may be rich
- Status: DEFERRED — reconsider strike before opening
```

#### Layer 3 Assessment
- **MU at $790.13 (+5.8% today)**: AI HBM memory supercycle fully confirmed; analyst targets $1,000+
  - Layer 3 candidate (max $10K, 2 positions). Entry now 22% above original plan price.
  - Consider 4–6 shares (~$3.2–$4.8K) or a CSP play. High conviction.
  - Action: Add MU as first Layer 3 position once Layer 1 is confirmed
- **IWM**: Not yet assessed today; Iran escalation may weigh on small caps
- **JETS**: Already in Layer 1 portfolio (80 shares); no separate Layer 3 add needed

#### Session Summary
- API status: BLOCKED (Day 5) — no trades executable from bot environment
- Layer 1: Outstanding for Day 5; execute via dashboard at open prices listed above
- Layer 2/2b: TSLA + NVDA CSPs still not opened; execute immediately after L1 confirmed
- TSLA today: Strong +4% open = more OTM buffer on $370 strike — favorable CSP entry
- MU surge: Reinforces AI theme; Layer 3 candidate once cash confirmed
- Iran: Talks dead = IV stays elevated = CSP window EXTENDED (positive for premium strategy)
- XLE: Oil $103.93 >> $85 threshold → HOLD; no exit signal
- **Immediate actions needed**:
  1. Verify L1 fills at app.alpaca.markets
  2. Open TSLA $370 Jun 20 CSP — 1 contract (~$800–1,000 credit)
  3. Open NVDA $190 Jun 20 CSP — 1 contract (~$400–600 credit)
  4. Consider MU Layer 3 entry (4–6 shares ~$3.2–4.8K)
