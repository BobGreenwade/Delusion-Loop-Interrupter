"""
phraseEditor.py — Utility for managing mitigation phrase library and editorial tone

Allows staff to add, remove, retag, preview, and rewrite phrases in phrases.json.
Supports tone adjustment, mirroring, escalation phrasing, and editorial rewrites.
Drafted collaboratively with Copilot.
"""

import json
from pathlib import Path

PHRASE_FILE = Path(__file__).parent / "data" / "phrases.json"

# 🔧 Phrase Library Management

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

# 🎭 Editorial Utilities

def adjust_tone(text, target_tone="neutral"):
    if target_tone == "validating":
        return f"I hear you. {text}"
    elif target_tone == "playful":
        return f"Let’s have some fun: {text}"
    elif target_tone == "concerned":
        return f"I'm here for you. {text}"
    elif target_tone == "defiant":
        return f"Not buying it: {text}"
    else:
        return text

def mirror_phrase(user_input):
    return f"You said: '{user_input}' — let’s unpack that."

def escalate_phrase(reason):
    phrases = {
        "emotional_distress": "It’s okay to feel overwhelmed. Let’s take a breath together.",
        "synthetic_limit": "This is beyond my current scope—let’s bring in a human.",
        "ethical_boundary": "I’m not equipped to handle this safely. Escalating support.",
        "loop_detected": "We seem to be circling—let’s pause and reset."
    }
    return phrases.get(reason, "Let’s bring in support to help with this.")

def editorial_rewrite(text, style="lyric"):
    if style == "lyric":
        return f"🎶 {text} — echoing truth in rhythm 🎶"
    elif style == "satire":
        return f"Oh really? {text} (said no one with a fact-checker)."
    elif style == "formal":
        return f"According to verified sources: {text}"
    elif style == "casual":
        return f"Here’s the deal: {text}"
    else:
        return text
