```python
"""
callHuman.py

Escalates to human support via platform-enabled channels.
Supports emergency contact, mental health authority, law enforcement, and staff.
Now integrates with embedding.py and transcript.py for profile-aware routing and transcript sharing.
Drafted collaboratively with Copilot.
"""

from config import CONFIG
from settings import NOTIFY_CHANNEL
from embedding import get_user_profile
from transcript import save_transcript

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

def escalate_to_human(reason, urgency="moderate", role="emergency_contact", include_transcript=True, username="User"):
    available = get_available_channels()
    contact = get_contact_profile(role)
    preferred_channel = NOTIFY_CHANNEL.get(urgency, "log_only")

    channel = preferred_channel if preferred_channel in available else next(
        (ch for ch in ["internal_dm", "email", "sms"] if ch in available), "log_only"
    )

    # Transcript logic
    transcript_file = save_transcript(username) if include_transcript else None
    privacy_policy = CONFIG.get("PLATFORM_PRIVACY_POLICY", "restrictive")
    allow_full_send = (
        include_transcript and
        urgency == "high" and
        privacy_policy != "restrictive"
    )

    transcript_action = (
        "send_full_transcript" if allow_full_send else
        "share_filename_only" if transcript_file else
        "hold_transcript"
    )

    return {
        "status": "escalated",
        "reason": reason,
        "urgency": urgency,
        "contact": contact["name"],
        "channel": channel,
        "transcript_action": transcript_action,
        "transcript_file": transcript_file,
        "message": f"Escalation triggered via {channel} to {contact['name']} for reason: {reason}"
    }
