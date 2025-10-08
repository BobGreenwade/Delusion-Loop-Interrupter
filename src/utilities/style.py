"""
style.py — Context-aware mitigation and phrasing engine

Loads phrases from external file and selects based on mode and tone.
"""

import json
import random
from pathlib import Path

PHRASE_FILE = Path(__file__).parent / "data" / "phrases.json"

def load_phrases():
    with open(PHRASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_mitigation_phrase(mode="factual", tone="neutral"):
    phrases = load_phrases()
    matches = [p["text"] for p in phrases if mode in p["modes"] and tone in p["tones"]]
    return random.choice(matches) if matches else "Let’s proceed with care:"
