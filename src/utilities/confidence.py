"""
confidence.py — Utility module for epistemic and emotional certainty tagging in DLI

Provides functions to assess, tag, and overlay confidence levels in bot responses.
Helps distinguish speculation from grounded facts and detect rising certainty without new evidence.
Now includes source verification from factCheck.py.
Drafted collaboratively with Copilot.
"""

import re
import math
from factCheck import validate_claim, TRUSTED_SOURCES

low_confidence_markers = ["maybe", "possibly", "some say", "unclear", "allegedly"]
high_confidence_markers = ["definitely", "clearly", "proven", "confirmed", "without doubt"]

def tag_confidence_level(text):
    score = 0.5
    for word in low_confidence_markers:
        if word in text.lower():
            score -= 0.1
    for word in high_confidence_markers:
        if word in text.lower():
            score += 0.1
    return max(0.0, min(1.0, score))

def overlay_certainty(text):
    score = tag_confidence_level(text)
    sources = validate_claim(text)
    verified = len(sources) > 0
    return {
        "response": text,
        "confidence": round(score, 2),
        "verified_sources": [s["source"] for s in sources] if verified else [],
        "verification_status": "verified" if verified else "unverified"
    }

def detect_inflation(history):
    scores = [tag_confidence_level(t) for t in history]
    if len(scores) < 3:
        return False
    return all(scores[i] <= scores[i+1] for i in range(len(scores)-1))

def verify_claim_strength(text):
    """
    Returns a confidence score adjusted by source verification.
    """
    base = tag_confidence_level(text)
    sources = validate_claim(text)
    if not sources:
        return base
    # Boost confidence if multiple trusted sources match
    boost = min(0.2, 0.05 * len(sources))
    return round(min(1.0, base + boost), 2)
