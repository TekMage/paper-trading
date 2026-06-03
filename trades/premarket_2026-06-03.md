# Premarket Summary — 2026-06-03

| | |
|---|---|
| **API Status** | UNAVAILABLE (paper API unreachable this session) |
| **Last Confirmed Equity** | $102,322.28 (exec_eod 2026-06-02) |
| **Options BP Remaining** | $49,686.57 |
| **Market Context** | S&P 500 hit all-time high above 7,600 yesterday; futures slightly soft (-0.10%) on Iran/Middle East tension |

---

## Account Snapshot (from exec_eod 2026-06-02)

| Metric | Value |
|---|---|
| Equity | $102,322.28 |
| Our Return | +2.32% |
| SPY Return | +3.89% ($760.00) |
| Alpha | -1.57% |
| Options BP Remaining | $49,686.57 |
| EOD Actions | None needed |

---

## Current Positions

### Layer 1 — Core ETFs (all at target, GitHub Actions maintains)

| Symbol | Shares | Notes |
|---|---|---|
| QQQ | 45 | — |
| SPY | 13 | — |
| XLY | 40 | — |
| JETS | 80 | ~$28.54 premarket; $35.69 close trigger (+30%) |
| XLE | 100 | **High risk** — Iran/Brent trigger watch today |

### Layer 2 — Open CSPs

exec_eod shows no actions needed; no open CSPs explicitly enumerated. API unavailable for live options check.

Confirmed strategy targets (only these are in scope):
- **NVDA $190P** — NVDA ~$224 premarket (+0.61%), Computex catalysts fresh; constructive for premium selling
- **AMZN $245P** — AMZN ~$256–261 range; Prime Day June 23–26 as near-term catalyst

---

## Iran / Oil Status

| | |
|---|---|
| **Iran MOU signed?** | **NO** — Deal largely negotiated but awaiting Trump's final sign-off; Iranian state media unconfirmed |
| **Brent crude** | ~**$96.89/bbl** (session range ~$92.87–$97.36) |
| **vs. $90 trim trigger** | +$6.89 above — no XLE trim triggered yet |
| **vs. $85 exit trigger** | +$11.89 above — no XLE exit triggered yet |
| **Key risk** | If MOU signs today, Brent could drop rapidly through both thresholds in sequence |

**Context:** U.S. struck Iran's Qeshm Island recently, adding geopolitical risk premium. Deal is close but not done. Oil is elevated and volatile — the asymmetric risk is a sudden drop if deal closes, not a gradual drift.

---

## Manual Triggers to Monitor Today

| Trigger | Condition | Action Required |
|---|---|---|
| Iran MOU signed | Any confirmation | **Sell 60 XLE at market immediately** |
| Brent ≤ $90 | Watch intraday | **Sell 30 XLE at market** |
| Brent ≤ $85 | Watch intraday | **Exit all XLE** |
| JETS ≥ $35.69 | +30% from $27.45 cost | **Close all 80 JETS** |

---

## Morning Priority Actions

1. **Iran MOU watch (highest priority)** — Deal close but unsigned. A signing could send Brent through $90 and $85 in a single move. Be ready to execute the 60-share XLE sell immediately, then the tiered exits if price keeps falling. Do NOT wait for confirmation — act on first credible report of MOU signing.

2. **Brent crude intraday monitoring** — Currently $97, elevated on risk premium. Watch for any Iran news that could compress the risk premium. The $90 trim and $85 full-exit triggers are ~$7 and ~$12 away respectively — achievable in a volatile session.

3. **NVDA CSP consideration** — NVDA at ~$224 with Computex catalysts (Vera CPU, Vera Rubin in full production, $5T market cap). Options BP is $49,686. If opening a new NVDA $190P CSP, current environment is constructive — stock has bullish momentum and the strike is ~15% OTM.

---

## Risk Flags

- **XLE Iran risk (HIGH)** — 100 shares of XLE exposed to a sudden oil price drop if Iran MOU signs. The drop could be fast and large, potentially requiring rapid sequential execution of multiple triggers. Have the sell orders ready.
- **JETS fuel cost headwind** — With Brent at $97, airline margins are compressed. JETS at ~$28.54 vs. $35.69 target; no immediate close trigger but monitor if oil stays high.
- **Alpha drag** — -1.57% alpha vs. SPY yesterday. Market is running on AI/tech momentum (S&P 500 new ATH); core ETF holdings tracking but not beating.
- **API unavailable** — Cannot confirm live options positions this session. exec_eod is authoritative; GitHub Actions will handle any needed reconciliation at next EOD.
- **Geopolitical volatility** — U.S. strikes on Qeshm Island add tail risk beyond the Iran deal narrative. Middle East situation is fluid.
