"""
slack_alert.py — Slack alerting + channel management.

Supports:
- Sending alerts via webhook or chat.postMessage
- Creating channels if they don't exist (requires bot token)

Environment variables:
    SLACK_BOT_TOKEN       → Recommended (xoxb-...) for channel creation & posting
    SLACK_WEBHOOK_URL     → Fallback for simple alerts
    SLACK_CHANNEL         → Default channel (e.g. #paper-trading-alerts)
"""

import os
import json
import requests
from datetime import datetime

SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
SLACK_CHANNEL = os.environ.get("SLACK_CHANNEL", "#paper-trading-alerts")


def _get_headers():
    if not SLACK_BOT_TOKEN:
        return None
    return {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8"
    }


def create_channel_if_not_exists(channel_name: str) -> bool:
    """Create a Slack channel if it doesn't already exist."""
    if not SLACK_BOT_TOKEN:
        print("[Slack] SLACK_BOT_TOKEN not set — cannot create channel")
        return False

    headers = _get_headers()

    # Check if channel exists
    resp = requests.post(
        "https://slack.com/api/conversations.list",
        headers=headers,
        json={"limit": 200},
        timeout=10
    )
    data = resp.json()

    if not data.get("ok"):
        print(f"[Slack] Failed to list channels: {data.get('error')}")
        return False

    existing = [c["name"] for c in data.get("channels", [])]
    clean_name = channel_name.lstrip("#")

    if clean_name in existing:
        print(f"[Slack] Channel #{clean_name} already exists")
        return True

    # Create channel
    resp = requests.post(
        "https://slack.com/api/conversations.create",
        headers=headers,
        json={"name": clean_name, "is_private": False},
        timeout=10
    )
    result = resp.json()

    if result.get("ok"):
        print(f"[Slack] Channel #{clean_name} created successfully")
        return True
    else:
        print(f"[Slack] Failed to create channel: {result.get('error')}")
        return False


def send_slack_alert(message: str, level: str = "info", extra: dict = None, channel: str = None):
    """
    Send alert to Slack.
    Prefers bot token + chat.postMessage if available, falls back to webhook.
    """
    target_channel = channel or SLACK_CHANNEL
    clean_channel = target_channel.lstrip("#")

    # Try bot token first (more capable)
    if SLACK_BOT_TOKEN:
        headers = _get_headers()
        payload = {
            "channel": f"#{clean_channel}",
            "text": f"*{level.upper()}* — Paper Trading System\n{message}"
        }
        if extra:
            payload["attachments"] = [{
                "color": "#ffcc00" if level == "warning" else "#36a64f",
                "fields": [{"title": k, "value": str(v), "short": False} for k, v in extra.items()]
            }]

        resp = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload, timeout=10)
        result = resp.json()
        if result.get("ok"):
            print(f"[Slack] Alert sent to #{clean_channel} via bot token")
            return True
        else:
            print(f"[Slack] Bot token failed: {result.get('error')}")

    # Fallback to webhook
    if SLACK_WEBHOOK_URL:
        payload = {
            "text": f"*{level.upper()}* — Paper Trading System\n{message}",
            "channel": f"#{clean_channel}"
        }
        try:
            resp = requests.post(SLACK_WEBHOOK_URL, json=payload, timeout=10)
            resp.raise_for_status()
            print(f"[Slack] Alert sent via webhook to #{clean_channel}")
            return True
        except Exception as e:
            print(f"[Slack] Webhook failed: {e}")

    print("[Slack] No valid Slack credentials configured")
    return False


if __name__ == "__main__":
    # Test channel creation + alert
    create_channel_if_not_exists("#paper-trading-alerts")
    send_slack_alert("Test alert from paper trading system", level="info")