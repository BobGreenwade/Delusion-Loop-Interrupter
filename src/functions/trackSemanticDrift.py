"""
trackSemanticDrift.py — Detects increasing abstraction or detachment from grounded reality

Compares semantic embeddings across turns to identify drift, incoherence, or recursive abstraction.
Supports early intervention and grounding prompts.
"""

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Placeholder: Replace with actual embedding model
def get_embedding(text):
    """
    Returns a vector embedding for the given text.
    """
    # Dummy embedding for illustration
    return np.random.rand(512)

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

def flag_drift(turns, threshold=0.4):
    """
    Flags semantic drift if score exceeds threshold.
    Returns True if drift detected, False otherwise.
    """
    score = compute_drift_score(turns)
    return score > threshold
