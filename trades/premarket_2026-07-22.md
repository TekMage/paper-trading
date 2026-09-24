# Premarket Summary — Wednesday, July 22, 2026

> **API status:** UNAVAILABLE (curl failed; exec_eod confirmed June 18 is authoritative source)
> **Last confirmed equity:** $102,108.69 (June 18, 2026 — GitHub Actions down Day 37)
> **Market context:** Futures sliding ~0.37%; Brent surged to $95.47 — XLE trim triggers DEACTIVATED; AMD Advancing AI 2026 event today; GOOGL + TSLA earnings after close.

---

## Account Snapshot

| Metric | Value | Note |
|---|---|---|
| **Equity** | $102,108.69 | Last confirmed — June 18, 2026 EOD (stale: ~24 trading sessions unconfirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026; stale |
| **Options BP** | $73,470.00 | Last confirmed June 18; Layer 2 flat since then |
| **Account floor** | $87,500.00 | Bot halts new positions below this level |
| **GitHub Actions** | ❌ DOWN — Day 37 | All 3 workflows `disabled_manually` since June 19 |

---

## Current Positions

**Layer 1 — Core ETFs (all unconfirmed — ~24 sessions since June 18):**

| Symbol | Shares (Est.) | Target | Est. Value | Notes |
|---|---|---|---|---|
| **QQQ** | 50 | 50 | — | Futures sliding; AMD AI conference + GOOGL/TSLA earnings AH = big QQQ catalyst day |
| **SPY** | 13 | 13 | — | S&P futures -0.37% (-28 pts); oil prices weighing premarket |
| **JETS** | 80 | 80 | ~$32.25 premarket | Pulling back from yesterday's $33.54 intraday high; oil surge ($95.47) is a fuel-cost headwind for airlines |
| **XLE** | 100 | EXIT | — | Brent $95.47 — XLE should be rallying; BUT FORCE_CLOSE still pending (see below) |
| **SPCX** | 15 (est.) | 15 | — | SpaceX; Nasdaq rally provides lift |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | — | 🔴 FORCE_CLOSE unexecuted — Day 37 |

**Layer 2 — Open CSPs:**

| Target | Strike / Expiry | Status |
|---|---|---|
| **NVDA CSP** | ≤$190P Aug21 | No confirmed open position; NVDA ~$208-210 area (~8-9% OTM); window open but bot offline; AMD AI conference today = chip sector volatility watch |
| **AMZN CSP** | $215P Aug21 | ⛔ Hard block — AMZN Q2 earnings July 30 (6 trading sessions); ~13-15% OTM cushion; no action |

---

## Iran / Oil Status

| Item | Status (Premarket Jul 22) |
|---|---|
| **Iran MOU** | ❌ NONE ACTIVE — June 17 MOU defunct (Trump declared ceasefire over July 7); no new deal signed overnight |
| **Formal MOU trigger** | ❌ NOT active — PBS "initial deal" from July 21 remains informal; active conflict continues |
| **US airstrikes** | ⚠️ 11th consecutive night of US airstrikes against Iran; Hormuz remains disrupted |
| **Brent crude (Jul 22)** | **$95.47/bbl** as of ~6:05 AM ET — up $1.06 from prior; surging on continued conflict |
| **vs $90 trim trigger** | ✅ **NOT active** — Brent $95.47 > $90; trigger DEACTIVATED (was active yesterday at $88.34–$89.04) |
| **vs $85 exit-all trigger** | ✅ **NOT active** — Brent $95.47 >> $85 |

> **Oil context:** Brent has surged from yesterday's $88-89 range to $95.47 today — the $90 XLE trim trigger that was firing for 35+ sessions is now DEACTIVATED. XLE (100 shares held) should be benefiting from this rally. The Iran conflict escalation (11th night of strikes) is pushing oil higher, not lower.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE at market | $90/bbl | ✅ NOT active — Brent $95.47; trigger would reactivate if Brent falls below $90 |
| Brent ≤ $85 → exit all XLE at market | $85/bbl | ✅ NOT active — Brent $95.47 |
| Iran MOU signed → sell 60 XLE immediately | Formal MOU | ❌ NOT active — no formal deal; active conflict ongoing |
| JETS ≥ $35.69 → close all 80 JETS | $35.69 (+30% from $27.45) | ⚠️ Watch — JETS premarket ~$32.25; $3.44 below trigger; pulled back from yesterday's $33.54 high on oil-rally headwind |

---

## Morning Priority Actions

| Priority | Action |
|---|---|
| 🔴 1 | **Re-enable GitHub Actions** — Day 37. Navigate to `github.com/TekMage/paper-trading/actions` before 9:30 AM ET. Bot will auto-execute: XLY FORCE_CLOSE, Layer 1 rebalance, NVDA CSP evaluation. Single highest-leverage action available. |
| 🔴 2 | **XLY FORCE_CLOSE** — Day 37 unexecuted. If Actions not re-enabled in time, close XLY manually via Alpaca paper dashboard before market open. |
| 🟡 3 | **GOOGL + TSLA earnings watch (AH)** — Both report after today's close. GOOGL AI capex commentary = direct read-through for NVDA/QQQ. TSLA: 480K deliveries (record), focus on gross margins. Expect QQQ volatility post-close; do NOT open NVDA CSP before reading GOOGL results. AMD Advancing AI 2026 conference also starts today — MI450X/MI550X announcements could move chip sector intraday. |

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 37** | ~24 missed sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted; NVDA CSP window open but bot offline |
| 🔴 **XLY FORCE_CLOSE Day 37** | Unexecuted; manual close or bot resumption required |
| ⚠️ **JETS fuel-cost headwind** | Brent $95.47 — oil surge hurts airlines; JETS premarket ~$32.25 (down from $33.54 yesterday high); $35.69 trigger $3.44 away |
| ⚠️ **GOOGL + TSLA earnings AH** | First Mag7 Q2 reports; GOOGL AI capex is the NVDA/QQQ bull/bear signal; TSLA margin risk; expect after-hours QQQ volatility |
| ⚠️ **AMD Advancing AI 2026 (today)** | MI450X/MI550X announcements; Jefferies flagged Anthropic as likely AMD customer announcement; could move chip sector broadly; watch for NVDA impact |
| ⚠️ **Iran conflict — no resolution** | 11th straight night of US airstrikes; Hormuz disrupted; no ceasefire talks confirmed; Brent rising on escalation |
| ⚠️ **AMZN earnings July 30** | 6 trading sessions away; hard block on AMZN CSP; $215P Aug21 queued post-earnings |
| ⚠️ **Brent $90 trim trigger watchlist** | Trigger DEACTIVATED at $95.47 today; if Brent reverses below $90 (e.g., on ceasefire news), sell-30-XLE rule reactivates immediately |
| 🟢 **XLE holding value** | Brent $95.47 = XLE position (100 shares) benefiting from oil rally; conflict premium supports energy exposure |
| 🟢 **XLE trim trigger deactivated** | The 35+ session ACTIVE trigger has now deactivated; no urgent XLE sell action required this morning |
| 🟢 **Options BP preserved** | $73,470 confirmed June 18; dry powder ready on bot resumption |
| 🟢 **NVDA setup** | ~8-9% OTM from ≤$190 target; GOOGL capex commentary tonight is the read-through; evaluate Aug21 CSP entry on next bot session |
| 🟢 **SMCI premarket surge** | Supermicro surged premarket on record AI server backlog — favorable AI infrastructure demand signal for NVDA thesis |

---

*Sources: eod_2026-07-21.md · eod_2026-07-20.md · exec_eod_2026-06-18.md (last authoritative confirmed account state) · [Fortune — Brent crude Jul 22](https://fortune.com/article/price-of-oil-07-22-2026/) · [Britannica — 2026 Iran war](https://www.britannica.com/event/2026-Iran-war) · [ABC News — Iran ceasefire timeline](https://abcnews.com/Politics/us-iran-ceasefire-mou-broke-timeline/story?id=134622392) · [Benzinga — Market futures Jul 22](https://www.benzinga.com/markets/equities/26/07/60600025/stock-market-today-sp-500-nasdaq-100-futures-fall-as-chip-stocks-cool-down-and-tesla-alphabet-gear-up-for-earnings-super-micro-adtran-capital-one-in-focus) · [Yahoo Finance — Market live Jul 22](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-july-22-dow-sp-500-nasdaq-alphabet-tesla-083644887.html) · [Yahoo Finance — AMD Jul 22](https://finance.yahoo.com/markets/stocks/articles/amd-stock-buy-july-22-055000164.html) · [GuruFocus — GOOGL/TSLA earnings](https://www.gurufocus.com/news/8971069/tesla-tsla-and-alphabet-goog-earnings-awaited-amid-market-decline) · Alpaca paper API (UNAVAILABLE) · ~9:00 AM ET*
