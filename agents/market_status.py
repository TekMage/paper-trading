"""
market_status.py — Shared utility for accurate market status using Alpaca API.

This module prevents the date/time and holiday confusion that plagued the previous bot.
Both Research and Trading Agents should use this before any planning or execution.
"""

import os
from datetime import datetime, timezone
from typing import Dict, Any

import requests

ALPACA_KEY = os.environ.get("ALPACA_API_KEY")
ALPACA_SECRET = os.environ.get("ALPACA_SECRET_KEY")
ALPACA_BASE = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET,
}


def get_clock() -> Dict[str, Any]:
    """Get current market clock from Alpaca."""
    url = f"{ALPACA_BASE}/clock"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_calendar(start: str, end: str) -> list:
    """Get market calendar between two dates (YYYY-MM-DD)."""
    url = f"{ALPACA_BASE}/calendar"
    params = {"start": start, "end": end}
    resp = requests.get(url, headers=HEADERS, timeout=10, params=params)
    resp.raise_for_status()
    return resp.json()


def get_market_status() -> Dict[str, Any]:
    """
    Returns a clean, reliable market status object.
    This should be the single source of truth for all agents.
    """
    clock = get_clock()

    status = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "is_open": clock.get("is_open", False),
        "next_open": clock.get("next_open"),
        "next_close": clock.get("next_close"),
        "current_session": "open" if clock.get("is_open") else "closed",
    }

    # Add human-readable note
    if status["is_open"]:
        status["note"] = "Market is currently OPEN"
    else:
        status["note"] = f"Market is CLOSED. Next open: {status['next_open']}"

    return status


def is_market_open() -> bool:
    """Simple boolean check."""
    return get_market_status()["is_open"]


if __name__ == "__main__":
    print(get_market_status())