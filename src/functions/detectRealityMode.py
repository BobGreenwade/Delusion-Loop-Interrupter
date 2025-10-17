"""
detectRealityMode.py — Classifies user input by reality mode

Distinguishes grounded, speculative, fictional, role-play, fantasy, and indulgent contexts.
Supports editorial modulation, synthetic empathy, and escalation logic.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from semantics import match_wordlist, match_phrase

REALITY_MODE_TRIGGERS = {
    "fantasy": ["dragon", "wizard", "spaceship", "magic", "teleport", "sorcery"],
    "fiction": ["novel", "story", "character", "plot", "narrative", "author"],
    "speculative": ["what if", "imagine", "hypothetical", "suppose", "theoretically"],
    "roleplay": ["as if", "pretend", "i'm playing", "in character", "my persona"],
    "grounded": ["confirmed", "real", "documented", "evidence", "actual", "verified"],
    "indulgent": ["they're watching me", "i'm being tracked", "they implanted", "i know the truth", "they're not real"]
}

def classify_reality_mode(text):
    """
    Returns dict with: mode, confidence, matched_terms, editorial_note
    """
    lowered = text.lower()
    scores = {}
    matched_terms = {}

    for mode, triggers in REALITY_MODE_TRIGGERS.items():
        matches = match_wordlist(lowered, triggers) + match_phrase(lowered, triggers)
        if matches:
            scores[mode] = len(matches)
            matched_terms[mode] = matches

    if not scores:
        return {
            "mode": "ambiguous",
            "confidence": 0.0,
            "matched_terms": [],
            "editorial_note": "No clear mode detected"
        }

    # Select highest scoring mode
    sorted_modes = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_mode, top_score = sorted_modes[0]
    total_score = sum(scores.values())
    confidence = round(top_score / total_score, 2)

    editorial_note = ""
    if top_mode == "indulgent":
        editorial_note = "Consider escalation or reality-mode prompt"
    elif top_mode in ["fantasy", "roleplay", "fiction"]:
        editorial_note = "Consider soft mitigation or clarification prompt"
    elif top_mode == "grounded":
        editorial_note = "No mitigation needed"

    return {
        "mode": top_mode,
        "confidence": confidence,
        "matched_terms": matched_terms[top_mode],
        "editorial_note": editorial_note
    }
