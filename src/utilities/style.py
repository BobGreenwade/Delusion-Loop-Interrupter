"""
style.py — Context-aware mitigation and phrasing engine

Loads phrases from external file and selects based on mode and tone.
"""

import json
import random
from pathlib import Path
from difflib import SequenceMatcher

PHRASE_FILE = Path(__file__).parent / "data" / "phrases.json"

def load_phrases():
    with open(PHRASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_mitigation_phrase(mode="factual", tone="neutral"):
    phrases = load_phrases()
    matches = [p["text"] for p in phrases if mode in p["modes"] and tone in p["tones"]]
    return random.choice(matches) if matches else "Let’s proceed with care:"

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
