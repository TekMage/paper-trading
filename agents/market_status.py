"""
market_status.py — Shared utility for accurate market status using Alpaca API.

This module prevents the date/time and holiday confusion that plagued the previous bot.
Both Research and Trading Agents should use this before any planning or execution.

Clock/calendar GETs retry on timeout/connection/SSL failures. Midday 2026-09-01 died
on a single 10s handshake timeout in get_clock(); do not reintroduce a one-shot 10s GET.
"""

import logging
import os
import time
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import requests

logger = logging.getLogger("market_status")

ALPACA_BASE = os.environ.get("ALPACA_BASE_URL", "https://paper-api.alpaca.markets/v2")

# Default timeout/retries sized for flaky paper-api TLS, not for hanging the cycle.
HTTP_TIMEOUT = float(os.environ.get("ALPACA_HTTP_TIMEOUT", "30"))
HTTP_ATTEMPTS = int(os.environ.get("ALPACA_HTTP_ATTEMPTS", "4"))

RETRYABLE = (
    requests.Timeout,
    requests.ConnectionError,
    requests.exceptions.SSLError,
)


def _headers() -> Dict[str, str]:
    key = os.environ.get("ALPACA_API_KEY") or os.environ.get("APCA_API_KEY_ID")
    secret = os.environ.get("ALPACA_SECRET_KEY") or os.environ.get("APCA_API_SECRET_KEY")
    return {
        "APCA-API-KEY-ID": key or "",
        "APCA-API-SECRET-KEY": secret or "",
    }


def alpaca_get(url: str, params: Optional[dict] = None, timeout: Optional[float] = None) -> Any:
    """GET with exponential backoff on timeout/connect/SSL. Raises last error if all attempts fail."""
    timeout = HTTP_TIMEOUT if timeout is None else timeout
    last: Optional[BaseException] = None
    for i in range(1, HTTP_ATTEMPTS + 1):
        try:
            resp = requests.get(url, headers=_headers(), params=params, timeout=timeout)
            resp.raise_for_status()
            return resp.json()
        except RETRYABLE as e:
            last = e
            wait = min(2 ** i, 16)
            logger.warning(
                "Alpaca GET %s failed (%s/%s): %s; retry in %ss",
                url, i, HTTP_ATTEMPTS, e, wait,
            )
            if i < HTTP_ATTEMPTS:
                time.sleep(wait)
        except requests.HTTPError:
            raise
    assert last is not None
    raise last


def get_clock() -> Dict[str, Any]:
    """Get current market clock from Alpaca."""
    return alpaca_get(f"{ALPACA_BASE}/clock")


def get_calendar(start: str, end: str) -> list:
    """Get market calendar between two dates (YYYY-MM-DD)."""
    return alpaca_get(f"{ALPACA_BASE}/calendar", params={"start": start, "end": end})


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
