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

        # High impact alerts
        if alpha < -1.5:
            send_alert(f"QQQ Alpha warning: {alpha}% (regime: {regime})", level="warning",
                       extra={"cycle": cycle, "equity": research_result.get("equity")})
        if research_result and research_result.get("equity", 100000) < 80000:
            send_alert("CRITICAL: Account below $80k floor!", level="critical",
                       extra={"equity": research_result.get("equity")})

        market_open = is_market_open() if callable(is_market_open) else status.get("is_open", False)

        if cycle == "research_only" or not market_open:
            logger.info("Running research-only cycle (market closed or explicit)")
            trading_result = {"status": "skipped", "reason": "research_only_or_closed"}
        else:
            logger.info("Market OPEN — passing research context to Trading Agent")
            # Pass context
            trading_context = {
                "research_brief": research_result.get("brief") if research_result else None,
                "qqq_alpha": alpha,
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
