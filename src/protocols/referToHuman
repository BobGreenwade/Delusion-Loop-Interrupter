"""
referToHuman.py — Triggers handoff to a qualified human when synthetic limits are reached

Used when the bot encounters ethical boundaries, emotional distress, or unverifiable claims.
Supports transparency, scoped memory, and external escalation.
"""

from protocols.ethicalPause import trigger_pause
from functions.interfaceWithMentalHealthModules import trigger_external_module

def refer(reason, context=None, urgency="moderate"):
    """
    Initiates a handoff to a human operator or support system.
    Returns a status dictionary.
    """
    print(f"[REFER] Reason: {reason} | Urgency: {urgency}")
    trigger_pause(reason)

    # Optional: escalate to external module
    if urgency == "high":
        trigger_external_module("CrisisBot", "escalate", payload=context)

    return {
        "status": "referred",
        "reason": reason,
        "urgency": urgency,
        "context": context
    }

def should_refer(flags):
    """
    Evaluates content flags to determine if referral is needed.
    Returns True if any critical flag is present.
    """
    referral_flags = ["synthetic_limit", "emotional_distress", "ethical_boundary", "loop_detected"]
    return any(flag in flags for flag in referral_flags)
