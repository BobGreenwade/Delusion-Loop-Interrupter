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
from embedding import get_user_profile
from config import load_config

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
        "context": context
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

