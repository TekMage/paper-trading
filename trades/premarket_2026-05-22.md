# Pre-Market Summary — Friday, May 22, 2026

> **API Status**: Alpaca paper-api.alpaca.markets blocked from Claude Code environment — Day 18.
> Account data from exec_eod_2026-05-21 (confirmed). Market prices from web search.
> Verify positions at https://app.alpaca.markets/paper-trading

---

## ACCOUNT SNAPSHOT

| Metric | Value | Notes |
|--------|-------|-------|
| **Account Equity (EOD May 21)** | **$100,893.34** | ✅ exec_eod confirmed |
| Starting capital (May 7) | $100,000.00 | Benchmark date |
| **Total P&L** | **+$893.34 (+0.89%)** | From $100K starting capital |
| Options BP Available | **$29,936.23** | ✅ exec_eod confirmed — major jump from midday $4,772 |
| **SPY EOD May 21** | **$742.91** | SPY total return: +1.56% |
| **Alpha vs SPY** | **-0.66%** | Down from best -0.15% at midday; SPY rallied hard late |
| Account vs $87,500 floor | ✅ **+$13,393 cushion** | No halt triggered |

**⚡ KEY BP INSIGHT:** Options BP jumped from $4,772 (midday) to $29,936 (EOD). This strongly implies the TSLA $370P and/or AMZN $245P GTC buy-to-close orders **filled during the afternoon session** (TSLA surged to $418+ range; AMZN closed $265). If both closed, ~$61.5K in collateral was freed. With only NVDA $180P remaining (~$18K collateral), BP of ~$30K checks out. **Priority 1 today: CONFIRM at app.alpaca.markets.**

---

## POSITIONS TABLE

### Layer 1 — Core ETFs (EOD May 21 estimates, carry-forward to May 22 open)

| Symbol | Qty | Avg Cost | EOD May 21 Close | Unreal P&L$ | Unreal P&L% | Notes |
|--------|-----|----------|-----------------|-------------|-------------|-------|
| QQQ | 45 | $710.93 | **~$716.97** | **~+$272** | **+0.85%** | Recovered from $703 lows yesterday; AI/tech thesis intact; NVDA beat |
| SPY | 13 | $736.39 | **$742.91** | **+$85** | **+0.88%** | Above cost; markets heading for longest weekly gain streak since 2023 |
| XLY | 40 | $117.00 | **~$119.00** | **+$80** | **+1.71%** | AMZN $265 (+2.19% Thu); TSLA $418 range; consumer strong |
| JETS | 80 | $27.45 | **$26.61** | **-$67** | **-3.06%** | Below cost; Rome Rd5 no breakthrough dampens immediate catalyst; thesis intact |
| XLE | 100 | $56.70 | **$60.04** | **+$334** | **+5.89%** | Brent $104.52 this morning (+1.89%); well above $85/$90 exit triggers; HOLD |
| **TOTAL L1** | | **~$54,111** | **~$54,793** | **~+$682** | **+1.26%** | |

### Layer 2/2b — Cash-Secured Puts

| Symbol | Strike | Expiry | DTE | Last Known Stock | OTM$ | OTM% | Sold For | Est. Mark | Status |
|--------|--------|--------|-----|-----------------|------|------|----------|-----------|--------|
| NVDA | $180 | Jun 18 '26 | **26** | **~$220** | $40 | **18.2%** | $0.78 | ~$0.35–0.45 | 🟡 Bot re-entry May 21; HOLD; 55–56% profit unrealized |
| TSLA | $370 | Jun 20 '26 | **28** | **~$418.40** | $48.40 | **13.1%** | ~$11 | N/A | 🟢 **LIKELY CLOSED via GTC $5.50** — BP jump from $4,772→$29,936 implies fill |
| AMZN | $245 | Jun 20 '26 | **28** | **~$265** | $20 | **8.2%** | ~$5 | N/A | 🟢 **LIKELY CLOSED via GTC $2.50** — same BP evidence |

**Options P&L Summary (inferred):**
| Position | Premium | Status | Est. Net P&L |
|----------|---------|--------|-------------|
| NVDA $180P Jun18 Rd1 | $1.67 | ✅ Closed $0.76 BTC | **+$91 confirmed** |
| TSLA $370P Jun20 | ~$11 | 🟢 GTC $5.50 likely filled | **~+$550 realized** |
| AMZN $245P Jun20 | ~$5 | 🟢 GTC $2.50 likely filled | **~+$250 realized** |
| NVDA $180P Jun18 Rd2 | $0.78 | 🟡 Open; 26 DTE | **~+$33–43 unrealized** |
| **Total options** | | | **~+$924–934 (est.)** |

---

## TODAY'S WATCHLIST (Pre-market / Early AM May 22)

| Symbol | Last Price | Source | vs Strategy Context |
|--------|-----------|--------|---------------------|
| **SPY** | ~$742–744 | Futures +0.2% from $742.91 close | ✅ Trending up; weekly gain streak |
| **QQQ** | **$716.97** | Range $706.77–$717.52 | ✅ Above $710.93 cost; NVDA beat tailwind |
| **TSLA** | **$418.40** | Range $412.90–$426.95 | ✅ $48+ above $370 strike; far OTM |
| **AMZN** | ~$265 | May 21 close confirmed | ✅ $20+ above $245 strike; still strong |
| **NVDA** | ~$220–225 | NVDA beat EPS+Rev+$80B buyback | ✅ $40+ above $180 strike; IV compressed post-earnings |
| **XLE** | ~$60 | Brent $104.52 (+1.89%) | ✅ No exit triggers; oil recovering from $105 close |
| **JETS** | ~$26.61 | May 21 close; Rome Rd5 no deal | 🟡 Below $27.45 cost; Iran thesis intact but patience needed |
| **IWM** | ~$280–285 | Small cap recovery | 🟡 Peace deal catalyst still pending |
| **Brent Crude** | **$104.52/bbl** | +1.89% from $102.58 | 🟡 Rising; $19+ above $85 XLE exit; $14+ above $90 trim |
| **INTC** | ~$95–100 | Hit 52-week high May 20 | 🟡 Near $95 CSP strike; monitor before adding |
| **MU** | ~$818 | AI memory momentum; +2.4% May 21 on NVDA beat | ✅ AI HBM demand strong |
| **TSM** | ~$380–420 | AI foundry; Layer 2 candidate | 🟡 Wheel candidate if BP confirmed free |

---

## IRAN DEAL STATUS — KEY UPDATE

| Item | Status |
|------|--------|
| MOU signed? | ❌ **NO — not yet** |
| Rome Round 5 (May 23 — tomorrow) | 🟡 **Ended without breakthrough** — both sides agreed to continue |
| US position | Wants Iran to dismantle uranium enrichment program |
| Iran position | Open to limiting enrichment but will NOT dismantle entirely |
| Trump statement | "Progress made" — optimistic framing |
| Talks description | "Constructive" — significant differences remain |
| Pakistan mediation | Active (army chief visited Tehran May 21) |
| Brent crude response | $104.52 (+1.89%) — rising because deal stalled |
| Brent trend (week) | **-4% for the week** — market had already priced in deal optimism |
| Hormuz blockade | Still officially active |
| XLE exit trigger ($85 Brent) | ❌ **NOT triggered — $19.52 above threshold. HOLD XLE.** |
| XLE trim trigger ($90 Brent) | ❌ **NOT triggered — $14.52 above threshold.** |
| JETS peace dividend | 🟡 Still live thesis — no deal yet but negotiations ongoing |
| Next catalyst | Round 6 talks (date TBD); any leak of resumed negotiations |

**Iran analysis:** Rome Round 5 produced no MOU signing. The core sticking point — uranium enrichment — remains unresolved. This is a **delay, not a collapse**: both sides agreed to continue. The "deal imminent" framing from last week was premature. This means:
1. **XLE stays**: Oil at $104 validates holding XLE ($60, +$334 unrealized)
2. **JETS thesis intact but timeline extends**: Airlines peace dividend plays requires patience; no immediate catalyst
3. **IV stays elevated longer**: Good news for CSP sellers — war-era IV persists
4. **Plan adjustment**: De-emphasize "act NOW before IV compresses" urgency; deal is weeks away, not days

---

## IV ENVIRONMENT CHECK

| Signal | Assessment |
|--------|------------|
| NVDA post-earnings IV | 🔴 **Compressed** — IV crush happened post-earnings. Jun18 $180P at $0.78 reflects lower vol |
| TSLA IV | 🟡 Still elevated (high-beta stock); TSLA $418 = good CSP positioning |
| War-era IV | 🟢 **Still elevated** — Rome Rd5 no deal = uncertainty persists = IV stays high |
| New CSP urgency | 🟡 **Less urgent than last week** — deal is delayed, IV compression not imminent |
| NVDA Jul18 CSP | 🟡 Can now be evaluated calmly (no rush); BP $29,936 allows it if TSLA/AMZN confirmed closed |
| INTC CSP | 🟡 $95 strike with INTC near 52-week highs — risk/reward less favorable now |

---

## TOP 3 PRIORITY ACTIONS

### 🥇 Priority 1 — Confirm TSLA $370P + AMZN $245P Status (CRITICAL — Day 18)
**Action required at app.alpaca.markets:**
- Open options → check TSLA 20JUN2026 370P and AMZN 20JUN2026 245P
- **If GTC $5.50 filled on TSLA**: Record exact fill date + P&L (~+$550). Mark position CLOSED.
- **If TSLA still open**: TSLA at $418 = $48 OTM = 12.9% OTM; put mark ~$1.50; SET BTC at $1.50 immediately
- **If GTC $2.50 filled on AMZN**: Record fill date + P&L (~+$250). Mark position CLOSED.
- **If AMZN still open**: AMZN at $265 = $20 OTM; put mark ~$0.30; SET BTC at $0.30 immediately
- **Why critical**: BP jump ($4,772→$29,936) strongly implies fills happened; confirmation unlocks next steps

### 🥈 Priority 2 — Evaluate NVDA Jul 18 $185–190P (Add the Intended Position)
**Condition**: Only proceed AFTER TSLA/AMZN status confirmed and BP $29,936 verified
- NVDA at ~$220–225; $185P = ~16–18% OTM; 57 DTE (Jul 18)
- Target premium: $3.00–5.00/contract (vs. bot's $0.78 on Jun18 $180P)
- Collateral required: $18,500 (fits within $29,936 BP)
- **Wait until 10 AM**: Confirm NVDA direction and check IV after open
- **Do NOT open** if BP confirmation shows TSLA/AMZN still open → not enough margin

### 🥉 Priority 3 — Monitor Iran + XLE Positioning
- **XLE HOLD**: Brent $104.52; no exit triggers; $334 unrealized profit protected
- **Prep XLE trim order (60 shares, market)** in Alpaca interface for when MOU eventually signs
- **JETS HOLD**: $26.61 vs $27.45 cost; thesis extends with talks continuing; $35 target unchanged
- **Watch for**: Round 6 Iran talks announcement or any surprise deal leak (weekend risk)

---

## RISK FLAGS

| Flag | Level | Detail |
|------|-------|--------|
| Rome Rd5 no deal → JETS stays below cost | 🟡 WATCH | JETS at -3.1% vs cost; patience required; exit if deal collapses entirely |
| TSLA/AMZN CSP status unconfirmed (Day 18) | 🟡 **OVERDUE** | Cannot finalize options BP picture without manual confirmation |
| NVDA bot re-entry ($180P Jun18 @ $0.78) | ⚠️ SUBOPTIMAL | Safe (18.2% OTM); only $78 premium; plan to add Jul18 position separately |
| Brent rebounding ($104.52 +1.89%) | 🟡 WATCH | Oil rising = Iran deal further away = XLE position extending |
| QQQ near cost ($710.93 avg vs ~$717) | 🟢 OK | Now +$272 unrealized; NVDA beat + Nasdaq weekly gains closing positive |
| SPY weekly gain streak (longest since 2023) | 🟡 MONITOR | Market extended; possible pullback if Iran deal fatigue sets in |
| Account vs $87,500 floor | ✅ OK | $100,893 — $13,393 cushion |
| Alpha gap -0.66% | 🟡 WATCH | Improved from -0.87% last week but widened from -0.15% midday yesterday; Iran deal is the alpha catalyst |

---

## BENCHMARK TRACKER (Updated)

| Date | Equity | SPY | Our Return | SPY Return | Alpha | Notes |
|------|--------|-----|------------|------------|-------|-------|
| 2026-05-07 | $100,000.00 | $731.53 | 0.00% | 0.00% | 0.00% | v2.0 start |
| 2026-05-11 | $100,210.63 | $738.29 | +0.21% | +0.92% | -0.71% | ✅ Confirmed |
| 2026-05-12 | $99,977.39 | $737.58 | -0.02% | +0.83% | -0.85% | ✅ Confirmed |
| 2026-05-13 | $100,614.57 | $742.77 | +0.61% | +1.54% | -0.92% | ✅ Confirmed |
| 2026-05-14 | $100,950.97 | $747.80 | +0.95% | +2.22% | -1.27% | ✅ Confirmed |
| 2026-05-15 | $100,058.34 | $737.71 | +0.06% | +0.84% | -0.79% | ✅ Confirmed |
| 2026-05-18 | $100,013.46 | $738.30 | +0.01% | +0.93% | -0.91% | ✅ exec_eod confirmed |
| 2026-05-19 | $99,744.04 | $733.42 | -0.26% | +0.26% | -0.51% | ✅ exec_eod confirmed |
| 2026-05-20 | $100,402.60 | $740.86 | +0.40% | +1.28% | -0.87% | ✅ exec_eod confirmed |
| 2026-05-21 | **$100,893.34** | **$742.91** | **+0.89%** | **+1.56%** | **-0.66%** | ✅ exec_eod confirmed; BP $29,936 (TSLA/AMZN likely closed); Rome Rd5 no deal |
| 2026-05-22 | ⏳ Pending | ~$744+ | — | — | — | Futures +0.2%; Brent $104.52 |

**Alpha path forward:** The -0.66% gap closes when: (1) Iran MOU signs → JETS rallies to $34-35 (+$592 unrealized); (2) Oil drops → XLE trim executed profitably; (3) New NVDA Jul18 CSP adds $300-500 in premium income. Each Iran deal progress report is a potential alpha accelerant.

---

## SESSION CONTEXT

**Week in review (May 18–21):** The week started with the best alpha reading (-0.15% on Thursday) but the SPY rallied hard into Friday EOD close ($742.91), widening the gap back to -0.66%. The portfolio is holding steady while the SPY outperforms on pure market momentum. The Iran deal delay keeps JETS depressed and oil elevated, which simultaneously supports XLE but holds back the peace dividend trades. The NVDA earnings beat (EPS+Revenue+$80B buyback) confirmed the AI capex thesis; QQQ recovering from $703 lows to $717 validates the core Layer 1 position.

**Overnight catalysts to watch:**
- Any Iran Round 6 announcement or weekend deal leak
- Brent crude direction (currently recovering +1.89% from $102→$104.52)
- NVDA stability above $215 (validates $180P safety)

---

*Pre-market report — Friday, May 22, 2026.*
*Account: $100,893.34 (exec_eod May 21, confirmed). SPY: $742.91. BP: $29,936.23.*
*Iran: Rome Rd5 ended without deal — MOU not signed. Next catalyst: Round 6 (TBD).*
*Oil: Brent $104.52 (+1.89%) — no XLE exit triggers. HOLD XLE.*
*Options: NVDA $180P Jun18 open (safe, 18.2% OTM). TSLA/AMZN likely closed (confirm at Alpaca).*
*Priority today: (1) Confirm TSLA/AMZN fills; (2) Evaluate NVDA Jul18 $185-190P if BP confirmed; (3) Hold all Layer 1 positions.*
