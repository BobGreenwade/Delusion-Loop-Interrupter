"""
style.py — Context-aware mitigation and phrasing engine

Loads phrases from external file and selects based on mode and tone.
"""

import json
import random
from emotion import analyze_emotion
from profile import get_user_profile
from style import get_mitigation_phrase
from pathlib import Path
from difflib import SequenceMatcher

PHRASE_FILE = Path(__file__).parent / "data" / "phrases.json"
TONE_MAP_PATH = "toneMap.json"

def load_phrases():
    with open(PHRASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def select_mitigation(username, user_input, confidence_score):
    emotion_vector = analyze_emotion(user_input)
    user_profile = get_user_profile(username)

    # Load tone map
    with open(TONE_MAP_PATH, "r", encoding="utf-8") as f:
        tone_map = json.load(f)

    # Determine tone from emotion vector
    tone = "neutral"
    for emotion in emotion_vector:
        if emotion in tone_map:
            tone = tone_map[emotion][0]  # Use first tone match
            break

    # Determine mode
    mode = "speculative" if confidence_score < 0.5 else "factual"

    # Style from profile or default
    style = user_profile.get("strategies", ["default"])[0]

    return get_mitigation_phrase(mode, tone, style)

def semantic_match(text_a, text_b, threshold=0.75):
    """
    Returns True if text_a and text_b are semantically similar.
    Uses fuzzy matching for now; can be upgraded to vector-based later.
    """
    ratio = SequenceMatcher(None, text_a.lower(), text_b.lower()).ratio()
    return ratio >= threshold

def infer_repeat_context(user_input, transcript_log, emotion_vector, recent_phrases, current_phrase):
    repeat_count = recent_phrases.count(current_phrase)

    # Check semantic similarity to recent transcript entries
    same_assertion = any(semantic_match(user_input, entry["text"]) for entry in transcript_log[-3:])

    # Emotion influence
    if "frustration" in emotion_vector or "anger" in emotion_vector:
        context_tag = "same_assertion"
    elif same_assertion:
        context_tag = "same_assertion"
    else:
        context_tag = "new_assertion" if repeat_count else "general"

    return repeat_count, context_tag
