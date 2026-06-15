# Pre-Market Summary — Monday, June 16, 2026

> **Market opens in ~30 min (9:30 AM ET). CRITICAL: Two XLE manual triggers active simultaneously.**

---

## Header

- **API status:** UNAVAILABLE — Alpaca paper API unreachable from cloud environment
- **Last confirmed equity:** $100,794.08 (exec_eod_2026-06-12, Friday close)
- **Market context:** Iran–US Hormuz MOU signed June 14 → oil gapping down hard; futures sharply positive; XLE triggers fully activated

---

## Account Snapshot (from exec_eod_2026-06-12 — authoritative)

| Metric | Value |
|--------|-------|
| **Equity** | **$100,794.08** |
| Our return (inception) | +0.79% |
| SPY benchmark return | +1.39% (SPY @ $741.67) |
| Alpha vs SPY | -0.59% |
| Options BP remaining | $31,843.08 |
| Starting capital | $100,000 (May 7, 2026) |
| Account floor | $87,500 |
| Headroom above floor | $13,294 |

---

## Current Positions

### Layer 1 — Core ETFs

| Symbol | Shares | Status | Notes |
|--------|--------|--------|-------|
| QQQ | 50 | At target (likely — +5 submitted Jun 12 open) | Fill unconfirmed via API; exec_eod BP consistent with fill |
| SPY | 13 | At target | Inception cost $731.53 |
| JETS | 80 | At target | Cost ~$27.45; close ~$28.56 Fri; Iran/oil TAILWIND today |
| **XLE** | **100** | 🔴🔴 **SELL ALL — TWO TRIGGERS ACTIVE** | See Iran/Oil section below |
| XLY | 0 | Closed Jun 11 | v2.1 exit complete |
| SPCX | 15 | Likely filled Jun 12 IPO day | Est. fill ~$150; closed ~$161 (+7% on fill est.) |

### Layer 2 — Open CSPs

| Position | Status | Strike OTM | Notes |
|----------|--------|------------|-------|
| **NVDA $180P Jul17** | CONFIRMED OPEN | ~12% OTM (NVDA ~$205 Fri) | Fill: $1.97; BTC target ~$0.99 — bot auto-closes at 50% |
| **AMZN $220P Jul17** | Likely open (BP evidence) | ~8% OTM (AMZN ~$238 Fri) | $220P submitted Jun 12; BP $57,970→$31,843 (~$26K drop) consistent with fill |

*No other CSPs open. TSLA, INTC are NOT part of the current strategy.*

---

## 🔴🔴 Iran / Oil Status — CRITICAL ALERT

| Item | Status |
|------|--------|
| **Iran MOU signed?** | **YES — signed June 14, 2026 in Switzerland** |
| **Brent crude (Jun 15)** | **$83.05–$84.48/bbl** |
| vs $90 trim trigger | 🔴 **BREACHED — $6–7 below** |
| vs $85 exit trigger | 🔴 **BREACHED — $0.52–$1.95 below** |

**Iran deal summary:** US–Iran framework MOU signed June 14 in Switzerland. Strait of Hormuz to reopen; $24B in frozen Iranian assets unfrozen; nuclear program enters 60-day negotiation window. Brent dropped from $87.27 (Jun 12 close) to $83–84 over the weekend in direct response.

### XLE Action Required — BOTH TRIGGERS ACTIVE

| Trigger | Rule | Status |
|---------|------|--------|
| Iran MOU signed | Sell 60 XLE at market immediately | 🔴 **TRIGGERED** |
| Brent ≤ $85 | Sell ALL remaining XLE | 🔴 **TRIGGERED** |

**Combined action: SELL ALL 100 XLE AT MARKET ON OPEN.**

The $85 exit trigger (sell all) and the MOU trigger (sell 60) are both active. The $85 trigger is the more comprehensive rule — all 100 shares should be exited. At ~$56/share, this releases ~$5,600 to cash. This is a MANUAL action — the bot does not execute XLE exits.

---

## Manual Triggers to Monitor Today

| Trigger | Level | Current | Status |
|---------|-------|---------|--------|
| Brent ≤ $85 → sell ALL XLE (100 shares) | $85.00 | ~$83–84 | 🔴 **TRIGGERED — ACT AT OPEN** |
| Iran MOU signed → sell 60 XLE immediately | — | Signed Jun 14 | 🔴 **TRIGGERED — ACT AT OPEN** |
| Brent ≤ $90 → sell 30 XLE | $90.00 | ~$83–84 | 🔴 Superseded by $85 trigger |
| JETS ≥ $35.69 (+30% from $27.45 cost) → close all 80 JETS | $35.69 | ~$28.56 | Not triggered ($7.13 gap) |

---

## Morning Priority Actions

1. **SELL ALL 100 XLE AT MARKET — immediately at 9:30 AM open.** Both the Iran MOU trigger and the Brent ≤ $85 trigger are active. Do not wait for bot confirmation — this is a manual action. XLE likely opens lower given oil gap-down.

2. **Verify QQQ, SPCX, AMZN CSP fills.** These were submitted June 12 but API is unavailable. Check account in Alpaca UI or via API when accessible. QQQ should be at 50 shares, SPCX at 15 shares, AMZN $220P should be open.

3. **Monitor JETS for upside.** Iran peace deal + lower oil = tailwind for airlines. JETS may rally toward $30–32 today. Exit trigger is $35.69 — watch intraday.

---

## Market Context

| Item | Finding |
|------|---------|
| S&P 500 futures | Strongly positive — Iran peace deal lifting risk assets |
| NVDA | Sector down 26% from highs; RTX Spark launch Jun 1; SK Hynix partnership; $180P at 12% OTM is safe |
| AMZN | ~$238 Fri; Prime Day June 23–26 (earlier than usual); $220P ~8% OTM — safe |
| JETS | Iran deal + oil drop = sector tailwind; hold for $35.69 trigger |
| SPCX | IPO day closed ~$161 (+19% vs $135 IPO price); est. unrealized gain ~+$165 on 15 shares |
| Juneteenth | NYSE **closed Thursday June 19** (not Monday) — today trades normally |

### Week Macro Calendar

| Date | Event |
|------|-------|
| Mon Jun 16 | Empire State Manufacturing 8:30 AM; **XLE exit at open** |
| Tue Jun 17 | Retail Sales 8:30 AM; Industrial Production |
| Wed Jun 18 | FOMC meeting begins |
| **Thu Jun 19** | **NYSE CLOSED — Juneteenth; FOMC decision** |
| Fri Jun 20 | Monthly options expiration (watch sector vol — no NVDA exposure) |

*FOMC: First decision for Chair Warsh. Expected hold given CPI +4.2%. Watch for hawkish tone.*

---

## Risk Flags

- 🔴 **XLE**: All trigger conditions satisfied — must exit at open or risk further oil-driven losses
- ⚠️ **AMZN CSP ($220P)**: Fill unconfirmed via API; if unfilled (GTC expired at 4 PM Fri), bot will resubmit today — may target $215P per current strategy target
- ⚠️ **NVDA sector**: Chips down 26% from highs; NVDA $180P Jul17 is 12% OTM with ~32 DTE — watch if NVDA drops below $190 (would reduce OTM buffer)
- ⚠️ **Alpha lag**: Account at -0.59% alpha vs SPY ITD. XLE exit + Iran rally on other positions may help close gap today.
- ⚠️ **FOMC week**: Rate decision Thursday (holiday) introduces midweek vol; plan around CSP positions

---

*Sources: exec_eod_2026-06-12.md (positions/equity), eod_2026-06-12.md (context/analysis), CNN/NPR/RFERL (Iran MOU June 14), Fortune/Trading Economics (Brent $83–84), TheStreet (futures), CNBC (NVDA), NBC News (Amazon Prime Day)*
