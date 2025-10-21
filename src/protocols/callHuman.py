"""
callHuman.py

Escalates to human support via platform-enabled channels.
Supports emergency contact, mental health authority, law enforcement, and staff.
Now integrates with embedding.py and transcript.py for profile-aware routing and transcript sharing.
Includes editorial headers, ML feedback, and escalation disclaimers.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from config import CONFIG
from settings import NOTIFY_CHANNEL
from embedding import get_user_profile
from transcript import save_transcript
from emotion import analyze_emotion, map_emotion_to_tone
from paraphrase import paraphrase
from learning import run_learning
from datetime import datetime

def get_available_channels():
    return CONFIG.get("enabled_channels", [
        "sms", "email", "voice_call", "voice_chat", "internal_dm", "push"
    ])

def get_contact_profile(role="emergency_contact"):
    profile = get_user_profile()
    if role == "emergency_contact" and profile.get("escalation_opt_in"):
        contacts = profile.get("emergency_contacts", [])
        return contacts[0] if contacts else {"name": "Platform Safeguard Desk", "channel": "email", "type": "family"}
    return CONFIG.get("contact_profiles", {}).get(role, {"name": "Platform Safeguard Desk", "channel": "email", "type": "default"})

def get_initiation_header(channel, username, persona, platform, reason, recipient_type="default"):
    """
    Returns a default initiation header for the specified communication channel and recipient type.
    Staff can override via CONFIG["custom_headers"].
    """
    custom = CONFIG.get("custom_headers", {}).get(channel, {}).get(recipient_type)
    if custom:
        return custom.format(User=username, Persona=persona, Platform=platform, Reason=reason)

    if channel == "email":
        if recipient_type == "family":
            return (
                f"To: Family Member\nFrom: {platform} Escalation System\nSubject: Concern for {username}\n\n"
                f"This is to inform you that {username}, a user here at {platform}, "
                f"has shown signs of distress or delusional escalation.\nReason: {reason}"
            )
        elif recipient_type == "law_enforcement":
            return (
                f"To: Scotland Yard\nFrom: {platform} Safeguard Desk\nSubject: Escalation Alert\n\n"
                f"{username} has triggered a high-severity escalation. Reason: {reason}"
            )
        else:
            return (
                f"To: {get_contact_profile()['name']}\nFrom: {platform} Escalation System\n"
                f"Subject: Escalation for {username}\n\nReason: {reason}"
            )
    elif channel == "voice_call":
        base = (
            f"Hello, this is {persona} calling on behalf of {platform}. "
            f"I'm concerned about {username} due to recent chat messages. Reason: {reason}"
        )
        return paraphrase(base, persona, map_emotion_to_tone(analyze_emotion(reason)), style="handoff")
    elif channel == "push":
        return f"{platform} escalation triggered for {username}. Reason: {reason}"
    elif channel == "sms":
        return f"{platform}: Escalation alert for {username}. Reason: {reason}"
    elif channel == "internal_dm":
        return f"[{platform} Alert] {username} flagged for escalation. Reason: {reason}"
    else:
        return f"{platform} escalation notice for {username}. Reason: {reason}"

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

    # Emotional tone and persona
    emotion_vector = analyze_emotion(reason)
    persona = get_user_profile(username).get("persona", "default")
    tone = map_emotion_to_tone(emotion_vector)

    # Escalation disclaimer
    disclaimer = CONFIG.get("ESCALATION_DISCLAIMER", "I can contact staff, but only if it's triggered by a major escalation.")
    override_allowed = CONFIG.get("ESCALATION_OVERRIDE", False)
    if not override_allowed:
        print(f"[DISCLAIMER] {disclaimer}")

    # ML feedback logic
    try:
        feedback_result = run_learning("classification", {
            "reason": reason,
            "urgency": urgency,
            "persona": persona,
            "channel": channel
        })
        print(f"[ML FEEDBACK] {feedback_result}")
    except Exception:
        pass  # Graceful fallback

    # Initiation header
    recipient_type = contact.get("type", "default")
    header = get_initiation_header(channel, username, persona, CONFIG.get("PLATFORM_NAME", "Platform"), reason, recipient_type)
    print(f"[HEADER] {header}")

    # Editorial escalation message
    base_message = f"Escalation triggered via {channel} to {contact['name']} for reason: {reason}"
    editorial_message = paraphrase(base_message, persona, tone, style="handoff")

    # Handoff logic
    handoff_enabled = channel in ["internal_dm", "voice_chat"]
    handoff_status = "handoff_ready" if handoff_enabled else "notification_only"

    if handoff_enabled:
        initiate_handoff(contact, transcript_file)

    return {
        "status": "escalated",
        "reason": reason,
        "urgency": urgency,
        "contact": contact["name"],
        "channel": channel,
        "transcript_action": transcript_action,
        "transcript_file": transcript_file,
        "handoff_status": handoff_status,
        "message": editorial_message
    }

def initiate_handoff(contact, transcript_file=None):
    """
    Prepares live chat handoff to a human agent or staff member.
    """
    print(f"[INITIATE HANDOFF] Inviting {contact['name']} to join the chat.")
    if transcript_file:
        print(f"[TRANSCRIPT] Sharing: {transcript_file}")
