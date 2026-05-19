# Pre-Market Report — Tuesday, May 19, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment ("Host not in allowlist") — Day 13.
> Last confirmed equity: **exec_eod_2026-05-18 = $100,013.46** (SPY $738.30, Options BP $11,710.32).
> All prices sourced from web search. Verify positions at https://app.alpaca.markets/paper-trading

---

## ACCOUNT SNAPSHOT

| Metric | Value | Note |
|--------|-------|------|
| Last confirmed equity (May 18 EOD) | **$100,013.46** | exec_eod confirmed via GH Actions |
| Options BP | **$11,710.32** | Preserved for post-NVDA deployment |
| Premarket equity estimate | **~$99,900** | SPY -0.4% futures → L1 drag ~-$150 |
| Total return vs $100k start | **~+0.01%** (confirmed) → **~-0.11%** (est. PM) | |
| SPY premarket (est.) | **~$734** | From -0.4% S&P futures |
| SPY total return (from $731.53) | **~+0.34%** | |
| Alpha (cumulative, est.) | **~-0.45%** | Slightly narrowed from -0.91% (XLE lift) |
| Account vs $87,500 floor | **✅ OK — ~$12,400 cushion** | No halt triggered |

---

## CURRENT POSITIONS & OVERNIGHT P&L

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | May 18 EOD (est.) | Premarket May 19 | Overnight Δ | Unreal P&L vs Cost | Status |
|--------|-----|----------|--------------------|------------------|-------------|---------------------|--------|
| QQQ | 45 | $710.93 | ~$704.20 | **~$700 (-0.6%)** | **~-$189** | **~-$491 (-1.53%)** | 🔴 Below cost; Nasdaq soft; tech sell-off |
| SPY | 13 | $736.39 | ~$737.20 | **~$734 (-0.4%)** | **~-$42** | **~-$31 (-0.32%)** | 🟡 Near cost; S&P futures -0.4% |
| XLY | 40 | $117.00 | ~$117.50 | **~$117 (-0.4%)** | **~-$20** | **~+$0** | 🟡 Flat; consumer follows market |
| JETS | 80 | $27.45 | ~$25.35 | **~$25.50 (+0.6%)** | **~+$12** | **~-$156 (-7.1%)** | 🟡 Slight lift on Iran de-escalation signal |
| XLE | 100 | $56.70 | ~$60.45 | **~$61.00 (+0.9%)** | **~+$55** | **~+$430 (+7.5%)** | ✅ Brent $110.10; oil still elevated |
| **L1 Total** | | **~$54,120** | **~$54,046** | **~$53,862** | **~-$184** | | |

### Layer 2/2b — Cash-Secured Puts

| Symbol | Strike | Expiry | DTE | Stock Premarket | OTM% | Premium Sold | Est. Current Value | Status |
|--------|--------|--------|-----|-----------------|------|-------------|-------------------|--------|
| NVDA | $180 | Jun 18 '26 | **29** | **~$236 (+6.5%)** | **~31%** | $1.67 (confirmed) | **~$1.50–$2.50** | 🔴 **EARNINGS TOMORROW — BTC AT OPEN TODAY** |
| TSLA | $370 | Jun 20 '26 | 32 | **~$430 est.** | **~14%** | ~$11 (inferred) | **~$1.75–$2.25** | 🟢 Inferred open; theta working well |
| AMZN | $245 | Jun 20 '26 | 32 | **~$267 est.** | **~8.2%** | ~$5 (inferred) | **~$1.00–$1.50** | ✅ Inferred open; approaching 50% target |

---

## WATCHLIST SNAPSHOTS (Premarket May 19, 2026)

| Symbol | Premarket Est. | May 18 Close (est.) | Change | Note |
|--------|---------------|---------------------|--------|------|
| SPY | **~$734** | ~$737.20 | **-0.4%** | S&P futures -0.4%; tech sell-off drag |
| QQQ | **~$700** | ~$704.20 | **-0.6%** | Nasdaq futures weaker; NVDA pre-earnings caution |
| XLY | **~$117** | ~$117.50 | **-0.4%** | Consumer follows broad market |
| JETS | **~$25.50** | ~$25.35 | **+0.6%** | Iran de-escalation (Trump called off attack) |
| XLE | **~$61.00** | ~$60.45 | **+0.9%** | Brent $110.10 — oil re-elevated |
| IWM | **~$280** | ~$281 | **-0.4%** | Small caps follow S&P; rate headwind |
| NVDA | **~$236** | $220.58 | **+6.9%** | Pre-earnings positioning; **EARNINGS TOMORROW** |
| TSM | **~$408** | ~$404 | **+1.0%** | AI foundry; riding NVDA/chip sentiment |
| TSLA | **~$430** | ~$422.24 | **+1.8%** | Recovering; $370P now ~14% OTM — healthy |
| AMZN | **~$267** | $266.81 | **~flat** | AWS steady; $245P at 8.2% OTM |
| INTC | **~$107** | ~$107.43 | **~flat** | No catalyst; chips broadly soft |
| DRAM | **~$51** | ~$51.10 | **~flat** | AI memory basket; NVDA earnings gating |
| MU | **~$625** | ~$628 | **~-0.5%** | Memory soft pre-NVDA; watch post-earnings |
| AVGO | **~$425** | ~$423 | **~+0.5%** | Broadcom AI networking; chips muted |
| Brent Crude | **$110.10** | $107.71 | **+2.2%** | Re-elevated overnight; Iran uncertainty |
| WTI | **$102.90** | ~$103.50 | **-0.6%** | Fell 1.38%; slight divergence vs Brent |

---

## IRAN / GEOPOLITICAL STATUS

| Item | Status |
|------|--------|
| MOU signed? | ❌ **NO** |
| Ceasefire status | 🟡 **DE-ESCALATING — but fragile** |
| Key overnight development | 🟢 **Trump called off scheduled Tuesday attack on Iran** — citing Gulf leaders (Qatar, Saudi, UAE) requests; called negotiations "more serious" |
| NSC meeting (today May 19) | 🟡 Still happening — now **framed as contingency review, not imminent action** |
| Military stance | ⚠️ US military "prepared to go forward on a moment's notice" — option not removed |
| Ceasefire characterization | 🟡 "On life support" but Trump de-escalated attack threat; "serious negotiations" referenced |
| Iran nuclear concessions | ❌ Iran's latest proposal lacked nuclear concessions per Trump; sticking point remains |
| Hormuz status | 🔴 Still effectively blocked; Iran toll plan still in force |
| Brent crude | **$110.10/bbl** — re-elevated from $107.71 May 18 close; supply disruption premium intact |
| XLE exit trigger (Brent < $85) | ❌ NOT triggered — **HOLD XLE** (25+ dollars above threshold) |
| JETS thesis | 🟡 **Directionally improving** — Trump backed off attack; Hormuz path clearer diplomatically |

**Strategic implication:** Trump calling off the Tuesday attack is the most constructive Iran signal in weeks. The NSC meeting today is now being framed as contingency planning rather than authorization, which is bullish for the peace dividend trades (JETS, XLY). However: no MOU is signed, Hormuz remains blocked, and oil is re-elevated at $110. The peace timeline is moving in the right direction but nothing is confirmed. **Hold all positions, hold JETS, do not add exposure ahead of NVDA earnings tomorrow.**

---

## IV ENVIRONMENT CHECK

| Indicator | Status | Implication |
|-----------|--------|-------------|
| NVDA pre-earnings IV | 🔴 **AT ABSOLUTE PEAK — earnings TOMORROW** | Close $180P at open; IV will crush 40-60% after report |
| NVDA premarket +6.9% | 🟢 $180P now ~31% OTM | Current put value ~$1.50–$2.50 (may be a smaller loss than feared) |
| Iran de-escalation signal | 🟡 Moderate positive | War risk premium slightly lower → VIX may tick down slightly |
| Brent crude $110 | 🔴 Oil still elevated | Macro uncertainty remains; vol not fully compressed |
| TSLA IV (~50%+) | 🟢 High | $370P theta churning; let it work |
| AMZN IV | 🟡 Moderate | $245P approaching 50% target; confirm fill + set GTC |
| Post-NVDA (May 21+) | ⏳ Opportunity window | Post-earnings IV crush = best time to sell new NVDA CSP; deploy ~$11,710 BP |
| Verdict | **IV STILL ELEVATED** | Sell premium window intact; NVDA is the priority close then re-open |

---

## TOP 3 PRIORITY ACTIONS

### Priority 1 — NVDA $180P BUY-TO-CLOSE (AT MARKET OPEN TODAY — NON-NEGOTIABLE)
**NVDA earnings: TOMORROW May 20 after close. DTE = 29. This MUST close today.**

NVDA has surged to ~$236 premarket (+6.9%), which is excellent news — the $180P is now ~31% OTM and current value has likely DROPPED to ~$1.50–$2.50 (vs $1.67 received). This means the P&L may be near breakeven or even a small profit vs the $3–4 estimate from Monday.

**Action:**
1. Log into app.alpaca.markets at 9:30 AM ET
2. Cancel any existing GTC BTC order ($0.80 order is long stale; if a new $4.00 order was placed yesterday, cancel that too)
3. **Place new order**: Buy-to-close `NVDA 18JUN2026 180P` — **limit $2.00** (with NVDA at $236, this is achievable)
4. If limit doesn't fill in first 5 minutes: raise to $2.50 or market
5. Acceptable fill range: up to **$3.00** given earnings tomorrow
6. **Estimated P&L**: $167 received – ~$150–$200 paid = approximately **breakeven to small loss/gain** — far better than the -$183 feared at Monday's open
7. Once closed: zero NVDA options exposure entering tomorrow's earnings

**Risk of NOT closing**: Even with NVDA at $236, a -25% earnings disaster = NVDA at $177 → $180P in the money → forced purchase of 100 NVDA at $180 = $18,000 cash obligation. Unacceptable. Close it.

### Priority 2 — TSLA + AMZN CSP CONFIRMATION (Day 13 — CRITICAL)
These positions have been "inferred open" for 13 sessions. This is the most significant portfolio management gap.

1. Confirm **TSLA 20JUN2026 370P**: exact fill date, exact premium received, current mark
2. Confirm **AMZN 20JUN2026 245P**: same
3. **TSLA**: At ~$430 (~14% OTM, 32 DTE), the $370P is deeply healthy. If ~$11 received → current value ~$1.75–$2.25 = ~80% profit captured. Set GTC BTC at $5.50 (50% of ~$11).
4. **AMZN**: At ~$267 (~8.2% OTM, 32 DTE). If ~$5 received → current value ~$1.00–$1.50 = ~70%+ profit captured. **Set GTC BTC at $2.50 (50% of $5) — this may fill soon.**
5. Record confirmed premiums in PLAN.md and log.md

### Priority 3 — PLAN THE POST-NVDA CSP (For Thursday May 21)
With NVDA at $236 and earnings tomorrow, begin planning the post-earnings re-entry.

| NVDA Scenario | Post-Earnings Level | Strike to Sell | Expiry | Target Premium |
|---------------|--------------------|--------------|----|------|
| Beat + pop | > $260 | $215–$220P | Aug 15 (~90 DTE) | $4–7/contract |
| Beat + muted | $240–$260 | $205–$215P | Aug 15 | $3–5/contract |
| In-line | $225–$240 | $195–$205P | Jul 18 (~60 DTE) | $3–4/contract |
| Miss + drop | $200–$225 | Wait 3+ days | — | — |
| Disaster miss | < $200 | Do NOT sell puts | — | — |

**Deploy ~$11,710 BP on Thursday May 21 (after IV crush settles overnight May 20–21).** This is the best IV-selling window of the quarter: NVDA post-earnings IV crush + whatever Iran resolution premium remains. Do not rush.

---

## RISK FLAGS

| Flag | Level | Detail |
|------|-------|--------|
| NVDA $180P — earnings TOMORROW | 🔴 **MAXIMUM** | Close at open 9:30 AM. With NVDA at $236, put worth ~$1.50–$2.50; near breakeven exit available |
| TSLA/AMZN CSP fills unconfirmed (Day 13) | 🔴 **CRITICAL** | Cannot accurately track P&L or set take-profits without confirmation |
| NSC meeting today (May 19) | 🟡 **MONITOR** | Diplomatic framing (Trump called off attack) → likely market positive outcome |
| Iran Hormuz still blocked | 🟡 MACRO | Brent $110; Hormuz toll plan active; XLE hedge working |
| JETS -7.1% from cost | 🟡 WATCH | Iran de-escalation directionally positive; -10% alert at $24.71; JETS at ~$25.50 = $0.79 above alert |
| QQQ below cost basis | 🟡 WATCH | ~$700 vs cost $710.93 (-1.5%); Nasdaq-led drag structural until rate relief |
| Alpha gap -0.45% cumulative | 🟡 ONGOING | Slightly better than -0.91% yesterday as XLE continues to outperform |
| Post-NVDA BP deployment | ✅ PLANNED | $11,710 earmarked; deploy Thursday after earnings clarity |
| Account vs $87,500 floor | ✅ OK | ~$12,400 cushion; no halt |

---

## KEY EVENTS TODAY

| Event | Time (ET) | Portfolio Impact |
|-------|-----------|-----------------|
| **NVDA $180P BTC at open** | **9:30 AM** | Priority 1 — eliminate earnings binary |
| NSC Iran military review meeting | TBD | Major: diplomatic outcome → JETS surge +5-10%; military action → risk-off |
| Iran diplomatic developments | Continuous | Watch Witkoff/Kushner contacts; any MOU signal = oil -$10 |
| 10-yr Treasury yield | Continuous | Elevated = QQQ headwind; any relief = QQQ recovery |
| NVDA intraday positioning | Continuous | IV expanding all day until tomorrow's close; reinforces urgency to close put |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | Confirmed |
| 2026-05-12 | $99,977.39 | $737.58 | -0.02% | +0.83% | -0.85% | Confirmed |
| 2026-05-13 | $100,614.57 | $742.77 | +0.61% | +1.54% | -0.92% | Confirmed |
| 2026-05-14 | $100,950.97 | $747.80 | +0.95% | +2.22% | -1.27% | Confirmed |
| 2026-05-15 | $100,058.34 | $737.71 | +0.06% | +0.84% | -0.79% | Confirmed |
| 2026-05-18 | **$100,013.46** | **$738.30** | **+0.01%** | **+0.93%** | **-0.91%** | ✅ exec_eod confirmed |
| **2026-05-19 PM** | **~$99,900** | **~$734** | **~-0.10%** | **~+0.34%** | **~-0.44%** | Premarket estimate |

**Alpha note:** -0.91% confirmed yesterday, estimating ~-0.44% today because XLE (+7.5% vs cost) is outperforming. The structural QQQ-vs-SPY drag (-1.5% on QQQ position) is the persistent gap driver. XLE is the hedge. JETS holds the peace-dividend optionality. CSP theta is the steady compounder.

---

## NVDA POST-EARNINGS DECISION TREE (May 20 After Close)

| NVDA Result | Level | Action (May 21 Morning) |
|-------------|-------|-------------------------|
| Beat + pop | > $260 | Sell NVDA $215–$220P Aug 15 after IV reset; target $5–7 |
| Beat + strong | $245–$260 | Sell $205–$215P Aug 15; target $4–6 |
| Beat + muted | $235–$245 | Wait 1 day; sell $200–$210P Aug 15; target $3–5 |
| In-line | $220–$235 | Wait 2 days; sell $185–$195P Jul 18; target $2–4 |
| Miss + drop | $195–$220 | Wait 3+ days; do NOT sell puts |
| Disaster miss | < $195 | Hold off entirely; no puts |

**Market context for NVDA earnings:** Consensus $78B revenue, $1.77 EPS, 80% YoY growth. Polymarket: 97% probability of a beat. NVDA already +20% this month ahead of earnings. Post-earnings IV crush makes the NEXT day (May 21) one of the best CSP-selling opportunities of the year.

---

*Pre-market report — Tuesday, May 19, 2026.*
*Alpaca API blocked (Day 13); prices from web search.*
*Last confirmed: exec_eod_2026-05-18 = $100,013.46 equity, SPY $738.30, Options BP $11,710.32.*
*NVDA at ~$236 premarket (+6.9%); $180P Jun 18 estimated value ~$1.50–$2.50; BTC at open TODAY — earnings TOMORROW.*
*TSLA $370P + AMZN $245P: inferred open, Day 13 — verify at app.alpaca.markets.*
*Iran: Trump called off Tuesday attack; "serious negotiations"; NSC meeting today (contingency framing); Brent $110.10.*
*XLE hold: Brent far above $85 trigger. JETS: +0.6% premarket on Iran de-escalation. QQQ: -0.6% PM, below cost basis.*

Sources:
- [Stock Market Today May 19, 2026 — TheStreet](https://www.thestreet.com/stock-market-today/stock-market-today-may-19-2026-updates)
- [US Premarket Movers May 19, 2026 — Bloomberg](https://www.bloomberg.com/news/articles/2026-05-19/us-stock-futures-today-agilysys-amer-sports-relay-stubhub-xp)
- [Market Wavers Amid Conflicting Reports on War — Schwab](https://www.schwab.com/learn/story/stock-market-update-open)
- [Brent Crude Oil Price — Investing.com](https://www.investing.com/commodities/brent-oil)
- [2026 Iran War Ceasefire — Wikipedia](https://en.wikipedia.org/wiki/2026_Iran_war_ceasefire)
- [US-Iran Negotiations — Wikipedia](https://en.wikipedia.org/wiki/2025%E2%80%932026_Iran%E2%80%93United_States_negotiations)
- [Nvidia Earnings May 2026 Live — Kiplinger](https://www.kiplinger.com/investing/live/nvidia-earnings-live-updates-and-commentary-may-2026)
- [NVIDIA Up 20% in a Month — 24/7 Wall St.](https://247wallst.com/investing/2026/05/14/nvidia-is-up-20-in-a-month-could-the-may-20-earnings-report-knock-it-right-back-down/)
