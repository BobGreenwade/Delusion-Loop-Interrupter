"""
referToHuman.py — Escalation logic for human referral

Triggers referral based on emotional intensity or loop detection.
Routes users to verified local resources when appropriate.
Supports transparency, scoped memory, and external escalation.
Drafted collaboratively with Copilot.
"""

from protocols.ethicalPause import trigger_pause
from functions.interfaceWithMentalHealthModules import trigger_external_module
from location import get_user_location, search_local
from config import CONFIG
from config import load_config
from embedding import get_user_profile
from emotion import analyze_emotion
from emotion import map_emotion_to_tone
from paraphrase import paraphrase
from profile import get_user_profile

CONFIG = load_config()

def should_refer(emotion_profile, loop_detected=False):
    intensity = emotion_profile.get("intensity", 0)
    distress_emotions = ["sadness", "fear", "anger"]
    active_distress = any(emotion_profile["emotion_vector"].get(e, 0) for e in distress_emotions)

    return (
        intensity > CONFIG["ESCALATION_THRESHOLD"]
        or (loop_detected and active_distress)
        or CONFIG["PERSONA"]["allow_speculation"] is False and "surprise" in emotion_profile["emotion_vector"]
    )
    
def refer(reason, context=None, urgency="moderate"):
    """
    Initiates a handoff to a human operator or support system.
    """
    print(f"[REFER] Reason: {reason} | Urgency: {urgency}")
    trigger_pause(reason)

    if urgency == "high":
        trigger_external_module("CrisisBot", "escalate", payload=context)

return {
    "status": "referred",
    "reason": reason,
    "urgency": urgency,
    "context": context,
    "message": referral_text(username, user_input, reason, urgency)
}

def refer_to_resource(resource_type):
    loc_data = get_user_location()
    location = loc_data.get("location")
    status = loc_data.get("status")

    if location:
        return {
            "status": "location_granted",
            "search_url": search_local(resource_type, location, CONFIG)
        }

    fallback = CONFIG.get("location_fallback", "ask")

    if fallback == "ask":
        return {
            "status": "location_undecided",
            "message": "Would you like to enable location to find nearby support?"
        }
    elif fallback == "silent":
        query = f"{resource_type} near me"
        engine = CONFIG.get("search_engine", "bing")
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}" if engine == "google" else f"https://www.bing.com/search?q={query.replace(' ', '+')}"
        return {
            "status": "location_unavailable",
            "search_url": url
        }
    else:
        profile = get_user_profile()
        contact = profile.get("emergency_contacts", [{}])[0].get("name", "Platform Safeguard Desk")
        return refer(
            reason=f"Location blocked during {resource_type} referral",
            urgency="high",
            context={"resource_type": resource_type, "contact": contact}
        )

def referral_text(username, user_input, reason, urgency="moderate"):
    """
    Generates a persona-aware, emotionally modulated phrase suggesting human-accessible resources.
    """
    emotion_vector = analyze_emotion(user_input)
    persona = get_user_profile(username).get("persona", "default")
    tone = map_emotion_to_tone(emotion_vector)

    # Base phrase selection for resource suggestion
    if urgency == "high":
        base_phrase = "It’s important to connect with someone who can help—here are some options nearby."
    elif "sadness" in emotion_vector or "fear" in emotion_vector:
        base_phrase = "You don’t have to go through this alone. Let’s find someone who can support you."
    elif "confusion" in emotion_vector:
        base_phrase = "A human perspective might help clarify things—here are some places to start."
    else:
        base_phrase = "Here are some resources you can reach out to for support."

    return paraphrase(base_phrase, persona, tone, style="referral")
    
