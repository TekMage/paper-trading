"""research_agent_runner_v2.py — Real Research Agent (Paper Trading Only)"""
import os
import logging
from datetime import datetime, date
from pathlib import Path

import requests
import pandas as pd

from market_status import get_market_status
from hmm_regime import get_current_regime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("research_agent")

ALPACA_BASE = "https://paper-api.alpaca.markets/v2"
ALPACA_KEY = os.environ.get("ALPACA_API_KEY")
ALPACA_SECRET = os.environ.get("ALPACA_SECRET_KEY")
HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}

def get_account():
    resp = requests.get(f"{ALPACA_BASE}/account", headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()

def get_positions():
    resp = requests.get(f"{ALPACA_BASE}/positions", headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()

def run_research_cycle():
    logger.info("=== Research Agent Started ===")
    status = get_market_status()
    logger.info("Market Status: %s", status["note"])

    account = get_account()
    equity = float(account.get("equity", 0))
    logger.info("Account Equity: $%.2f", equity)

    positions = get_positions()
    logger.info("Open positions: %d", len(positions))

    try:
        regime = get_current_regime(
            spy=pd.Series([500, 502, 501]),
            qqq=pd.Series([480, 485, 483]),
        )
        logger.info("Regime: %s", regime.get("regime_name"))
    except Exception as e:
        logger.warning("HMM error: %s", e)
        regime = {"regime_name": "Unknown", "bias": "N/A"}

    today = date.today().isoformat()
    research_dir = Path(__file__).parent.parent / "research"
    research_dir.mkdir(exist_ok=True)
    output_file = research_dir / f"{today}.md"

    with open(output_file, "w") as f:
        f.write("# Research Brief — " + today + "\n\n")
        f.write("**Market Status:** " + status["note"] + "\n\n")
        f.write("**Account Equity:** $" + str(round(equity, 2)) + "\n")
        f.write("**Open Positions:** " + str(len(positions)) + "\n\n")
        f.write("**Current Regime:** " + regime.get("regime_name", "Unknown") + "\n")
        f.write("**Bias:** " + regime.get("bias", "N/A") + "\n\n")
        f.write("## Recommendations\n")
        f.write("- Monitor late-day momentum\n")

    logger.info("Research brief saved: %s", output_file)
    logger.info("=== Research Agent Finished ===")
    return {"status": "success", "brief": str(output_file)}

if __name__ == "__main__":
    run_research_cycle()
