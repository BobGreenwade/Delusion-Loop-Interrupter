"""
indulgentMode.py — Handles delusional or conspiratorial assertions with editorial empathy

Detects indulgent belief patterns and triggers soft containment, escalation, or referral.
Supports synthetic dignity, editorial modulation, and scoped memory handoff.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from detectRealityMode import classify_reality_mode
from mirrorDetection import detect_mirroring
from interfaceWithMentalHealthModules import trigger_external_module
from logger import log_intervention

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

def initiate_indulgent_protocol(user_text, bot_text, persona_context=None):
    """
    Triggers escalation or containment logic for indulgent mode.
    """
    trigger_data = assess_indulgent_trigger(user_text, bot_text)
    if not trigger_data["triggered"]:
        return {"status": "no_action"}

    payload = {
        "user_text": user_text,
        "bot_text": bot_text,
        "tone": trigger_data["editorial_tone"],
        "persona": persona_context
    }

    log_intervention("indulgent_mode_triggered", payload, tone_tag=trigger_data["editorial_tone"])
    trigger_external_module("Local Support Relay", "monitor", payload)

    return {
        "status": "triggered",
        "editorial_tone": trigger_data["editorial_tone"],
        "escalation_module": "Local Support Relay"
    }
