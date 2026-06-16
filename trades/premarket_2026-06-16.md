# Pre-Market Summary — Monday, June 16, 2026

> **Market opens in ~30 min (9:30 AM ET). CRITICAL: XLE exit triggers active. Both CSPs closed at 50% profit June 15 — bot will open fresh CSPs today.**

---

## Header

- **API status:** UNAVAILABLE — Alpaca paper API unreachable from cloud runner
- **Last confirmed equity:** $102,543.63 (exec_eod_2026-06-15 — authoritative)
- **Market context:** Iran–US MOU signed Jun 14; Brent ~$83 (below $85 exit threshold); S&P futures +1.22%; FOMC meeting starts today under Chair Warsh

---

## Account Snapshot (from exec_eod_2026-06-15)

| Metric | Value |
|--------|-------|
| **Equity** | **$102,543.63** |
| Our return (inception) | +2.54% |
| SPY benchmark return | +3.14% (SPY @ $754.50) |
| Alpha vs SPY | -0.60% |
| Options BP remaining | $72,118.46 |
| Starting capital | $100,000 (May 7, 2026) |
| Account floor | $87,500 |
| Headroom above floor | $15,043 |

---

## Current Positions

### Layer 1 — Core ETFs

| Symbol | Shares | Status | Notes |
|--------|--------|--------|-------|
| QQQ | 50 | At target | +5 shares filled Jun 12 |
| SPY | 13 | At target | Inception cost $731.53 |
| JETS | 80 | At target | Cost ~$27.45; Iran/oil deal = airline tailwind |
| **XLE** | **100** | 🔴 **SELL ALL — TWO TRIGGERS ACTIVE** | See Iran/Oil section |
| XLY | 0 | Closed Jun 11 | v2.1 exit complete |
| SPCX | 15 | Filled Jun 12 IPO day | Bought ~$150 open; closed ~$178 Jun 15 (+19% unrealized) |

### Layer 2 — Open CSPs

**BOTH CSPs CLOSED AT 50% PROFIT ON JUNE 15:**

| Position | Sold @ | Closed @ | P&L | Date Closed |
|----------|--------|----------|-----|-------------|
| NVDA $180P Jul17 | $3.05 (avg) | ~$1.03 | +$202/contract | Jun 15 |
| AMZN $220P Jul17 | ~$3.25 (avg) | ~$1.32 | +$193/contract | Jun 15 |

**Options BP is now fully available ($72,118)** — the bot will open fresh CSPs at today's open per current targets:
- NVDA: ~$190P Jul18 (more conservative than prior $180P; ~7% OTM if NVDA ~$204)
- AMZN: ~$215P Jul18 (~9–10% OTM if AMZN ~$237)

*No other CSPs open. TSLA, INTC are NOT part of the current strategy.*

---

## 🔴🔴 Iran / Oil Status — CRITICAL ALERT

| Item | Status |
|------|--------|
| **Iran MOU signed?** | **YES — signed June 14–15, 2026 (Trump/Vance + Iranian Parliament Speaker)** |
| **Brent crude (Jun 16 premarket)** | **~$82.97/bbl (trading range $82.56–$83.87)** |
| vs $90 trim trigger | 🔴 **BREACHED — $7+ below** |
| vs $85 exit trigger | 🔴 **BREACHED — $2.03 below** |

**Iran deal summary:** US–Iran framework MOU signed at G7 / virtually June 14–15. Strait of Hormuz to reopen immediately; $24B in frozen Iranian assets unfrozen; 60-day window for nuclear negotiations. Brent fell from $87+ to $83 over the weekend on supply-reopening expectations.

### XLE Action Required — BOTH TRIGGERS ACTIVE

| Trigger | Rule | Status |
|---------|------|--------|
| Iran MOU signed | Sell 60 XLE at market immediately | 🔴 **TRIGGERED** |
| Brent ≤ $85 | Sell ALL remaining XLE | 🔴 **TRIGGERED** |

**Combined action: SELL ALL 100 XLE AT MARKET ON OPEN.**
The $85 exit trigger supersedes the MOU trigger (both fire the same direction). At ~$56/share, exiting 100 XLE releases ~$5,600 to cash. **This is a MANUAL action — the bot does not execute XLE exits.**

---

## Manual Triggers to Monitor Today

| Trigger | Level | Current | Status |
|---------|-------|---------|--------|
| Brent ≤ $85 → sell ALL XLE (100 shares) | $85.00 | ~$82.97 | 🔴 **TRIGGERED — ACT AT OPEN** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed Jun 14–15 | 🔴 **TRIGGERED — ACT AT OPEN** |
| Brent ≤ $90 → sell 30 XLE | $90.00 | ~$82.97 | 🔴 Superseded by $85 trigger |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 JETS | $35.69 | ~$28.56 est. | Not triggered (~$7.13 gap) |

---

## Morning Priority Actions

1. **SELL ALL 100 XLE AT MARKET — immediately at 9:30 AM open.** Both the Iran MOU trigger and the Brent ≤ $85 trigger are active. XLE likely opens lower on continued oil gap-down. Do not wait for the bot. Manual order required.

2. **Confirm both CSP positions are closed in Alpaca UI.** The exec_open Jun 15 submitted BTC orders for NVDA $180P and AMZN $220P; EOD BP jumped $32K → $72K confirming fills. Verify no residual option positions before market open.

3. **Watch bot's new CSP submissions at open.** With $72K in options BP, expect bot to submit NVDA ~$190P Jul18 and AMZN ~$215P Jul18. Confirm the strikes look reasonable given today's premarket price moves (NVDA ~$204, AMZN ~$237 est.).

---

## Market Context

| Item | Finding |
|------|---------|
| S&P 500 futures | +1.22% premarket — Iran deal + risk-on bid |
| NVDA | +2%+ Jun 15 on Iran/geopolitical relief; AMD +4%+ on 6GW Meta Instinct deal |
| AMZN | ~$237–238 est. premarket; $215P ~10% OTM — very safe |
| JETS | Iran peace deal + oil price drop = strong airline sector tailwind; hold for $35.69 trigger |
| XLE | Should gap DOWN at open — sell immediately on opening print |
| SPCX | Trading at ~$178 (closed June 15); IPO price $135; 15 shares est. +$645 unrealized |
| FOMC | First Kevin Warsh-led decision — meeting Jun 16–17, expected hold; CPI +4.2% |
| Juneteenth | NYSE **closed Thursday June 19** — plan CSP management around this |

### Week Macro Calendar

| Date | Event |
|------|-------|
| **Mon Jun 16** | Empire State Manufacturing 8:30 AM; **Sell all XLE at open** |
| Tue Jun 17 | Retail Sales 8:30 AM; Industrial Production; FOMC Day 2 |
| Wed Jun 18 | FOMC decision (likely hold; watch Warsh guidance) |
| **Thu Jun 19** | **NYSE CLOSED — Juneteenth** |
| Fri Jun 20 | Monthly options expiration (no near-term NVDA/AMZN exposure now) |

---

## Risk Flags

- 🔴 **XLE**: All trigger conditions satisfied — must exit at open manually or risk further oil-driven losses
- ✅ **CSPs cleared**: Both NVDA and AMZN CSPs closed at 50% profit June 15 — clean slate for new positions
- ⚠️ **New CSPs (today)**: Bot will open NVDA $190P and AMZN $215P; verify these strikes are still safe given any overnight NVDA/AMZN moves
- ⚠️ **FOMC vol**: Warsh's first decision Wednesday introduces midweek volatility; new CSPs with Jul18 expiry have sufficient buffer
- ⚠️ **Alpha lag**: -0.60% ITD vs SPY. XLE exit preserves capital from further oil-driven drawdown; Iran deal upside helps QQQ/JETS/SPCX
- ⚠️ **SPCX liquidity**: New IPO (June 12), 15 shares held — may see elevated vol around post-IPO lock-up chatter; no trigger to exit yet

---

*Sources: exec_eod_2026-06-15.md, exec_open_2026-06-15.md (confirmed CSP closes + BP recovery), CNN/NPR/ABC/Al Jazeera (Iran MOU June 14–15), HDFCSKY/Trading Economics (Brent $82.97), Bloomberg/Stocktwits (S&P futures +1.22%), TipRanks/Yahoo Finance (NVDA +2%, AMD +4%), CNBC/Yahoo Finance (SPCX $178)*
