# Premarket Summary — Thursday, July 30, 2026

> **Generated: ~9:00 AM ET** | Market opens in ~30 minutes

---

## Header

- **API status:** UNAVAILABLE — curl to paper-api.alpaca.markets returned no data (consistent since June 19)
- **Last confirmed equity:** $102,108.69 (June 18 EOD — authoritative; ~30 unconfirmed trading sessions)
- **Market context:** MSFT Q4 blowout (Azure >$100B, +8% premarket) lifts futures; US air strikes on Iran overnight push Brent above $90; AMZN + META report AH tonight — peak volatility event

---

## Account Snapshot

> All figures from `exec_eod_2026-06-18.md` — last authoritative confirmed state. GitHub Actions DOWN — **Day 43**.

| Metric | Value | Source |
|---|---|---|
| **Equity** | $102,108.69 | exec_eod_2026-06-18.md (confirmed) |
| **Return (inception)** | +2.11% | vs $100,000 starting capital May 7, 2026 |
| **Options BP remaining** | $73,470.00 | exec_eod_2026-06-18.md |
| **Account floor** | $87,500.00 | Bot halts new positions below this |
| **GitHub Actions** | ❌ DOWN — **Day 43** | All 3 workflows disabled since June 19 |
| **API status** | ❌ UNAVAILABLE | Consistent since June 19 |

> Actual current equity is unknown. ~30 unconfirmed trading sessions since June 18.

---

## Current Positions (from exec_eod_2026-06-18 + prior premarket context)

### Layer 1 — Core ETFs (GitHub Actions maintains these — but Actions DOWN Day 43)

| Symbol | Shares (Est.) | Target | Status |
|---|---|---|---|
| **QQQ** | 50 (est.) | 50 | At target; Nasdaq rebounding on MSFT beat premarket |
| **SPY** | 13 (est.) | 13 | At target; S&P futures +0.4–0.7% |
| **JETS** | 80 (est.) | 80 | At target; $31.86 yesterday; trigger at $35.69 (+12%) |
| **XLE** | 100 (est.) | EXIT | 🔴 FORCE_CLOSE unexecuted — Day 43; see oil section below |
| **SPCX** | 15 (est.) | 15 | SpaceX ETF held |
| **XLY** | Unknown | 0 (FORCE_CLOSE) | 🔴 FORCE_CLOSE unexecuted — Day 43; strategy violation ongoing |

### Layer 2 — Open CSPs

**No confirmed open options positions.** Bot offline Day 43; NVDA $190P Jul18 expired worthless.

| Target | Strike / Expiry | Context | Status |
|---|---|---|---|
| **NVDA CSP** | $190P Aug21 | DTE = 22 days today (below OPT_DTE_MIN=25) | ⛔ Window closed for Aug21; next valid: Sep expiry |
| **AMZN CSP** | $215P / post-earnings | AMZN reports AH **tonight** | ⛔ Hard block until tomorrow morning post-earnings |

---

## Iran / Oil Status

| Item | Status |
|---|---|
| **New MOU signed overnight?** | ❌ NOT signed — no new formal agreement |
| **June 17 MOU status** | ⚠️ Under stress — conflict resumed July 6–7; informal ceasefire holds; Oman mediating |
| **US air strikes on Iran (Jul 30)** | 🔴 ACTIVE ESCALATION — US carried out fresh air strikes overnight; driving Brent surge |
| **Brent crude (Jul 30 premarket ~6:30 AM ET)** | **~$90–$92.65/bbl** — surged sharply from yesterday's $89.53; conflicting data points ($90.04 some sources, $92.65 Fortune) |
| **vs $90 XLE trim trigger** | 🟡 WATCH — Brent appears to be at or above $90 today on escalation; trigger was active yesterday ($89.53) and unexecuted; **at current price (~$90-$92) trigger condition NOT met but situation volatile** |
| **vs $85 XLE exit trigger** | 🟢 Not threatened — Brent well above $85 |

**Oil context:** Brent has surged above $90 today after overnight US air strikes against Iran, reversing yesterday's pattern where it sat at $89.53 (below the $90 trim trigger). This creates an unusual situation: the $90 trim trigger was technically met yesterday and went unexecuted again, but today's price spike removes the immediate trigger condition. With US military action now active, Brent volatility is extremely elevated — could rapidly swing back below $90 intraday. The XLE position may actually appreciate on this escalation. Monitor closely. The $90 trim trigger has now been "touched" on multiple days without execution across ~30 sessions.

---

## Manual Triggers to Monitor Today

| Trigger | Threshold | Status |
|---|---|---|
| **Brent ≤ $90 → sell 30 XLE at market** | $90/bbl | 🟡 WATCH — Brent elevated to ~$90-92 on air strike news; trigger was active yesterday ($89.53) and unexecuted; monitor intraday dips |
| **Brent ≤ $85 → exit ALL XLE at market** | $85/bbl | 🟢 Not triggered — well above $85 today |
| **Iran MOU signed → sell 60 XLE immediately** | New formal MOU | ❌ NOT triggered — US air strikes suggest escalation, not resolution |
| **JETS ≥ $35.69 → close all 80 JETS** | $35.69/share | ❌ NOT triggered — JETS $31.86; $3.83 (+12%) away |

---

## Morning Priority Actions

**1. 🔴 RE-ENABLE GITHUB ACTIONS — DAY 43 CRITICAL**
> Navigate to github.com/TekMage/paper-trading/actions and re-enable all 3 workflows before or at the 9:30 AM ET open. 43 days offline = $0 Layer 2 premium collected, XLY FORCE_CLOSE unexecuted, NVDA Aug21 DTE window expired. This is the single highest-leverage action available.

**2. 🟡 MONITOR BRENT INTRADAY — $90 TRIGGER WATCH**
> Brent at $90-92 premarket on US air strike news but highly volatile. If it dips back below $90 intraday, the trim trigger (sell 30 XLE) is active. With US escalation ongoing, this can move fast in either direction. Have the Alpaca paper dashboard open and ready. Note: if Brent stays above $90 on sustained escalation, XLE itself may be gaining value — this cuts both ways.

**3. 🟡 HOLD FOR AMZN + META EARNINGS AH TONIGHT — REASSESS FRIDAY**
> AMZN and META both report after the close today. Hard block on all options entry remains in effect. Full portfolio reassessment (QQQ calls, AMZN CSP strike selection, NVDA Sep expiry entry) should happen tomorrow morning after all Big Tech earnings are digested. MSFT blowout is a positive signal — cloud AI spending confirmed robust.

---

## Risk Flags

| Flag | Detail |
|---|---|
| 🔴 **GitHub Actions Day 43** | ~30 missed sessions; $0 Layer 2 premium collected; XLY/XLE FORCE_CLOSE unexecuted |
| 🔴 **US air strikes on Iran** | Fresh escalation overnight — Brent surge; Hormuz risk elevated; uncertain ceasefire status |
| 🔴 **XLY FORCE_CLOSE Day 43** | Strategy violation ongoing; manual close or bot resumption required |
| ⚠️ **Brent $90 trigger unresolved** | Met yesterday ($89.53), unexecuted again; today's air strike spike complicates the picture |
| ⚠️ **AMZN + META earnings AH tonight** | Maximum QQQ/Nasdaq volatility event; no options entry until tomorrow post-digestion |
| ⚠️ **NVDA Aug21 DTE window closed** | DTE = 22 (below OPT_DTE_MIN=25); Sep expiry is next valid entry window |
| ⚠️ **Chip sector recovery attempt** | AMD, Micron, SK Hynix bouncing after 3-day sell-off; NVDA ~$197; MSFT beat may provide sector tailwind |
| 🟢 **MSFT Q4 blowout — AI cloud confirmed** | Azure topped $100B annually; EPS $4.74 vs $4.25 est; MSFT +8% premarket; AI capex concerns easing |
| 🟢 **S&P 500 futures positive** | +0.4–0.7% premarket; MSFT-driven recovery after Wednesday's -1.52% session |
| 🟢 **Options BP preserved ($73,470)** | Dry powder intact since June 18; ready to deploy Layer 2 when Actions re-enabled |
| 🟢 **JETS well below trigger** | $31.86 vs $35.69 trigger; $3.83 (+12%) away; Brent surge could weigh on airlines |
| 🟢 **Brent above $85 — full exit not triggered** | No forced XLE liquidation required at current prices |

---

## Market Context — Premarket July 30

| Asset | Premarket | Note |
|---|---|---|
| **Brent crude** | **~$90–$92.65/bbl** | Surged on US air strikes against Iran overnight; was $89.53 yesterday |
| **S&P 500 futures** | **+0.4–0.7%** | MSFT blowout driving recovery; S&P closed -1.52% Wednesday |
| **MSFT** | **+8% premarket** | Q4: EPS $4.74 vs $4.25 est; Azure $100B+ annually; massive beat |
| **NVDA** | ~$197 range | Semiconductor complex attempting recovery; 3-day sell-off ending |
| **AMD** | Attempting recovery | Was -5.51% yesterday; bouncing with semiconductor complex |
| **AMZN** | Reports AH tonight | Hard block on CSP; reassess Friday |
| **META** | Reports AH tonight | QQQ maximum volatility event |
| **JETS** | $31.86 | Trigger at $35.69; Brent surge a headwind for airline fuel costs |

---

*Sources: exec_eod_2026-06-18.md · premarket_2026-07-29.md · [Fortune — Brent Jul 30](https://fortune.com/article/price-of-oil-07-30-2026/) · [Bloomberg — US Premarket Movers Jul 30](https://www.bloomberg.com/news/articles/2026-07-30/us-stock-futures-today-chipotle-crocs-meta-microsoft-starbucks) · [Yahoo Finance — S&P futures Jul 30](https://finance.yahoo.com/markets/live/stock-market-today-thursday-july-30-dow-sp-500-nasdaq-082255995.html) · [Yahoo Finance — MSFT Q4 earnings](https://finance.yahoo.com/technology/article/microsoft-beats-q4-expectations-as-azure-revenue-tops-100-billion-120144134.html) · [Yahoo Finance — Chip recovery attempt](https://finance.yahoo.com/technology/article/amd-micron-sk-hynix-climb-as-semiconductor-complex-attempt-recovery-133110868.html) · [ABC News — Iran MOU timeline](https://abcnews.com/Politics/us-iran-ceasefire-mou-broke-timeline/story?id=134622392) · Alpaca API UNAVAILABLE · ~9:00 AM ET*
