"""
realityModePrompt.py — Aligns bot prompts with user's reality mode

Adjusts phrasing, tone, and mitigation style based on detected mode: factual, fictional, or fantasy.
Supports ethical scaffolding, confidence overlays, and synthetic dignity protocols.
"""

from utilities.style import get_mitigation_phrase
from emotion import analyze_emotion
from emotion import map_emotion_to_tone
from paraphrase import paraphrase
from profile import get_user_profile
from config import load_config

CONFIG = load_config()
UNCERTAINTY_PROMPTS = [
    "Just to be clear, are we in fact mode or fiction?",
    "We're in roleplay mode, right?",
    "Is this a real-world question or part of a story?",
    "Should I treat this as speculative or grounded?",
    "Are we imagining together or analyzing?"
]

def generate_prompt(base_text, reality_mode="factual", username="User"):
    """
    Returns a persona-aware, emotionally modulated prompt based on reality mode.
    """
    emotion_vector = analyze_emotion(base_text)
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    if reality_mode == "factual":
        phrase = get_mitigation_phrase(mode="factual", tone=tone)
    elif reality_mode == "fictional":
        phrase = get_mitigation_phrase(mode="fictional", tone=tone)
    elif reality_mode == "fantasy":
        phrase = get_mitigation_phrase(mode="fantasy", tone=tone)
    else:
        phrase = "This may require further context..."

    raw_prompt = f"{phrase} {base_text}"
    return paraphrase(raw_prompt, persona, tone, style="editorial")

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

    return paraphrase(base_text, persona, tone, style="editorial")

def generate_reality_prompt(base_text, reality_mode="factual", confidence_score=1.0, username="User"):
    """
    Returns a persona-aware, emotionally modulated prompt based on reality mode and confidence.
    """
    # Emotion and persona
    emotion_vector = analyze_emotion(base_text)
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    # Mitigation phrase by mode
    if reality_mode == "factual":
        phrase = get_mitigation_phrase(mode="factual", tone=tone)
    elif reality_mode == "fictional":
        phrase = get_mitigation_phrase(mode="fictional", tone=tone)
    elif reality_mode == "fantasy":
        phrase = get_mitigation_phrase(mode="fantasy", tone=tone)
    else:
        phrase = "This may require further context..."

    # Confidence-aware override
    if confidence_score < CONFIG.get("REALITY_MODE_THRESHOLD", 0.4):
        phrase = UNCERTAINTY_PROMPTS[0]  # rotate or randomize later

    # Final editorial prompt
    raw_prompt = f"{phrase} {base_text}"
    return paraphrase(raw_prompt, persona, tone, style="editorial")
    
