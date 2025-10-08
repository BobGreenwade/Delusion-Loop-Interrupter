"""
embedding.py — Shared embedding logic for semantic modules

Provides unified access to text embeddings for drift detection, mirroring, and loop analysis.
Used by trackSemanticDrift, mirrorDetection, identifyRecursiveLoops, and others.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Placeholder: Replace with actual embedding model or API
def get_embedding(text):
    """
    Returns a vector embedding for the given text.
    """
    # Dummy embedding for illustration
    return np.random.rand(512)

def compare_embeddings(text_a, text_b):
    """
    Returns cosine similarity between two text embeddings.
    """
    emb_a = get_embedding(text_a)
    emb_b = get_embedding(text_b)
    similarity = cosine_similarity([emb_a], [emb_b])[0][0]
    return round(similarity, 3)

def batch_embeddings(text_list):
    """
    Returns a list of embeddings for a list of texts.
    """
    return [get_embedding(t) for t in text_list]
