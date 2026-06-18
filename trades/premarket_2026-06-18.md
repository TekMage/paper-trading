# Premarket Summary — 2026-06-18

> Generated ~9:00 AM ET | Market opens in ~30 minutes

---

## Header

- **API status:** UNAVAILABLE (live curl test failed; exec_eod is authoritative)
- **Last confirmed equity (EOD 2026-06-17):** $101,674.82 (+1.67% vs SPY +1.49%)
- **Market context:** S&P 500 futures +0.87%, Nasdaq +1.32% premarket — rebound after Fed held rates with hawkish dot plot; oil retreating sharply on Iran deal news

---

## Account Snapshot (EOD 2026-06-17 — confirmed)

| Metric | Value |
|---|---|
| Equity | $101,674.82 |
| Our return | +1.67% |
| SPY return | +1.49% (SPY @ $742.43) |
| Alpha | +0.18% |
| Options BP remaining | $73,253.07 |
| Account floor | $87,500 |
| Headroom above floor | +$14,174.82 |

EOD bot action: No actions needed.

---

## Current Positions (from exec_eod + CLAUDE.md targets)

**Layer 1 — Core ETFs:**
- QQQ: 50 shares (at target)
- SPY: 13 shares (at target)
- JETS: 80 shares (at target) — $30.30 today, +10.4% vs $27.45 cost; trigger at $35.69 not reached
- XLE: 100 shares (at target) — **⚠️ SEE CRITICAL FLAGS BELOW**
- XLY: closing via FORCE_CLOSE_EQUITY (June sprint exit — confirm closed at open)

**Layer 2 — Open CSPs (targets per CLAUDE.md):**
- NVDA $190P Jul18: NVDA ~$200.42 → ~5% OTM, safe; no threat to assignment
- AMZN $215P: monitor for confirmation of open position

**Layer 2b — QQQ Calls:**
- QQQ 1 contract, 2% OTM, 10–20 DTE — bot manages at open session

---

## 🚨 CRITICAL: Iran / Oil Status — BOTH TRIGGERS HIT

### Iran MOU: SIGNED ✅
- Trump signed the US-Iran MOU electronically at the Palace of Versailles on June 17, 2026
- Terms: 60-day ceasefire, Strait of Hormuz reopens to commercial traffic, US lifts naval blockade
- **STRATEGY TRIGGER ACTIVE: Iran MOU signed → sell 60 XLE at market immediately (MANUAL)**

### Brent Crude: ~$78.96/barrel
- Down four straight sessions to three-month lows, pressured by anticipated supply increase from Iran deal
- **$90 trigger: HIT** (Brent ≤ $90 → sell 30 XLE) — distance: -$11.04 below trigger
- **$85 trigger: HIT** (Brent ≤ $85 → exit all remaining XLE) — distance: -$6.04 below trigger

### Combined XLE Action Required
Both the Iran MOU trigger and the Brent ≤ $85 trigger are independently active:
- MOU trigger: sell 60 XLE
- Brent ≤ $85 trigger: sell ALL remaining XLE
- **Recommendation: CLOSE ALL 100 XLE SHARES at market open (manual action required)**
- At current XLE ~$54.67 → 100 shares ≈ $5,467 proceeds released to cash/BP

---

## Manual Triggers Status

| Trigger | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90.00 | ~$78.96 | 🔴 HIT — MANUAL ACTION NEEDED |
| Brent ≤ $85 → exit all XLE | $85.00 | ~$78.96 | 🔴 HIT — MANUAL ACTION NEEDED |
| Iran MOU signed → sell 60 XLE | N/A | SIGNED Jun 17 | 🔴 HIT — MANUAL ACTION NEEDED |
| JETS ≥ $35.69 (+30%) → close all 80 | $35.69 | ~$30.30 | 🟢 Clear — $5.39 below trigger |

---

## Morning Priority Actions

1. **URGENT — Close all 100 XLE at market open.** Both the Iran MOU and sub-$85 Brent triggers are active simultaneously. At ~$54.67/share this is a ~$5,467 position. Place a market sell order for 100 XLE at or just after 9:30 AM ET.

2. **Confirm XLY is fully closed.** CLAUDE.md shows XLY was targeted for FORCE_CLOSE removal during the June sprint. Verify zero XLY shares remain; if any linger, close them today.

3. **Monitor AMZN CSP after open.** AMZN $215P — confirm position is open and check intraday AMZN price vs strike. With market up +0.87% premarket, risk of early assignment is low but verify the position is live (bot CSP GTC orders are cancelled at session end).

---

## Risk Flags

- **XLE / Iran thesis resolved:** The Iran thesis that justified holding XLE has materialized. Both manual oil price and geopolitical triggers are now active. Holding XLE further exposes the account to continued oil price decline as Strait of Hormuz reopens and supply ramps.
- **Oil supply glut risk:** Brent at $79 and falling — once Hormuz fully reopens, further downside to $70s is plausible. Every day XLE is held increases downside risk.
- **Fed hawkish shift:** Median dot plot now at 3.8% for year-end (vs 3.4% in March), implying possible rate hike. Markets rebounding today but this is a medium-term equity headwind, particularly for JETS (airline fuel + rates).
- **NVDA $190P Jul18 safe:** NVDA at ~$200 gives ~5% cushion above the $190 strike with 30 DTE. No immediate CSP threat.
- **API unavailable this morning:** Could not confirm live positions. Relying on EOD June 17 data. Recommend manually verifying positions via Alpaca dashboard before executing XLE close.

---

*Sources: Al Jazeera (Iran MOU), CNN (Trump signing), TradingEconomics/Investing.com (Brent ~$78.96), TheStreet/Benzinga (S&P futures +0.87%), Yahoo Finance (NVDA ~$200, JETS ~$30.30, XLE ~$54.67)*
