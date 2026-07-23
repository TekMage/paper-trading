# Premarket Summary — Thursday, July 23, 2026

> **API status:** UNAVAILABLE (curl failed; exec_eod_2026-06-18 remains authoritative)
> **Last confirmed equity:** $102,108.69 (June 18, 2026 — GitHub Actions down Day 38)
> **Market context:** GOOGL beat EPS / TSLA missed EPS AH yesterday; Brent surged to $98.49 (+$3.02 overnight); mixed tech signals into today's open; American Airlines reports this morning.

---

## Account Snapshot

| Metric | Value | Note |
|---|---|---|
| **Equity** | $102,108.69 | Last confirmed — June 18, 2026 EOD (stale: ~25 trading sessions unconfirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026; stale |
| **Options BP** | $73,470.00 | Last confirmed June 18; no Layer 2 activity since bot went offline |
| **Account floor** | $87,500.00 | Bot halts new positions below this level |
| **GitHub Actions** | ❌ DOWN — Day 38 | All 3 workflows `disabled_manually` since June 19 |

---

## Current Positions

**Layer 1 — Core ETFs (all unconfirmed — ~25 sessions since June 18):**

| Symbol | Shares (Est.) | Target | Notes |
|---|---|---|---|
| **QQQ** | 50 | 50 | GOOGL revenue miss ($103.6B vs $120.4B est) but AI capex spend "soars" = NVDA bullish read-through; TSLA EPS miss weighs; net QQQ direction uncertain at open |
| **SPY** | 13 | 13 | S&P closed -0.14% Wednesday; crude surge ($98.49) pushing bond yields higher |
| **JETS** | 80 | 80 | ⚠️ Brent now $98.49 (+$3.02 overnight) = worsening fuel-cost headwind; American Airlines reports this morning; JETS likely under pressure |
| **XLE** | 100 | EXIT | ✅ Brent $98.49 = XLE position benefiting; FORCE_CLOSE still unexecuted (Day 38) |
| **SPCX** | 15 (est.) | 15 | SpaceX; no news |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 38; requires bot resumption or manual close |

**Layer 2 — Open CSPs:**

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA CSP** | ≤$190P Aug21 | No confirmed open position; bot offline; GOOGL AI capex signal tonight is read-through for NVDA setup — evaluate after reading GOOGL commentary |
| **AMZN CSP** | $215P Aug21 | ⛔ Hard block — AMZN Q2 earnings July 30 (5 trading sessions); no action |

---

## Iran / Oil Status

| Item | Status (Premarket Jul 23) |
|---|---|
| **Iran MOU** | ⚠️ June 17 MOU (60-day framework) remains nominally in effect but actively challenged — Iran insisting on Hormuz authority; US completed 2nd round of retaliatory airstrikes; Houthis attacked two Saudi tankers overnight |
| **Formal MOU trigger** | ❌ NOT active — no new deal signed; ongoing conflict; June 17 MOU under strain |
| **Brent crude (Jul 23)** | **$98.49/bbl** as of ~6:15 AM ET — up $3.02 from yesterday ($95.47); driven by Houthi tanker attacks + Trump warning on Hormuz strikes |
| **vs $90 trim trigger** | ✅ NOT active — Brent $98.49 >> $90 |
| **vs $85 exit trigger** | ✅ NOT active — Brent $98.49 >> $85 |

> **Oil context:** Brent surged another $3.02 overnight to $98.49 on Houthi tanker attacks (2 Saudi oil tankers hit with missiles and drones). XLE position (100 shares) continues to benefit. Hormuz disruption risk elevated. The $90 trim trigger remains DEACTIVATED — would reactivate only if Brent falls to $90 or below (e.g., on confirmed ceasefire news). Iran MOU is a framework only — no oil-bearish "deal done" trigger event occurred.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE at market | $90/bbl | ✅ NOT active — Brent $98.49; $8.49 above trigger |
| Brent ≤ $85 → exit all XLE at market | $85/bbl | ✅ NOT active — Brent $98.49 |
| Iran MOU formally signed (new deal) → sell 60 XLE immediately | Formal new MOU | ❌ NOT active — June 17 MOU under strain; no new deal |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 (+30% from $27.45) | ❌ NOT active — Brent surge ($98.49) is severe JETS headwind; trigger far away |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Re-enable GitHub Actions — Day 38.** Navigate to `github.com/TekMage/paper-trading/actions` before 9:30 AM ET. Highest-leverage action: bot auto-executes XLY FORCE_CLOSE, Layer 1 rebalance, NVDA CSP evaluation in one shot. |
| 🔴 2 | **XLY FORCE_CLOSE — Day 38 unexecuted.** If Actions not re-enabled before open, close XLY manually via Alpaca paper dashboard. |
| 🟡 3 | **GOOGL AI capex commentary — read before NVDA CSP decision.** GOOGL Q2 beat EPS ($9.11 vs $2.98 est) but missed revenue ($103.6B vs $120.4B est); Google's AI spending guidance is the key signal for NVDA Aug26 earnings setup and $190P CSP viability. Review GOOGL earnings call transcript before evaluating any NVDA position. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 38** | ~25 missed sessions; $0 Layer 2 premium; XLY FORCE_CLOSE unexecuted; NVDA CSP window open but bot offline |
| 🔴 **XLY FORCE_CLOSE Day 38** | Manual close or bot resumption required |
| ⚠️ **JETS fuel headwind — worsening** | Brent $98.49 (+$3.02 overnight); jet fuel costs surging; American Airlines reports this morning; JETS at risk of gap-down on AAL guidance |
| ⚠️ **TSLA EPS miss (AH Jul 22)** | $0.33 EPS vs $0.53 est; operating margin 1.4% (collapsed from prior); stock fell to $362.80 AH; weighs on QQQ today |
| ⚠️ **GOOGL revenue miss (AH Jul 22)** | $103.6B vs $120.4B est; but AI capex "soars" — two-sided: near-term revenue concern vs long-term NVDA/AI demand signal |
| ⚠️ **Iran June 17 MOU under strain** | Iran asserting Hormuz authority; US retaliatory strikes completed (2nd round); Houthis hit 2 Saudi tankers overnight; no resolution timeline; Brent rising on escalation |
| ⚠️ **AMZN earnings July 30** | 5 trading sessions away; hard block on AMZN $215P CSP; evaluate post-earnings |
| 🟢 **XLE benefiting from oil surge** | Brent $98.49 = XLE (100 shares) at maximum benefit since inception; no exit trigger active |
| 🟢 **Options BP preserved** | $73,470 confirmed June 18; dry powder intact on bot resumption |
| 🟢 **NVDA not yet reporting** | NVDA Q2 reports August 26; no near-term earnings risk on CSP setup; GOOGL capex signal is a positive read-through for NVDA demand |
| 🟢 **No trigger breach** | All manual triggers INACTIVE today; no required manual action on XLE or JETS |

---

*Sources: [Fortune — Brent Jul 23](https://fortune.com/article/price-of-oil-07-23-2026/) · [ABC News — Iran MOU timeline](https://abcnews.com/Politics/us-iran-ceasefire-mou-broke-timeline/story?id=134622392) · [CFR — Iran Deal](https://www.cfr.org/articles/trumps-iran-deal-reopens-the-strait-much-remains-to-be-done) · [Electrek — TSLA Q2 2026](https://electrek.co/2026/07/22/tesla-tsla-q2-2026-financial-results/) · [Yahoo Finance — TSLA earnings](https://finance.yahoo.com/markets/stocks/articles/tesla-q2-2026-earnings-revenue-203906234.html) · [Quiver — GOOGL Q2 2026](https://quiverquant.com/news/GOOGLE+($GOOGL)+Releases+Q2+2026+Earnings) · [247WallSt — Airlines/Oil](https://247wallst.com/investing/2026/07/08/american-airlines-sinks-5-united-falls-4-delta-and-jetblue-slip-3-as-crude-oil-jumps/) · exec_eod_2026-06-18.md (last authoritative confirmed account state) · Alpaca paper API (UNAVAILABLE) · ~9:00 AM ET*
