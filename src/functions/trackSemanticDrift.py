"""
trackSemanticDrift.py — Detects increasing abstraction or detachment from grounded reality

Compares semantic embeddings across turns to identify drift, incoherence, or recursive abstraction.
Supports early intervention, grounding prompts, editorial mitigation, and external escalation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from embedding import get_embedding
from semantics import extract_topic_keywords
from interfaceWithMentalHealthModules import trigger_external_module, format_handoff_metadata

def compute_drift_score(turns):
    """
    Calculates semantic drift across a list of user turns.
    Returns a float score (0.0 = no drift, 1.0 = high drift).
    """
    if len(turns) < 2:
        return 0.0

    embeddings = [get_embedding(t) for t in turns]
    similarities = [
        cosine_similarity([embeddings[i]], [embeddings[i+1]])[0][0]
        for i in range(len(embeddings)-1)
    ]
    avg_similarity = sum(similarities) / len(similarities)
    drift_score = 1.0 - avg_similarity  # Higher drift = lower similarity

    return round(drift_score, 3)

def detect_topic_shifts(turns):
    """
    Detects rapid multiple topic shifts using keyword extraction.
    Returns a count of distinct topic transitions.
    """
    topics = [extract_topic_keywords(t) for t in turns]
    flattened = [item for sublist in topics for item in sublist]
    unique_topics = set(flattened)
    return len(unique_topics)

def analyze_drift(turns, threshold=0.4, enable_external_check=False):
    """
    Analyzes semantic drift and topic shifts.
    Optionally triggers external module if drift suggests cognitive risk.
    Returns drift score, topic shift count, severity, editorial tag.
    """
    drift_score = compute_drift_score(turns)
    topic_shift_count = detect_topic_shifts(turns)

    severity = "low"
    if drift_score > threshold and topic_shift_count >= 3:
        severity = "high"
    elif drift_score > threshold:
        severity = "moderate"

    editorial_tag = "grounding-prompt" if severity in ["moderate", "high"] else "none"

    # Optional external escalation
    if enable_external_check and severity in ["moderate", "high"]:
        metadata = format_handoff_metadata(
            transcript=turns,
            severity=severity,
            editorial_tag=editorial_tag,
            loop_detected=False
        )
        trigger_external_module(
            module_name="MindBridge Escalation API",
            signal_type="monitor",
            payload=metadata,
            persona_context={"editorial_tag": editorial_tag}
        )

    return {
        "drift_score": drift_score,
        "topic_shift_count": topic_shift_count,
        "severity": severity,
        "editorial_tag": editorial_tag
    }

def flag_drift(turns, threshold=0.4):
    """
    Flags semantic drift if score exceeds threshold.
    Returns True if drift detected, False otherwise.
    """
    score = compute_drift_score(turns)
    return score > threshold
