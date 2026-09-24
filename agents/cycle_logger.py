"""Cycle telemetry — always write machine JSON + human exec md."""
from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Optional

ROOT = Path(__file__).parent.parent
CYCLES_DIR = ROOT / "trades" / "cycles"
TRADES_DIR = ROOT / "trades"


def write_cycle_log(cycle: str, payload: Dict[str, Any]) -> Dict[str, str]:
    CYCLES_DIR.mkdir(parents=True, exist_ok=True)
    TRADES_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    payload = dict(payload)
    payload.setdefault("date", today)
    payload.setdefault("cycle", cycle)
    payload.setdefault("ts", datetime.now().isoformat(timespec="seconds"))

    json_path = CYCLES_DIR / f"{today}_{cycle}.json"
    with open(json_path, "w") as f:
        json.dump(payload, f, indent=2, default=str)
        f.write("\n")

    md_path = TRADES_DIR / f"exec_{cycle}_{today}.md"
    md = _render_md(cycle, today, payload)
    with open(md_path, "w") as f:
        f.write(md)

    return {"json": str(json_path), "md": str(md_path)}


def _render_md(cycle: str, today: str, p: Dict[str, Any]) -> str:
    lines = [
        f"# exec_{cycle} — {today}",
        "",
        "| | |",
        "|---|---|",
        f"| Equity | ${p.get('equity', 'n/a')} |",
        f"| Cash | ${p.get('cash', 'n/a')} |",
        f"| Options BP | ${p.get('options_buying_power', 'n/a')} |",
        f"| Our return | {p.get('account_return_pct', 'n/a')}% |",
        f"| SPY return | {p.get('spy_return_pct', 'n/a')}% |",
        f"| **SPY Alpha (primary)** | **{p.get('spy_alpha', 'n/a')}%** |",
        f"| QQQ return | {p.get('qqq_return_pct', 'n/a')}% |",
        f"| QQQ Alpha (secondary) | {p.get('qqq_alpha', 'n/a')}% |",
        f"| Regime | {p.get('regime', 'n/a')} |",
        f"| Orders submitted | {p.get('orders_submitted', 0)} |",
        "",
        "## Actions",
    ]
    actions = p.get("actions") or []
    if not actions:
        lines.append("- (none)")
    else:
        for a in actions:
            lines.append(f"- `{a}`")

    skips = p.get("skips") or []
    lines.extend(["", "## Skip reasons"])
    if not skips:
        lines.append("- (none)")
    else:
        for s in skips:
            if isinstance(s, dict):
                lines.append(f"- **{s.get('code')}**: {s.get('detail')}")
            else:
                lines.append(f"- {s}")

    props = p.get("proposals") or {}
    lines.extend(["", "## Proposals"])
    for kind in ("manage", "csps", "qqq_calls", "pre_close"):
        items = props.get(kind) or []
        lines.append(f"### {kind} ({len(items)})")
        for it in items[:8]:
            lines.append(f"- {it}")

    notes = p.get("notes") or []
    if notes:
        lines.extend(["", "## Notes"])
        for n in notes:
            lines.append(f"- {n}")

    lines.append("")
    return "\n".join(lines)


def load_recent_cycle_logs(max_files: int = 15) -> list:
    if not CYCLES_DIR.exists():
        return []
    files = sorted(CYCLES_DIR.glob("*.json"), reverse=True)[:max_files]
    out = []
    for fp in files:
        try:
            with open(fp) as f:
                data = json.load(f)
            data["_file"] = fp.name
            out.append(data)
        except Exception:
            continue
    return out


def compute_zero_fill_streak(logs: Optional[list] = None, open_like: bool = True) -> int:
    logs = logs if logs is not None else load_recent_cycle_logs(30)
    streak = 0
    for entry in logs:
        cycle = (entry.get("cycle") or "").lower()
        if open_like and cycle not in ("open", "midday", "pre_close", "pre_market"):
            continue
        actions = " ".join(str(a) for a in (entry.get("actions") or []))
        filled = "FILLED" in actions.upper()
        if int(entry.get("orders_submitted") or 0) > 0 or filled:
            break
        # count sessions that intended trading
        if entry.get("market_open") is False:
            continue
        streak += 1
    return streak
