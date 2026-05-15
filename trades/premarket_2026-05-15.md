# Pre-Market Summary — Friday, May 15, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment ("Host not in allowlist").
> Account equity sourced from exec_eod_2026-05-14.md (**confirmed: $100,950.97**). NVDA CSP position confirmed open from same file.
> Prices from web search / premarket data. Verify positions at https://app.alpaca.markets/paper-trading

---

## ACCOUNT VALUE & CASH

| Metric | Value | Note |
|--------|-------|------|
| EOD equity (May 14, **CONFIRMED**) | **$100,950.97** | exec_eod_2026-05-14 |
| Starting capital | $100,000.00 | May 7, 2026 |
| Total return (May 14 EOD) | **+0.95%** | +$950.97 |
| SPY close May 14 | **$747.80** | exec_eod confirmed |
| SPY benchmark return (May 14) | **+2.22%** | $731.53 → $747.80 |
| Alpha vs SPY (May 14 EOD) | **-1.27%** | Structural QQQ/Nasdaq lag |
| Options BP remaining (May 14 EOD) | **$12,071.08** | exec_eod confirmed |
| Account vs $87,500 floor | **OK — ~$12,462 cushion** | No stop triggered |

**Pre-open equity estimate (May 15): ~$99,950 — $100,000**
*(Based on Nasdaq-100 futures -1.6%, QQQ premarket $700.08 vs $718-720 May 14 close → L1 decline ~-$989; XLE partially offsets on Brent +1.11%; tech names down 2–3%)*

---

## CRITICAL NEW POSITION DISCOVERY — NVDA CSP CONFIRMED OPEN

From exec_eod_2026-05-14.md — **IMPORTANT correction to prior reports:**

| Item | Prior Assumption | Confirmed Reality |
|------|-----------------|-------------------|
| NVDA CSP open? | ❌ Assumed NOT open (based on BP math) | ✅ **CONFIRMED OPEN** |
| NVDA strike | $190 (planned) | **$180** (actual) |
| NVDA expiry | Jun 20 '26 (assumed) | **Jun 18, 2026** |
| Premium received | ~$5.00 (estimate) | **$1.67/share ($167 credit)** |
| Buy-to-close submitted? | No | ✅ **YES — GTC limit at $0.80** |

**NVDA $180P Jun 18: The bot submitted a buy-to-close at $0.80 at May 14 EOD.** This is the correct pre-earnings move. With NVDA at $228.70 premarket today, the $180P is ~21% OTM and worth very little. The order may have filled or may fill at open today.

**Key action: Verify the NVDA $180P buy-to-close fill status immediately. If not filled by 10am, raise the limit to $1.00–$1.20 and ensure it closes before May 20 earnings.**

---

## CURRENT POSITIONS & OVERNIGHT P&L

### Layer 1 — Core ETFs

| Symbol | Qty | Avg Cost | May 14 Close (est.) | Premarket May 15 | Overnight ΔP&L | Unreal P&L vs Cost | Status |
|--------|-----|----------|---------------------|-----------------|----------------|---------------------|--------|
| QQQ | 45 | $710.93 | ~$719 | **$700.08 (-2.6%)** | **-$851** | **-$489 (-1.53%)** | 🔴 BELOW COST BASIS |
| SPY | 13 | $736.39 | $747.80 | **~$739 (-1.1%)** | **-$114** | **+$34 (+0.35%)** | ✅ Slight gain |
| XLY | 40 | $117.00 | ~$124 | **~$122.14 (-1.5%)** | **-$74** | **+$205 (+4.36%)** | ✅ Consumer strong |
| JETS | 80 | $27.45 | ~$27.20 | **~$26.97 (-0.85%)** | **-$18** | **-$38 (-1.75%)** | ⚠️ Hormuz blocked; hold |
| XLE | 100 | $56.70 | ~$58.80 | **~$59.45 (+1.1%)** | **+$65** | **+$275 (+4.85%)** | ✅ Brent $106.89 |
| **L1 Total** | | **~$54,111** | **~$55,176** | **~$54,189** | **-$989** | **+$78 (+0.14%)** | |

*Note: QQQ dropped below cost basis overnight for first time. Not a stop trigger (portfolio stop = $87,500) but worth monitoring.*

### Layer 2/2b — Cash-Secured Puts

| Symbol | Strike | Expiry | Premium Sold | Stock Premarket | OTM% | Status |
|--------|--------|--------|-------------|-----------------|------|--------|
| TSLA | $370 | Jun 20 '26 | ~$11.00 (inferred) | **$441.41 open** | **~16.0%** | ✅ INFERRED OPEN — healthy cushion |
| AMZN | $245 | Jun 20 '26 | ~$5.00 (inferred) | **~$264–267 est.** | **~7.6–8.5%** | 🟡 INFERRED OPEN — watch if AMZN < $258 |
| NVDA | $180 | Jun 18 '26 | **$1.67 (confirmed)** | **$228.70** | **~21.3%** | 🔶 CONFIRMED OPEN — BTC at $0.80 submitted; **VERIFY FILL** |

**CSP Health Summary:**
- TSLA $370P: TSLA at $441 = **16% OTM** — very healthy despite today's tech selloff. Still well-protected.
- AMZN $245P: AMZN estimated ~$265 = **~8% OTM** — adequate but narrowing. Monitor if AMZN falls below $258 (5.3% OTM triggers roll evaluation).
- NVDA $180P: At 21.3% OTM and $0.80 buy-to-close submitted — this MUST close before May 20 earnings. **Verify immediately.**

---

## WATCHLIST SNAPSHOTS (Premarket May 15, 2026)

| Symbol | Premarket (est.) | May 14 Close | Change | Note |
|--------|-----------------|-------------|--------|------|
| SPY | ~$739 | $747.80 | **-1.1%** | S&P futures -1%; tech profit-taking |
| QQQ | **$700.08** | ~$719 | **-2.6%** | 🔴 Nasdaq futures -1.6%; chips/tech selling off |
| XLY | ~$122.14 | ~$124 | **-1.5%** | Consumer following market; TSLA drag |
| JETS | ~$26.97 | ~$27.20 | **-0.85%** | Airlines subdued; no Iran breakthrough |
| XLE | **~$59.45** | ~$58.80 | **+1.1%** | Brent $106.89 +1.1%; energy bucking selloff |
| IWM | ~$283 | ~$288 | **~-1.7%** | Small caps follow Nasdaq |
| NVDA | **$228.70** | $235.74 | **-2.99%** | Pre-earnings profit-taking; 5 days to May 20 |
| TSM | ~$410 | ~$415 | **~-1.2%** | AI foundry; general tech drag |
| TSLA | **$441.41** | ~$455 | **-3.0%** | Range $422–448 today; still well above $370P |
| AMZN | ~$264–267 | ~$270 | **~-1.5%** | Watch $245P cushion; needs to hold > $258 |
| INTC | **$109–116 range** | ~$120 | **-3.3–8.5%** | 🔴 Big drop — AMD/MU down too; chip profit-taking |
| MU | ~$635 | ~$645 | **~-1.6%** | AI memory selling off with chips |
| DRAM | ~$54 | ~$55 | **~-1.8%** | Memory ETF follows MU |
| AVGO | ~flat | ~flat | — | Less tech-beta today |
| Brent Crude | **$106.89** | ~$105.87 | **+1.1%** | IEA: Hormuz -4M bbl/day; supply still tight |

---

## IRAN / TRUMP-XI SUMMIT OUTCOME

| Item | Status |
|------|--------|
| MOU signed? | ❌ **NO** |
| Trump-Xi summit result | ✅ **Cordial conclusion** — joint statement released |
| Hormuz joint commitment | 🟢 **NEW: "Strait of Hormuz must remain open"** — both US and China committed in writing |
| China opposes Hormuz toll | ✅ China explicitly opposed militarization / toll-charging on Strait |
| Iran war breakthrough? | ❌ **No** — departed Beijing "with little evidence of agreement on ending the war" |
| Xi offered to broker peace | 🟡 **Yes** — Trump says Xi offered to help broker Iran peace (constructive, not binding) |
| Trade deals | ✅ US firms get expanded China market access; China buys more US oil/agriculture |
| H200 chip sales | ✅ **Confirmed** — approved yesterday (NVDA catalyst) |
| Hormuz strait | **STILL BLOCKED** — IEA: -4M bbl/day; market undersupplied through October even if resolved |
| Brent crude | **$106.89 (+1.1%)** — IEA warns supply tight through October |
| XLE exit trigger (Brent < $85) | ❌ NOT triggered — **HOLD XLE** |
| JETS thesis | **Delayed, intact** — Hormuz joint statement is the most constructive language yet |

**Strategic implication:** The Hormuz "must remain open" joint statement is the most significant diplomatic development in weeks. It creates a framework for resolution and signals Xi is now actively in the mediation role. However, NO concrete Iran war ending deal was struck — war premium persists, IV stays elevated, CSP thesis intact. Brent at $106.89 (up) reflects continued tight supply.

**JETS outlook revised slightly positive:** US + China joint Hormuz commitment is a real diplomatic step. The peace dividend trade is still coming — the timeline just moved closer. Don't add yet (no confirmed deal), but hold conviction.

---

## IV ENVIRONMENT CHECK

| Indicator | Status | Implication |
|-----------|--------|-------------|
| Iran war continuing | ✅ No deal yet | War risk premium = IV stays elevated |
| Brent crude > $100 | ✅ $106.89 | Supply squeeze = IV-positive |
| Trump-Xi Hormuz commitment | 🟡 **New** — constructive but no deal | Mild IV-dampening signal; not yet compressing |
| NVDA pre-earnings IV | 🔴 **PEAK** — 5 days to May 20 | Do NOT open NEW NVDA options; close existing $180P |
| Market selloff today | 🟡 VIX likely ticking up | Short-term spike; adds to put premiums |
| TSLA IV (estimated) | >55% (high-IV name) | $370P still rich; hold to 50% profit target |
| INTC selloff | ⚠️ Chipping down hard | If considering INTC CSP, recalibrate strike (now ~$110, not $120) |
| Verdict | **IV ELEVATED — HOLD CSPs** | No rush to close TSLA/AMZN early; let theta work |

---

## TOP 3 PRIORITY ACTIONS

### Priority 1 — NVDA $180P BUY-TO-CLOSE CONFIRMATION (URGENT — Pre-Earnings)
**Deadline: Close before May 20 (5 days). Buy-to-close at $0.80 submitted at May 14 EOD.**
- Log into app.alpaca.markets immediately
- Check: Did the NVDA 18JUN2026 $180P BTC limit order ($0.80) fill?
- If **YES**: Log the profit ($167 received - $80 paid = $87 net). Position closed. 
- If **NOT filled**: Raise limit to $1.00–$1.20 and resubmit. **Must close before May 20 earnings.**
- Reason: NVDA has binary earnings gap risk on May 20. Even at 21% OTM ($228 vs $180), a bad print could move stock -15% and threaten the position.

### Priority 2 — VERIFY TSLA + AMZN CSP FILLS (CRITICAL — Day 9+)
**Still the longest-running unresolved item. These are inferred but MUST be confirmed.**
- Confirm **TSLA 20JUN2026 370P**: fill date, exact premium received, current mark
- Confirm **AMZN 20JUN2026 245P**: same
- With AMZN potentially ~$264-267 today (down from $270), $245P cushion is ~7.7–8.2% OTM
- If fills confirmed: place GTC buy-to-close limit orders at 50% of received premium on both
- TSLA: Still very healthy at 16% OTM; no defensive action needed
- AMZN: Watch level — if AMZN breaks below $258 (5.3% OTM), evaluate rolling down/out

### Priority 3 — QQQ MONITORING + NVDA POST-EARNINGS PLAN PREPARATION
**QQQ dropped to $700.08 premarket — first time below our cost basis ($710.93).**
- Monitor QQQ through the session. If it stabilizes near $700 and tech finds a bid, hold.
- Do NOT add QQQ on this dip — capital is constrained, risk-off day, better to preserve.
- NVDA earnings preparation (May 20, 5 days): After NVDA reports, plan is:
  - Beat + pop (NVDA → $240+): Sell NVDA $190P (or $200P) Aug 15 expiry (~45 DTE), IV reset = $3–5 premium
  - Beat but flat/muted: Same — wait 1–2 days for IV reset, then sell
  - Miss + drop (NVDA < $210): Wait 2–3 days for stabilization; stay out until new floor confirmed
- Do NOT open any NVDA options before May 20. Let earnings happen.

---

## RISK FLAGS

| Flag | Level | Detail |
|------|-------|--------|
| NVDA $180P open into earnings | 🔴 CRITICAL | **Buy-to-close at $0.80 submitted — VERIFY FILL. Must close before May 20.** |
| TSLA/AMZN CSP fills unconfirmed (Day 9+) | 🔴 CRITICAL | Must verify at app.alpaca.markets |
| QQQ below cost basis ($700 vs $710.93) | 🟡 WATCH | Nasdaq profit-taking post-Trump-Xi summit; not a stop signal but monitor |
| AMZN $245P cushion | 🟡 WATCH | AMZN ~$264-267; if breaks $258 → trigger roll evaluation |
| INTC massive drop | 🟡 INTC NOTE | INTC range $109-116 today (was $120 yesterday) — $95 CSP strike is extremely far OTM; if planning INTC CSP, recalibrate to $95-100 strike or skip entirely |
| Negative alpha vs SPY | 🟡 WATCH | ~-1.3% since May 7; today Nasdaq -1.6% vs S&P -1% will widen alpha gap further |
| Risk-off Friday selloff | 🟡 MACRO | Post-summit profit-taking; Treasury yields rising; no new positions today |
| IEA supply warning | 🟡 OIL | Even if Hormuz resolves next month, market undersupplied through October → Brent stays elevated → HOLD XLE |
| Options BP ($12,071) | ✅ OK | Enough for one more small CSP; preserve for post-NVDA-earnings entry |

---

## BENCHMARK TRACKER

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-08 | $100,000.00* | $737.27 | 0.00%* | +0.78% | -0.78% | API blocked; trades unconfirmed |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | GH Actions confirmed |
| 2026-05-12 | $99,977.39 | $737.58 | -0.02% | +0.83% | -0.85% | GH Actions confirmed |
| 2026-05-13 | $100,614.57 | $742.77 | +0.61% | +1.54% | -0.92% | exec_eod confirmed |
| 2026-05-14 | **$100,950.97** | **$747.80** | **+0.95%** | **+2.22%** | **-1.27%** | ✅ exec_eod CONFIRMED |
| **2026-05-15 PM** | **~$99,950–100,000** | **~$739** | **~-0.04%** | **~+1.02%** | **~-1.06%** | Premarket estimate; Nasdaq -1.6% |

*Today's risk-off selloff will temporarily widen our alpha gap. Nasdaq heavy = more pain than SPY today. XLE offsetting slightly (Brent +1.11%).*

---

## SESSION CONTEXT

**Macro: Risk-off Friday. Post-summit profit-taking in tech. Yields rising.**

Futures: S&P -1% to -1.2%, Nasdaq -1.6%, Dow -0.9% (-440 pts). After Thursday's record-breaking session (S&P 7,500, Dow 50,000), markets are giving back gains as investors digest the Trump-Xi summit conclusions. The headline disappointment: **no Iran war breakthrough**. The constructive takeaway: **joint Hormuz commitment in writing** — a new diplomatic baseline.

Tech is the hardest hit: NVDA -3%, INTC down -3 to -8.5% (range $109-116), AMD/MU selling off. Reason: profit-taking after Wednesday-Thursday surge (NVDA +5.3%, H200 China approval), rising Treasury yields (rate-sensitive tech), and no additional AI/China catalysts overnight.

Energy is the outperformer: Brent $106.89 (+1.1%) after IEA warned that Hormuz disruption removed 4M bbl/day and the market will remain undersupplied through October even if resolved next month. XLE should be up ~+0.5–1.1% at open.

Iran: No deal. But Xi explicitly offered to broker peace and both sides wrote "Hormuz must remain open" into a joint communique. This is the most concrete peace-framework language yet — weeks ahead of where we were. The JETS peace-dividend trade's timeline moved closer, even without a signed deal.

**The v2.0 thesis is intact.** Hold all positions. The pullback is macro/yield-driven, not a structural breakdown. The NVDA earnings event (May 20) is the next major catalyst — close the $180P, then prepare a new post-earnings CSP entry.

---

*Pre-market report — May 15, 2026. API blocked; prices from web search.*
*Confirmed equity: exec_eod_2026-05-14 = $100,950.97. Options BP: $12,071.08.*
*NVDA $180P Jun 18 CONFIRMED OPEN — BTC at $0.80 submitted. Verify fill immediately.*
*TSLA $370P + AMZN $245P still inferred open — verify at app.alpaca.markets (Day 9+).*
*Iran: No MOU signed. Trump-Xi joint Hormuz commitment ("must remain open") — most constructive diplomatic signal yet.*
*Brent $106.89 (+1.1%). XLE hold. No exit triggers fired.*
*NVDA earnings May 20 — 5 days. No new NVDA options until after earnings.*

Sources:
- [Axios: US and Iran closing in on one-page memo](https://www.axios.com/2026/05/06/iran-us-deal-one-page-memo)
- [Trump-Xi Summit: Joint Hormuz Commitments](https://www.thedefensenews.com/news-details/Trump-and-Xi-Publish-Detailed-List-of-Commitments-on-Iran-Hormuz-Strait-and-Bilateral-Trade/)
- [Al Jazeera: Xi-Trump summit failed to yield Iran breakthrough](https://www.aljazeera.com/news/2026/5/15/how-xi-trump-summit-failed-to-yield-iran-war-breakthrough)
- [Bloomberg: US Premarket Movers May 15, 2026](https://www.bloomberg.com/news/articles/2026-05-15/us-stock-futures-today-dexcom-figma-gemini-nu-papa-john-s)
- [OilPriceAPI: Brent $109.03 / WTI $104.81](https://www.oilpriceapi.com/oil-prices-today)
- [Time: Trump says Xi offered to help broker peace with Iran](https://time.com/article/2026/05/14/trump-xi-china-iran-strait-hormuz/)
