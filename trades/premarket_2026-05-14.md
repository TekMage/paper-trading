# Pre-Market Summary — Thursday, May 14, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment ("Host not in allowlist").
> Account equity sourced from exec_eod_2026-05-13.md (estimated; GH Actions May 12 confirmed $99,977.39 was last hard data point).
> Prices from web search / premarket data. Verify positions at https://app.alpaca.markets/paper-trading

---

## ACCOUNT VALUE & CASH

| Metric | Value | Note |
|--------|-------|------|
| EOD equity (May 13, estimated) | **$100,614.57** | exec_eod_2026-05-13 (no API confirm; GH Actions may have confirmed separately) |
| Starting capital | $100,000.00 | May 7, 2026 |
| Total return (May 13 EOD) | **+0.61%** | +$614.57 on $100,000 |
| SPY benchmark return | **+1.54%** | SPY $731.53 → $742.77 |
| Alpha vs SPY | **-0.92%** | Lagging; QQQ CPI/rate headwind + JETS drag |
| Options BP remaining | **~$11,922** | exec_eod figure; after TSLA + AMZN CSP collateral |
| Account vs $87,500 floor | **OK — ~$13,115 cushion** | No stop triggered |
| Cash reserve (est.) | **~$5,900** | Layer 4 target $5,000 ✅ |

**Pre-open equity estimate (May 14):** ~$100,700 — $100,720
*(Based on futures: S&P +0.27%, Nasdaq +0.19%; L1 positions marked up ~+$80–110)*

---

## CURRENT POSITIONS & OVERNIGHT P&L

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | May 13 EOD (est.) | Premarket May 14 (est.) | Overnight ΔP&L | Total Unreal. P&L | Status |
|--------|-----|----------|-------------------|------------------------|----------------|-------------------|--------|
| QQQ | 45 | $710.93 | ~$718 | ~$719.36 (+0.19%) | **+$61** | **+$325 (+1.01%)** | ✅ Above cost basis |
| SPY | 13 | $736.39 | $742.77 | ~$744.55 (+0.24%) | **+$23** | **+$107 (+1.12%)** | ✅ Hold |
| XLY | 40 | $117.00 | ~$122 | ~$122.24 (+0.2%) | **+$10** | **+$210 (+4.49%)** | ✅ Consumer strong |
| JETS | 80 | $27.45 | ~$26.90 | ~$27.00 (+0.37%) | **+$8** | **-$36 (-1.64%)** | ⚠️ Hormuz still blocked; hold |
| XLE | 100 | $56.70 | ~$59.10 | ~$58.92 (-0.3%) | **-$18** | **+$222 (+3.92%)** | ✅ Brent $107.82; above exit trigger |
| **L1 Total** | | **$54,111** | **~$54,955** | **~$55,039** | **+$84** | **+$928 (+1.71%)** | |

*Cash (est.): ~$45,889 | Options collateral locked: ~$61,500 | Free cash: ~$5,900*

### Layer 2/2b — Cash-Secured Puts (INFERRED — still unconfirmed; verify immediately at app.alpaca.markets)

| Symbol | Strike | Expiry | Collateral | Stock Premarket | OTM% | Est. Status |
|--------|--------|--------|------------|-----------------|------|-------------|
| TSLA | $370 | Jun 20 '26 | $37,000 | **~$445 (+2.58%)** | **~16.9%** | 🔶 INFERRED OPEN — healthy margin |
| AMZN | $245 | Jun 20 '26 | $24,500 | **~$268–271** | **~8.5–9.3%** | 🔶 INFERRED OPEN — watch if AMZN < $260 |
| NVDA | $190 | Jun 20 '26 | — | **~$228 (+1.9%)** | — | ❌ NOT OPEN — confirmed by BP math |

**CSP Health Summary:**
- TSLA $370P: TSLA at $445 = **16.9% OTM** — excellent buffer. P&L likely positive from entry.
- AMZN $245P: AMZN ~$268–271 = **8.5–9.3% OTM** — adequate; monitor if AMZN dips below $260.
- NVDA $190P: NOT open (Options BP would show $19K additional drawdown). **Do NOT open before May 20 earnings.**

---

## WATCHLIST SNAPSHOTS (Premarket May 14, 2026)

| Symbol | Premarket Price (est.) | May 13 EOD (est.) | Change | Note |
|--------|------------------------|-------------------|--------|------|
| SPY | ~$744.55 | $742.77 | **+0.24%** | S&P 500 futures +0.27%; extending record highs |
| QQQ | ~$719 | ~$718 | **+0.19%** | Nasdaq futures +0.19%; chips leading |
| XLY | ~$122.24 | ~$122 | **~flat** | Consumer disc. following market |
| JETS | ~$27.00 | ~$26.90 | **+0.37%** | Modest peace hopes; Hormuz still blocked |
| XLE | ~$58.92 | ~$59.10 | **-0.3%** | Brent ~$107.82 (-0.2% yday) — slight pullback |
| IWM | ~$285 | ~$284 | **+0.35%** | Small caps: risk-on tone |
| NVDA | **~$228** | ~$223.62 | **+1.9%** | 🔴 6th consecutive gain; EARNINGS MAY 20 — 6 days |
| TSM | ~$415 | ~$414 | **~flat** | AI foundry; steady |
| TSLA | **~$445** | ~$433 | **+2.77%** | Robotaxi momentum; Austin → Dallas/Houston expansion |
| AMZN | ~$268–271 | ~$265 | **+1.1–2.3%** | Watch re: AMZN $245P cushion |
| INTC | ~$120 | ~$118 | **+1.7%** | Gave back PM gains yesterday; some recovery |
| DRAM | ~$55–56 | ~$54.65 | **+0.6–2.5%** | AI memory ETF — strong structural theme |
| MU | ~$655 | ~$645 | **+1.5%** | AI HBM demand + Samsung union risk |
| AVGO | ~flat | ~flat | — | Not a priority position |
| Brent Crude | **~$107.82** | ~$108 | **-0.2%** | Elevated; Hormuz disruption continues |

---

## IRAN DEAL STATUS

| Item | Status |
|------|--------|
| MOU signed today? | ❌ **NO** |
| Latest development | One-page MOU being drafted (Witkoff/Kushner + Iranian officials); NOT signed |
| Sticking points | Iran wants Hormuz resolved BEFORE nuclear talks; US maintains naval blockade |
| Trump's stance | Ceasefire on **"massive life support"** — rejected Iran's counter-proposal |
| Naval situation | US maintains blockade on Iranian-linked vessels; sporadic clashes |
| Strait of Hormuz | **STILL BLOCKED** — civilian traffic suspended since ~Feb 28 |
| Brent crude (premarket) | **~$107.82/bbl** — elevated, down -0.2% from yesterday's ~$108 |
| WTI crude | ~$101–103/bbl |
| XLE exit trigger (Brent < $85) | ❌ NOT triggered — **HOLD XLE** |
| XLE trim trigger (Brent < $90) | ❌ NOT triggered |
| JETS thesis | **Delayed but intact** — peace dividend is coming, timing uncertain |

**Strategic implication**: No deal today. War premium in IV continues. CSP thesis remains valid. 
Oil declining slightly from peak ($108 → $107.82) but nowhere near XLE exit trigger ($85).

---

## IV ENVIRONMENT CHECK

| Indicator | Status | Implication |
|-----------|--------|-------------|
| Iran war continuing | ✅ Ongoing — MOU not signed | War risk premium = IV stays elevated |
| Brent crude > $100 | ✅ $107.82 | Energy uncertainty = IV-positive |
| NVDA pre-earnings IV | 🔴 **PEAK** — 6 days to earnings | Do NOT open NVDA CSP; earnings gap risk |
| PPI was +1.4% (hot) | ⚠️ Rate cut timeline extended | Rate uncertainty = higher IV across board |
| Peace deal imminent? | ❌ MOU only drafted; weeks away | IV compression NOT imminent |
| TSLA IV estimate | Likely >55% (high-IV name) | Existing $370P well-positioned |
| Verdict | **IV ELEVATED** | Hold existing CSPs; no rush to close below 50% profit target |

---

## TOP 3 PRIORITY ACTIONS

### Priority 1 — VERIFY CSP FILLS (NOW — CRITICAL, DAY 3+)
**This is the most urgent outstanding item. Log into app.alpaca.markets immediately.**
- Confirm **TSLA 20JUN2026 370P**: strike, expiry, premium received, current mark
- Confirm **AMZN 20JUN2026 245P**: same
- If fills confirmed, place **GTC buy-to-close limit orders at 50% of received premium** on both
- Determine exact options BP and any other open positions

### Priority 2 — NVDA EARNINGS DECISION (Deadline: May 18–19 EOD)
**Nvidia reports fiscal Q1 2027 on May 20. Analyst consensus: $78.75B rev / $1.76 EPS.**
- Confirm: Is NVDA $190P Jun 20 open? (Almost certainly NO given BP math)
- **Do NOT open any NVDA CSP before May 20** — binary gap risk on earnings
- Post-May 20 plan: After earnings, sell NVDA CSP at July expiry when IV resets. If NVDA beats + pops, sell $190P Jul 18 for ~$2–3. If NVDA misses + drops, wait for stabilization.
- Decision deadline: **May 19 EOD** — verify no NVDA options exposure before market close

### Priority 3 — POST-EARNINGS POSITIONING PREP
**Use today to prepare the post-NVDA CSP trade (to execute week of May 20).**
- NVDA $190P Jul 18 CSP: collateral $19K, premium est. ~$2–4 depending on IV post-earnings
- Also evaluate: INTC $115P (at ~$120 now, 4.2% OTM — tighter than ideal; monitor)
- AMZN $245P: if fills confirmed and in profit, may close early at 50%; if still holding, keep
- MU: Consider 5–8 share Layer 3 position if cash allows (~$3.3–5.2K at ~$655)

---

## RISK FLAGS

| Flag | Level | Detail |
|------|-------|--------|
| CSP fills unconfirmed (Day 3+) | 🔴 CRITICAL | Must verify at app.alpaca.markets TODAY |
| NVDA earnings May 20 (6 days) | 🔴 CRITICAL | No NVDA CSP likely open; but prepare post-earnings plan |
| AMZN $245P cushion | 🟡 WATCH | AMZN ~$268; if drops below $260 → 6.1% OTM → evaluate roll |
| Negative alpha vs SPY | 🟡 WATCH | -0.92% behind SPY since May 7; QQQ drag (CPI/PPI rate fears) |
| Options BP constrained (~$11.9K) | 🟡 CONSTRAINED | No new CSPs requiring > $11.9K collateral until options close |
| Iran — naval escalation risk | 🟡 WATCH | Combat resumption risk = spike in oil → XLE surge but JETS down |
| JETS at -1.6% from entry | 🟡 MINOR | Below cost basis; thesis intact but Hormuz must open for payoff |
| Hot inflation (PPI +1.4%) | 🟡 QQQ HEADWIND | Fed cuts pushed further out; growth stocks face rate pressure |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-08 | $100,000.00* | $737.27 | 0.00%* | +0.78% | -0.78% | API blocked; trades unconfirmed |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | GH Actions confirmed |
| 2026-05-12 | $99,977.39 | $737.58 | -0.02% | +0.83% | -0.85% | GH Actions confirmed |
| 2026-05-13 | ~$100,614.57 | $742.77 | **+0.61%** | **+1.54%** | **-0.92%** | Estimated (exec_eod) |
| **2026-05-14 PM** | **~$100,700** | **~$744.55** | **~+0.70%** | **~+1.78%** | **~-1.08%** | Premarket estimate |

*Alpha trending slightly more negative premarket as SPY gapped up more than our L1 (QQQ slower mover pre-open).*

---

## SESSION CONTEXT

**Macro: Mildly risk-on; tech/AI extends streak; Iran war drags on**

Futures modestly green (Dow +0.64%, S&P +0.24–0.30%, Nasdaq +0.19%) extending Wednesday's record highs.
Key drivers: Cisco beat, strong AI chip IPO appetite, NVDA +1.9% premarket (6th straight gain).
PPI was hot yesterday (+1.4% vs +0.5% est) but the "bad news priced in" reaction held — market shrugged off rate-cut pushback by close.

Iran: A one-page MOU framework is being drafted by Witkoff/Kushner but is NOT signed and NOT imminent. Fundamental sticking points remain (Hormuz sovereignty, nuclear enrichment). Trump publicly described the ceasefire as on "massive life support." Oil sits at $107.82 — the peace-deal oil drop ($10–20/barrel) is not priced in yet.

**The v2.0 thesis is intact but on pause.** Peace deal = oil drops = JETS soars = XLE trims. None of those triggers have fired. Hold L1 patiently. Collect CSP premium. Prepare the post-NVDA-earnings CSP entry. 

**One key thing changed today**: TSLA at $445 means our inferred $370 CSP is now 16.9% OTM — very safe. If fills are confirmed and premium was ~$11/share, we're comfortably ahead on that position.

---

*Pre-market report — May 14, 2026. API blocked; prices from web search.*
*Last confirmed equity: exec_eod_2026-05-13 $100,614.57 (estimated; GH Actions last hard data May 12 $99,977.39).*
*Iran: MOU being drafted but NOT signed. Brent $107.82. No exit triggers fired.*
*NVDA earnings May 20 — 6 days. No NVDA CSP open. Verify TSLA + AMZN CSP fills at app.alpaca.markets immediately.*
