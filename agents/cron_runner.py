#!/usr/bin/env python3
"""cron_runner.py — Simple entrypoint for Hermes cron jobs.

Usage: python cron_runner.py --cycle open
"""

import sys
import argparse
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", default="open", choices=["pre_market", "open", "midday", "pre_close", "eod", "research_only"])
    args = parser.parse_args()

    project_dir = Path(__file__).parent.parent
    agents_dir = Path(__file__).parent
    venv_python = project_dir / ".venv" / "bin" / "python"

    cmd = [
        str(venv_python),
        str(agents_dir / "hermes_orchestrator.py"),
        "--cycle", args.cycle
    ]

    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(agents_dir), capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr, file=sys.stderr)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
