# Premarket Summary — 2026-06-04

| | |
|---|---|
| **API Status** | UNAVAILABLE (paper API unreachable this morning) |
| **Last Confirmed Equity** | $101,589.93 (from exec_eod_2026-06-03) |
| **Options BP Remaining** | $49,465.40 |
| **Market Context** | S&P futures -0.5%; tech under pressure after Broadcom revenue miss |

---

## Account Snapshot

| Metric | Value |
|--------|-------|
| Equity | $101,589.93 |
| Our return (since inception) | +1.59% |
| SPY benchmark return | +3.00% |
| Alpha | -1.41% |
| Options BP remaining | $49,465.40 |

*All figures from exec_eod_2026-06-03 — authoritative GitHub Actions data.*

---

## Current Positions

### Layer 1 — Core ETFs (GitHub Actions maintains these)

| Symbol | Shares | Notes |
|--------|--------|-------|
| QQQ | 45 | Watch: tech weakness from AVGO miss |
| SPY | 13 | Futures -0.5% premarket |
| XLY | 40 | Consumer discretionary; futures drag |
| JETS | 80 | Monitor vs. $35.69 exit trigger |
| XLE | 100 | **Active watch — Iran/oil triggers below** |

### Layer 2 — Open CSPs

exec_eod Actions section shows "No actions needed" but does not explicitly confirm open positions. Current CSP targets per strategy:

- **NVDA $190P** — status unconfirmed from EOD; tech selloff (AVGO -13%) may pressure NVDA today
- **AMZN $245P** — status unconfirmed from EOD

*No other CSP targets are in the strategy. Confirm open/closed status via Alpaca dashboard.*

---

## Iran / Oil Status

### MOU Signed? **NO — still in negotiation**

As of overnight reporting, no MOU has been signed. The deal framework is reportedly close:
- 60-day ceasefire extension proposed
- Strait of Hormuz would become "unrestricted" (30 days to clear mines)
- Iran would be allowed to freely sell oil
- Iran commits not to build nuclear weapon; enrichment talks deferred

**Key risk:** If the MOU signs today or this week, it immediately unlocks Iran oil supply and could push Brent down $5–10 in a session, potentially triggering XLE trim/exit levels.

### Brent Crude

| | |
|---|---|
| **Current price** | ~$96.97/bbl (June 4 morning) |
| **$90 trim trigger** | $6.97 away (-7.2% move needed) |
| **$85 exit trigger** | $11.97 away (-12.3% move needed) |

Brent fell 0.86% overnight from $101.36 on June 3. The trend is down. An Iran MOU announcement could accelerate the move toward $90 in a single session.

---

## Manual Triggers to Monitor Today

| Trigger | Action Required |
|---------|----------------|
| Brent ≤ **$90.00** | Sell 30 XLE at market (manual) |
| Brent ≤ **$85.00** | Exit all 100 XLE at market (manual) |
| Iran MOU **signed** | Sell 60 XLE immediately (manual) |
| JETS ≥ **$35.69** (+30% from $27.45 cost) | Close all 80 JETS at market (manual) |

---

## Morning Priority Actions

1. **Watch Iran headlines** — MOU signing is the highest-impact single event. If announced, sell 60 XLE before the oil price fully reprices. Keep a tab open on news (Axios, CNBC). A signed MOU could push Brent from $97 toward $90 quickly.

2. **Confirm open CSP positions** — exec_eod did not explicitly list open NVDA or AMZN CSPs. Log into Alpaca paper dashboard to verify which contracts are open and their current P&L. Tech is weak today (AVGO -13%, CRWD -10%); check NVDA direction before any new CSP writing.

3. **Monitor JETS intraday** — current price unknown; verify vs. $35.69 exit trigger. Airline sector may move on any Iran/Hormuz resolution news (reopened strait = lower jet fuel costs = JETS bullish).

---

## Risk Flags

- **Tech sector weakness** — Broadcom (AVGO) -13% after revenue miss; CrowdStrike (CRWD) -10% on weak guidance. S&P futures -0.5%. QQQ and XLY positions will feel this at open.
- **Marvell (MRVL) +32% on June 2** — Jensen Huang "next trillion-dollar company" call; if holding any MRVL-adjacent positions or NVDA CSPs, note the AI sentiment remains bifurcated.
- **Brent declining trend** — down from $101 (June 3) to $97 (June 4). The direction is toward triggers. Iran deal risk is asymmetric: no deal = oil stays up; deal signed = sharp drop possible.
- **Alpha lag** — account is -1.41% vs SPY since inception. No immediate action, but worth tracking if alpha continues to erode through next week.
- **API unavailable** — cannot confirm live position values or option marks. All position data is T-1 from exec_eod.

---

*Sources: exec_eod_2026-06-03 (authoritative), Axios/CNBC/Al Jazeera (Iran deal), TradingEconomics/Fortune (Brent crude), Bloomberg/Benzinga (S&P futures), CNBC/Yahoo Finance (MRVL/AVGO semiconductor news)*
