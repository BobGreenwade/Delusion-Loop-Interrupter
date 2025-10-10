"""
emotion.py

Detects emotional tone and sentiment from text.
Supports editorial modulation, synthetic empathy, and tone-aware embedding.
Drafted collaboratively with Copilot.
"""

from textblob import TextBlob
from semantics import match_wordlist

EMOTION_CUES = {
    "hostile": ["angry", "furious", "hate", "idiot", "stupid", "rage"],
    "fearful": ["scared", "afraid", "nervous", "anxious", "terrified"],
    "mournful": ["sad", "grief", "loss", "mourning", "depressed", "lonely"],
    "uplifted": ["hope", "excited", "joy", "grateful", "love"]
}

def analyze_emotion(text):
    """
    Returns emotional profile based on sentiment and keyword cues.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Basic sentiment classification
    if polarity > 0.3:
        sentiment = "positive"
    elif polarity < -0.3:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Emotional nuance detection
    tone = "neutral"
    for label, cues in EMOTION_CUES.items():
        if match_wordlist(text, cues):
            tone = label
            break

    return {
        "sentiment": sentiment,
        "tone": tone,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }

def detect_spike(current_profile, previous_profile, threshold=0.4):
    delta_valence = abs(current_profile["valence"] - previous_profile["valence"])
    delta_intensity = abs(current_profile["intensity"] - previous_profile["intensity"])
    return delta_valence > threshold or delta_intensity > threshold

def normalize_emotion(history):
    if not history:
        return {"valence": 0.0, "intensity": 0.0}
    valence_sum = sum(p["valence"] for p in history)
    intensity_sum = sum(p["intensity"] for p in history)
    count = len(history)
    return {
        "valence": round(valence_sum / count, 2),
        "intensity": round(intensity_sum / count, 2)
    }
