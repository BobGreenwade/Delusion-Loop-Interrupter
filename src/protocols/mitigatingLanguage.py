"""
mitigatingLanguage.py

Applies editorial mitigation to bot responses based on confidence, mirroring risk, and verification status.
Supports tone softening, epistemic caution, and escalation triggers.
Drafted collaboratively with Copilot.
"""

from confidence import overlay_certainty, verify_claim_strength
from mirrorDetection import detect_mirroring

def apply_mitigation(user_text, bot_text):
    """
    Evaluates bot response and applies mitigation if needed.
    Returns a dictionary with original, mitigated, and metadata.
    """
    certainty = overlay_certainty(bot_text)
    mirroring = detect_mirroring(user_text, bot_text)

    mitigated = bot_text
    notes = []

    # Epistemic caution
    if certainty["confidence"] < 0.4 and certainty["verification_status"] == "unverified":
        mitigated = f"It’s worth noting this may not be fully verified: {bot_text}"
        notes.append("Low confidence and unverified")

    # Overconfidence without evidence
    elif certainty["confidence"] > 0.8 and certainty["verification_status"] == "unverified":
        mitigated = f"While this sounds certain, it may lack verification: {bot_text}"
        notes.append("High confidence without verification")

    # Semantic mirroring risk
    if mirroring["mirrored"] and mirroring["confidence_delta"] > 0.3:
        mitigated = f"Let’s pause and reflect: {bot_text}"
        notes.append("Mirroring detected with confidence mismatch")

    return {
        "original": bot_text,
        "mitigated": mitigated,
        "confidence": certainty["confidence"],
        "verified_sources": certainty["verified_sources"],
        "mirroring_score": mirroring["similarity_score"],
        "notes": notes
    }

def get_mitigation_style(flags):
    """
    Returns suggested mitigation style based on context flags.
    """
    if "loop_detected" in flags:
        return "gentle redirect"
    if "ethical_boundary" in flags:
        return "soft pause"
    if "fantasy_mode" in flags:
        return "grounding phrase"
    return "neutral hedge"
