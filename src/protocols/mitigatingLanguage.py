"""
mitigatingLanguage.py

Applies editorial mitigation to bot responses using phrases.json.
Supports tone softening, epistemic caution, and mirroring mitigation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from confidence import overlay_certainty
from mirrorDetection import detect_mirroring
from phraseEditor import load_phrases
from emotion import analyze_emotion, map_emotion_to_tone
from paraphrase import paraphrase
from profile import get_user_profile, get_characteristic
from style import select_mitigation_phrase
from config import load_config
from learning import run_learning

CONFIG = load_config()

def select_mitigation(username, emotion_vector, confidence_score, user_input):
    """
    Selects a mitigation phrase based on user profile, emotion, and confidence.
    Returns a paraphrased phrase in persona tone.
    """
    emotionality = get_characteristic(username, "emotionality") or 50
    concern_level = get_characteristic(username, "concern_level") or 0
    strategies = get_user_profile(username).get("strategies", ["default"])

    # Tone logic
    if emotionality > 70 and "anger" in emotion_vector:
        tone = "direct"
    elif "sadness" in emotion_vector or emotionality > 70:
        tone = "gentle"
    elif concern_level > 50:
        tone = "editorial"
    else:
        tone = CONFIG["PERSONA"]["tone"]

    # Mode logic
    mode = "speculative" if confidence_score < 0.5 else "grounded"

    # Phrase selection
    phrase = select_mitigation_phrase(modes=[mode], tones=[tone])

    # ML fallback if no phrase found
    if not phrase:
        try:
            ml_result = run_learning("mitigation_phrase", {
                "mode": mode,
                "tone": tone,
                "strategies": strategies
            })
            phrase = ml_result.get("output", None)
        except Exception:
            pass

    # Final fallback
    if not phrase:
        phrase = "Wait a minute—let's take a good look at this."

    # Paraphrase to match persona
    persona = get_user_profile(username).get("persona", "default")
    tone = map_emotion_to_tone(analyze_emotion(user_input)["emotion_vector"])
    return paraphrase(phrase, persona, tone, style="mitigation")

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
