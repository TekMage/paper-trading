# Premarket Summary — 2026-06-17

| | |
|---|---|
| **API Status** | UNAVAILABLE (network-blocked in this environment) |
| **Last Confirmed Equity** | $102,149.58 (exec_eod_2026-06-16) |
| **Our Return** | +2.15% since May 7 |
| **SPY Return** | +2.60% ($750.58) |
| **Alpha** | -0.45% |
| **Options BP Remaining** | $73,413.00 |
| **Market Context** | S&P 500 futures +0.28% premarket; Fed rate decision at 2:00 PM ET today |

---

## ⚠️ CRITICAL MANUAL ACTION REQUIRED — XLE TRIGGERS ACTIVE

**ALL THREE XLE exit conditions have been triggered simultaneously:**

1. **Iran MOU SIGNED** (June 16, 2026) — US and Iran electronically signed MOU; Strait of Hormuz reopening → **Sell 60 XLE at market immediately (manual trigger)**
2. **Brent ≤ $90** — Brent at ~$79.45 → **Sell 30 XLE at market (triggered)**
3. **Brent ≤ $85** — Brent at ~$79.45 → **Exit ALL remaining XLE (triggered)**

The Brent ≤ $85 / Iran MOU conditions together mean the strategy calls for **exiting the full 100-share XLE position**. XLE last price: ~$55.40. Manual execution required — bot does not auto-execute these.

---

## Account Snapshot (exec_eod_2026-06-16 — authoritative)

| Metric | Value |
|---|---|
| Equity | $102,149.58 |
| Return since May 7 | +2.15% |
| SPY benchmark | +2.60% ($750.58) |
| Alpha | -0.45% |
| Options BP remaining | $73,413.00 |
| Account floor | $87,500 (bot halts new positions below this) |

---

## Current Positions (from exec files)

**Layer 1 — Core ETFs (GitHub Actions maintains these):**
- QQQ: 50 shares (rebalanced June 12)
- SPY: 13 shares
- JETS: 80 shares (~$30.78; below $35.69 trigger)
- XLE: 100 shares (~$55.40) — **ALL EXIT TRIGGERS ACTIVE**
- XLY: closing in progress (June sprint exit via FORCE_CLOSE_EQUITY)
- SPCX: closed June 16 at +21.3% profit

**Layer 2 — Open CSPs:**
- **None currently open.** AMZN 220P Jul17 and NVDA 180P Jul17 both closed June 15 at 50% profit.
- Bot will attempt to open new CSPs at today's 9:30 AM open session:
  - NVDA $190P Jul18 (~14% OTM target)
  - AMZN $215P (~14% OTM target)
  - Requires premium ≥ $1.50, DTE 25–60 days, CSP_MIN_PREMIUM filter applies
- Options BP available for new CSPs: $73,413

**Layer 2b — QQQ Calls (June Alpha):**
- Bot will buy 1x QQQ call contract (2% OTM, DTE 10–20) at open if no long QQQ options held

---

## Iran / Oil Status

| Item | Status |
|---|---|
| Iran MOU signed? | **YES — Signed electronically June 16, 2026** |
| MOU details | Ends fighting, lifts US naval blockade; Hormuz to reopen within 30 days; 60-day window for nuclear technical agreement |
| Brent crude (June 17) | **~$79.45/bbl** |
| Distance from $90 trim trigger | **$10.55 BELOW — TRIGGERED** |
| Distance from $85 exit trigger | **$5.55 BELOW — TRIGGERED** |
| XLE price | ~$55.40 (52wk range: $42.05–$63.46) |

Brent fell to three-month lows ~$79 on expectations of increased Iranian oil supply following the peace agreement. This validates the original Iran/oil thesis — the thesis has now played out.

---

## Manual Triggers Status

| Trigger | Status | Action Required |
|---|---|---|
| Brent ≤ $90 → sell 30 XLE | **TRIGGERED** ($79.45) | Manual — sell 30 XLE at market |
| Brent ≤ $85 → exit all XLE | **TRIGGERED** ($79.45) | Manual — sell remaining 70 XLE at market |
| Iran MOU signed → sell 60 XLE | **TRIGGERED** (June 16) | Manual — sell 60 XLE at market |
| JETS ≥ $35.69 → close 80 JETS | Not triggered ($30.78) | No action |

**Net conclusion: Exit full 100-share XLE position.** The $85 Brent trigger supersedes the $90 trigger; combined with the Iran MOU trigger, both call for full XLE exit. XLE ~$55.40 × 100 shares = ~$5,540 in proceeds to redeploy.

---

## Morning Priority Actions

1. **[URGENT — PRE-OPEN] Exit 100 shares XLE at market open.** All three manual exit conditions are active. XLE ~$55.40. The original Iran/oil thesis has concluded; Brent is $5.55 below the full-exit threshold. Execute at or shortly after 9:30 AM ET.

2. **[MONITOR — 2:00 PM ET] Fed rate decision.** S&P futures mildly positive (+0.28%) pre-open. Market positioning for potential hold or cut. Watch for volatility around 2 PM that could affect CSP fills and QQQ call position value.

3. **[VERIFY] Confirm new CSPs open correctly.** Bot will attempt NVDA $190P and AMZN $215P at open. With $73K options BP available this is well within capacity. Check exec_open_2026-06-17.md post-open to confirm fills; CSPs may not fill if premium < $1.50 or no contract in DTE window.

---

## Risk Flags

- **XLE thesis concluded — exit risk increases if held:** Brent already at $79; Iran supply coming back online over next 30 days could push Brent lower still. Holding XLE past today adds downside exposure with no upside thesis.
- **Fed decision volatility (2 PM ET):** Any QQQ call position opened this morning will face potential IV crush or directional risk around the Fed announcement. Short-dated calls (DTE 10–20) are especially sensitive.
- **Alpha lag persists:** Account is -0.45% alpha vs SPY. XLE drag is likely a contributor; exiting XLE and redeploying into options premium may help close the gap.
- **No open CSPs overnight:** Options BP is fully deployed in cash ($73K available). New CSPs at open will put that to work; confirm bot targets correct strikes given recent IV environment.

---

*Generated by pre-market routine — exec_eod_2026-06-16.md (authoritative). Live API unavailable from this environment; use Alpaca MCP or local dry-run to verify live positions.*
