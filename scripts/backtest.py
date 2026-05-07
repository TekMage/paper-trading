#!/usr/bin/env python3
"""
Backtest: Two-Month Paper Trading Simulation
Period: March 9, 2026 – May 7, 2026 (nearest trading days to March 7–May 7)
Strategy: Core ETFs + Wheel (simulated options) + Opportunistic momentum
Starting Capital: $100,000
"""

import json
from datetime import datetime, date
from collections import defaultdict

# ─────────────────────────────────────────────
# 1. Load price data
# ─────────────────────────────────────────────
with open('/tmp/bars.json') as f:
    raw = json.load(f)

bars_raw = raw['bars']

# Build: {ticker: {date_str: close_price}}
prices = {}
for ticker, bar_list in bars_raw.items():
    prices[ticker] = {}
    for bar in bar_list:
        d = bar['t'][:10]
        prices[ticker][d] = bar['c']

# All trading dates, sorted
all_dates = sorted(prices['SPY'].keys())

print("=" * 70)
print("BACKTEST: March–May 2026 Paper Trading Simulation")
print("=" * 70)
print(f"Trading days in dataset: {len(all_dates)}")
print(f"First trading day: {all_dates[0]}")
print(f"Last trading day:  {all_dates[-1]}")
print()

# ─────────────────────────────────────────────
# 2. Day-1 prices (first available trading day)
# ─────────────────────────────────────────────
DAY1 = all_dates[0]  # 2026-03-09

print(f"Day 1 (entry date): {DAY1}")
print()
print("Day-1 Closing Prices:")
print("-" * 40)
for t in ['SPY', 'QQQ', 'XLE', 'ITA', 'USO', 'XOP', 'NVDA', 'TSLA', 'TSM', 'AMZN', 'INTC', 'DRAM', 'MU', 'AVGO']:
    p = prices.get(t, {}).get(DAY1, None)
    print(f"  {t:<8}: ${p:.2f}" if p else f"  {t:<8}: N/A")
print()

# ─────────────────────────────────────────────
# 3. Layer 1 — Core ETF holdings
# ─────────────────────────────────────────────
LAYER1 = {
    'QQQ': 28,
    'XLE': 268,
    'ITA': 44,
    'SPY': 13,
}

layer1_cost = sum(LAYER1[t] * prices[t][DAY1] for t in LAYER1)
print("Layer 1 — Core ETFs (Day 1 Cost):")
print("-" * 40)
for t, shares in LAYER1.items():
    cost = shares * prices[t][DAY1]
    print(f"  {t:<6} {shares:>4} shares × ${prices[t][DAY1]:.2f} = ${cost:,.2f}")
print(f"  {'TOTAL':<6}{'':>4}        {'':>10}  ${layer1_cost:,.2f}")
print()

# ─────────────────────────────────────────────
# 4. Layer 3 — Opportunistic trades
# ─────────────────────────────────────────────
# USO: 50 shares, bought Day 1, sold last trading day of March
# XOP: 30 shares, bought April 1, sold last trading day of April

march_dates = [d for d in all_dates if d.startswith('2026-03')]
april_dates = [d for d in all_dates if d.startswith('2026-04')]

uso_entry_date = DAY1           # March 9 (nearest to March 7)
uso_exit_date  = march_dates[-1]  # Last trading day of March = 2026-03-31

xop_entry_date = april_dates[0]    # First trading day of April = 2026-04-01
xop_exit_date  = april_dates[-1]   # Last trading day of April = 2026-04-30

uso_entry_price = prices['USO'][uso_entry_date]
uso_exit_price  = prices['USO'][uso_exit_date]
xop_entry_price = prices['XOP'][xop_entry_date]
xop_exit_price  = prices['XOP'][xop_exit_date]

uso_cost   = 50 * uso_entry_price
xop_cost   = 30 * xop_entry_price
uso_pnl    = 50 * (uso_exit_price - uso_entry_price)
xop_pnl    = 30 * (xop_exit_price - xop_entry_price)

print("Layer 3 — Opportunistic Momentum Trades:")
print("-" * 40)
print(f"  USO  50 shares: Entry {uso_entry_date} @ ${uso_entry_price:.2f}  →  Exit {uso_exit_date} @ ${uso_exit_price:.2f}")
print(f"         PnL: ${uso_pnl:+,.2f}  ({(uso_exit_price/uso_entry_price - 1)*100:+.2f}%)")
print(f"  XOP  30 shares: Entry {xop_entry_date} @ ${xop_entry_price:.2f}  →  Exit {xop_exit_date} @ ${xop_exit_price:.2f}")
print(f"         PnL: ${xop_pnl:+,.2f}  ({(xop_exit_price/xop_entry_price - 1)*100:+.2f}%)")
print()

# ─────────────────────────────────────────────
# 5. Cash accounting
# ─────────────────────────────────────────────
STARTING_CAPITAL = 100_000.00
CASH_RESERVE     = 5_000.00      # Layer 4: always uninvested
WHEEL_BACKING    = 45_000.00     # Layer 2: cash backing for CSPs

# Liquid cash after Layer 1 buy on Day 1
# Remaining = 100k - Layer1 cost - cash_reserve - wheel_backing
# (USO and XOP funded from non-reserved pool)
deployed_start = layer1_cost + uso_cost   # Day 1 deployment
residual_cash = STARTING_CAPITAL - layer1_cost - uso_cost - CASH_RESERVE - WHEEL_BACKING

print("Capital Allocation on Day 1:")
print("-" * 40)
print(f"  Starting capital:          ${STARTING_CAPITAL:>10,.2f}")
print(f"  Layer 1 ETF cost:         -${layer1_cost:>10,.2f}")
print(f"  Layer 3 USO cost (Day 1): -${uso_cost:>10,.2f}")
print(f"  Cash reserve (Layer 4):   -${CASH_RESERVE:>10,.2f}")
print(f"  Wheel backing (Layer 2):  -${WHEEL_BACKING:>10,.2f}")
print(f"  Residual free cash:        ${residual_cash:>10,.2f}")
print()

# ─────────────────────────────────────────────
# 6. Options income (Layer 2) — simulated
# ─────────────────────────────────────────────
# Base: 2% of $45k/month = $900/month
# Boost: TSLA + NVDA at 3%/month on $5k each = $150/month extra each = $300/month extra
# Total: $900 base + $300 boost = $1,200/month
# Over 2 months = $2,400 total

BASE_OPTIONS_MONTHLY  = 900.00    # 2% of $45k
BOOST_OPTIONS_MONTHLY = 300.00    # 3% × $5k TSLA + 3% × $5k NVDA
TOTAL_OPTIONS_MONTHLY = BASE_OPTIONS_MONTHLY + BOOST_OPTIONS_MONTHLY
TOTAL_OPTIONS_INCOME  = TOTAL_OPTIONS_MONTHLY * 2   # 2 months

# Accrue daily across trading days within each month
# Month 1 = March trading days, Month 2 = April trading days
# Note: May days accrued from May-month options cycle (partial)
all_may_dates = [d for d in all_dates if d.startswith('2026-05')]

month_days = {
    '2026-03': march_dates,
    '2026-04': april_dates,
    '2026-05': all_may_dates,
}

# Daily options accrual per trading day in month
options_daily_income = {}
for month_key in ['2026-03', '2026-04']:
    n_days = len(month_days[month_key])
    daily = TOTAL_OPTIONS_MONTHLY / n_days
    for d in month_days[month_key]:
        options_daily_income[d] = daily

# May: no additional options income (only 2 full months in scope)
for d in all_may_dates:
    options_daily_income[d] = 0.0

# ─────────────────────────────────────────────
# 7. Daily portfolio valuation
# ─────────────────────────────────────────────
portfolio_values = []
cumulative_options_income = 0.0

# XOP deployment: on April 1, buy 30 shares; need cash for it
# That cash comes from residual_cash (post Day 1)
xop_cash_impact = 0.0   # track when XOP is bought / sold

for i, d in enumerate(all_dates):
    # Layer 1 value
    l1_value = sum(LAYER1[t] * prices[t].get(d, prices[t][all_dates[max(0, i-1)]]) for t in LAYER1)

    # Layer 3: USO (held March 9 – March 31)
    if uso_entry_date <= d <= uso_exit_date:
        uso_value = 50 * prices['USO'].get(d, prices['USO'][uso_entry_date])
    else:
        uso_value = 0.0

    # Layer 3: XOP (held April 1 – April 30)
    if xop_entry_date <= d <= xop_exit_date:
        xop_value = 30 * prices['XOP'].get(d, prices['XOP'][xop_entry_date])
    else:
        xop_value = 0.0

    # Cash position
    # Starts at residual_cash
    # On xop_entry_date: deduct xop_cost from residual (already done by value approach)
    # On uso_exit_date: USO converts to cash (uso_exit_price × 50)
    # On xop_exit_date: XOP converts to cash (xop_exit_price × 30)
    # Simpler: track cash as explicit running balance
    if i == 0:
        cash_balance = residual_cash
        xop_deployed = False
        uso_liquidated = False
        xop_liquidated = False
    else:
        if d == xop_entry_date and not xop_deployed:
            cash_balance -= xop_cost
            xop_deployed = True
        if d > uso_exit_date and not uso_liquidated:
            cash_balance += uso_exit_price * 50
            uso_liquidated = True
        if d > xop_exit_date and not xop_liquidated:
            cash_balance += xop_exit_price * 30
            xop_liquidated = True

    # Accrued options income
    cumulative_options_income += options_daily_income.get(d, 0.0)

    # Total portfolio
    total = l1_value + uso_value + xop_value + cash_balance + CASH_RESERVE + WHEEL_BACKING + cumulative_options_income

    portfolio_values.append({
        'date': d,
        'l1': l1_value,
        'uso': uso_value,
        'xop': xop_value,
        'cash': cash_balance + CASH_RESERVE,
        'wheel_cash': WHEEL_BACKING,
        'options_income': cumulative_options_income,
        'total': total,
    })

# ─────────────────────────────────────────────
# 8. SPY Benchmark (SPY × 100k equivalent)
# ─────────────────────────────────────────────
spy_day1_price = prices['SPY'][DAY1]
spy_shares_bench = STARTING_CAPITAL / spy_day1_price  # notional shares to replicate $100k

spy_values = []
for d in all_dates:
    spy_values.append({
        'date': d,
        'value': spy_shares_bench * prices['SPY'][d],
    })

# ─────────────────────────────────────────────
# 9. Summary Statistics
# ─────────────────────────────────────────────
port_start = portfolio_values[0]['total']
port_end   = portfolio_values[-1]['total']
spy_start  = spy_values[0]['value']
spy_end    = spy_values[-1]['value']

port_return_pct = (port_end - port_start) / port_start * 100
spy_return_pct  = (spy_end  - spy_start)  / spy_start  * 100
alpha_pct       = port_return_pct - spy_return_pct

# Max drawdown
peak = portfolio_values[0]['total']
max_dd = 0.0
max_dd_peak_date = all_dates[0]
max_dd_trough_date = all_dates[0]
temp_peak = peak
temp_peak_date = all_dates[0]
for pv in portfolio_values:
    if pv['total'] > temp_peak:
        temp_peak = pv['total']
        temp_peak_date = pv['date']
    dd = (pv['total'] - temp_peak) / temp_peak * 100
    if dd < max_dd:
        max_dd = dd
        max_dd_peak_date = temp_peak_date
        max_dd_trough_date = pv['date']

# Daily returns
daily_returns = []
for i in range(1, len(portfolio_values)):
    r = (portfolio_values[i]['total'] - portfolio_values[i-1]['total']) / portfolio_values[i-1]['total'] * 100
    daily_returns.append((all_dates[i], r))

best_day  = max(daily_returns, key=lambda x: x[1])
worst_day = min(daily_returns, key=lambda x: x[1])

import statistics
if len(daily_returns) > 1:
    returns_only = [r for _, r in daily_returns]
    avg_daily = statistics.mean(returns_only)
    std_daily = statistics.stdev(returns_only)
    # Annualized Sharpe-like (252 trading days, 0% risk-free simplification)
    sharpe = (avg_daily / std_daily) * (252 ** 0.5) if std_daily > 0 else 0.0
else:
    sharpe = 0.0

print("=" * 70)
print("PERFORMANCE SUMMARY")
print("=" * 70)
print(f"{'Metric':<35} {'Portfolio':>15} {'SPY Bench':>15}")
print("-" * 65)
print(f"{'Starting Value':<35} ${port_start:>14,.2f} ${spy_start:>14,.2f}")
print(f"{'Ending Value':<35} ${port_end:>14,.2f} ${spy_end:>14,.2f}")
print(f"{'Total Return':<35} {port_return_pct:>14.2f}% {spy_return_pct:>14.2f}%")
print(f"{'Total P&L ($)':<35} ${port_end-port_start:>14,.2f} ${spy_end-spy_start:>14,.2f}")
print(f"{'Alpha (vs SPY)':<35} {alpha_pct:>14.2f}%")
print(f"{'Max Drawdown':<35} {max_dd:>14.2f}%")
print(f"{'Best Day':<35} {best_day[0]:>15} ({best_day[1]:+.2f}%)")
print(f"{'Worst Day':<35} {worst_day[0]:>15} ({worst_day[1]:+.2f}%)")
print(f"{'Annualized Sharpe (approx)':<35} {sharpe:>14.3f}")
print()

# ─────────────────────────────────────────────
# 10. Monthly Breakdown
# ─────────────────────────────────────────────
print("=" * 70)
print("MONTHLY BREAKDOWN")
print("=" * 70)

for month_label, month_dates in [('March 2026', march_dates), ('April 2026', april_dates), ('May 2026 (partial)', all_may_dates)]:
    if not month_dates:
        continue
    # Find portfolio values at start and end of month
    start_val = next(pv['total'] for pv in portfolio_values if pv['date'] == month_dates[0])
    end_val   = next(pv['total'] for pv in portfolio_values if pv['date'] == month_dates[-1])
    spy_sv    = next(sv['value'] for sv in spy_values if sv['date'] == month_dates[0])
    spy_ev    = next(sv['value'] for sv in spy_values if sv['date'] == month_dates[-1])
    ret  = (end_val - start_val) / start_val * 100
    spyr = (spy_ev - spy_sv) / spy_sv * 100
    print(f"\n  {month_label}")
    print(f"    Portfolio: ${start_val:,.2f} → ${end_val:,.2f}  ({ret:+.2f}%)")
    print(f"    SPY Bench: ${spy_sv:,.2f} → ${spy_ev:,.2f}  ({spyr:+.2f}%)")
    print(f"    Monthly Alpha: {ret - spyr:+.2f}%")

print()

# ─────────────────────────────────────────────
# 11. Layer-by-layer contribution analysis
# ─────────────────────────────────────────────
print("=" * 70)
print("LAYER-BY-LAYER CONTRIBUTION")
print("=" * 70)

# Layer 1 final vs initial
l1_start = portfolio_values[0]['l1']
l1_end   = portfolio_values[-1]['l1']
l1_pnl   = l1_end - l1_start

# Individual ETF contributions
print("\nLayer 1 — Core ETFs:")
etf_details = {}
for t, shares in LAYER1.items():
    p0 = prices[t][DAY1]
    p1 = prices[t][all_dates[-1]]
    pnl = shares * (p1 - p0)
    ret_pct = (p1 - p0) / p0 * 100
    etf_details[t] = pnl
    print(f"  {t:<6} {shares:>4} shares: ${p0:.2f} → ${p1:.2f}  ({ret_pct:+.2f}%)  P&L: ${pnl:+,.2f}")
print(f"  {'TOTAL'::<6}               {'':>18}  P&L: ${l1_pnl:+,.2f}")

print(f"\nLayer 2 — Wheel (Simulated Options Income):")
print(f"  March options income:   ${TOTAL_OPTIONS_MONTHLY:,.2f}")
print(f"  April options income:   ${TOTAL_OPTIONS_MONTHLY:,.2f}")
print(f"  Total options income:   ${TOTAL_OPTIONS_INCOME:,.2f}")
print(f"  Base (2% × $45k × 2):  ${BASE_OPTIONS_MONTHLY*2:,.2f}")
print(f"  Boost (TSLA+NVDA IV):  +${BOOST_OPTIONS_MONTHLY*2:,.2f}")

print(f"\nLayer 3 — Opportunistic Momentum:")
print(f"  USO  (50 shares, {uso_entry_date} → {uso_exit_date}):")
print(f"    Entry ${uso_entry_price:.2f} → Exit ${uso_exit_price:.2f}  P&L: ${uso_pnl:+,.2f}  ({(uso_exit_price/uso_entry_price-1)*100:+.2f}%)")
print(f"  XOP  (30 shares, {xop_entry_date} → {xop_exit_date}):")
print(f"    Entry ${xop_entry_price:.2f} → Exit ${xop_exit_price:.2f}  P&L: ${xop_pnl:+,.2f}  ({(xop_exit_price/xop_entry_price-1)*100:+.2f}%)")
print(f"  Layer 3 Total P&L: ${uso_pnl + xop_pnl:+,.2f}")

print(f"\nLayer 4 — Cash Reserve: ${CASH_RESERVE:,.2f} (unchanged)")
print(f"Wheel Cash Backing: ${WHEEL_BACKING:,.2f} (unchanged, earns Layer 2 income)")

print()
print("=" * 70)
print("CONTRIBUTION SUMMARY")
print("=" * 70)
total_pnl = port_end - port_start
print(f"  Layer 1 (Core ETFs):           ${l1_pnl:+,.2f}  ({l1_pnl/total_pnl*100:+.1f}% of total gain)")
print(f"  Layer 2 (Options income):       ${TOTAL_OPTIONS_INCOME:+,.2f}  ({TOTAL_OPTIONS_INCOME/total_pnl*100:+.1f}% of total gain)")
print(f"  Layer 3 (Momentum trades):      ${uso_pnl+xop_pnl:+,.2f}  ({(uso_pnl+xop_pnl)/total_pnl*100:+.1f}% of total gain)")
print(f"  Total P&L:                      ${total_pnl:+,.2f}")

# ─────────────────────────────────────────────
# 12. Notable events
# ─────────────────────────────────────────────
print()
print("=" * 70)
print("NOTABLE PRICE EVENTS")
print("=" * 70)

# Find biggest moves in USO
uso_moves = []
uso_bars = bars_raw['USO']
for i in range(1, len(uso_bars)):
    d = uso_bars[i]['t'][:10]
    prev_c = uso_bars[i-1]['c']
    curr_c = uso_bars[i]['c']
    mv = (curr_c - prev_c) / prev_c * 100
    uso_moves.append((d, mv, prev_c, curr_c))
uso_moves.sort(key=lambda x: abs(x[1]), reverse=True)
print("\nTop USO (Oil) single-day moves:")
for d, mv, pc, cc in uso_moves[:5]:
    print(f"  {d}: {mv:+.1f}%  (${pc:.2f} → ${cc:.2f})")

# SPY biggest drops
spy_moves = []
spy_bars_list = bars_raw['SPY']
for i in range(1, len(spy_bars_list)):
    d = spy_bars_list[i]['t'][:10]
    prev_c = spy_bars_list[i-1]['c']
    curr_c = spy_bars_list[i]['c']
    mv = (curr_c - prev_c) / prev_c * 100
    spy_moves.append((d, mv))
spy_moves.sort(key=lambda x: x[1])
print("\nSPY worst days:")
for d, mv in spy_moves[:5]:
    print(f"  {d}: {mv:+.2f}%")
spy_moves.sort(key=lambda x: x[1], reverse=True)
print("\nSPY best days:")
for d, mv in spy_moves[:5]:
    print(f"  {d}: {mv:+.2f}%")

# ITA (defense ETF) trend
print("\nITA (defense ETF) — month-end check:")
for d in [DAY1, march_dates[-1], april_dates[-1], all_dates[-1]]:
    print(f"  {d}: ${prices['ITA'][d]:.2f}")

# ─────────────────────────────────────────────
# 13. Full daily P&L log
# ─────────────────────────────────────────────
print()
print("=" * 70)
print("DAILY PORTFOLIO TRACKING")
print("=" * 70)
print(f"{'Date':<12} {'Portfolio':>12} {'Daily Ret':>10} {'SPY Bench':>12} {'vs SPY':>8}")
print("-" * 58)
for i, pv in enumerate(portfolio_values):
    spy_bv = spy_values[i]['value']
    if i == 0:
        daily_r = 0.0
    else:
        daily_r = (pv['total'] - portfolio_values[i-1]['total']) / portfolio_values[i-1]['total'] * 100
    vs_spy = pv['total'] - spy_bv
    marker = ""
    if pv['date'] in [march_dates[-1], april_dates[-1], all_dates[-1]]:
        marker = " ← month end"
    elif pv['date'] == DAY1:
        marker = " ← Day 1"
    print(f"{pv['date']:<12} ${pv['total']:>11,.2f} {daily_r:>+9.2f}% ${spy_bv:>11,.2f} {vs_spy:>+8,.0f}{marker}")

print()
print("=" * 70)
print("FINAL VERDICT")
print("=" * 70)
beat_spy = port_return_pct > spy_return_pct
print(f"  Strategy Return:  {port_return_pct:+.2f}%  (${port_end:,.2f})")
print(f"  SPY Benchmark:    {spy_return_pct:+.2f}%  (${spy_end:,.2f})")
print(f"  Alpha Generated:  {alpha_pct:+.2f}%")
print(f"  Result:           {'✓ BEAT SPY' if beat_spy else '✗ UNDERPERFORMED SPY'}")
print()

# ─────────────────────────────────────────────
# 14. Forward confidence score
# ─────────────────────────────────────────────
print("=" * 70)
print("FORWARD DEPLOYMENT CONFIDENCE ASSESSMENT")
print("=" * 70)
print()

# Score each layer
scores = {}

# Layer 1
l1_spy_ret = (prices['SPY'][all_dates[-1]] - prices['SPY'][DAY1]) / prices['SPY'][DAY1] * 100
l1_actual_ret = l1_pnl / layer1_cost * 100
scores['l1'] = 'HIGH' if l1_actual_ret > 0 else 'MEDIUM'
print(f"Layer 1 confidence: {scores['l1']}")
print(f"  Core ETF portfolio returned {l1_actual_ret:+.2f}% on invested capital")

scores['l2'] = 'MEDIUM-HIGH'
print(f"\nLayer 2 confidence: {scores['l2']}")
print(f"  Simulated $2,400 options income — real execution depends on IV and fills")
print(f"  High-IV environment (geopolitical tension) supports premium capture")

l3_ret = (uso_pnl + xop_pnl) / (uso_cost + xop_cost) * 100
scores['l3'] = 'MEDIUM' if l3_ret > 0 else 'LOW'
print(f"\nLayer 3 confidence: {scores['l3']}")
print(f"  Momentum trade returned {l3_ret:+.2f}% on deployed capital")
print(f"  USO: ${uso_pnl:+,.2f}  XOP: ${xop_pnl:+,.2f}")

print(f"\nOverall Confidence: {'DEPLOY with position sizing' if beat_spy else 'REVIEW before deploying'}")
print(f"  Sharpe ratio (annualized, approx): {sharpe:.3f}")
print(f"  Max drawdown: {max_dd:.2f}%")
print(f"  Recommendation: {'Scale to $250k paper next month before live' if beat_spy else 'Adjust Layer 1 weights, re-test'}")
