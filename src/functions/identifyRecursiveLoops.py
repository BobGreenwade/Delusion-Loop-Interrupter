"""
identifyRecursiveLoops.py — Detects belief reinforcement cycles with rising certainty

Analyzes user and bot turns for repetition, certainty inflation, and recursive framing.
Supports loop interruption, mitigation tagging, and editorial escalation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from confidence import tag_confidence_level
from factCheck import check_fact  # Optional: only if fact check module is active

def detect_reinforcement_pattern(turns, certainty_threshold=0.8, repetition_threshold=2, enable_fact_check=False):
    """
    Detects recursive reinforcement loops based on rising certainty and repeated phrasing.
    Returns loop signature, reinforcement index, severity score, and editorial tag.
    """
    if len(turns) < 3:
        return {
            "loop_detected": False,
            "reinforcement_index": 0.0,
            "severity": "low",
            "editorial_tag": "none"
        }

    # Certainty tracking
    certainty_scores = [tag_confidence_level(t) for t in turns]
    inflation_score = sum(
        1 for i in range(len(certainty_scores)-1)
        if certainty_scores[i+1] > certainty_scores[i]
    ) / (len(certainty_scores)-1)

    # Repetition tracking
    normalized = [t.lower().strip() for t in turns]
    repeats = sum(normalized.count(t) > 1 for t in set(normalized))

    reinforcement_index = (repeats / len(turns)) + inflation_score

    # Optional fact check
    fact_check_results = []
    if enable_fact_check:
        fact_check_results = [check_fact(t) for t in turns]
        invalid_facts = sum(1 for r in fact_check_results if r.get("valid") is False)
    else:
        invalid_facts = 0

    # Severity scoring
    severity = "low"
    if reinforcement_index >= repetition_threshold:
        if invalid_facts >= 2:
            severity = "high"
        elif inflation_score > 0.5:
            severity = "moderate"

    # Editorial tag
    editorial_tag = "interrupt-loop" if severity in ["moderate", "high"] else "none"

    return {
        "loop_detected": reinforcement_index >= repetition_threshold,
        "reinforcement_index": round(reinforcement_index, 2),
        "severity": severity,
        "editorial_tag": editorial_tag
    }
