"""
callHuman.py

Escalates to human support via platform-enabled channels.
Supports emergency contact, mental health authority, law enforcement, and staff.
Drafted collaboratively with Copilot.
"""

from config import CONFIG
from settings import NOTIFY_CHANNEL

def get_available_channels():
    """
    Returns list of enabled channels based on platform config.
    """
    return CONFIG.get("enabled_channels", [
        "sms", "email", "voice_call", "voice_chat", "internal_dm", "push"
    ])

def get_contact_profile(role="emergency_contact"):
    """
    Returns contact details based on role.
    """
    contacts = CONFIG.get("contact_profiles", {})
    return contacts.get(role, {"name": "Platform Safeguard Desk", "channel": "email"})

def escalate_to_human(reason, urgency="moderate", role="emergency_contact"):
    """
    Routes escalation to appropriate human contact via best available channel.
    """
    available = get_available_channels()
    contact = get_contact_profile(role)
    preferred_channel = NOTIFY_CHANNEL.get(urgency, "log_only")

    if preferred_channel not in available:
        fallback = next((ch for ch in ["internal_dm", "email", "sms"] if ch in available), "log_only")
        channel = fallback
    else:
        channel = preferred_channel

    return {
        "status": "escalated",
        "reason": reason,
        "urgency": urgency,
        "contact": contact["name"],
        "channel": channel,
        "message": f"Escalation triggered via {channel} to {contact['name']} for reason: {reason}"
    }
