# PLAN v3.0 — Wheel restore (2026-07-17)

Superseded 2026-09-24 by the $110k test. Live rules are `README.md` and `agents/config/strategy_config.json`. Do not restore the locked decisions below.

Historical decisions (no longer in force):

- **SPY primary** benchmark; **QQQ secondary** (start QQQ close 2026-05-07 = 694.94)
- **Cash-secured CSPs only** until options BP recovers
- **NVDA short puts**: profit-take at ≥50% (executed 2026-07-17)
- **SPCX**: hold for recovery; dump only if capital needed for clearly better ROI
- **Research self-correct**: live cycle logs + safe auto config tweaks + stall alerts

Implementation still lives in:

- `agents/config/strategy_config.json`, `agents/config/benchmarks.json`
- `agents/strategy_lib.py`, `agents/cycle_logger.py`
- `agents/trading_agent_runner.py`, `agents/research_agent_runner.py`

See also: `.hermes/plans/2026-07-17_144646-wheel-lessons-postmortem-repair.md`
