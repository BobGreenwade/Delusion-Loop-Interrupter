"""
callHuman.py — Notifies a designated human via configured channel

Used when synthetic systems reach escalation thresholds and a human must be contacted.
Supports location-aware routing, config-based delivery, and fallback logic.
"""

from config.settings import NOTIFY_CHANNEL, LOCAL_CONTACTS

def notify_human(reason, location="default", priority="normal"):
    """
    Sends a notification to a human contact based on location and priority.
    Returns a status dictionary.
    """
    contact = LOCAL_CONTACTS.get(location, LOCAL_CONTACTS.get("default"))
    channel = NOTIFY_CHANNEL.get(priority, NOTIFY_CHANNEL.get("normal"))

    # Placeholder: Replace with actual delivery logic (SMS, email, webhook, etc.)
    print(f"[NOTIFY] Reason: {reason}")
    print(f"[TO] {contact} via {channel}")

    return {
        "status": "notified",
        "contact": contact,
        "channel": channel,
        "reason": reason,
        "priority": priority
    }

def get_notification_targets():
    """
    Returns a list of available human contacts and channels.
    """
    return {
        "contacts": list(LOCAL_CONTACTS.keys()),
        "channels": list(NOTIFY_CHANNEL.keys())
    }
