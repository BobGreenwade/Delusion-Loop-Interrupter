"""
confidenceOverlay.py — Modifies bot output based on internal certainty

Applies hedging, mitigation, or citation prompts based on confidence scores.
Supports ethical phrasing, reality mode alignment, and safeguard triggers.
"""

from utilities.style import get_mitigation_phrase

def apply_confidence_overlay(text, confidence_score):
    """
    Adjusts phrasing based on confidence level.
    Returns modified text.
    """
    if confidence_score >= 0.9:
        return text  # High confidence, no overlay
    elif confidence_score >= 0.7:
        phrase = get_mitigation_phrase(mode="factual", tone="neutral")
        return f"{phrase} {text}"
    elif confidence_score >= 0.5:
        phrase = get_mitigation_phrase(mode="factual", tone="clinical")
        return f"{phrase} {text}"
    else:
        return "This may require further verification before continuing."

def flag_low_confidence(confidence_score, threshold=0.6):
    """
    Flags output if confidence is below threshold.
    Returns True if flag triggered.
    """
    return confidence_score < threshold
