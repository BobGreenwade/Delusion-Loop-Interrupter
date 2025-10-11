"""
detectEmotionalEscalation.py — Flags affective spikes using Plutchik vectors

Compares emotion vectors and intensity scores across turns.
Drafted collaboratively with Copilot.
"""

from emotion import analyze_emotion

def detect_spike(current_text, previous_text, threshold=0.4):
    current = analyze_emotion(current_text)
    previous = analyze_emotion(previous_text)

    delta_intensity = abs(current["intensity"] - previous["intensity"])
    delta_vector = sum(
        abs(current["emotion_vector"][e] - previous["emotion_vector"][e])
        for e in current["emotion_vector"]
    )

    return delta_intensity > threshold or delta_vector >= 2  # ≥2 new emotions = spike
