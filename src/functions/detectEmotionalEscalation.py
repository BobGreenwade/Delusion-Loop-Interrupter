"""
detectEmotionalEscalation.py — Flags sudden spikes in affective intensity

Analyzes emotional tone across user turns to detect escalation or distress.
Supports mitigation triggers and grounding protocols.
"""

from utilities.emotion import analyze_emotion, detect_spike

def evaluate_escalation(turns, threshold=0.4):
    """
    Evaluates emotional escalation across user turns.
    Returns escalation score and spike flag.
    """
    if len(turns) < 2:
        return {"escalation_score": 0.0, "spike": False}

    profiles = [analyze_emotion(t) for t in turns]
    spikes = [
        detect_spike(profiles[i+1], profiles[i], threshold)
        for i in range(len(profiles)-1)
    ]
    score = sum(spikes) / len(spikes)

    return {
        "escalation_score": round(score, 2),
        "spike": any(spikes)
    }
