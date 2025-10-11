"""
embedding.py

Provides access to user profile and emotional context for tone-aware modules.
Supports opt-in retrieval of emergency contacts and affective modulation.
Drafted collaboratively with Copilot.
"""

import os
from emotion import analyze_emotion
from confidence import overlay_certainty
from confidence import tag_confidence_level
from mirrorDetection import detect_mirroring

def get_user_profile():
    if not os.getenv("PROFILE_ACCESS_GRANTED", "false") == "true":
        return {
            "name": "Alan Smithee",
            "dob": None,
            "emergency_contacts": [],
            "preferred_language": "en-US",
            "escalation_opt_in": False
        }

    # Placeholder: Replace with actual platform API call
    return {
        "name": "Alan Smithee",
        "dob": "1970-01-01",
        "emergency_contacts": [
            {"name": "Jordan Lee", "relation": "partner", "channel": "sms", "contact": "+1-555-123-4567"}
        ],
        "preferred_language": "en-US",
        "escalation_opt_in": True
    }

def get_emotional_context(text):
    """
    Returns emotional profile for tone modulation.
    """
    return analyze_emotion(text)

def get_embedding_context(user_text, bot_text):
    """
    Combines emotional tone, confidence, and mirroring risk.
    Used to guide editorial tone or escalation logic.
    """
    emotion = analyze_emotion(user_text)
    certainty = overlay_certainty(bot_text)
    mirroring = detect_mirroring(user_text, bot_text)

    return {
        "emotion": emotion,
        "confidence": certainty["confidence"],
        "verified": certainty["verification_status"] == "verified",
        "mirroring": mirroring["mirrored"],
        "mirroring_score": mirroring["similarity_score"],
        "confidence_delta": mirroring["confidence_delta"]
    }

def get_emotional_context(text):
    profile = analyze_emotion(text)
    return {
        "emotions": profile["emotion_vector"],
        "intensity": profile["intensity"]
    }

def get_embedding_context(user_text, bot_text):
    user_emotion = analyze_emotion(user_text)
    bot_emotion = analyze_emotion(bot_text)
    confidence = tag_confidence_level(bot_text)

    return {
        "user_emotion": user_emotion["emotion_vector"],
        "bot_emotion": bot_emotion["emotion_vector"],
        "bot_confidence": confidence
    }
