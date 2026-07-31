# Premarket Summary — Friday, July 31, 2026

> Generated ~9:00 AM ET | GitHub Actions DOWN — **Day 44** | API UNAVAILABLE

---

## Header

- **API status:** UNAVAILABLE — consistent since June 19; no live account data
- **Last confirmed equity:** $102,108.69 (June 18 EOD — ~31 unconfirmed trading sessions)
- **GitHub Actions:** ❌ DOWN — Day 44 (all 3 workflows `disabled_manually` since June 19)
- **Market context:** S&P 500 futures +0.47% (~+35pts to ~7,507) on AMZN massive earnings beat (AWS +37%); AAPL reports AH tonight; Iran war active, no MOU; Brent ~$92.27/bbl (above $90 — XLE triggers INACTIVE)

---

## Account Snapshot

> All figures from exec_eod_2026-06-18.md — the last authoritative source. ~31 unconfirmed trading sessions since then.

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Confirmed June 18 EOD; stale — 31 sessions unconfirmed |
| **Return (inception)** | **+2.11%** | vs $100,000 starting capital May 7, 2026 |
| **SPY at inception** | $731.53 | Benchmark |
| **SPY (est. Jul 30 close)** | ~$736 | ~+0.61% inception — portfolio showing positive alpha (unverified) |
| **Options BP remaining** | $73,470.00 | Confirmed June 18; fully undeployed — Layer 2 FLAT all 44 sessions |
| **Account floor** | $87,500.00 | Not at risk given last confirmed equity |
| **Layer 2 premium (since Jun 18)** | $0.00 | ~31 missed sessions, 90+ bot run-slots |

---

## Current Positions

> All share counts are estimates from June 18 confirmed state. No exec files have been generated since June 18 (GitHub Actions disabled).

### Layer 1 — Core ETFs

| Symbol | Shares (Est.) | Target | Est. Jul 30 Close | Status |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | $681.64 | At target; +3.0% Thu on MSFT +15%; AMZN beat → gap-up at open |
| **SPY** | 13 | 13 | ~$736 | At target; above inception benchmark $731.53 |
| **JETS** | 80 | 80 | $31.49 | At target; $35.69 trigger $4.20 (+13.4%) away |
| **XLE** | 100 | EXIT (FORCE_CLOSE) | $58.38 | 🔴 FORCE_CLOSE unexecuted Day 44; Brent $92.27 — triggers inactive |
| **SPCX** | 15 | 15 | Unknown | No price data available |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | Unknown | 🔴 FORCE_CLOSE unexecuted Day 44; strategy violation ongoing |

### Layer 2 — Open CSPs (FLAT since June 18)

**No confirmed open options positions.**

| Target | Strike / Expiry | Underlying (Est.) | Status |
|---|---|---|---|
| **NVDA CSP** | $180P Sep19 (revised target) | ~$197.01 (Jul 30 close) | ⚠️ Bot offline; NVDA recovered from $190.27 ATM crisis; **must update CSP_TARGETS to $180P BEFORE re-enabling GitHub Actions** |
| **AMZN CSP** | $215P Sep18 | ~$249 AH / opens ~$249+ | 🟢 Hard block LIFTED post-earnings; $215P = ~13.7% OTM at $249; actionable if bot re-enabled; DTE Sep18 ~49 days ✅ |

---

## Iran / Oil Status

| Item | Status (July 31 Premarket) |
|---|---|
| **Iran MOU signed overnight?** | ❌ **NO** — June 17 MOU defunct since ~July 8; full US-Iran war active; no new deal; no Hormuz MOU signed |
| **US strikes** | US conducted major strikes on Iranian targets Jul 29–30 (Bandar Abbas, Kish Island, command centers, Egypt); war actively escalating |
| **Senate War Powers** | Failed 49-50 Thursday — Trump retains full strike authorization |
| **IRGC status** | Threatened retaliation "today" (Jul 30) — counter-strikes unconfirmed at summary time |
| **Hormuz** | RESTRICTED — partially functional; ~14 ships passed last 24h |
| **Brent crude (premarket Jul 31)** | **~$92.27/bbl** — up from $90.04 Thursday close; Iran war escalation overnight keeping price elevated |
| **vs $90 XLE trim trigger** | ✅ **INACTIVE** — Brent $92.27 > $90; trigger NOT met this morning |
| **vs $85 XLE exit trigger** | ✅ NOT triggered — $7.27 above threshold |

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | ✅ INACTIVE — Brent ~$92.27; $2.27 above trigger (war premium elevated) |
| **Brent ≤ $85 → exit ALL XLE at market** | $85/bbl | ✅ NOT triggered — $7.27 above threshold |
| **Iran MOU signed → sell 60 XLE immediately** | New formal MOU | ❌ NOT triggered — war actively escalating; opposite scenario |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69/share | ❌ NOT triggered — JETS $31.49; $4.20 (+13.4%) away |

> ⚠️ **Brent watch note:** While triggers are inactive at $92.27, Brent saw an intraday low of $89.95 yesterday before recovering. The $90 trigger was technically met intraday multiple times over 6+ sessions. If Iran counter-retaliation fails to materialize, Brent could fade again. Keep Alpaca paper dashboard accessible today.

---

## Morning Priority Actions

1. **🔴 Re-enable GitHub Actions — Day 44 (CRITICAL):** Before re-enabling, **update `CSP_TARGETS` in `scripts/trading_agent.py`** — change NVDA from `190` → `180`. NVDA closed at ~$197; $190P is only 3.6% OTM (unsafe); $180P Sep19 = 8.6% OTM (strategy-compliant). Navigate to github.com/TekMage/paper-trading/actions and enable all 3 workflows after the code update is pushed.

2. **🟡 AAPL earnings AH tonight (key risk):** AAPL reports after close today — iPhone 17 cycle, services growth, China supply chain. This is the 3rd consecutive mega-cap catalyst this week (MSFT +15% Thu, AMZN +9% AH Thu). Hold all new leveraged options entry until post-AAPL results. A beat → continued QQQ momentum; a miss → potential Nasdaq pull-back. No new CSP entries that depend on QQQ staying elevated until results clear.

3. **🟡 AMZN $215P CSP (actionable if bot re-enabled):** AMZN opens ~$249+ today post-earnings beat (AWS +37%, EPS $5.75 vs $1.82 est.). Hard block on AMZN CSP is LIFTED. The $215P Sep18 target is ~13.7% OTM at $249 — within strategy cushion. If bot is re-enabled this morning, it may attempt AMZN $215P Sep18; this is appropriate given current price. Sep18 = ~49 DTE ✅ within OPT_DTE_MIN/MAX (25/60). Monitor fill.

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 44** | ~31 missed sessions; $0 Layer 2 premium; XLY FORCE_CLOSE unexecuted; NVDA Jul18 expired worthless; 90+ bot session misses |
| 🔴 **NVDA CSP_TARGETS must be updated** | Bot targets $190P; NVDA at ~$197 = 3.6% OTM at $190P = unsafe; **update to $180P Sep19 BEFORE re-enabling GitHub Actions** |
| 🔴 **XLY FORCE_CLOSE Day 44** | Strategy violation ongoing; auto-executes if bot is re-enabled |
| 🔴 **Iran war active** | US strikes ongoing; Senate authorized Trump to continue; IRGC threatened retaliation; Hormuz restricted; no peace pathway |
| ⚠️ **AAPL earnings AH tonight** | Hold new options/leveraged entries until post-results; $33B+ expected from services + hardware |
| ⚠️ **XLE / Brent watch** | Brent $92.27 today vs. $89.95 intraday low yesterday — rapid $2+ swings on Iran news; have Alpaca dashboard ready if Brent falls back below $90 |
| ⚠️ **Equity stale 31 sessions** | Account state unverified since June 18; Alpaca API consistently unavailable; true P&L unknown |
| 🟢 **AMZN massive beat** | Rev $200.6B, EPS $5.75, AWS +37% (fastest 18 qtrs); AMZN +7–9% AH to ~$249; QQQ gap-up expected at open |
| 🟢 **QQQ 50 shares benefiting** | +3.0% Thu + expected gap-up Fri from AMZN; 50-share position is the primary portfolio driver |
| 🟢 **Brent triggers INACTIVE** | $92.27 — no manual XLE action required this morning |
| 🟢 **AMZN CSP block lifted** | $215P Sep18 now ~13.7% OTM at $249 — strategy-compliant when bot re-enabled |
| 🟢 **NVDA recovering** | ~$197 Jul 30 close; MSFT + AMZN AWS beats confirm AI capex demand; chip ATM risk from $190 receding |
| 🟢 **S&P futures +0.47%** | AMZN-driven; constructive open; AI spending signal strong this week |
| 🟢 **Options BP intact** | $73,470 confirmed June 18; fully available for Layer 2 when GitHub Actions re-enabled |

---

*Sources: eod_2026-07-30.md · midday_2026-07-30.md · exec_eod_2026-06-18.md (last authoritative account state) · Alpaca API UNAVAILABLE · GitHub Actions disabled (Day 44) · Web: Fortune (Brent ~$92.27 Jul 31) · TheStreet (S&P futures +0.47%) · Al Jazeera/ABC News (Iran MOU defunct, war active) · Yahoo Finance (NVDA/AMD semiconductor context) · ~9:00 AM ET*
