"""hermes_orchestrator.py — Top-level Hermes orchestrator for Paper Trading.

Coordinates Research + Trading agents.
Enforces market status, account floor, QQQ alpha focus.
Supports cycle types: pre_market, open, midday, pre_close, eod.
Full autonomous via Hermes cron / delegate_task.
"""

import logging
import sys
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

# Add path for local imports when run directly
sys.path.insert(0, str(Path(__file__).parent))

from market_status import get_market_status, is_market_open
from research_agent_runner import run_research_cycle
from trading_agent_runner import run_trading_cycle

# Fresh dashboard generator for EOD updates (research + live Alpaca snapshot + QQQ focus)
try:
    from dashboard_generator import generate_dashboard
except Exception:
    generate_dashboard = None
# ------------------------------------------------------------------
# Delegate Task Integration (preferred for full autonomy)
# ------------------------------------------------------------------
try:
    from run_cycle import run_research_agent as delegate_research, run_trading_agent as delegate_trading
    DELEGATION_AVAILABLE = True
except Exception:
    DELEGATION_AVAILABLE = False

try:
    from slack_alert import send_slack_alert
except ImportError:
    send_slack_alert = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("hermes_orchestrator")

VALID_CYCLES = ["pre_market", "open", "midday", "pre_close", "eod", "research_only"]

def send_alert(message: str, level: str = "info", extra: Optional[Dict] = None):
    """Wrapper for Slack alerts with graceful fallback."""
    if send_slack_alert:
        try:
            return send_slack_alert(message, level=level, extra=extra or {})
        except Exception as e:
            logger.warning(f"Slack alert failed: {e}")
    logger.info(f"[ALERT {level.upper()}] {message} | extra={extra}")
    return False

def run_cycle(cycle: str = "open") -> Dict[str, Any]:
    """Run a specific trading cycle."""
    if cycle not in VALID_CYCLES:
        cycle = "open"

    logger.info("=== Hermes Orchestrator Started | Cycle: %s ===", cycle)
    status = get_market_status()
    logger.info("Market Status: %s", status.get("note"))

    research_result: Optional[Dict[str, Any]] = None
    trading_result: Optional[Dict[str, Any]] = None

    try:
        # Prefer delegated sub-agent execution when available (full Hermes autonomy)
        if DELEGATION_AVAILABLE and os.environ.get("USE_DELEGATE_TASK", "true").lower() != "false":
            logger.info("Using delegate_task path for Research + Trading (autonomous sub-agents)")
            research_result = delegate_research(context={"cycle": cycle})
            alpha = research_result.get("qqq_alpha", 0) if isinstance(research_result, dict) else 0
            regime = research_result.get("regime", {}).get("regime_name", "Unknown") if isinstance(research_result, dict) else "Unknown"
        else:
            # Always run research for context (direct)
            research_result = run_research_cycle()
        alpha = research_result.get("qqq_alpha", 0) if research_result else 0
        regime = research_result.get("regime", {}).get("regime_name", "Unknown") if research_result else "Unknown"

        # High impact alerts — SPY primary
        spy_alpha = research_result.get("spy_alpha") if research_result else None
        if spy_alpha is not None and spy_alpha < -1.5:
            send_alert(f"SPY Alpha warning: {spy_alpha}% (regime: {regime})", level="warning",
                       extra={"cycle": cycle, "equity": research_result.get("equity")})
        elif alpha < -1.5:
            send_alert(f"QQQ Alpha warning: {alpha}% (regime: {regime})", level="warning",
                       extra={"cycle": cycle, "equity": research_result.get("equity")})
        if research_result and research_result.get("zero_fill_streak", 0) >= 3:
            send_alert(f"CRITICAL: zero-fill streak {research_result.get('zero_fill_streak')}", level="critical",
                       extra={"cycle": cycle})
        if research_result and research_result.get("equity", 100000) < 80000:
            send_alert("CRITICAL: Account below $80k floor!", level="critical",
                       extra={"equity": research_result.get("equity")})

        market_open = is_market_open() if callable(is_market_open) else status.get("is_open", False)

        if cycle == "research_only" or not market_open:
            logger.info("Running research-only cycle (market closed or explicit)")
            trading_result = {"status": "skipped", "reason": "research_only_or_closed"}
            # Always emit cycle JSON/md when trading is skipped (closed or research_only).
            # pre_market/open/midday holes previously left no YYYY-MM-DD_{cycle}.json.
            if cycle in ("eod", "pre_close", "research_only", "pre_market", "open", "midday"):
                try:
                    from cycle_logger import write_cycle_log
                    eod_payload = {
                        "status": "success",
                        "equity": research_result.get("equity") if research_result else None,
                        "spy_alpha": research_result.get("spy_alpha") if research_result else None,
                        "qqq_alpha": research_result.get("qqq_alpha") if research_result else None,
                        "account_return_pct": (research_result or {}).get("analysis", {}).get("our_return")
                            if isinstance((research_result or {}).get("analysis"), dict) else None,
                        "regime": regime,
                        "orders_submitted": 0,
                        "market_open": False,
                        "paper_only": True,
                        "account_floor": 80000,
                        "actions": [
                            f"{cycle.upper()}: market closed — research + dashboard only (no new risk)",
                        ],
                        "skips": [{"code": "MARKET_CLOSED", "detail": f"{cycle} after close — no new risk"}],
                        "notes": list((research_result or {}).get("analysis", {}).get("lessons") or [])[:6]
                            if isinstance((research_result or {}).get("analysis"), dict) else [],
                        "zero_fill_streak": (research_result or {}).get("zero_fill_streak"),
                        "positions_count": (research_result or {}).get("positions_count"),
                    }
                    # Prefer richer fields if research top-level carries them
                    for k in ("account_return_pct", "spy_return_pct", "qqq_return_pct"):
                        if research_result and research_result.get(k) is not None:
                            eod_payload[k] = research_result.get(k)
                    paths = write_cycle_log(cycle if cycle != "research_only" else "research", eod_payload)
                    logger.info("Wrote closed-market cycle log: %s", paths)
                except Exception as e:
                    logger.warning("Failed to write closed-market cycle log: %s", e)
        else:
            logger.info("Market OPEN — passing research context to Trading Agent")
            # Pass context
            trading_context = {
                "research_brief": research_result.get("brief") if research_result else None,
                "qqq_alpha": alpha,
                "spy_alpha": research_result.get("spy_alpha") if research_result else None,
                "regime": research_result.get("regime") if research_result else {},
                "cycle": cycle,
            }
            if DELEGATION_AVAILABLE and os.environ.get("USE_DELEGATE_TASK", "true").lower() != "false":
                trading_result = delegate_trading(research_output=research_result, context={"trading_context": trading_context})
            else:
                trading_result = run_trading_cycle(context=trading_context)

            # Post-trade alerts
            if trading_result and trading_result.get("status") == "success":
                if trading_result.get("orders_submitted", 0) > 0:
                    send_alert(f"Trading cycle executed orders in {cycle}", level="info",
                               extra={"alpha": alpha, "orders": trading_result.get("orders_submitted")})

        # Pre-close specific
        if cycle == "pre_close":
            logger.info("Pre-close review cycle (~3:15 PM ET) — institutional flows focus")
            # Could add extra momentum checks here in future

        send_alert(f"Cycle {cycle} complete | Alpha: {alpha}% | Regime: {regime}", level="info",
                   extra={"status": "success"})

        logger.info("Orchestrator results — Research: %s | Trading: %s",
                    research_result.get("status") if research_result else "N/A",
                    trading_result.get("status") if trading_result else "N/A")

    except Exception as e:
        logger.error(f"Orchestrator error in cycle {cycle}: {e}")
        send_alert(f"Orchestrator error in {cycle}: {str(e)[:100]}", level="error")
        return {"status": "error", "error": str(e), "cycle": cycle}

    if cycle in ("eod", "pre_close") and "generate_dashboard" in globals() and generate_dashboard:
        try:
            generate_dashboard()
            logger.info("Dashboard regenerated via fresh generator for EOD")
        except Exception as e: logger.warning(f"Dashboard call error: {e}")

    logger.info("=== Hermes Orchestrator Finished | Cycle: %s ===", cycle)
    return {
        "status": "success",
        "cycle": cycle,
        "research": research_result,
        "trading": trading_result,
        "market_open": status.get("is_open"),
    }

def main():
    # Default to open cycle when run directly
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", default="open", choices=VALID_CYCLES,
                        help="Cycle type to run")
    args = parser.parse_args()
    return run_cycle(args.cycle)

if __name__ == "__main__":
    result = main()
    print("Orchestrator result:", result)
