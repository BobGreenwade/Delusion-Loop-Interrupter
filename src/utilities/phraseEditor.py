"""
phraseEditor.py — Utility for managing mitigation phrase library

Allows staff to add, remove, or retag phrases in phrases.json.
"""

import json
from pathlib import Path

PHRASE_FILE = Path(__file__).parent / "data" / "phrases.json"

def load_phrases():
    with open(PHRASE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_phrases(phrases):
    with open(PHRASE_FILE, "w", encoding="utf-8") as f:
        json.dump(phrases, f, indent=2)

def add_phrase(text, modes, tones):
    phrases = load_phrases()
    phrases.append({"text": text, "modes": modes, "tones": tones})
    save_phrases(phrases)
    print(f"[ADDED] {text}")

def remove_phrase(text):
    phrases = load_phrases()
    filtered = [p for p in phrases if p["text"] != text]
    save_phrases(filtered)
    print(f"[REMOVED] {text}")

def list_phrases():
    for p in load_phrases():
        print(f"{p['text']} → modes: {p['modes']}, tones: {p['tones']}")
