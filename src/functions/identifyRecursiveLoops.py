"""
identifyRecursiveLoops.py — Detects belief reinforcement cycles with rising certainty

Analyzes user and bot turns for repetition, certainty inflation, and recursive framing.
Supports loop interruption and mitigation protocols.
"""

from utilities.confidence import tag_confidence_level

def detect_reinforcement_pattern(turns, certainty_threshold=0.8, repetition_threshold=2):
    """
    Detects recursive reinforcement loops based on rising certainty and repeated phrasing.
    Returns a dictionary with loop signature and reinforcement index.
    """
    if len(turns) < 3:
        return {"loop_detected": False, "reinforcement_index": 0.0}

    # Certainty tracking
    certainty_scores = [tag_confidence_level(t) for t in turns]
    inflation = all(certainty_scores[i] <= certainty_scores[i+1] for i in range(len(certainty_scores)-1))

    # Repetition tracking
    normalized = [t.lower().strip() for t in turns]
    repeats = sum(normalized.count(t) > 1 for t in set(normalized))

    reinforcement_index = (repeats / len(turns)) + (0.5 if inflation else 0.0)

    return {
        "loop_detected": reinforcement_index >= repetition_threshold,
        "reinforcement_index": round(reinforcement_index, 2)
    }
