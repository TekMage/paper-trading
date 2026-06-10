# Premarket Summary — Wednesday, June 10, 2026

> **API status: UNAVAILABLE** — Alpaca paper-API unreachable from cloud environment. All positions confirmed via exec_eod_2026-06-09.md.
>
> **CPI alert:** May CPI data drops this morning. Economists expect +4.2% YoY — first reading above 4% since May 2023. Market-moving event; equities already pricing risk-off.

---

## Account Snapshot (from exec_eod_2026-06-09 — authoritative)

| Metric | Value |
|--------|-------|
| **Equity** | **$99,961.39** |
| **Our return (inception)** | **-0.04%** |
| **SPY return (inception)** | **+0.67%** ($736.42 notional) |
| **Alpha** | **-0.71%** |
| **Options BP remaining** | **$55,174.08** |

Market context: S&P 500 futures -0.47% premarket; Brent at $92 on renewed US-Iran hostilities; CPI due at 8:30 AM ET.

---

## Current Positions

### Layer 1 — Core ETFs (all at target; GitHub Actions maintains)

| Symbol | Shares | Notes |
|--------|--------|-------|
| QQQ | 45 | Nasdaq futures weak; chip-stock volatility ongoing |
| SPY | 13 | S&P futures -0.47% premarket |
| XLY | 40 | Consumer discretionary under pressure (inflation + tariff risk) |
| JETS | 80 | Oil elevated ($92) = fuel cost headwind; cost basis $27.45; **target exit $35.69** |
| XLE | 100 | **Brent $92 = $2 above $90 trim trigger; geopolitical risk intact — hold** |

### Layer 2 — Open CSPs

**NVDA $180P Jul17 — LIKELY FILLED (exec_eod confirms):**

| Field | Value |
|-------|-------|
| Symbol | NVDA260717P00180000 |
| Strike / Expiry | $180 / 2026-07-17 (~37 DTE) |
| Fill price | $1.97 (submitted Jun 9) |
| Collateral held | ~$18,000 (≈ open BP $72,496 → EOD BP $55,174 = -$17,322 delta) |
| Status | **[likely filled]** — BP drop persisted through EOD (vs. Jun 8 pattern where BP fully recovered = unfilled) |
| NVDA buffer | ~10–15% OTM (NVDA ~$199–210 range Jun 9) |
| 50% profit BTC target | ~$0.99 |

> Treat as open and live. Four prior submission attempts unfilled; this one appears different based on BP delta.

**AMZN $245P Jun26:**
- Still NOT opened. 16 DTE as of today. Too close to ATM to open. Do not act unless AMZN moves convincingly above $252.

---

## Iran / Oil Status

| Item | Value |
|------|-------|
| **MOU status** | **NOT SIGNED — ACTIVELY DISRUPTED** |
| **Overnight development** | US launched retaliatory "self-defense strikes" on Iran (after Iran shot down US Apache helicopter near Strait of Hormuz on Jun 9). Iran response overnight: TBD at time of writing. |
| **Deal trajectory** | Negotiations suspended. Iran-Israel bilateral ceasefire intact, but US-Iran kinetic exchange now active. MOU is effectively off the table near-term. |
| **Brent crude** | **~$92/barrel** — fresh hostilities pushing oil higher |
| Distance from $90 XLE trim | **+$2.00 above trigger** — trigger NOT active |
| Distance from $85 XLE exit | **+$7.00 above trigger** |

**Oil directional risk today:** With US strikes overnight, the path of least resistance is oil staying elevated or moving higher, not lower toward $90. The $90 trim trigger is unlikely to fire today unless there's a sudden diplomatic breakthrough — which would require Iran to stand down publicly. Monitor Brent at open (9:30 AM).

---

## Manual Triggers to Monitor Today

| Trigger | Level vs. Current | Status |
|---------|------------------|--------|
| Brent ≤ $90 → sell 30 XLE at market | Brent ~$92 (+$2 buffer) | **NOT TRIGGERED** — watch if de-escalation news breaks |
| Brent ≤ $85 → exit all XLE | Brent ~$92 (+$7 buffer) | NOT TRIGGERED |
| Iran MOU signed → sell 60 XLE immediately | Negotiations collapsed | NOT TRIGGERED — extremely unlikely today |
| JETS ≥ $35.69 → close all 80 JETS (cost $27.45) | JETS ~$27–28 est. (~$8 gap) | NOT TRIGGERED |

---

## Morning Priority Actions

1. **Watch CPI at 8:30 AM ET:** Expected +4.2% YoY. A hot print (≥4.2%) reinforces Fed-hold narrative, pressures equities further — tech/QQQ most exposed. A cool miss could trigger a relief rally. No direct trigger for our positions but sets the tone for the day.

2. **Confirm NVDA $180P Jul17 fill status:** Check exec_open_2026-06-10 when it posts (~9:30 AM ET via GitHub Actions). If BP is ~$55K = filled (hold the CSP). If BP rebounds to ~$72K = unfilled (bot will attempt another submission at open). The eod-to-eod BP comparison strongly implies fill, but verify.

3. **Monitor Brent at open:** Current ~$92. If Iran retaliates before 9:30 AM ET and oil spikes above $95, XLE becomes a stronger hedge — no action needed. If overnight news shows Iranian stand-down and oil reverses below $90 at open, be ready to manually sell 30 XLE at market (do not wait — trigger fires the moment Brent ≤ $90).

---

## Risk Flags

| Flag | Severity | Note |
|------|----------|------|
| CPI print ≥4.2% at 8:30 AM | **HIGH** | Could accelerate pre-open equity selloff; QQQ/SPY downside risk |
| US-Iran kinetic escalation | **HIGH** | Oil could spike further if Iran retaliates; Strait of Hormuz closure risk |
| Equity below $100K | **MEDIUM** | Account at $99,961 — alpha -0.71% vs SPY. Needs options income + equity recovery. |
| NVDA $180P Jul17 (if filled) | **LOW** | ~37 DTE, ~10–15% OTM with NVDA in $199–210 range; well-cushioned. Monitor NVDA for any gap below $195. |
| AMZN $245P Jun26 (16 DTE) | **LOW** | Not open. Risk is bot re-submitting too close to ATM — verify exec_open_2026-06-10 does NOT attempt AMZN order today. |

---

*Confirmed data: exec_eod_2026-06-09.md ($99,961.39 equity / $55,174.08 options BP). Live API: unavailable.*

*Sources: [HDFCSky — Brent $92 Jun 10](https://hdfcsky.com/news/brent-crude-oil-price-today-june-10-2026-oil-prices-climb-to-92-as-fresh-hostilities-break-out-in-middle-east) · [TheStreet — S&P futures Jun 10](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-june-10-2026) · [Benzinga — CPI / S&P premarket](https://www.benzinga.com/markets/prediction-markets/26/06/53108294/sp500-june-10-open-up-or-down-polymarket-cpi-inflation-iran-strikes) · [CNBC — Marvell / Huang trillion-dollar](https://www.cnbc.com/2026/06/02/jensen-huang-nvidia-marvell-trillion-dollar-ai.html) · [Axios — Iran deal framework](https://www.axios.com/2026/05/24/iran-deal-strait-hormuz-sanctions-nuclear)*
