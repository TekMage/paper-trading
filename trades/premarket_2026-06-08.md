# Pre-Market Summary — 2026-06-08 (Monday)

| | |
|---|---|
| **API Status** | UNAVAILABLE (paper-api.alpaca.markets unreachable) |
| **Last Confirmed Equity** | $99,624.68 (exec_eod 2026-06-05) |
| **Options BP Remaining** | $72,742.74 |
| **Market Context** | S&P 500 futures +0.6% premarket; Brent surges 4.93% on Israel-Iran missile exchange over weekend |

---

## Account Snapshot (from exec_eod 2026-06-05)

| Metric | Value |
|---|---|
| Equity | $99,624.68 |
| Options BP Used | ~$27,257 |
| Options BP Remaining | $72,742.74 |
| Our Return (EOD Fri) | -0.38% |
| SPY Return (EOD Fri) | +0.40% |
| Alpha | -0.78% |

---

## Current Positions

### Layer 1 — Core ETFs (all at target; GitHub Actions maintains)

| Symbol | Shares | Notes |
|---|---|---|
| QQQ | 45 | At target |
| SPY | 13 | At target |
| XLY | 40 | At target |
| JETS | 80 | At target; monitor $35.69 close trigger |
| XLE | 100 | At target; Brent $97.68 well above sell thresholds |

### Layer 2 — Open CSPs

EOD actions section: "No actions needed." No specific CSPs listed as opened/closed in Friday's EOD.
Active CSP targets per strategy: **NVDA $190P** and **AMZN $245P**.
Options BP usage (~$27k) suggests at least one CSP is likely open — verify via Alpaca dashboard when API is available.

---

## Iran / Oil Status

**MOU signed? NO**

The MOU remains unsigned. As of early June, Trump sent the draft back to Iran demanding amendments requiring: (1) a clear timeline on nuclear commitments, and (2) explicit language that Iran ends Strait of Hormuz control immediately upon signing. Over the **weekend (June 7–8), Iran and Israel exchanged missile strikes**, severely damaging ceasefire prospects and pushing Brent sharply higher.

| | |
|---|---|
| **Brent Crude (June 8)** | ~$97.68 / bbl (+4.93% today) |
| **Distance from $90 trim trigger** | +$7.68 above — NO trim trigger active |
| **Distance from $85 exit trigger** | +$12.68 above — NO exit trigger active |

**XLE outlook:** Elevated oil from Hormuz disruption and failed ceasefire benefits XLE. Sell triggers ($90/$85) would only activate on a significant oil price decline — unlikely today given escalation. XLE is a tailwind, not a risk, in this environment.

---

## Manual Triggers to Monitor Today

| Trigger | Level | Action Required | Status |
|---|---|---|---|
| Brent ≤ $90 | ~$7.68 below current | Sell 30 XLE at market | **INACTIVE** — Brent rising |
| Brent ≤ $85 | ~$12.68 below current | Exit all 100 XLE | **INACTIVE** |
| Iran MOU signed | — | Sell 60 XLE immediately | **INACTIVE** — deal stalled |
| JETS ≥ $35.69 | +30% from $27.45 cost | Close all 80 JETS | Monitor — verify JETS price |

---

## Morning Priority Actions

1. **Verify open CSP positions** — API was unavailable at summary time. Log into Alpaca dashboard to confirm whether NVDA $190P and/or AMZN $245P are open, and check their current P&L given Monday's premarket moves.

2. **Monitor JETS price at open** — High oil ($97.68) is a headwind for airlines. Confirm JETS hasn't approached the $35.69 close trigger (would be unusual given oil pressure, but verify). Also watch for a gap down open given fuel cost concerns.

3. **Watch Iran ceasefire headlines intraday** — Weekend missile exchange between Iran and Israel makes the MOU signing less likely near-term, but any sudden peace breakthrough could spike the MOU signing risk and trigger the "sell 60 XLE immediately" rule. Keep a news tab open.

---

## Risk Flags

- **Israel-Iran escalation** — Weekend missile exchange raises risk of broader conflict; Hormuz closure sustained or worsened. XLE benefits but JETS faces fuel cost headwinds.
- **API unavailable** — Cannot confirm exact open CSP positions or current mark-to-market. Account state is 3 business days stale (last EOD: 2026-06-05).
- **Alpha lag** — Account underperformed SPY by -0.78% on Friday. Monitor whether this persists as a trend.
- **MRVL S&P 500 addition** — Marvell added to S&P 500 index, premarket +9%. Jensen Huang called MRVL "next trillion-dollar company" on June 2 (NVDA announced $2B investment in MRVL). Positive read-through for NVDA sentiment; NVDA $190P CSP gains additional cushion if NVDA lifts with MRVL momentum.

---

## Market Intelligence

- **S&P 500 futures**: +0.6% premarket — modest recovery from Friday's slide despite Middle East tensions
- **Brent crude**: $97.68 (+4.93%) — driven by Iran-Israel strikes threatening ceasefire
- **MRVL**: +9% premarket ($287.05) on S&P 500 index inclusion; semiconductor sector broadly positive
- **NVDA**: Benefiting from MRVL halo effect; Jensen Huang's AI infrastructure comments remain a sector catalyst
- **Iran deal timeline**: 60-day framework discussed but unsigned; Trump's amendment demands and weekend escalation push timeline further out

---

*Sources: exec_eod_2026-06-05.md (authoritative account state), Alpaca paper API (unavailable), web search 2026-06-08*
