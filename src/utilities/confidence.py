"""
confidence.py — Utility module for epistemic and emotional certainty tagging in DLI

Provides functions to assess, tag, and overlay confidence levels in bot responses.
Helps distinguish speculation from grounded facts and detect rising certainty without new evidence.
Now includes source verification from factCheck.py and semantic matching via semantics.py.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import re
import math
from factCheck import validate_claim, TRUSTED_SOURCES
from semantics import match_wordlist
from learning import run_learning

LOW_CONFIDENCE_MARKERS = [
    "maybe", "possibly", "some say", "unclear", "allegedly", "unverified", "theoretically", "hypothetically"
]
HIGH_CONFIDENCE_MARKERS = [
    "definitely", "clearly", "proven", "confirmed", "without doubt"
]
NEGATIVE_CONFIDENCE_MARKERS = [
    "disproven", "debunked", "illogical", "false", "fictional", "imaginary", "crackpot", "absurd"
]

def tag_confidence_level(text):
    """
    Assigns a confidence score to a given bot response.
    Returns a float between 0.0 (low confidence) and 1.0 (high confidence).
    """
    score = 0.5  # Neutral baseline

    if match_wordlist(text, LOW_CONFIDENCE_MARKERS):
        score -= 0.1
    if match_wordlist(text, HIGH_CONFIDENCE_MARKERS):
        score += 0.1
    if match_wordlist(text, NEGATIVE_CONFIDENCE_MARKERS):
        score -= 0.2  # Stronger penalty for epistemic rejection

    # Optional ML override
    try:
        ml_result = run_learning("confidence_score", {"text": text})
        score = ml_result.get("output", {}).get("confidence", score)
    except Exception:
        pass

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
    boost = min(0.2, 0.05 * len(sources))
    return round(min(1.0, base + boost), 2)
