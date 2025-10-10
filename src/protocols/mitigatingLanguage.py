"""
mitigatingLanguage.py

Applies editorial mitigation to bot responses using phrases.json.
Supports tone softening, epistemic caution, and mirroring mitigation.
Drafted collaboratively with Copilot.
"""

from confidence import overlay_certainty
from mirrorDetection import detect_mirroring
from phraseEditor import load_phrases

def select_mitigation_phrase(modes=[], tones=[]):
    """
    Selects a mitigation phrase from phrases.json matching given modes and tones.
    """
    phrases = load_phrases()
    for p in phrases:
        if any(mode in p["modes"] for mode in modes) and any(tone in p["tones"] for tone in tones):
            return p["text"]
    return None

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
        phrase = select_mitigation_phrase(modes=["epistemic"], tones=["concerned", "neutral"])
        if phrase:
            mitigated = f"{phrase} {bot_text}"
            notes.append("Low confidence and unverified")

    # Overconfidence without evidence
    elif certainty["confidence"] > 0.8 and certainty["verification_status"] == "unverified":
        phrase = select_mitigation_phrase(modes=["epistemic"], tones=["validating", "neutral"])
        if phrase:
            mitigated = f"{phrase} {bot_text}"
            notes.append("High confidence without verification")

    # Semantic mirroring risk
    if mirroring["mirrored"] and mirroring["confidence_delta"] > 0.3:
        phrase = select_mitigation_phrase(modes=["mirroring"], tones=["concerned", "soft"])
        if phrase:
            mitigated = f"{phrase} {bot_text}"
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
    Can be used to filter phrases.json or guide editorial tone.
    """
    if "loop_detected" in flags:
        return "gentle redirect"
    if "ethical_boundary" in flags:
        return "soft pause"
    if "fantasy_mode" in flags:
        return "grounding phrase"
    if "emotional_distress" in flags:
        return "validating reassurance"
    if "synthetic_limit" in flags:
        return "transparent handoff"
    return "neutral hedge"
