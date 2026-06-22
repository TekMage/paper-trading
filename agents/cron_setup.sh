#!/bin/bash
# Cron setup for Paper Trading Hermes Orchestrator (updated)
# Uses cron_runner.sh which sources env and runs specific cycles

CRON_ENTRY1="30 11 * * 1-5 /home/tekmage/projects/paper-trading/agents/cron_runner.sh pre_market >> /home/tekmage/projects/paper-trading/agents/run_cycle.log 2>&1"
CRON_ENTRY2="30 13 * * 1-5 /home/tekmage/projects/paper-trading/agents/cron_runner.sh open >> /home/tekmage/projects/paper-trading/agents/run_cycle.log 2>&1"
CRON_ENTRY3="0 16 * * 1-5 /home/tekmage/projects/paper-trading/agents/cron_runner.sh midday >> /home/tekmage/projects/paper-trading/agents/run_cycle.log 2>&1"
CRON_ENTRY4="15 20 * * 1-5 /home/tekmage/projects/paper-trading/agents/cron_runner.sh pre_close >> /home/tekmage/projects/paper-trading/agents/run_cycle.log 2>&1"
CRON_ENTRY5="0 21 * * 1-5 /home/tekmage/projects/paper-trading/agents/cron_runner.sh eod >> /home/tekmage/projects/paper-trading/agents/run_cycle.log 2>&1"

(crontab -l 2>/dev/null | grep -v "cron_runner.sh" ; echo "$CRON_ENTRY1"; echo "$CRON_ENTRY2"; echo "$CRON_ENTRY3"; echo "$CRON_ENTRY4"; echo "$CRON_ENTRY5") | sort -u | crontab -

echo "Cron jobs installed/updated"
crontab -l | grep -E "cron_runner|paper-trading"
