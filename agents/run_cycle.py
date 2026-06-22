"""
run_cycle.py — Orchestration runner using Hermes delegate_task.

This is the primary entrypoint for fully autonomous operation via Hermes sub-agents.

When running inside a Hermes session, it uses delegate_task to spawn isolated
Research and Trading sub-agents (each with their own context, tools, and state).

Fallback: direct Python calls when delegate_task is not available (standalone testing).
"""

import sys
import logging
import os
from datetime import datetime
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from market_status import get_market_status, is_market_open

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("run_cycle.log", mode="a"),
    ],
)
logger = logging.getLogger("run_cycle")

# ------------------------------------------------------------------
# Delegate Task Support (Hermes-native)
# ------------------------------------------------------------------
try:
    # In a real Hermes session this will be available
    from hermes_tools import delegate_task
except ImportError:
    delegate_task = None
    logger.info("delegate_task not available in this environment — using direct calls (fallback mode)")

def _delegate_or_direct(agent_name: str, goal: str, context: dict, toolsets: list = None, workdir: str = None):
    """Spawn via delegate_task when possible, otherwise run directly."""
    if delegate_task is not None:
        try:
            logger.info(f"Delegating to {agent_name} sub-agent via delegate_task...")
            result = delegate_task(
                goal=goal,
                context=context,
                toolsets=toolsets or ["web", "terminal", "file", "skills"],
                role="leaf",
                workdir=workdir or str(Path(__file__).parent),
            )
            logger.info(f"{agent_name} delegate_task completed")
            return {"status": "delegated", "result": result}
        except Exception as e:
            logger.warning(f"delegate_task for {agent_name} failed: {e}. Falling back to direct execution.")
    
    # Fallback: direct execution (useful for local testing or non-Hermes runs)
    logger.info(f"Running {agent_name} directly (fallback)")
    if "research" in agent_name.lower():
        from research_agent_runner import run_research_cycle
        return run_research_cycle()
    elif "trading" in agent_name.lower():
        from trading_agent_runner import run_trading_cycle
        return run_trading_cycle(context=context.get("trading_context", {}))
    return {"status": "error", "reason": "unknown agent"}

# ------------------------------------------------------------------
# Public Agent Spawners (designed for delegation)
# ------------------------------------------------------------------

def run_research_agent(context: dict = None) -> dict:
    """Spawn the Research Agent via delegate_task (or direct fallback)."""
    context = context or {}
    goal = (
        "Run full research cycle for paper-trading system: "
        "fetch market status via Alpaca, run HMM regime detection on SPY/QQQ, "
        "compute QQQ alpha, analyze recent trades from trades/ and backtest_results.md, "
        "generate structured research brief with what-worked/failed lessons and plan evolution recommendations. "
        "Focus on consistent QQQ alpha. Strictly paper-only."
    )
    full_context = {
        "instructions": "Use the research_agent_runner.py logic. Output structured dict + save research/YYYY-MM-DD.md",
        "previous_research": context.get("previous_research"),
        "alpaca_env": "Use paper API only. Source .env if needed.",
        **context
    }
    toolsets = ["web", "terminal", "file", "skills"]  # research needs web for news
    return _delegate_or_direct(
        "Research Agent",
        goal=goal,
        context=full_context,
        toolsets=toolsets,
        workdir=str(Path(__file__).parent)
    )

def run_trading_agent(research_output: dict = None, context: dict = None) -> dict:
    """Spawn the Trading Agent via delegate_task (or direct fallback)."""
    context = context or {}
    goal = (
        "Execute paper trades based on latest Research brief and HMM regime. "
        "Dynamically select best strikes from option chains. Enforce $80k floor. "
        "Only trade when market is open. Log all actions. Strictly paper trading only. "
        "Use dynamic best-contract selection and regime-aware posture."
    )
    full_context = {
        "research_brief": research_output.get("brief") if research_output else None,
        "regime": research_output.get("regime") if research_output else context.get("regime"),
        "qqq_alpha": research_output.get("qqq_alpha") if research_output else 0,
        "account_snapshot": context.get("account_snapshot"),
        "instructions": "Call run_trading_cycle with the provided context. Prefer dynamic option pricing and submission.",
        **context
    }
    toolsets = ["terminal", "file"]  # trading primarily needs execution + file access
    return _delegate_or_direct(
        "Trading Agent",
        goal=goal,
        context=full_context,
        toolsets=toolsets,
        workdir=str(Path(__file__).parent)
    )

# ------------------------------------------------------------------
# Main orchestration (supports full delegation)
# ------------------------------------------------------------------

def main():
    logger.info("=== Run Cycle (delegate_task enabled) Started ===")

    status = get_market_status()
    logger.info("Market Status: %s", status.get("note", "unknown"))

    research_result = run_research_agent()

    if not is_market_open():
        logger.warning("Market closed — Research only (planning / improvement mode)")
        trading_result = {"status": "skipped", "reason": "market_closed"}
    else:
        logger.info("Market OPEN — delegating Research → Trading sequence")
        trading_result = run_trading_agent(research_output=research_result)

    logger.info("=== Run Cycle Finished ===")
    return {
        "status": "success",
        "research": research_result,
        "trading": trading_result,
        "delegation_used": delegate_task is not None,
    }

if __name__ == "__main__":
    result = main()
    print("Final result:", result)
