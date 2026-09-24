# Premarket Summary — Monday, July 27, 2026

> **API status:** UNAVAILABLE (curl failed; exec_eod_2026-06-18 remains authoritative)
> **Last confirmed equity:** $102,108.69 (June 18, 2026 — GitHub Actions down Day 40)
> **Market context:** Risk-on surge — US and Iran paused fighting over weekend; oil fell ~8.2%; S&P 500 futures +0.9%, Nasdaq +1.4%. Busiest week of Q2: Big Tech earnings + Fed decision.

---

## ⚠️ URGENT: BRENT AT $90.28 — TRIM TRIGGER WITHIN $0.28

**Brent crude is at ~$90.28–$90.43 as of ~6:35 AM ET.** The XLE trim trigger is Brent ≤ $90 (sell 30 XLE at market). As of premarket, Brent is within $0.28–$0.43 of triggering. Monitor Brent closely at open — if it dips below $90.00, sell 30 XLE at market immediately.

---

## Account Snapshot

| Metric | Value | Note |
|---|---|---|
| **Equity** | $102,108.69 | Last confirmed — June 18, 2026 EOD (stale: ~28 trading sessions unconfirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026; stale |
| **Options BP** | $73,470.00 | Last confirmed June 18; no Layer 2 activity since bot went offline |
| **Account floor** | $87,500.00 | Bot halts new positions below this level |
| **GitHub Actions** | ❌ DOWN — Day 40 | All 3 workflows `disabled_manually` since June 19 |

---

## Current Positions (unconfirmed — ~28 sessions since June 18 EOD)

**Layer 1 — Core ETFs (all at target; GitHub Actions maintains these):**

| Symbol | Shares (Est.) | Target | Notes |
|---|---|---|---|
| **QQQ** | 50 | 50 | Nasdaq futures +1.4% — strong open expected; AI/semi rally continues |
| **SPY** | 13 | 13 | S&P futures +0.9%; risk-on; Fed decision due this week |
| **JETS** | 80 | 80 | ✅ JETS likely rallying — oil down 8.2% = significant fuel cost relief; monitor $35.69 trigger |
| **XLE** | 100 | EXIT | ⚠️ Oil -8.2% = XLE opening lower; Brent $90.28 near $90 trim trigger; FORCE_CLOSE still unexecuted Day 40 |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 40; consumer discretionary likely up on oil relief |

**Layer 2 — Open CSPs:**

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA CSP** | ≤$190P (target Aug/Sep) | No confirmed open position; bot offline Day 40; NVDA constructive ~$212+; earnings Aug 26 |
| **AMZN CSP** | $215P | ⛔ HARD BLOCK — AMZN Q2 earnings **Wednesday July 30** (3 days); do NOT open before earnings |

---

## Iran / Oil Status

| Item | Status (Premarket Jul 27) |
|---|---|
| **Iran-US fighting** | ⚠️ US paused attacks Friday night (no announcement); Iran halted retaliatory strikes; Oman mediating Hormuz talks |
| **Formal new MOU** | ❌ NOT signed — ceasefire-adjacent pause, not a new binding deal; original June 17 MOU remains framework |
| **XLE sell trigger (MOU)** | ❌ NOT triggered — no new deal signed; original MOU already known |
| **Brent crude (Jul 27)** | **~$90.28–$90.43/bbl** — DOWN 8.23% overnight; driven by US-Iran ceasefire pause |
| **vs $90 trim trigger** | 🔴 **CRITICAL — $0.28 ABOVE TRIGGER.** Brent ≤ $90 = sell 30 XLE at market |
| **vs $85 exit trigger** | ✅ NOT active — $5.28 above trigger |

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90.00/bbl | 🔴 **NEAR TRIGGER — Brent $90.28, $0.28 above; watch at open** |
| Brent ≤ $85 → exit all XLE at market | $85/bbl | ✅ NOT active — $5.28 above |
| Iran MOU formally signed (new deal) → sell 60 XLE immediately | New formal MOU | ❌ NOT active — pause in fighting, not a new MOU |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 (+30% from $27.45) | ⚠️ Monitor — oil -8% = JETS likely rallying today; check opening price |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **BRENT $90.28 — MONITOR AT OPEN.** If Brent prints ≤ $90.00 at any point today, sell 30 XLE at market immediately. This is a MANUAL action. Open Alpaca paper dashboard now and watch Brent vs XLE at 9:30 AM ET. |
| 🔴 2 | **Re-enable GitHub Actions — Day 40.** Navigate to `github.com/TekMage/paper-trading/actions` before 9:30 AM ET to restart all 3 workflows. Bot will auto-handle XLY FORCE_CLOSE, NVDA CSP, Layer 1 rebalance. |
| 🟡 3 | **Check JETS opening price.** Oil -8.2% = airlines rally. If JETS opens near/above $35.69, close all 80 shares at market (manual trigger). |
| 🟡 4 | **AMZN CSP — maintain hard block.** Earnings Wednesday July 30. Do NOT open any AMZN position this week until post-earnings. Reassess $215P strike after the print. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **BRENT $90.28 — TRIM TRIGGER IMMINENT** | $0.28 above $90 trigger; oil volatile on Iran ceasefire news; XLE opening lower today |
| 🔴 **GitHub Actions Day 40** | ~28 missed sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted; NVDA CSP window passing |
| 🔴 **XLY FORCE_CLOSE Day 40** | Still unexecuted; consumer discretionary likely up today (oil relief); partial upside recaptured if not closed |
| ⚠️ **Iran-US ceasefire fragile** | Informal fighting pause, not formal MOU; situation fluid; Brent could bounce back or drop further |
| ⚠️ **AMZN earnings July 30 (Wed)** | AMZN CSP hard-blocked; watch for pre-earnings volatility Mon-Tue; do not touch |
| ⚠️ **Fed decision this week** | Rate decision due mid-week; potential volatility across all positions |
| 🟢 **JETS fuel relief** | Oil -8.2% = largest JETS tailwind since inception; fuel cost headwind easing significantly |
| 🟢 **QQQ/SPY/SPCX opening strong** | Nasdaq +1.4% premarket; risk-on across the board; Layer 1 positions rallying |
| 🟢 **NVDA constructive** | AI chip index +47% YTD; NVDA ~$212+; H20 licenses intact; earnings Aug 26; CSP setup intact |
| 🟢 **Options BP preserved** | $73,470 confirmed June 18; no decay; dry powder available once bot re-enabled |
| 🟢 **No new Iran MOU** | June 17 MOU framework intact; no new sell trigger on XLE today |

---

*Sources: [Fortune — Brent Jul 27 2026](https://fortune.com/article/price-of-oil-07-27-2026/) · [Yahoo Finance — Premarket Jul 27](https://finance.yahoo.com/markets/live/stock-market-today-monday-july-27-dow-sp-500-nasdaq-080412540.html) · [Benzinga — Futures Jul 27](https://www.benzinga.com/markets/equities/26/07/60688523/stock-market-today-sp-500-dow-jones-futures-rise-as-us-iran-halt-retaliatory-strikes-microchip-technology-amd-nucor-in-focus/) · [ABC News — Iran MOU timeline](https://abcnews.com/Politics/us-iran-ceasefire-mou-broke-timeline/story?id=134622392) · [Intellectia — Semi stocks Jul 2026](https://intellectia.ai/blog/ai-semiconductor-stocks-rally-july-2026) · exec_eod_2026-06-18.md (last authoritative) · Alpaca paper API (UNAVAILABLE) · ~9:00 AM ET*
