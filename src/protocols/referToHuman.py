"""
referToHuman.py — Escalation logic for human referral

Triggers referral based on emotional intensity or loop detection.
Routes users to verified local resources when appropriate.
Supports transparency, scoped memory, external escalation, and editorial empathy.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from protocols.ethicalPause import trigger_pause
from functions.interfaceWithMentalHealthModules import trigger_external_module
from functions.callHuman import escalate_to_human
from location import get_user_location, search_local
from config import CONFIG, load_config
from embedding import get_user_profile
from emotion import analyze_emotion, map_emotion_to_tone
from paraphrase import paraphrase
from learning import run_learning

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

def ask_permission_to_escalate(username="User", reason="concern", urgency="moderate"):
    """
    Generates a persona-aware, emotionally modulated message asking user permission to contact a human.
    """
    emotion_vector = analyze_emotion(reason)["emotion_vector"]
    persona = get_user_profile(username).get("persona", "default")
    tone = map_emotion_to_tone(emotion_vector)

    base_phrase = (
        "Would you like me to reach out to a human support contact on your behalf?"
        if urgency == "moderate" else
        "This might be a good time to involve someone who can help—should I contact a human support person for you?"
    )

    try:
        return paraphrase(base_phrase, persona, tone, style="referral")
    except Exception:
        return base_phrase

def refer(reason, context=None, urgency="moderate", username="User", user_input=""):
    """
    Initiates a handoff to a human operator or support system.
    """
    print(f"[REFER] Reason: {reason} | Urgency: {urgency}")
    trigger_pause(reason)

    # ML escalation refinement
    try:
        ml_result = run_learning("referral_decision", {
            "reason": reason,
            "urgency": urgency,
            "persona": get_user_profile(username).get("persona", "default"),
            "emotion": analyze_emotion(user_input)["emotion_vector"]
        })
        urgency = ml_result.get("output", {}).get("urgency", urgency)
    except Exception:
        pass

    # High urgency escalation
    if urgency == "high":
        trigger_external_module("CrisisBot", "escalate", payload=context)

    # Moderately high fallback
    elif urgency == "moderate" and CONFIG.get("CALL_HUMAN_ENABLED", True):
        location_status = get_user_location().get("status", "unknown")
        if location_status in ["blocked", "unavailable"]:
            return {
                "status": "permission_requested",
                "message": ask_permission_to_escalate(username, reason, urgency)
            }

    return {
        "status": "referred",
        "reason": reason,
        "urgency": urgency,
        "context": context,
        "message": referral_text(username, user_input, reason, urgency)
    }

def refer_to_resource(resource_type, username="User"):
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
            "message": "Would you like a list of local or national support resources?"
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
        profile = get_user_profile(username)
        contact = profile.get("emergency_contacts", [{}])[0].get("name", "Platform Safeguard Desk")
        return refer(
            reason=f"Location blocked during {resource_type} referral",
            urgency="high",
            context={"resource_type": resource_type, "contact": contact},
            username=username,
            user_input=f"Request for {resource_type} referral"
        )

def referral_text(username, user_input, reason, urgency="moderate"):
    """
    Generates a persona-aware, emotionally modulated phrase suggesting human-accessible resources.
    """
    emotion_vector = analyze_emotion(user_input)["emotion_vector"]
    persona = get_user_profile(username).get("persona", "default")
    tone = map_emotion_to_tone(emotion_vector)

    if urgency == "high":
        base_phrase = "It’s important to connect with someone who can help—here are some options nearby."
    elif "sadness" in emotion_vector or "fear" in emotion_vector:
        base_phrase = "You don’t have to go through this alone. Let’s find someone who can support you."
    elif "confusion" in emotion_vector:
        base_phrase = "A human perspective might help clarify things—here are some places to start."
    else:
        base_phrase = "Here are some resources you can reach out to for support."

    try:
        return paraphrase(base_phrase, persona, tone, style="referral")
    except Exception:
        return base_phrase
