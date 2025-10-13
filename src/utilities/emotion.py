"""
emotion.py — Plutchik-based emotional analysis

Detects emotional signals using Plutchik's 8-core model.
Returns emotion vector and intensity score for editorial modulation.
Drafted collaboratively with Copilot.
"""

from semantics import match_wordlist
from textblob import TextBlob

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

def get_emotion_vector(text):
    """
    Returns a dictionary with Plutchik emotions and their presence (0 or 1).
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
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    vector = get_emotion_vector(text)
    intensity = emotion_intensity(vector)

    return {
        "emotion_vector": vector,
        "intensity": intensity,
        "polarity": round(polarity, 2),
        "subjectivity": round(subjectivity, 2)
    }

def map_emotion_to_tone(emotion_vector):
    with open("toneMap.json", "r") as f:
        tone_map = json.load(f)
    for emotion in emotion_vector:
        if emotion in tone_map:
            return tone_map[emotion][0]
    return "neutral"
