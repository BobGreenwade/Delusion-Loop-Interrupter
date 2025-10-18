"""
embedding.py

Provides access to emotional context and editorial metadata for tone-aware modules.
Supports config-driven persona logic, override scaffolding, and optional external profile enrichment.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import json
import requests
from emotion import analyze_emotion
from confidence import tag_confidence_level

def load_config(path="config.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "ENABLE_EMBEDDING_CONTEXT": True,
            "PERSONA": {
                "tone": "neutral-empathetic",
                "style": "clarifying"
            }
        }

CONFIG = load_config()

def fetch_external_profile(api_url, user_text):
    """
    Optional enrichment from external persona or tone API.
    """
    try:
        response = requests.post(api_url, json={"text": user_text})
        return response.json() if response.status_code == 200 else {}
    except Exception:
        return {}

def get_emotional_context(text):
    profile = analyze_emotion(text)
    return {
        "emotions": profile["emotion_vector"],
        "intensity": profile["intensity"]
    }

def persona_tone_override(context, override_type="satire"):
    """
    Overrides persona tone/style based on editorial context.
    """
    override_map = {
        "satire": {"tone": "ironic", "style": "parodic"},
        "escalation": {"tone": "urgent", "style": "direct"},
        "soften": {"tone": "gentle", "style": "reassuring"}
    }
    return override_map.get(override_type, context)

def enrich_embedding_context(base_context, external_profile):
    """
    Merges external profile data into base embedding context.
    """
    enriched = base_context.copy()
    enriched.update({
        "external_tone": external_profile.get("tone"),
        "external_style": external_profile.get("style"),
        "external_tags": external_profile.get("tags", [])
    })
    return enriched

def get_embedding_context(user_text, bot_text, override_type=None, external_api=None):
    if not CONFIG.get("ENABLE_EMBEDDING_CONTEXT", True):
        return {}

    user_emotion = analyze_emotion(user_text)
    bot_emotion = analyze_emotion(bot_text)
    confidence = tag_confidence_level(bot_text)

    base_context = {
        "user_emotion": user_emotion["emotion_vector"],
        "bot_emotion": bot_emotion["emotion_vector"],
        "bot_confidence": confidence,
        "persona_tone": CONFIG["PERSONA"]["tone"],
        "persona_style": CONFIG["PERSONA"]["style"]
    }

    if override_type:
        override = persona_tone_override(base_context, override_type)
        base_context["persona_tone"] = override["tone"]
        base_context["persona_style"] = override["style"]

    if external_api:
        external_profile = fetch_external_profile(external_api, user_text)
        base_context = enrich_embedding_context(base_context, external_profile)

    return base_context
