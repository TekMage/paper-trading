# Premarket Summary — Tuesday, July 28, 2026

> **Generated: ~9:00 AM ET** | Market opens in ~30 minutes

---

## Header

- **API status:** UNAVAILABLE — curl to paper-api.alpaca.markets returned no data (consistent with all sessions since June 19)
- **Last confirmed equity:** $102,108.69 (June 18 EOD exec file — authoritative; ~28+ trading sessions unconfirmed)
- **Market context:** Chip sell-off extends into Tuesday; Nasdaq futures -1%, S&P flat/slightly down; Dow futures +0.6%; Brent crude well below $90 trigger — **$85 exit trigger now in active watch range**

---

## Account Snapshot

> All figures from `exec_eod_2026-06-18.md` — last authoritative confirmed state. GitHub Actions DOWN — **Day 41**.

| Metric | Value | Source |
|---|---|---|
| **Equity** | $102,108.69 | exec_eod_2026-06-18.md (confirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026 |
| **Options BP remaining** | $73,470.00 | exec_eod_2026-06-18.md |
| **Account floor** | $87,500.00 | Bot halts new positions below this |
| **GitHub Actions** | ❌ DOWN — **Day 41** | All 3 workflows `disabled_manually` since June 19 |
| **Last confirmed bot action** | June 18 open | AMZN 220P close order (unfilled; expired worthless) |

> Actual current equity is unknown. ~28 unconfirmed trading sessions since June 18.

---

## Current Positions (from exec_eod_2026-06-18 + EOD Jul 27 context)

### Layer 1 — Core ETFs (GitHub Actions maintains these — but Actions DOWN Day 41)

| Symbol | Shares (Est.) | Target | Status |
|---|---|---|---|
| **QQQ** | 50 (est.) | 50 | At target; Nasdaq futures -1% premarket — chip drag |
| **SPY** | 13 (est.) | 13 | At target; S&P futures -0.1% |
| **JETS** | 80 (est.) | 80 | At target; Brent-driven fuel relief continues; $35.69 trigger ~$5–6 away |
| **XLE** | 100 (est.) | EXIT | 🔴 **FORCE_CLOSE unexecuted — Day 41; $90 trim trigger breached yesterday; see below** |
| **SPCX** | 15 (est.) | 15 | No confirmed close; SpaceX ETF held |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 41; strategy violation |

### Layer 2 — Open CSPs (FLAT since June 18)

**No confirmed open options positions.** Bot has been offline 41 days; NVDA $190P Jul18 expired worthless.

| Target | Strike / Expiry | Underlying Est. (Jul 27 close) | Status |
|---|---|---|---|
| **NVDA CSP** | $190P Aug21 | ~$203–207 est. | ⚠️ NVDA hit intraday low $195.47 yesterday; further drop premarket (-1%+); Aug21 DTE ~25 — window at limit; no open position; entry requires bot re-enable |
| **AMZN CSP** | $215P (post-earnings) | $241.76 (Jul 27 close) | ⛔ Hard block — earnings July 30 AH; reassess strike Wednesday night |

---

## Iran / Oil Status

| Item | Status |
|---|---|
| **June 17 MOU framework** | ⚠️ Under stress — conflict resumed July 6–7 (Iran struck 3 commercial vessels); informal fighting pause as of Jul 27 weekend; Oman mediating Hormuz transit talks; no new formal agreement signed |
| **New formal MOU (July 28)** | ❌ NOT signed — informal ceasefire holds; PBS/BBC "initial deal" language refers to ongoing negotiations, not a signed agreement |
| **XLE MOU trigger (sell 60 XLE)** | ❌ NOT active — no new formal MOU signed |
| **Brent crude (Jul 27 settle)** | ~$90.28/bbl — intraday low was $88.81 (1:37 PM ET); $90 trim trigger breached intraday |
| **Brent crude (Jul 28 premarket)** | 🔴 **~$84.99–$87.73 range** — multiple sources; well below $90; **some sources show ~$84.99, within $0.01 of the $85 ALL-OUT trigger** |
| **vs $90 XLE trim trigger** | 🔴 **ACTIVE** — Brent clearly below $90; sell 30 XLE required (if not yet done from yesterday) |
| **vs $85 XLE exit trigger** | 🔴 **CRITICAL WATCH** — lowest reading $84.99; settle/open confirmation needed; if any print ≤ $85.00, sell ALL remaining XLE immediately |

**Oil context:** Brent has collapsed ~12–15% over the past two sessions on US-Iran informal ceasefire optimism. Yesterday's intraday low of $88.81 triggered the $90 rule (sell 30 XLE). Today's premarket range includes prints at or below $85, meaning the full-exit trigger ($85 = sell all XLE) may fire at or shortly after the 9:30 AM open. Treat this as the **top manual priority** of the session.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🔴 **TRIGGERED** — breached intraday Jul 27 ($88.81); sell 30 XLE MANUAL ACTION REQUIRED if not yet executed |
| **Brent ≤ $85 → exit ALL XLE at market** | $85/bbl | 🔴 **CRITICAL WATCH** — premarket readings as low as $84.99; confirm at 9:30 AM open; if triggered, sell all remaining XLE (100 or 70 shares depending on whether 30 were sold yesterday) |
| **Iran MOU formally signed → sell 60 XLE immediately** | New formal MOU | ❌ NOT triggered — informal fighting pause only |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69/share | ❌ NOT triggered — JETS ~$30 est.; $5–6 below trigger; oil-driven fuel relief positive but insufficient |

---

## Morning Priority Actions

**1. 🔴 CONFIRM BRENT AT 9:30 AM — DOUBLE TRIGGER SITUATION**
> Check Brent at the 9:30 AM open. Any print ≤ $90 = sell 30 XLE at market (if not done from yesterday). Any print ≤ $85 = sell ALL remaining XLE immediately. Premarket readings include $84.99 — both triggers may be active simultaneously. Open Alpaca paper dashboard → sell XLE at market. MANUAL — bot offline.

**2. 🔴 RE-ENABLE GITHUB ACTIONS — DAY 41 CRITICAL**
> Navigate to `github.com/TekMage/paper-trading/actions` and re-enable all 3 workflows before or immediately at 9:30 AM ET. This is the single highest-leverage action: restores automatic XLY FORCE_CLOSE, Layer 1 rebalance, and NVDA CSP evaluation. 41 days of missed sessions = $0 Layer 2 premium; XLY FORCE_CLOSE unexecuted.

**3. 🟡 NVDA PREMARKET WATCH — APPROACHING $190P STRIKE**
> NVDA down another ~1%+ premarket after yesterday's -5.5%. Chip sell-off extending (Korean memory, AI financing concerns). At yesterday's low of $195.47, the $190P Aug21 target was only $5.47 OTM. Further premarket pressure puts the strike at risk. Monitor NVDA at open; if bot is re-enabled today, assess whether $185P or lower strike is more appropriate given proximity.

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **Brent $85 exit trigger at risk** | Premarket low readings ~$84.99; if $85 level breaks at open, ALL XLE must be sold immediately (manual — bot offline) |
| 🔴 **$90 trim trigger unexecuted from yesterday** | Brent breached $88.81 intraday Jul 27; 30 XLE sell flagged as required manual action in midday report; status unknown — no API confirmation |
| 🔴 **GitHub Actions Day 41** | ~28 missed sessions; $0 Layer 2 premium; XLY FORCE_CLOSE unexecuted; NVDA DTE window expiring |
| 🔴 **XLY FORCE_CLOSE Day 41** | Manual close or bot resumption required; strategy violation ongoing |
| ⚠️ **NVDA chip sell-off extending** | NVDA -1%+ premarket after -5.5% yesterday; $190P Aug21 CSP target strike now ~$5–10 OTM depending on open; Aug21 DTE ~25 — window closing today |
| ⚠️ **Nasdaq futures -1% premarket** | Chip rout: NVDA, AMD (-5.17% yesterday), MU, MRVL all declining; AI circular financing (NVDA $250B OpenAI backstop) and Korean memory sell-off driving tech weakness |
| ⚠️ **Big Tech earnings triple-header July 30 AH** | MSFT + META + AMZN all reporting after close Wednesday; maximum volatility event for QQQ; AMZN hard block on $215P CSP until post-earnings |
| ⚠️ **Fed rate decision this week** | Rate path uncertainty; cross-asset volatility risk |
| ⚠️ **Iran ceasefire fragile** | June 17 MOU under stress (conflict resumed July 6–7); informal pause holds for now; any breakdown = Brent spikes back toward $95–100; any formalization = more Brent pressure, $85 trigger more active |
| 🟢 **Options BP preserved ($73,470)** | Dry powder intact since June 18; ready to deploy Layer 2 when Actions re-enabled |
| 🟢 **AMZN $215P at ~12.4% OTM** | $241.76 at Jul 27 close; sufficient cushion; hard block appropriate pre-earnings |
| 🟢 **JETS fuel relief ongoing** | Brent collapse = structural tailwind for airline fuel costs; JETS ~$30; $35.69 trigger $5–6 away |

---

## Market Context — Premarket July 28

| Index / Asset | Premarket Signal | Note |
|---|---|---|
| **S&P 500 futures** | -0.1% | Flat; chip drag offset by Dow/non-tech resilience |
| **Nasdaq 100 futures** | ~-1% | Chip sell-off extends; Korean memory, AI financing fears |
| **Dow futures** | +0.6% | Less chip exposure; energy/industrials resilient |
| **Brent crude** | **~$84.99–$87.73** | 🔴 Well below $90 trigger; $85 exit trigger in range |
| **NVDA** | ~-1% premarket | After -4.99% Jul 27; analysts say reaction "overdone" but momentum negative |
| **AMD** | ~-3%+ premarket | Extending -5.17% Jul 27 decline |
| **AMZN** | Flat/slightly down | Holding ahead of Jul 30 AH earnings |

---

*Sources: eod_2026-07-27.md · exec_eod_2026-06-18.md · [Vantage Markets — Brent Jul 28](https://www.vantagemarkets.com/market-analysis/crude-oil-prices-today-brent-wti-july-28-2026/) · [Fortune — Brent Jul 28](https://fortune.com/article/price-of-oil-07-28-2026/) · [Bloomberg — S&P futures Jul 28](https://www.bloomberg.com/news/articles/2026-07-28/s-p-500-futures-muted-as-semiconductors-drop-earnings-roll-in) · [TheStreet — Market Today Jul 28](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-july-28-2026) · [Yahoo Finance — NVDA chip rout Jul 28](https://finance.yahoo.com/markets/stocks/articles/nvda-chip-stocks-extend-rout-094902224.html) · [Invezz — Chip stocks plunge Jul 28](https://invezz.com/news/2026/07/28/why-are-micron-nvidia-and-amd-stocks-plunging-before-wall-street-opens-today/) · [PBS — Iran initial deal](https://www.pbs.org/newshour/world/iran-and-u-s-reach-an-initial-deal-to-extend-the-ceasefire-and-open-the-strait-of-hormuz-but-challenges-remain) · [Wikipedia — 2026 Iran war ceasefire](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire) · GitHub Actions (all 3 workflows disabled_manually — Day 41) · Alpaca API UNAVAILABLE · ~9:00 AM ET*
