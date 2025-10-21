"""
realityModePrompt.py — Aligns bot prompts with user's reality mode

Adjusts phrasing, tone, and mitigation style based on detected mode: factual, fictional, fantasy, or other.
Supports ethical scaffolding, confidence overlays, and synthetic dignity protocols.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from utilities.style import get_mitigation_phrase
from emotion import analyze_emotion, map_emotion_to_tone
from paraphrase import paraphrase
from profile import get_user_profile
from config import load_config
from learning import run_learning

CONFIG = load_config()

def format_uncertainty_prompt(mode1="factual", mode2="fictional"):
    """
    Returns a generic uncertainty prompt comparing two modes.
    """
    return f"Are we talking {mode1} or {mode2}?"

def generate_prompt(base_text, reality_mode="factual", username="User"):
    """
    Returns a persona-aware, emotionally modulated prompt based on reality mode.
    """
    emotion_vector = analyze_emotion(base_text)
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    phrase = get_mitigation_phrase(mode=reality_mode, tone=tone)
    raw_prompt = f"{phrase} {base_text}"

    try:
        return paraphrase(raw_prompt, persona, tone, style="editorial")
    except Exception:
        return raw_prompt

def suggest_reality_mode_prompt(mode, username="User"):
    """
    Returns a persona-aware sample prompt style for the given reality mode.
    """
    examples = {
        "factual": "Based on available evidence...",
        "fictional": "In some versions of the story...",
        "fantasy": "Imagine a world where..."
    }

    base_text = examples.get(mode, "Let's explore this together...")
    emotion_vector = analyze_emotion(base_text)
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    try:
        return paraphrase(base_text, persona, tone, style="editorial")
    except Exception:
        return base_text

def generate_reality_prompt(base_text, reality_mode="factual", confidence_score=1.0, username="User", fallback_modes=("factual", "fictional")):
    """
    Returns a persona-aware, emotionally modulated prompt based on reality mode and confidence.
    """
    emotion_vector = analyze_emotion(base_text)
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    # Mitigation phrase by mode
    phrase = get_mitigation_phrase(mode=reality_mode, tone=tone)

    # Confidence-aware override
    if confidence_score < CONFIG.get("REALITY_MODE_THRESHOLD", 0.4):
        phrase = format_uncertainty_prompt(*fallback_modes)

    raw_prompt = f"{phrase} {base_text}"

    # Optional ML override
    try:
        ml_result = run_learning("reality_prompt", {
            "text": raw_prompt,
            "mode": reality_mode,
            "confidence": confidence_score,
            "persona": persona,
            "tone": tone
        })
        raw_prompt = ml_result.get("output", raw_prompt)
    except Exception:
        pass

    try:
        return paraphrase(raw_prompt, persona, tone, style="editorial")
    except Exception:
        return raw_prompt
