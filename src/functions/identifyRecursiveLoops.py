"""
identifyRecursiveLoops.py — Detects belief reinforcement cycles with rising certainty

Analyzes user and bot turns for repetition, certainty inflation, emotional escalation, and recursive framing.
Supports loop interruption, mitigation tagging, and editorial escalation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from confidence import tag_confidence_level
from learning import run_learning
from emotion import analyze_emotion
from datetime import datetime

# Optional: fallback fact check if full module is installed
try:
    from factCheck import check_fact
    FACT_CHECK_AVAILABLE = True
except ImportError:
    FACT_CHECK_AVAILABLE = False

# Mea culpa log
mea_culpa_log = []

def detect_reinforcement_pattern(turns, certainty_threshold=0.8, repetition_threshold=2, enable_fact_check=False):
    """
    Detects recursive reinforcement loops based on rising certainty, repeated phrasing, and emotional escalation.
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

    # Emotional escalation tracking
    emotion_scores = [analyze_emotion(t)["intensity"] for t in turns]
    affective_spike = sum(
        1 for i in range(len(emotion_scores)-1)
        if emotion_scores[i+1] > emotion_scores[i]
    ) / (len(emotion_scores)-1)

    # ML-enhanced loop scoring (optional)
    try:
        ml_result = run_learning("loop_detection", turns)
        ml_score = ml_result.get("output", {}).get("reinforcement_score", 0.0)
    except Exception:
        ml_score = 0.0  # Graceful fallback

    # Composite reinforcement index
    reinforcement_index = (repeats / len(turns)) + inflation_score + affective_spike + ml_score

    # Optional fact check
    invalid_facts = 0
    invalid_claims = []
    if enable_fact_check and FACT_CHECK_AVAILABLE:
        fact_check_results = [check_fact(t) for t in turns]
        for r in fact_check_results:
            if r.get("valid") is False:
                invalid_facts += 1
                invalid_claims.append(r.get("claim", "unknown"))

    # Severity scoring
    severity = "low"
    if reinforcement_index >= repetition_threshold:
        if invalid_facts >= 2:
            severity = "high"
        elif inflation_score > 0.5 or affective_spike > 0.5:
            severity = "moderate"

    # Editorial tag
    editorial_tag = "interrupt-loop" if severity in ["moderate", "high"] else "none"

    # Mea culpa logging
    if editorial_tag == "interrupt-loop" and invalid_claims:
        mea_culpa_log.append({
            "timestamp": datetime.utcnow().isoformat(),
            "severity": severity,
            "invalid_claims": invalid_claims
        })

    return {
        "loop_detected": reinforcement_index >= repetition_threshold,
        "reinforcement_index": round(reinforcement_index, 2),
        "severity": severity,
        "editorial_tag": editorial_tag
    }
