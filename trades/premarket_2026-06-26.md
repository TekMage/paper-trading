# Pre-Market Summary — Friday, June 26, 2026

> **🔴🔴 CRITICAL: (1) XLE exit — ALL 3 TRIGGERS ACTIVE Day 14 — manual sell 100 XLE immediately at open. (2) GitHub Actions DOWN — 14th consecutive missed session. (3) PCE came in HOT (4.1% headline / 3.4% core) — do NOT open any CSPs until market settles today. (4) S&P 500 futures down ~0.37% premarket; tech selloff continuing.**

---

## Header

| Item | Value |
|---|---|
| API status | **UNAVAILABLE** — Alpaca paper API unreachable from this environment (consistent with prior sessions) |
| Last confirmed equity | **$102,108.69** — from `exec_eod_2026-06-18` (6 trading sessions stale) |
| Last confirmed Options BP | **$73,470.00** — same source; Layer 2 FLAT since June 18 |
| Market context | PCE inflation hot at 4.1%; futures down; Mag7 tech selloff Day 5; Brent ~$73–74 well below XLE thresholds |
| GitHub Actions status | **DOWN** — last run June 18 at 21:39 UTC; 14 consecutive missed sessions confirmed via Actions API |

---

## Account Snapshot

> ⚠️ All figures from `exec_eod_2026-06-18` — 6 trading sessions stale. No bot execution since June 18 EOD.

| Metric | Value | Notes |
|---|---|---|
| Equity | $102,108.69 | June 18 baseline — unconfirmed since |
| Our return (inception) | +2.11% | Unconfirmed since June 18 |
| SPY benchmark price | $748.46 | June 18 reference |
| SPY return vs benchmark | +2.31% | June 18 reference |
| Alpha | -0.21% | June 18 reference |
| Options BP | $73,470.00 | Layer 2 FLAT; no open options |
| Account floor | $87,500.00 | Bot halts new positions below this |
| Distance from floor | ~$14,609 | Estimated; actual equity unknown |

---

## Current Positions (exec_eod_2026-06-18 + premarket data)

### Layer 1 — Core ETFs (all assumed at June 18 targets; no bot rebalancing for 6 sessions)

| Symbol | Shares | Target | Premarket Price | Notes |
|---|---|---|---|---|
| QQQ | 50 | 50 | — | Tech selloff headwind; futures ~-0.37% |
| SPY | 13 | 13 | — | Near target |
| JETS | 80 | 80 | ~$33.50 | Well below $35.69 close trigger (~6% gap) |
| **XLE** | **100** | **EXIT** | **~$53–54** | 🔴🔴🔴 **ALL 3 EXIT TRIGGERS ACTIVE — Day 14 — SELL NOW** |
| SPCX | 15 | 15 | — | SpaceX IPO position; hold |
| XLY | Closing | 0 | — | FORCE_CLOSE_EQUITY pending; awaiting bot resumption |

### Layer 2 — Open CSPs

**Layer 2 is FLAT.** No open options positions. Bot has not run since June 18; CSP entry on hold pending:
1. GitHub Actions fix
2. PCE settling (data released June 25 — hot print; let market digest)

| Target | Strike | Expiry | DTE Today | Underlying (premarket) | OTM % | Status |
|---|---|---|---|---|---|---|
| NVDA $190P | Aug 21 | 2026-08-21 | ~56 DTE | ~$192.46 | ~1.3% OTM | FLAT — NVDA dipped below $195; $190P now only ~1.3% OTM — wait for recovery above $205 |
| AMZN $215P | Aug 21 | 2026-08-21 | ~56 DTE | ~$227.67 | ~5.6% OTM | FLAT — acceptable OTM cushion; do not open until Actions fixed and PCE settled |

**Note on NVDA:** At $192.46 premarket, the $190P is dangerously close to ATM (~1.3% OTM). Do NOT open this CSP today unless NVDA recovers above $200–205. The strategy requires meaningful OTM cushion.

### Layer 2b — QQQ Calls

FLAT. Bot not running. Entry deferred.

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran-US MOU | ✅ **SIGNED June 17, 2026** — 14-point framework; 60-day ceasefire; Hormuz open |
| MOU trigger | 🔴 **TRIGGERED — Day 14 — sell 60 XLE at market (manual)** |
| Strait of Hormuz | ✅ OPEN — tanker traffic surging; US 60-day Iran oil supply licence active |
| Brent crude (est.) | **~$73–74/barrel** (Jun 25 close ~$73.43; Jun 26 premarket consistent) |
| vs $90 trim trigger | ~$16–17 below — 🔴 **TRIGGERED Day 14** |
| vs $85 exit trigger | ~$11–12 below — 🔴 **TRIGGERED Day 14** |
| Switzerland nuclear talks | Ongoing; no new breakthrough; not a near-term reversal catalyst |
| Oil bear case | Fully intact — Iranian crude entering market, Hormuz traffic normalizing |

---

## Manual Triggers to Monitor Today

| Rule | Threshold | Current | Status | Days Active |
|---|---|---|---|---|
| Brent ≤ $90 → sell 30 XLE | $90 | ~$73–74 | 🔴 **TRIGGERED** | Day 14 |
| Brent ≤ $85 → exit ALL XLE | $85 | ~$73–74 | 🔴 **TRIGGERED** | Day 14 |
| Iran MOU signed → sell 60 XLE | — | Signed Jun 17 | 🔴 **TRIGGERED** | Day 14 |
| JETS ≥ $35.69 → close all 80 | $35.69 | ~$33.50 | 🟢 Clear — ~$2.19 gap (~6.5%) | — |
| Equity < $87,500 → halt new | $87,500 | ~$102K (stale) | 🟢 Estimated clear | — |

---

## Morning Priority Actions

**1. 🔴 CRITICAL — Sell all 100 XLE at market (execute manually via Alpaca paper UI)**
All 3 exit triggers have been simultaneously active for 14 trading days. Brent is ~$17 below the top trigger and ~$12 below the full exit trigger. XLE has been declining with oil; every day of delay is additional unrealized loss. Proceeds ~$5,300–5,400. Execute immediately at open: Alpaca paper UI → Trade → XLE → Market Sell → 100 shares.

**2. 🔴 CRITICAL — Fix GitHub Actions (14 missed sessions)**
Go to github.com/TekMage/paper-trading/actions. Check `trading-open.yml`, `trading-midday.yml`, `trading-eod.yml` run history for failure reason. Bot has been completely offline since June 18 EOD. Layer 2 has been FLAT for 5+ weeks. Without bot execution, no CSP entry, no rebalancing, no automated triggers.

**3. ⚠️ HIGH — Do NOT open any CSPs today**
PCE came in hot (4.1% headline / 3.4% core, released June 25) — highest in 3 years. S&P futures are down premarket. NVDA is at $192.46 — dangerously close to the $190 CSP strike. Let the market settle post-PCE before evaluating CSP entry next week.

---

## Risk Flags

- 🔴 **XLE position decay** — 100 shares × ~$53.50 = ~$5,350 held in a position with all 3 exit triggers active for 14 days. Oil structural bear case (Iranian supply, Hormuz open) intact; no reversal catalyst.
- 🔴 **GitHub Actions outage** — No automated execution for 14 sessions; bot cannot rebalance Layer 1 or enter Layer 2 CSPs. XLY close (FORCE_CLOSE_EQUITY) also stalled.
- ⚠️ **NVDA at $192.46 premarket** — Only ~1.3% above $190P target strike. CSP entry would be reckless today. Wait for $200–205 recovery.
- ⚠️ **Hot PCE macro** — 4.1% headline PCE is a hawkish Fed signal. QQQ likely to face pressure. Not an immediate portfolio emergency (QQQ target long) but the macro tailwind for the June sprint is deteriorating.
- ⚠️ **Tech selloff Day 5** — AAPL/MSFT price hike fallout (hardware cost squeeze from AI memory shortage) dragging Nasdaq. Mag7 weakness is a QQQ headwind but not a trigger for any strategy change.
- ⚠️ **Equity figure 6 sessions stale** — Actual equity unknown; estimated ~$102K but XLE losses since June 18 (XLE was ~$54–55 then vs ~$53–54 now) create modest headwind. Account floor at $87,500 still has large buffer.
- ℹ️ **Aug21 CSP window open** — 56 DTE today; still 31+ trading days before window closes. No cliff yet but bot must be fixed soon.

---

*Sources: exec_eod_2026-06-18 (account state) · eod_2026-06-25.md (positions, XLE trigger history) · GitHub Actions API (workflow run history) · PCE inflation May 2026 — CBS News / CNBC · Brent crude — Trading Economics · NVDA/AMZN premarket — CNBC/Public.com · S&P 500 futures — TheStreet/CNBC*
