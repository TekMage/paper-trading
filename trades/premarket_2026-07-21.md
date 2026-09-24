# Premarket Summary — 2026-07-21 (Tuesday)

**Generated:** Pre-market (~9:00 AM ET)  
**API status:** UNAVAILABLE (live curl call confirmed failed)  
**Last confirmed equity:** $102,108.69 (exec_eod_2026-06-18 — GitHub Actions down Day 35+)  
**Market context:** S&P 500 futures +0.45% premarket; chip stocks rallying; Brent crude ~$89.93 pre-market (approaching $90 XLE trim trigger); GOOGL + TSLA earnings Wednesday AH

---

## ⚠️ GitHub Actions — DOWN Day 35 (Confirmed)

GitHub Actions workflows (`trading-open.yml`, `trading-midday.yml`, `trading-eod.yml`) confirmed disabled/manually disabled. No exec files generated since June 18 (~22 trading sessions unconfirmed). **Last confirmed bot action:** June 18 open — submitted AMZN $220P close @ $2.20 (unfilled; GTC canceled EOD June 18).

**Highest-leverage action:** Re-enable GitHub Actions at `github.com/TekMage/paper-trading/actions` before 9:30 AM ET today → bot runs open session automatically (XLY FORCE_CLOSE, Layer 1 rebalance, new NVDA CSP evaluation).

---

## Account Snapshot (confirmed June 18 — 22 sessions stale)

| Metric | Value | Note |
|---|---|---|
| **Equity** | **$102,108.69** | Stale — last exec_eod June 18; actual equity unknown |
| **Return (inception)** | **+2.11%** | vs $100,000 starting capital May 7, 2026 |
| **SPY benchmark (inception)** | **~+1.02% est.** | SPY ~$739 close Jul 20 vs $731.53 inception |
| **Options BP remaining** | **$73,470.00** | Confirmed June 18; Layer 2 flat since then |
| **Account floor** | **$87,500** | Bot halts new positions below this |

---

## Current Positions (from eod_2026-07-20.md + June 18 exec_eod)

### Layer 1 — Core ETFs

| Symbol | Shares | Target | Price (Jul 20 close) | Notes |
|---|---|---|---|---|
| **QQQ** | 50 (est.) | 50 | ~$745 est. | At target; Nasdaq faded Monday from +1% open to slight negative |
| **SPY** | 13 (est.) | 13 | ~$739 est. | At target |
| **JETS** | 80 (est.) | 80 | **$30.57** | Confirmed close Jul 20; $35.69 trigger $5.12 away |
| **XLE** | 100 (est.) | **EXIT** | ~$57–58 est. | 🔴 $90 XLE trim trigger ACTIVE; $85 exit-all watch; MOU defunct |
| **SPCX** | 15 (est.) | 15 | ~$132–134 est. | SpaceX; Starship overhang remains |
| **XLY** | Unknown | **0 (FORCE_CLOSE)** | — | 🔴 FORCE_CLOSE unexecuted 35+ sessions |

### Layer 2 — Open CSPs

**FLAT since June 18.** No confirmed open options positions.

| Target | Strike / Expiry | Underlying (Jul 20) | Status |
|---|---|---|---|
| **NVDA** | $185P Aug21/Sep19 | $203.81 | ✅ Clean window — $190P Jul18 expired worthless July 18 (not held); new entry queued; **hard block until bot resumes** |
| **AMZN** | $215P Aug21 | ~$249.65 (post-mkt) | ⛔ Hard block — Q2 earnings ~July 30 (6 trading sessions away); ~14.1% OTM; solid cushion |

---

## Iran / Oil Status

| Item | Status (Pre-market Jul 21) |
|---|---|
| **June 17 MOU** | ❌ **DEFUNCT** — Trump declared ceasefire over July 8 after resumed US airstrikes |
| **Military situation** | ⚠️ **ACTIVE CONFLICT** — US conducting strikes 10+ consecutive nights on Iranian assets; Iran disabling tankers attempting Hormuz transit; mutual exchange ongoing |
| **Hormuz status** | 🔴 **DISRUPTED** — Tanker traffic severely curtailed; US naval blockade active on Iranian ports |
| **Brent crude (Jul 21 pre-market)** | **~$89.93/bbl** — up from $88.59 Monday close; Jul 20 saw intraday spike to $91.41 |
| **vs $90 trim trigger** | 🔴 **~$0.07 below trigger** — Brent essentially AT the $90 level pre-market |
| **vs $85 exit-all trigger** | ~$4.93 above (was triggered Jul 15–16; recovered since) |
| **New MOU today** | ❌ None — mediators pushing for 10-day ceasefire; no deal announced |

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **ACTIVE — Brent $89.93 pre-market, essentially at trigger (Day 35+ unexecuted)** |
| **Brent ≤ $85 → exit all XLE at market** | $85/bbl | ⚠️ **Watch** — $4.93 above; intraday moves of $3–5 are now routine given Iran volatility |
| **Iran MOU signed → sell 60 XLE immediately** | Formal new MOU | ✅ Not triggered — June 17 MOU defunct; no new deal |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69 | ✅ Not triggered — JETS $30.57; $5.12 away |

---

## Morning Priority Actions (Human Required)

1. **🔴 Re-enable GitHub Actions BEFORE 9:30 AM ET** — Day 35. Navigate to `github.com/TekMage/paper-trading/actions`, re-enable all 3 workflows. Bot will auto-execute XLY FORCE_CLOSE, Layer 1 rebalance, and evaluate NVDA CSP at open. Single highest-leverage action.

2. **🔴 Brent $89.93 pre-market — watch $90 XLE trim trigger** — The $90 trim-30-XLE rule is active and has been for 35+ sessions. If Brent trades at or below $90 at open: sell 30 XLE at market via Alpaca paper dashboard. Monday saw a $91.41 intraday spike then retreat — be ready for similar volatility today.

3. **🟡 Watch Brent for $85 exit-all** — $4.93 above; Brent moved $3+ in a single session on Monday. Any Iran escalation headline (tanker attack, Hormuz closure announcement) could gap Brent down through $85. If triggered: sell all 100 XLE immediately.

4. **🟡 GOOGL + TSLA earnings Wednesday AH** — Alphabet AI capex commentary is a direct NVDA/QQQ driver. Expect QQQ to drift today on positioning. Watch for elevated QQQ call buying as a bullish signal for NVDA CSP entry timing.

5. **🟡 XLY manual close** — FORCE_CLOSE pending 35+ sessions. Execute via Alpaca dashboard if bot not restored before 9:30 AM ET.

---

## Semiconductor / AI Context

- **NVDA:** $203.81 Monday close; Philadelphia Semiconductor Index +47% YTD; chip stocks led pre-market (+0.4% S&P futures)
- **Market rotation:** AI semiconductor market projected $500B in generative AI chip revenue; AMD +186% Q2 2026 on Meta $60B MI400 deal
- **NVDA CSP window:** $185P Aug21/Sep19, ~10% OTM vs $203.81 — clean setup; queued for first bot session on Actions resumption

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions DOWN Day 35** | ~22 missed trading sessions; $0 Layer 2 premium collected; XLY FORCE_CLOSE unexecuted; strategy paralyzed |
| 🔴 **$90 XLE trim ACTIVE** | Sell-30-XLE rule firing continuously; Brent $89.93 pre-market = rule active at open |
| ⚠️ **Brent $4.93 above $85 exit-all** | Monday's intraday range was $87.72–$91.41 ($3.69 swing); $85 trigger can activate intraday on one headline |
| ⚠️ **Iran conflict — no resolution visible** | Active US airstrikes + Iranian retaliation + Hormuz disruption; gas prices $4.00/gallon national avg |
| ⚠️ **GOOGL + TSLA earnings Wednesday AH** | Biggest QQQ catalyst of the week; miss risk on TSLA margin; Alphabet AI capex = NVDA read-through |
| ⚠️ **JETS fuel headwind** | JETS $30.57; Brent $89.93 is meaningful fuel cost pressure for airlines |
| ⚠️ **XLY FORCE_CLOSE unexecuted** | 35+ sessions; still holding an exit-targeted position |
| 🟢 **Options BP preserved** | $73,470 confirmed June 18; no positions since; ready to deploy |
| 🟢 **NVDA $190P Jul18 expired worthless** | Confirmed not held; clean handoff to Aug21/Sep19 window |
| 🟢 **AMZN solid cushion** | ~$249.65 vs $215P target; ~14.1% OTM; strong buffer into July 30 earnings |

---

*Sources: eod_2026-07-20.md · exec_eod_2026-06-18.md · Alpaca paper API (UNAVAILABLE) · Fortune/Yahoo Finance Brent $89.93 Jul 21 pre-market · Yahoo Finance S&P 500 futures +0.45% Jul 21 · Al Jazeera / CBS Iran conflict updates · Intellectia AI semiconductor July 2026 analysis*
