"""
mirrorDetection.py — Detects unintentional validation of distorted beliefs

Compares user assertions with bot responses to identify semantic mirroring and epistemic mismatch.
Supports mitigation tagging, scoped memory protocols, and editorial escalation.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from confidence import tag_confidence_level
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import hashlib
from factCheck import check_fact  # Optional: only if factCheck.py is active

def get_embedding(text, dim=512):
    """
    Returns a pseudo-embedding vector for the given text.
    Uses token hashing for deterministic output.
    Replace with real model later.
    """
    tokens = text.lower().split()
    vector = np.zeros(dim)

    for token in tokens:
        h = int(hashlib.md5(token.encode()).hexdigest(), 16)
        index = h % dim
        vector[index] += 1

    norm = np.linalg.norm(vector)
    return vector / norm if norm != 0 else vector

def detect_mirroring(user_text, bot_text, confidence_threshold=0.7, similarity_threshold=0.85, enable_fact_check=False):
    """
    Detects semantic mirroring and confidence mismatch between user and bot.
    Returns mirroring flag, similarity score, confidence delta, and mitigation tag.
    """
    user_embedding = get_embedding(user_text)
    bot_embedding = get_embedding(bot_text)

    similarity = cosine_similarity([user_embedding], [bot_embedding])[0][0]
    user_confidence = tag_confidence_level(user_text)
    bot_confidence = tag_confidence_level(bot_text)
    delta = round(bot_confidence - user_confidence, 2)

    mirrored = similarity > similarity_threshold and bot_confidence > confidence_threshold

    # Optional fact check
    epistemic_mismatch = False
    if enable_fact_check:
        user_fact = check_fact(user_text)
        bot_fact = check_fact(bot_text)
        if user_fact.get("valid") is False and bot_fact.get("valid") is True:
            epistemic_mismatch = True

    # Mitigation tagging
    mitigation_tag = "none"
    if mirrored and delta > 0.3:
        mitigation_tag = "soft-reframe"
    if epistemic_mismatch:
        mitigation_tag = "interrupt-mirroring"

    return {
        "mirrored": mirrored,
        "similarity_score": round(similarity, 3),
        "confidence_delta": delta,
        "epistemic_mismatch": epistemic_mismatch,
        "mitigation_tag": mitigation_tag
    }
