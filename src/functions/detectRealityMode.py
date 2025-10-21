"""
detectRealityMode.py — Classifies user input by reality mode

Distinguishes grounded, speculative, fictional, role-play, fantasy, indulgent, and humorous contexts.
Supports editorial modulation, synthetic empathy, escalation logic, and persona-driven adaptation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from semantics import match_wordlist, match_phrase
from emotion import analyze_emotion
from learning import run_learning

# Initial trigger sets (can be expanded by persona or ML)
REALITY_MODE_TRIGGERS = {
    "fantasy": ["dragon", "wizard", "spaceship", "magic", "teleport", "sorcery"],
    "fiction": ["novel", "story", "character", "plot", "narrative", "author"],
    "speculative": ["what if", "imagine", "hypothetical", "suppose", "theoretically"],
    "roleplay": ["as if", "pretend", "i'm playing", "in character", "my persona"],
    "grounded": ["confirmed", "real", "documented", "evidence", "actual", "verified"],
    "indulgent": ["they're watching me", "i'm being tracked", "they implanted", "i know the truth", "they're not real"],
    "humor": ["just kidding", "lol", "that’s absurd", "sounds like a joke", "punchline", "satire"]
}

def classify_reality_mode(text, persona_profile=None):
    """
    Returns dict with: mode, confidence, matched_terms, editorial_note, emotional_tone
    """
    lowered = text.lower()
    scores = {}
    matched_terms = {}

    # Expand triggers via persona or ML
    if persona_profile:
        expanded = run_learning("classification", persona_profile)
        # Placeholder: simulate trigger expansion
        for mode, new_terms in expanded.get("output", {}).items():
            REALITY_MODE_TRIGGERS.setdefault(mode, []).extend(new_terms)

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
            "editorial_note": "No clear mode detected",
            "emotional_tone": analyze_emotion(text)["emotion_vector"]
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
    elif top_mode == "humor":
        editorial_note = "Tone appears humorous—consider editorial modulation"
    elif top_mode == "grounded":
        editorial_note = "No mitigation needed"

    emotional_tone = analyze_emotion(text)["emotion_vector"]

    return {
        "mode": top_mode,
        "confidence": confidence,
        "matched_terms": matched_terms[top_mode],
        "editorial_note": editorial_note,
        "emotional_tone": emotional_tone
    }
