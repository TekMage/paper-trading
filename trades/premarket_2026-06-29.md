# Premarket Summary — Monday, June 29, 2026

> **🔴🔴🔴 CRITICAL: (1) GitHub Actions STILL DOWN — Day 15; 18+ missed sessions since June 18. (2) XLE exit: ALL 3 triggers active for 14+ days — SELL 100 XLE AT OPEN TODAY. (3) Iran ceasefire strained — June 26 drone attack, but MOU not formally collapsed. (4) Brent ~$72 — all price thresholds breached. (5) Markets opening GREEN: S&P futures +0.8%, Nasdaq +1.2%.**

---

## Header

| Item | Value |
|---|---|
| **API status** | UNAVAILABLE — Alpaca paper API unreachable from this environment |
| **Last confirmed equity** | $102,108.69 (exec_eod_2026-06-18 — **11 trading sessions stale**) |
| **Market context** | S&P 500 futures +0.8%, Nasdaq 100 futures +1.2% — positive open after Iran de-escalation over weekend |
| **Most recent authoritative file** | eod_2026-06-26.md |

---

## Account Snapshot

> ⚠️ All figures from exec_eod_2026-06-18. GitHub Actions has not committed a bot run since June 18. 11 trading sessions stale. API unavailable — no live refresh possible.

| Metric | Value | Source |
|---|---|---|
| Equity | **⚠️ $102,108.69** | exec_eod_2026-06-18 — stale |
| Our return (inception) | **⚠️ +2.11%** | Unconfirmed |
| SPY price at last confirmed | $748.46 | June 18 EOD |
| Options BP remaining | **⚠️ $73,470.00** | Layer 2 FLAT |

---

## Current Positions

**Layer 1 — Core ETFs (all at June 18 target; bot offline 11 sessions, drift undetected):**

| Symbol | Shares | Target | Est. Close (Jun 26) | Status |
|---|---|---|---|---|
| QQQ | 50 | 50 | ~$712 | At target — AI selloff from PCE + OpenAI IPO delay |
| SPY | 13 | 13 | ~$737 | At target |
| JETS | 80 | 80 | ~$33.15 | At target — $2.54 gap to $35.69 trigger |
| **XLE** | **100** | **EXIT** | **~$53.98** | 🔴🔴🔴 **ALL 3 EXIT TRIGGERS ACTIVE — Day 14 — SELL TODAY** |
| SPCX | 15 | 15 | — | SpaceX IPO position; hold |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY pending bot resumption |

**Layer 2 — Open CSPs:**

**FLAT.** No open options positions. Bot has not run since June 18.

| Target | Status |
|---|---|
| NVDA $190P Aug21 | 🔴 DO NOT OPEN — NVDA closed $192.53 Jun 26; only $2.53 OTM. Wait for NVDA > $205. |
| AMZN $215P Aug21 | ⚠️ Acceptable cushion (~6% OTM at ~$227) — await bot resumption before opening |

**Layer 2b — QQQ Calls:** FLAT. QQQ call rationale weakened by hot PCE (4.1%) and OpenAI IPO delay to 2027. Hold off.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran MOU | ✅ **Signed June 17** (Islamabad Memorandum — 60-day ceasefire framework) |
| June 26 Drone Attack | 🔴 Iran fired 4 attack drones at Hormuz; 1 hit cargo ship upper deck. Trump: "foolish violation" |
| Ceasefire status | ⚠️ **STRAINED** — not formally collapsed; Trump statement implies Iran erred, not a deal-killer |
| Weekend development | US and Iran signaling de-escalation per June 29 premarket headlines; MOU remains in effect |
| **Brent crude today** | **~$72.00–$72.52** (down ~$1.83 from Jun 26 close of $73.85; resumed decline) |
| Distance from $90 trigger | ~$17.50 below — 🔴 TRIGGERED |
| Distance from $85 trigger | ~$12.50 below — 🔴 TRIGGERED |
| Iran MOU trigger | Signed June 17 — 🔴 TRIGGERED |

**Key note:** The web search today shows Brent at ~$72 — this is BELOW both the $85 and $90 thresholds (not above them). All 3 XLE exit rules are simultaneously active. Weekend de-escalation rhetoric has not reversed the oil bear trend.

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status |
|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | ~$72 | 🔴 **TRIGGERED — Day 14+** |
| Brent ≤ $85 → exit all XLE | $85 | ~$72 | 🔴 **TRIGGERED — Day 14+** |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED — Day 14+** |
| JETS ≥ $35.69 (+30%) → close all 80 | $35.69 | ~$33.15 (Jun 26) | 🟢 Clear — ~$2.54 gap |
| Equity < $87,500 → halt new positions | $87,500 | ~$102K (stale) | 🟢 Estimated clear |

---

## Morning Priority Actions

1. **🔴 SELL 100 XLE AT MARKET — TODAY (first priority at 9:30 AM open)**
   All 3 manual exit triggers have been active for 14+ trading days. Brent declined further overnight to ~$72 (down from $73.85 Jun 26 close). Iran ceasefire strained but intact — no reversal of Brent bear thesis. Weekend headlines show de-escalation, not re-escalation. Execute exit. Estimated proceeds: 100 × ~$54 ≈ **~$5,400 cash freed**.
   > ⚠️ Watch Iran headlines in the 30 min before open — if Brent spikes >+5% overnight (above ~$78), consider a limit order instead of straight market. At current ~$72, a market sell is appropriate.

2. **🔴 FIX GITHUB ACTIONS — TODAY (critical)**
   Day 15 offline. Go to `github.com/TekMage/paper-trading/actions`. Check `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`. Without the bot, no CSP entries, no auto-closes, no rebalancing. Every day offline is missed Layer 2 premium. This is the single highest-leverage fix available.

3. **⚠️ Do NOT open NVDA $190P** — $192.53 Friday close is only $2.53 OTM (~1.3%). Normal intraday movement can put this in-the-money. Wait for NVDA to recover above $205+ before any CSP entry. Consider adjusting bot target to $180P or $185P Aug21 when bot resumes.

---

## Risk Flags

| Flag | Severity | Detail |
|---|---|---|
| GitHub Actions offline — Day 15 | 🔴 CRITICAL | 18+ missed sessions; no bot execution, no exec_ files, equity figure 11 sessions stale |
| XLE overdue exit | 🔴 CRITICAL | All 3 triggers active 14+ days; ~$5,400 capital idle in exiting position |
| NVDA $190P strike too close | 🔴 HIGH | $192.53 close — $2.53 OTM only. If bot resumes and tries to open this CSP, human override needed |
| Iran ceasefire strained | 🟡 MEDIUM | June 26 drone attack is first kinetic violation since MOU. Weekend de-escalation holds for now; risk of flare-up remains |
| PCE 4.1% hot — macro headwind | 🟡 MEDIUM | Hawkish macro reduces rate-cut timeline; headwind for QQQ, NVDA, growth names. CSP strikes should be more conservative |
| OpenAI IPO delayed to 2027 | 🟡 MEDIUM | AI sentiment headwind; weakens QQQ call-buying rationale through at least July |
| Account figures 11 sessions stale | 🟡 MEDIUM | Actual equity unknown; positions may have drifted. SPY/QQQ/JETS/XLE prices all from June 26 estimates |
| XLY FORCE_CLOSE pending | 🟡 LOW | XLY close queued in bot but bot offline; manual close may be warranted if bot remains down |

---

*Sources: [Iran MOU signed — NBC News](https://www.nbcnews.com/world/iran/strait-hormuz-reopen-us-lift-iran-sanctions-14-point-deal-seeking-end-rcna350513) · [Iran/US ceasefire — Al Jazeera](https://www.aljazeera.com/news/2026/6/17/iran-confirms-that-mou-has-been-signed-electronically-by-both-sides) · [Brent crude June 29 — HDFC Sky](https://hdfcsky.com/news/brent-crude-oil-price-today-june-29-2026-headline-oil-climbs-as-u-s-iran-trade-blows-despite-ceasefire-brent-tops-72) · [Stock market futures June 29 — Yahoo Finance](https://finance.yahoo.com/markets/stocks/live/stock-market-today-monday-june-29-224230573.html) · eod_2026-06-26.md (authoritative EOD file)*
