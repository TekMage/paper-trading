"""Score fetched headlines for materiality to the open book.

Code fetches the headlines and decides the cutoff. TypeSafe only answers
one yes/no per headline. A missing key or a failed call leaves the list
unchanged and logs the failure — it does not invent a judgment.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger("research_agent")

# Starting cutoff, not a universal rule. Logged so it can be moved after
# looking at real probabilities on this book.
MATERIAL_MIN = 0.60


def book_symbols(positions: List[Dict[str, Any]] | None) -> List[str]:
    """Held underlyings plus the two benchmarks the account is scored on."""
    from strategy_lib import parse_occ

    names = {"SPY", "QQQ"}
    for pos in positions or []:
        symbol = str(pos.get("symbol") or "").strip()
        if not symbol:
            continue
        occ = parse_occ(symbol)
        names.add(occ["underlying"] if occ else symbol)
    return sorted(names)


def _ensure_api_key() -> bool:
    if os.environ.get("TYPESAFE_API_KEY"):
        return True
    env_path = Path.home() / ".hermes" / ".env"
    if not env_path.exists():
        return False
    try:
        from dotenv import load_dotenv
    except ImportError:
        return False
    load_dotenv(env_path)
    return bool(os.environ.get("TYPESAFE_API_KEY"))


def filter_news_for_book(
    items: List[Dict[str, str]],
    positions: List[Dict[str, Any]] | None,
) -> List[Dict[str, Any]]:
    """Keep headlines whose yes-probability clears MATERIAL_MIN.

    Independent Nouls go in one request. If nothing clears the cutoff, the
    brief gets an explicit no-match line instead of unrelated stories.
    """
    if not items:
        return items
    if not _ensure_api_key():
        logger.warning("TYPESAFE_API_KEY missing; news left unfiltered")
        return items

    try:
        from typesafe_sdk import Noul, TypeSafeClient
    except ImportError:
        logger.warning("typesafe-sdk not installed; news left unfiltered")
        return items

    symbols = book_symbols(positions)
    state = {
        "book": {
            "symbols": symbols,
            "benchmarks": ["SPY", "QQQ"],
            "goal": (
                "Paper account measured against SPY, with QQQ secondary. "
                "Only the held symbols and those two benchmarks are the book."
            ),
        },
        "headlines": [
            {
                "id": f"h{i}",
                "region": item.get("region", ""),
                "text": item.get("headline", ""),
            }
            for i, item in enumerate(items)
        ],
    }
    questions = {
        f"h{i}": Noul(
            instructions=(
                f"Does headline `headlines[{i}].text` materially affect this "
                "paper-trading book (`book.symbols`) or the SPY or QQQ benchmarks?"
            ),
            criteria={
                "true": (
                    "A trader of this book would change size, hedges, or which "
                    "names to watch because of this headline. That includes a "
                    "held symbol, SPY, QQQ, a broad index move, rates, volatility, "
                    "or a macro or geopolitical shock that would move those."
                ),
                "false": (
                    "The headline is about a company or event with no link to the "
                    "held symbols or to SPY and QQQ. A single-name story that is "
                    "not in the book is not material."
                ),
            },
        )
        for i in range(len(items))
    }

    try:
        with TypeSafeClient() as client:
            result = client.system_one(state, questions)
    except Exception as exc:
        logger.warning("TypeSafe news filter failed: %s", type(exc).__name__)
        return items

    kept: List[Dict[str, Any]] = []
    for i, item in enumerate(items):
        probability = float(result.nouls[f"h{i}"].noul)
        logger.info(
            "news relevance h%d %.2f %s",
            i,
            probability,
            (item.get("headline") or "")[:80],
        )
        if probability >= MATERIAL_MIN:
            kept.append({**item, "material": round(probability, 2)})

    if kept:
        return kept
    return [
        {
            "region": "Filter",
            "headline": "No fetched headline was material to the open book or to SPY/QQQ",
            "material": 0.0,
        }
    ]
