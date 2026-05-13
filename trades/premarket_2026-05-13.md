# Pre-Market Summary — Wednesday, May 13, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment.
> Account equity sourced from exec_eod_2026-05-12.md (GitHub Actions API call — confirmed).
> Prices from web search / premarket data. Verify positions at https://app.alpaca.markets/paper-trading

---

## ACCOUNT VALUE & CASH

| Metric | Value | Note |
|--------|-------|------|
| EOD equity (confirmed) | **$99,977.39** | GH Actions API — EOD May 12 |
| Starting capital | $100,000.00 | May 7, 2026 |
| Total return | **-0.02%** | (-$22.61) |
| SPY benchmark return | **+0.91%** | SPY $731.53 → $737.58 |
| Alpha vs SPY | **-0.93%** | Underperforming since inception |
| Options BP remaining | **$11,666.84** | After inferred CSP collateral (~$61.5K tied) |
| Account vs $87,500 floor | **OK — $12,477 cushion** | No stop triggered |
| Cash reserve (est.) | ~$5,900 | Layer 4 target $5,000 ✅ |

---

## CURRENT POSITIONS

### Layer 1 — Core ETFs

*Entry prices reflect L1 execution at May 11 open. EOD values from May 12. Premarket estimated from web search.*

| Symbol | Qty | Avg Cost | May 12 EOD | Premarket May 13 | Overnight P&L | Total Unrealized P&L |
|--------|-----|----------|------------|------------------|---------------|---------------------|
| QQQ | 45 | $710.93 | $706.23 | ~$707.25 | +$46 (+0.14%) | -$165 (-0.52%) |
| SPY | 13 | $736.39 | $737.58 | ~$737 | -$8 (-0.08%) | +$8 (+0.06%) |
| XLY | 40 | $117.00 | $119.87 | ~$120 | flat | +$120 (+2.46%) |
| JETS | 80 | $27.45 | $26.61 | $27.07 | +$37 (+1.73%) | -$30 (-1.38%) |
| XLE | 100 | $56.70 | $57.79 | ~$58.20 | +$41 (+0.71%) | +$150 (+2.65%) |
| **L1 Total** | | **$54,111** | | | **+$116** | **+$83** |

### Layer 2 / 2b — Options (CSPs, inferred from Options BP drop May 12)

*Still unconfirmed — log into app.alpaca.markets to verify fills.*

| Symbol | Strategy | Strike | Expiry | Collateral | TSLA/Stock Now | OTM% | Status |
|--------|----------|--------|--------|-----------|---------------|------|--------|
| TSLA | CSP (short put) | $370 | Jun 20 '26 | $37,000 | ~$433–441 | **14–15.5%** | 🔶 INFERRED — verify |
| AMZN | CSP (short put) | $245 | Jun 20 '26 | $24,500 | ~$265–270 | **7.5–9%** | 🔶 INFERRED — verify |
| NVDA | CSP (short put) | $190 | Jun 20 '26 | $19,000 | ~$218 | **12.8%** | ⚠️ UNKNOWN — BP only $11.6K left, may not be open |

**CSP collateral accounting:** $37K (TSLA) + $24.5K (AMZN) = $61.5K → matches Options BP drop of $61,505.73 exactly. NVDA $190P likely NOT open (would need $19K; only $11.6K BP remaining).

---

## WATCHLIST SNAPSHOTS (Premarket May 13, 2026)

| Symbol | Premarket Price | Prev Close | Change | Note |
|--------|----------------|------------|--------|------|
| SPY | ~$737 | $737.58 | ~-0.1% | S&P futures -0.1% |
| QQQ | ~$707.25 | $706.23 | +0.1% | Nasdaq futures +0.3% |
| XLY | ~$120 | $119.87 | ~flat | Consumer disc. |
| JETS | $27.07 | $26.61 | +1.7% | Peace hopes; Brent still elevated |
| XLE | ~$58.20 | $57.79 | +0.7% | Brent $107 → energy premium intact |
| IWM | ~$283 | ~$282 | ~flat | Small caps follow mixed futures |
| NVDA | ~$218 | ~$216 | +1.0% | Chip stocks leading today |
| TSM | ~$415 | ~$414 | ~flat | Earnings beat context intact |
| TSLA | ~$433–441 | ~$424 | +2–4% | Premarket up; robotaxi concerns offset |
| AMZN | ~$267 | ~$265 | ~flat | AWS + consumer recovery |
| INTC | $123.48 | ~$120 | +2.9% | **52-week high territory** — up 12.5% from May 7 |
| DRAM | $54.65 | ~$52 | +5.1% | **Memory ETF surging** — up 17.5% from May 7 |
| MU | +5%+ PM | ~$645 | +5%+ | **Samsung union strike risk** → Micron benefits; 52-wk high |
| AVGO | ~flat | ~flat | — | Not a priority today |

---

## IRAN DEAL STATUS

| Item | Status |
|------|--------|
| MOU signed? | ❌ **NO — deal talks actively stalling** |
| Latest development | Trump called Iran's counter-proposal "**totally unacceptable**" |
| Iran's counter-demand | Sovereignty recognition over Hormuz + war damages compensation |
| Peace talks status | **On life support** — both sides hardening positions |
| US response | New Treasury sanctions (May 9): 10 individuals/entities for weapons supply to Iran |
| Naval situation | Sporadic US-Iran naval clashes resuming in Hormuz (May 8–9) |
| Strait of Hormuz | **Still blocked** since Feb 28; 20% of global oil supply disrupted |
| Brent crude | **$107.05/bbl** (May 13 morning) — up from $104.97 on May 12 |
| WTI crude | ~$101/bbl |
| Iran deal probability (next 7 days) | **LOW** — counter-proposals rejected, new sanctions, naval escalation |
| XLE exit trigger (Brent < $85) | ❌ NOT triggered — **HOLD XLE** |
| JETS thesis | **Delayed but intact** — Hormuz closed = airlines hurt; Hormuz open = surge |

**Strategic implication**: The pivot narrative from v2.0 (peace deal = oil drops) is NOT imminent. War premium in oil and IV continues. This means:
- IV stays elevated → CSPs currently open remain profitable as planned
- XLE is NOT a short-side trade yet ($107 Brent → XLE likely grinds higher)
- JETS recovery is delayed — hold but do not add until Hormuz signals opening
- The "sell CSPs before IV compresses" window remains OPEN

---

## IV ENVIRONMENT CHECK

| Indicator | Status | Implication |
|-----------|--------|-------------|
| Iran war continuing | ✅ Yes — escalating | War risk premium = elevated IV |
| PPI today +1.4% (vs +0.5% est) | ⚠️ HOT | Fed cuts pushed out → higher rate uncertainty = IV-positive |
| Peace deal imminent? | ❌ No | IV compression NOT coming soon |
| NVDA pre-earnings IV | 🔴 **HIGH** | 7 days to earnings = IV at peak |
| TSLA/NVDA IV > 50%? | Likely yes | Good for existing CSPs; TSLA $370P healthy at ~$433–441 |
| Verdict | **IV STAYS ELEVATED** | Continue selling; no rush to close CSPs at discount |

---

## TOP 3 PRIORITY ACTIONS

### Priority 1 — VERIFY CSP FILLS (IMMEDIATE)
**Log into app.alpaca.markets right now.**
- Confirm TSLA $370 Jun 20 CSP: exact expiry, strike, premium received
- Confirm AMZN $245 Jun 20 CSP: same
- Determine if any NVDA CSP was opened (Options BP $11.6K suggests NO)
- Set 50% profit take-back limit orders on confirmed CSPs

### Priority 2 — NVDA EARNINGS DECISION (By May 18–19 EOD)
**Nvidia reports May 20 — 7 days away.**
- If NVDA $190P Jun 20 CSP is open: **close it May 18–19** to avoid earnings gap risk
- If NOT open (most likely given BP): Decide whether to open NVDA CSP NOW (pre-earnings IV peak) or wait until post-May-20 (IV drops but gap risk gone)
- Analyst consensus: Beat expected ($78.8B rev, $1.77 EPS). Bullish, but gap up/down both possible
- **Recommendation**: If NVDA CSP is open → close it. If not → do NOT open before May 20. Wait for post-earnings IV re-entry.

### Priority 3 — MU LAYER 3 ENTRY EVALUATION
**MU up 5%+ premarket on Samsung union strike risk.**
- Micron benefits from Samsung supply disruption (HBM AI memory is structural demand)
- Layer 3 rules: max 2 positions, +20% take profit, -10% stop review
- Current Layer 3 exposure: JETS x80 is technically a Layer 1 position
- **Action**: Evaluate MU as a Layer 3 position if cash allows. With only $11.6K options BP remaining, use available cash not backing CSPs. Verify cash position at broker first.
- Note: DRAM ETF also +5% today — alternative to single-stock MU risk

---

## RISK FLAGS

| Flag | Level | Detail |
|------|-------|--------|
| Account below $100K baseline | 🟡 MINOR | -$22.61 from start; not at risk floor |
| Negative alpha vs SPY | 🟡 WATCH | -0.93% behind SPY; QQQ CPI drag is primary cause |
| NVDA earnings May 20 | 🔴 CRITICAL | 7 days; must make decision on any NVDA options by May 18–19 |
| Options BP only $11.6K | 🟡 CONSTRAINED | No new CSPs above $11.6K collateral requirement possible |
| Iran talks stalled/escalating | 🟡 WATCH | No deal = XLE headwind removed; but JETS thesis delayed |
| PPI +1.4% (hot inflation) | 🟡 QQQ HEADWIND | Fed cuts pushed out; QQQ most sensitive to rate expectations |
| TSLA robotaxi/battery issues | 🟡 MINOR | TSLA at $433 → $370 CSP still 14.5% OTM; safe margin |
| Hormuz naval clashes resuming | 🟡 WATCH | Risk of escalation vs. off-ramp; oil could spike further |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-08 | $100,000.00* | $737.27 | 0.00%* | +0.78% | -0.78% | API blocked, trades unconfirmed |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | GH Actions confirmed |
| 2026-05-12 | $99,977.39 | $737.58 | -0.02% | +0.83% | -0.85% | GH Actions confirmed (exec_eod) |
| **2026-05-13 PM** | **~$100,093** | **~$737** | **~+0.09%** | **~+0.75%** | **~-0.66%** | Estimated premarket |

*SPY benchmark start: $731.53. Our benchmark start: $100,000.*

---

## SESSION CONTEXT

**Macro theme: Hot inflation meets stalled peace talks**

The dual shock of PPI +1.4% (vs +0.5% expected) and Iran talks collapsing creates a split market:
- Tech/chips outperforming (Nasdaq +0.3% futures, NVDA/MU/INTC leading)
- Broad market flat-to-down (S&P futures -0.1%, Dow -0.5%)
- Energy elevated: Brent $107 = XLE holds, JETS hurt
- Rate-cut timeline pushing further out: bad for QQQ/growth long-term, but today chips winning

The v2.0 peace pivot thesis is NOT dead — it's delayed. When the deal eventually comes (weeks not days based on current signals), the rotations into JETS, XLY, and away from XLE will be sharp. **Hold positions. No panic exits. This is the waiting game.**

---

*Pre-market report — May 13, 2026. API blocked; prices from web search.*
*Key sources: exec_eod_2026-05-12.md (equity confirmed $99,977.39 via GH Actions), Alpaca Options BP $11,666.84.*
*Iran: no deal — new US sanctions, naval clashes, Trump rejected counter-proposal. Brent $107.05.*
*PPI +1.4% (hot). NVDA earnings May 20. MU +5% PM on Samsung strike risk.*
*Verify all positions at app.alpaca.markets before market open.*
