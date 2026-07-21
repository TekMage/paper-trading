# Premarket Summary — 2026-07-21

**Generated:** Pre-market (~9:00 AM ET)  
**API status:** UNAVAILABLE (live curl call failed — exec_eod is sole source)  
**Last confirmed equity:** $102,108.69 (from exec_eod_2026-06-18)  
**Market context:** S&P 500 futures +0.45% premarket; chip stocks rallying; Iran-US military situation escalated

---

## ⚠️ CRITICAL: GitHub Actions Gap — 33 Days of Missing Data

**The last exec_eod file is from 2026-06-18.** Today is 2026-07-21. GitHub Actions workflows have not produced an EOD commit in 33 calendar days (~23 trading days). Account state below reflects the June 18 snapshot only — actual positions are unknown.

**Immediate action required:** Check GitHub Actions logs to determine why trading workflows stopped. Verify account state via Alpaca dashboard directly.

---

## Account Snapshot (confirmed as of 2026-06-18)

| | |
|---|---|
| Equity | $102,108.69 |
| Return vs start ($100k) | +2.11% |
| SPY benchmark (at close) | +2.31% ($748.46) |
| Alpha | -0.21% |
| Options BP remaining | $73,470.00 |
| Account floor | $87,500 |

> **Note:** These are 33 trading days stale. Actual equity and positions are unknown until the Alpaca dashboard is checked manually.

---

## Current Positions (as of exec_eod 2026-06-18 — STALE)

**Layer 1 — Core ETFs (target state per CLAUDE.md):**
- QQQ: 50 shares (target)
- SPY: 13 shares (target)
- JETS: 80 shares (target)
- XLE: 100 shares (target — see Iran/Oil section)
- XLY: **REMOVED** — force-close was in progress as of June sprint

**Layer 2 — CSPs (status UNKNOWN — must verify live):**
- NVDA $190P Jul18: **EXPIRED** — expiry was July 18, 2026 (3 days ago). Assignment or expiry worthless — unknown.
- AMZN $215P: Status unknown — contract may still be open or have rolled.
- QQQ calls (Layer 2b): Status unknown.

> TSLA, INTC are NOT strategy targets. Do not re-enter.

---

## Iran / Oil Status — ACTION REQUIRED

| Item | Status |
|---|---|
| Iran-US MOU signed? | **YES — signed June 17, 2026** |
| Current Iran situation | US has conducted 10 consecutive nights of airstrikes on Iran as of July 21. Ceasefire mediators pushing for 10-day pause. Hormuz commercial traffic severely curtailed. |
| Brent crude (July 21 AM) | **~$89.93/barrel** (sources vary: $88.56–$89.93) |
| Distance from $90 trim trigger | **At or within $0.07 of trigger** |
| Distance from $85 exit trigger | ~$5 above |

### Iran MOU Trigger
The MOU was signed June 17 — the day before the last EOD file. The June 18 EOD noted "No actions needed," suggesting the XLE sell was not executed at that time. **The MOU trigger (sell 60 XLE immediately) has not been confirmed as actioned.** With US now actively striking Iran and Hormuz traffic disrupted, the oil thesis is highly uncertain — XLE could spike (supply disruption) or crash (demand destruction/deal). **Manual review of XLE position and Iran trigger status is required.**

---

## Manual Triggers to Monitor Today

| Trigger | Status |
|---|---|
| Brent ≤ $90 → sell 30 XLE at market | **IMMINENT — Brent ~$89.93, essentially at trigger** |
| Brent ≤ $85 → exit all XLE | ~$5 away |
| Iran MOU signed → sell 60 XLE immediately | MOU signed June 17 — **confirm if this was executed** |
| JETS ≥ $35.69 (+30% from $27.45) → close all 80 JETS | JETS price unknown — check vs threshold |

---

## Morning Priority Actions (Human Required)

1. **Check Alpaca dashboard NOW** — 33 days of account state are dark. Verify equity, all positions, and any option assignments or expirations (especially NVDA Jul18 $190P which expired 3 days ago).

2. **Confirm Iran MOU trigger was actioned (or wasn't)** — The MOU was signed June 17. If 60 XLE shares were not sold at that time, decide whether to sell now given active US-Iran military strikes and Hormuz disruption.

3. **Brent crude is at $89.93 — decide on the $90 XLE trim** — The $90 trigger (sell 30 XLE) is essentially here. With the Hormuz situation active, this could gap above or below quickly. Manual call needed.

4. **Diagnose GitHub Actions failure** — Check `.github/workflows/` logs to understand why trading-open, trading-midday, and trading-eod have not committed since June 18.

---

## Risk Flags

- **DATA GAP (HIGH):** 33 trading days of unknown account activity. Options may have been assigned, positions may have changed, equity is unknown.
- **NVDA $190P Jul18 EXPIRED (HIGH):** This contract expired July 18. If NVDA was below $190 at expiry, 100 shares were assigned (~$19,000 cost). Need to confirm.
- **Brent at $90 trigger (HIGH):** XLE trim trigger is effectively here. Hormuz disruption adds volatility in both directions.
- **Iran MOU vs active strikes (MEDIUM):** MOU signed June 17 but US-Iran military conflict has resumed/continued. The geopolitical picture is more complex than the simple "MOU signed → sell XLE" rule captured.
- **JETS price vs trigger (MEDIUM):** JETS at $35.69 is the exit signal. Price unknown — check before open.
- **GitHub Actions dark (HIGH):** Automation is not running. All strategy execution requires manual intervention or debugging.

---

## Semiconductor Context (informational)

- NVDA maintaining ~80% AI accelerator market share; data center revenue $193.7B FY2026
- AMD surged 186% in Q2 2026; $60B Meta deal for MI400 series
- Philadelphia Semiconductor Index +47% YTD
- Chip stocks leading premarket rally today

> If NVDA Jul18 put expired worthless (NVDA well above $190), the premium was kept. If assigned, 100 NVDA shares now sit in the account.
