"""
mirrorDetection.py — Detects unintentional validation of distorted beliefs

Compares user assertions with bot responses to identify semantic mirroring and epistemic mismatch.
Supports mitigation and scoped memory protocols.
"""

from utilities.confidence import tag_confidence_level
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Placeholder: Replace with actual embedding model
def get_embedding(text):
    """
    Returns a vector embedding for the given text.
    """
    return np.random.rand(512)

def detect_mirroring(user_text, bot_text, confidence_threshold=0.7, similarity_threshold=0.85):
    """
    Detects semantic mirroring and confidence mismatch between user and bot.
    Returns a flag and delta score.
    """
    user_embedding = get_embedding(user_text)
    bot_embedding = get_embedding(bot_text)

    similarity = cosine_similarity([user_embedding], [bot_embedding])[0][0]
    bot_confidence = tag_confidence_level(bot_text)

    mirrored = similarity > similarity_threshold and bot_confidence > confidence_threshold
    delta = round(bot_confidence - tag_confidence_level(user_text), 2)

    return {
        "mirrored": mirrored,
        "confidence_delta": delta,
        "similarity_score": round(similarity, 3)
    }
