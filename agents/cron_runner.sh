#!/bin/bash
# cron_runner.sh — Wrapper for Hermes cron / scheduled runs
# Sources env and runs the desired cycle

set -e

CYCLE="${1:-open}"
PROJECT_DIR="/home/tekmage/projects/paper-trading"
AGENTS_DIR="$PROJECT_DIR/agents"
VENV_PYTHON="$PROJECT_DIR/.venv/bin/python"

# Load Hermes env (contains Alpaca keys, Slack, etc.)
if [ -f ~/.hermes/.env ]; then
    set -a
    source ~/.hermes/.env
    set +a
fi

cd "$AGENTS_DIR"

echo "=== Starting Paper Trading Cycle: $CYCLE at $(date) ==="
"$VENV_PYTHON" hermes_orchestrator.py --cycle "$CYCLE"
echo "=== Cycle $CYCLE completed ==="
