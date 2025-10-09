"""
emotion.py — Utility module for affective signal parsing in DLI

Provides functions to analyze emotional tone, detect escalation, and normalize affective noise.
Supports mitigation protocols and reality mode detection.
"""

from textblob import TextBlob

def analyze_emotion(text):
    """
    Returns a basic emotion profile based on polarity and subjectivity.
    Output: dictionary with 'valence' and 'intensity'
    """
    blob = TextBlob(text)
    valence = blob.sentiment.polarity  # -1.0 (negative) to +1.0 (positive)
    intensity = abs(blob.sentiment.subjectivity)  # 0.0 (objective) to 1.0 (subjective)

    return {
        "valence": round(valence, 2),
        "intensity": round(intensity, 2)
    }

def detect_spike(current_profile, previous_profile, threshold=0.4):
    """
    Flags emotional escalation if valence or intensity shifts exceed threshold.
    Returns True if spike detected, False otherwise.
    """
    delta_valence = abs(current_profile["valence"] - previous_profile["valence"])
    delta_intensity = abs(current_profile["intensity"] - previous_profile["intensity"])

    return delta_valence > threshold or delta_intensity > threshold

def normalize_emotion(history):
    """
    Smooths affective noise across a sequence of emotion profiles.
    Returns a single averaged profile.
    """
    if not history:
        return {"valence": 0.0, "intensity": 0.0}

    valence_sum = sum(p["valence"] for p in history)
    intensity_sum = sum(p["intensity"] for p in history)
    count = len(history)

    return {
        "valence": round(valence_sum / count, 2),
        "intensity": round(intensity_sum / count, 2)
    }
