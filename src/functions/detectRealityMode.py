"""
detectRealityMode.py — Classifies user input by reality mode

Used to distinguish grounded, speculative, and fantasy contexts.
Supports editorial modulation, synthetic empathy, and escalation logic.
Drafted collaboratively with Copilot.
"""

from semantics import match_wordlist, match_phrase

REALITY_MODE_TRIGGERS = {
    "fantasy": ["dragon", "wizard", "spaceship", "magic", "teleport", "sorcery"],
    "speculative": ["what if", "imagine", "hypothetical", "suppose", "theoretically"],
    "grounded": ["confirmed", "real", "documented", "evidence", "actual", "verified"]
}

def classify_reality_mode(text):
    """
    Returns one of: 'fantasy', 'speculative', 'grounded', or 'ambiguous'
    """
    lowered = text.lower()

    if match_wordlist(lowered, REALITY_MODE_TRIGGERS["fantasy"]):
        return "fantasy"
    if match_phrase(lowered, REALITY_MODE_TRIGGERS["speculative"]):
        return "speculative"
    if match_wordlist(lowered, REALITY_MODE_TRIGGERS["grounded"]):
        return "grounded"

    return "ambiguous"
