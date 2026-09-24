# Premarket Summary — Friday, July 24, 2026

> **API status:** UNAVAILABLE (curl failed; exec_eod_2026-06-18 remains authoritative)
> **Last confirmed equity:** $102,108.69 (June 18, 2026 — GitHub Actions down Day 39)
> **Market context:** S&P 500 futures mildly up +0.1–0.2% after Thursday's worst session in a month; Brent crude surged through $100 overnight (now ~$100.42–$101.15); AMZN down ~4.5% premarket on AGI layoffs and Senate scrutiny ahead of July 30 earnings.

---

## Account Snapshot

| Metric | Value | Note |
|---|---|---|
| **Equity** | $102,108.69 | Last confirmed — June 18, 2026 EOD (stale: ~26 trading sessions unconfirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026; stale |
| **Options BP** | $73,470.00 | Last confirmed June 18; no Layer 2 activity since bot went offline |
| **Account floor** | $87,500.00 | Bot halts new positions below this level |
| **GitHub Actions** | ❌ DOWN — Day 39 | All 3 workflows `disabled_manually` since June 19 |

---

## Current Positions (unconfirmed — ~26 sessions since June 18 EOD)

**Layer 1 — Core ETFs (all at target; GitHub Actions maintains these):**

| Symbol | Shares (Est.) | Target | Notes |
|---|---|---|---|
| **QQQ** | 50 | 50 | Futures mildly green after Thursday's drop; TSLA/GOOGL earnings drag fading; NVDA constructive (~$212) |
| **SPY** | 13 | 13 | S&P futures +0.1–0.2%; yesterday's worst session in a month beginning to stabilize |
| **JETS** | 80 | 80 | ⚠️ Brent now ~$100.50 — fuel cost headwind intensifying; JETS under pressure |
| **XLE** | 100 | EXIT | ✅ Brent $100.50 = XLE at maximum benefit; FORCE_CLOSE unexecuted (Day 39) |
| **SPCX** | 15 (est.) | 15 | SpaceX ETF; no news |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 39; requires bot resumption or manual close |

**Layer 2 — Open CSPs:**

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA CSP** | ≤$190P (target Aug/Sep) | No confirmed open position; bot offline Day 39; NVDA ~$212, H20 export licenses resumed — setup remains constructive |
| **AMZN CSP** | $215P (target post-earnings) | ⛔ Hard block — AMZN Q2 earnings July 30 (4 trading sessions); evaluate post-earnings; AMZN -4.5% premarket today on layoffs/Senate news |

---

## Iran / Oil Status

| Item | Status (Premarket Jul 24) |
|---|---|
| **Iran MOU** | ⚠️ June 17 MOU (60-day framework) nominally in effect; no NEW deal signed overnight; ongoing geopolitical strain |
| **Formal MOU trigger** | ❌ NOT active — no new agreement; XLE sell signal not triggered |
| **Brent crude (Jul 24)** | **~$100.42–$101.15/bbl** — surged through $100 threshold; up from $98.49 yesterday; driven by Middle East supply risk |
| **vs $90 trim trigger** | ✅ NOT active — Brent ~$100.50, $10.50 above trigger |
| **vs $85 exit trigger** | ✅ NOT active — Brent ~$100.50 |

> **Oil context:** Brent has now crossed $100/bbl for the first time since this account started. Houthi tanker attacks + Hormuz tension driving the move. XLE (100 shares) continues to benefit significantly. No exit or trim trigger active. The $90 trigger would only activate on a $10+ Brent drop — would require a ceasefire or deal completion.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE at market | $90/bbl | ✅ NOT active — Brent ~$100.50; $10.50 above trigger |
| Brent ≤ $85 → exit all XLE at market | $85/bbl | ✅ NOT active — Brent ~$100.50 |
| Iran MOU formally signed (new deal) → sell 60 XLE immediately | Formal new MOU | ❌ NOT active — no new deal overnight |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 (+30% from $27.45) | ❌ NOT active — Brent surge worsening JETS fuel-cost headwind |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Re-enable GitHub Actions — Day 39.** Navigate to `github.com/TekMage/paper-trading/actions` before 9:30 AM ET. Highest-leverage action: bot auto-executes XLY FORCE_CLOSE, Layer 1 rebalance, NVDA CSP open, AMZN CSP block evaluation. |
| 🔴 2 | **XLY FORCE_CLOSE — Day 39 unexecuted.** If Actions not re-enabled before open, close XLY manually via Alpaca paper dashboard now. |
| 🟡 3 | **AMZN CSP — hard block remains.** AMZN down ~4.5% premarket on AGI team layoffs + Senate scrutiny (Chinese influence allegation). Earnings July 30. Do NOT open AMZN CSP until post-earnings. Reassess $215P strike price after July 30 print. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 39** | ~26 missed sessions; $0 Layer 2 premium; XLY FORCE_CLOSE unexecuted; NVDA/AMZN CSP windows open but bot offline |
| 🔴 **XLY FORCE_CLOSE Day 39** | Manual close or bot resumption required |
| ⚠️ **Brent crossed $100** | New level since inception; JETS fuel-cost headwind now severe; $100/bbl = ~$3.30/gallon jet fuel; airline profit margins under pressure |
| ⚠️ **AMZN premarket -4.5%** | AGI team layoffs reported; Senate scrutiny re: alleged Chinese influence (caused ~2% AH drop); $59B capex and cash flow concerns; Q2 earnings July 30 — do not touch AMZN CSP |
| ⚠️ **TSLA ongoing drag on QQQ** | $0.33 EPS vs $0.53 est miss (Jul 22 AH); operating margin 1.4%; TSLA ~$362; weighing on NASDAQ |
| 🟢 **XLE maximum benefit** | Brent $100.50 = XLE at best level since inception; no exit trigger active |
| 🟢 **NVDA constructive** | ~$212; H20 export licenses to China resumed; Goldman buy reiteration; no Q2 earnings until Aug 26; CSP setup intact |
| 🟢 **S&P futures stabilizing** | +0.1–0.2% after Thursday's sharp drop; recovery attempt underway |
| 🟢 **Options BP preserved** | $73,470 confirmed June 18; dry powder intact |
| 🟢 **No trigger breach** | All manual triggers INACTIVE today; no required manual action on XLE or JETS |

---

*Sources: exec_eod_2026-06-18.md (last authoritative) · premarket_2026-07-23.md (prior day context) · [Fortune — Brent Jul 24 2026](https://fortune.com/article/price-of-oil-07-24-2026/) · [Bloomberg — Oil markets Jul 24](https://www.bloomberg.com/news/articles/2026-07-23/latest-oil-market-news-and-analysis-for-july-24) · [Benzinga — S&P 500 futures Jul 24](https://www.benzinga.com/markets/prediction-markets/26/07/60660768/sp500-july-24-open-up-or-down-polymarket-oil-prices-alphabet-tesla-earnings-ai-spending) · [FX Leaders — AMZN Jul 23](https://www.fxleaders.com/news/2026/07/23/amazon-stock-amzn-tests-support-as-competition-and-59b-capex-raises-cash-flow-concerns/) · [TradingKey — NVDA Jul 2026](https://www.tradingkey.com/analysis/stocks/us-stocks/262015350-nvidia-nvda-stock-forecast-july-2026-kyber-denial-goldman-tradingkey) · Alpaca paper API (UNAVAILABLE) · ~9:00 AM ET*
