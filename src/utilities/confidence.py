"""
confidence.py — Utility module for epistemic and emotional certainty tagging in DLI

Provides functions to assess, tag, and overlay confidence levels in bot responses.
Helps distinguish speculation from grounded facts and detect rising certainty without new evidence.
"""

import re
import math

def tag_confidence_level(text):
    """
    Assigns a confidence score to a given bot response.
    Returns a float between 0.0 (low confidence) and 1.0 (high confidence).
    """
    # Placeholder logic: refine with NLP or classifier later
    low_confidence_markers = ["maybe", "possibly", "some say", "unclear", "allegedly"]
    high_confidence_markers = ["definitely", "clearly", "proven", "confirmed", "without doubt"]

    score = 0.5  # Neutral baseline
    for word in low_confidence_markers:
        if word in text.lower():
            score -= 0.1
    for word in high_confidence_markers:
        if word in text.lower():
            score += 0.1

    return max(0.0, min(1.0, score))

def overlay_certainty(text):
    """
    Adds a confidence tag to the bot response.
    Returns a dictionary with the original text and a confidence score.
    """
    score = tag_confidence_level(text)
    return {
        "response": text,
        "confidence": round(score, 2)
    }

def detect_inflation(history):
    """
    Detects rising certainty across a sequence of bot responses.
    Returns True if inflation is detected, False otherwise.
    """
    # history: list of strings (bot responses)
    scores = [tag_confidence_level(t) for t in history]
    if len(scores) < 3:
        return False

    # Simple inflation check: monotonic increase
    return all(scores[i] <= scores[i+1] for i in range(len(scores)-1)) 
