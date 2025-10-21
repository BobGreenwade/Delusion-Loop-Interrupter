"""
emotion.py — Plutchik-based emotional analysis

Detects emotional signals using Plutchik's 8-core model.
Returns emotion vector and intensity score for editorial modulation.
Supports future expansion to nuanced and compound emotions.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import json
from semantics import match_wordlist
from textblob import TextBlob
from learning import run_learning

# Core Plutchik emotions with basic cues
PLUTCHIK_EMOTIONS = {
    "joy": ["happy", "joyful", "elated", "content", "cheerful"],
    "trust": ["safe", "secure", "reliable", "faith", "confident"],
    "fear": ["afraid", "scared", "terrified", "anxious", "nervous"],
    "surprise": ["shocked", "amazed", "startled", "unexpected", "astonished"],
    "sadness": ["sad", "depressed", "grief", "loss", "lonely"],
    "disgust": ["gross", "repulsed", "nauseated", "sickened", "distaste"],
    "anger": ["angry", "furious", "rage", "hate", "irritated"],
    "anticipation": ["excited", "eager", "curious", "hopeful", "expecting"]
}

# Reserved for future expansion
PLUTCHIK_EXTENSIONS = {
    "ecstasy": ["ecstatic", "blissful"],
    "serenity": ["calm", "peaceful"],
    "terror": ["horrified", "panicked"],
    "apprehension": ["uneasy", "worried"],
    "amazement": ["awe", "dumbfounded"],
    "distraction": ["confused", "scattered"],
    "loathing": ["revulsion", "abhorrence"],
    "boredom": ["indifferent", "apathetic"]
}

def get_emotion_vector(text):
    """
    Returns a dictionary with Plutchik emotions and their presence (0 or 1).
    Future-ready for nuanced and compound emotions.
    """
    vector = {emotion: 0 for emotion in PLUTCHIK_EMOTIONS}
    for emotion, cues in PLUTCHIK_EMOTIONS.items():
        if match_wordlist(text, cues):
            vector[emotion] = 1
    return vector

def emotion_intensity(vector):
    """
    Returns an intensity score based on number of active emotions.
    """
    active = sum(vector.values())
    return round(active / len(vector), 2)

def analyze_emotion(text):
    """
    Returns full emotional metadata including vector, intensity, polarity, and subjectivity.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    vector = get_emotion_vector(text)
    intensity = emotion_intensity(vector)

    # Optional ML override
    try:
        ml_result = run_learning("emotion_analysis", {"text": text})
        vector.update(ml_result.get("output", {}).get("emotion_vector", {}))
        intensity = ml_result.get("output", {}).get("intensity", intensity)
    except Exception:
        pass

    return {
        "emotion_vector": vector,
        "intensity": intensity,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }

def map_emotion_to_tone(emotion_vector):
    """
    Maps dominant emotion to editorial tone using toneMap.json.
    """
    try:
        with open("toneMap.json", "r") as f:
            tone_map = json.load(f)
        for emotion in emotion_vector:
            if emotion_vector[emotion] and emotion in tone_map:
                return tone_map[emotion][0]
    except Exception:
        pass
    return "neutral"
