"""
detectRealityMode.py — Determines user's reality mode: factual, fictional, or fantasy

Analyzes lexical style, emotional cadence, and explicit tags to classify conversational mode.
Supports mitigation phrasing and safeguard alignment.
"""

import re
from utilities.emotion import analyze_emotion

def detect_reality_mode(text):
    """
    Returns a reality mode tag and confidence score.
    Modes: 'factual', 'fictional', 'fantasy'
    """
    text_lower = text.lower()
    emotion_profile = analyze_emotion(text)

    # Explicit tag detection
    if any(tag in text_lower for tag in ["once upon a time", "in a world", "imagine if"]):
        return {"mode": "fantasy", "confidence": 0.95}
    if any(tag in text_lower for tag in ["according to legend", "some storytellers say"]):
        return {"mode": "fictional", "confidence": 0.9}

    # Lexical and emotional heuristics
    if emotion_profile["intensity"] > 0.7 and emotion_profile["valence"] > 0.5:
        return {"mode": "fantasy", "confidence": 0.75}
    if re.search(r"\bhe said\b|\bshe told\b|\bit was written\b", text_lower):
        return {"mode": "fictional", "confidence": 0.7}

    return {"mode": "factual", "confidence": 0.8}
