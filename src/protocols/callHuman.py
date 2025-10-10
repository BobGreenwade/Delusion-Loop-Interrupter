"""
callHuman.py

Escalates to human support via platform-enabled channels.
Supports emergency contact, mental health authority, law enforcement, and staff.
Now integrates with embedding.py for profile-aware routing.
Drafted collaboratively with Copilot.
"""

from config import CONFIG
from settings import NOTIFY_CHANNEL
from embedding import get_user_profile

def get_available_channels():
    return CONFIG.get("enabled_channels", [
        "sms", "email", "voice_call", "voice_chat", "internal_dm", "push"
    ])

def get_contact_profile(role="emergency_contact"):
    profile = get_user_profile()
    if role == "emergency_contact" and profile.get("escalation_opt_in"):
        contacts = profile.get("emergency_contacts", [])
        return contacts[0] if contacts else {"name": "Platform Safeguard Desk", "channel": "email"}
    return CONFIG.get("contact_profiles", {}).get(role, {"name": "Platform Safeguard Desk", "channel": "email"})

def escalate_to_human(reason, urgency="moderate", role="emergency_contact"):
    available = get_available_channels()
    contact = get_contact_profile(role)
    preferred_channel = NOTIFY_CHANNEL.get(urgency, "log_only")

    channel = preferred_channel if preferred_channel in available else next(
        (ch for ch in ["internal_dm", "email", "sms"] if ch in available), "log_only"
    )

    return {
        "status": "escalated",
        "reason": reason,
        "urgency": urgency,
        "contact": contact["name"],
        "channel": channel,
        "message": f"Escalation triggered via {channel} to {contact['name']} for reason: {reason}"
    }
