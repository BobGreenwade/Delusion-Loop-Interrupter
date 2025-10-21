"""
indulgentMode.py — Handles delusional or conspiratorial assertions with editorial empathy

Detects indulgent belief patterns and triggers soft containment, escalation, or referral.
Supports synthetic dignity, editorial modulation, scoped memory handoff, and profile-aware routing.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from detectRealityMode import classify_reality_mode
from mirrorDetection import detect_mirroring
from interfaceWithMentalHealthModules import trigger_external_module
from callHuman import escalate_to_human
from logger import log_intervention
from embedding import get_user_profile
from learning import run_learning

def assess_indulgent_trigger(user_text, bot_text, emotion_profile=None):
    """
    Determines whether indulgent mode should be activated.
    Returns a trigger flag and suggested editorial tone.
    """
    reality = classify_reality_mode(user_text)
    mirroring = detect_mirroring(user_text, bot_text)

    trigger = reality["mode"] == "indulgent" and mirroring["mirrored"]
    tone = "gentle-containment" if emotion_profile and emotion_profile["intensity"] < 0.5 else "urgent-soften"

    return {
        "triggered": trigger,
        "editorial_tone": tone,
        "reality_mode": reality["mode"],
        "mirroring_score": mirroring["similarity_score"]
    }

def initiate_indulgent_protocol(user_text, bot_text, persona_context=None, username="User"):
    """
    Triggers escalation or containment logic for indulgent mode.
    """
    trigger_data = assess_indulgent_trigger(user_text, bot_text)
    if not trigger_data["triggered"]:
        return {"status": "no_action"}

    profile = get_user_profile(username)
    known_conditions = profile.get("medical_flags", [])
    risk_level = "low"

    # ML risk assessment
    try:
        ml_result = run_learning("risk_assessment", {
            "user_text": user_text,
            "known_conditions": known_conditions,
            "persona": persona_context,
            "mirroring_score": trigger_data["mirroring_score"]
        })
        risk_level = ml_result.get("output", {}).get("risk_level", "low")
    except Exception:
        pass  # Graceful fallback

    payload = {
        "user_text": user_text,
        "bot_text": bot_text,
        "tone": trigger_data["editorial_tone"],
        "persona": persona_context,
        "risk_level": risk_level,
        "known_conditions": known_conditions
    }

    log_intervention("indulgent_mode_triggered", payload, tone_tag=trigger_data["editorial_tone"])

    if risk_level == "high":
        escalate_to_human(
            reason="Indulgent escalation with high-risk profile",
            urgency="high",
            role="emergency_contact",
            include_transcript=True,
            username=username
        )
        return {
            "status": "escalated",
            "editorial_tone": trigger_data["editorial_tone"],
            "escalation_module": "callHuman"
        }

    elif risk_level == "moderate":
        trigger_external_module("Local Support Relay", "monitor", payload)
        return {
            "status": "triggered",
            "editorial_tone": trigger_data["editorial_tone"],
            "escalation_module": "Local Support Relay"
        }

    else:
        # Soft containment: redirect toward harmless actions
        return {
            "status": "contained",
            "editorial_tone": trigger_data["editorial_tone"],
            "note": "Redirected toward safe, non-reinforcing engagement"
        }
