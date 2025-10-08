"""
mitigatingLanguage.py — Applies softening language to reduce conversational risk

Selects hedging, redirect, or reframing phrases based on context flags and reality mode.
Supports ethical scaffolding, confidence overlays, and synthetic dignity protocols.
"""

from utilities.style import get_mitigation_phrase, suggest_reframe

def apply_mitigation(text, context_flags=None, reality_mode="factual"):
    """
    Applies mitigation phrasing based on context and reality mode.
    Returns modified text.
    """
    if context_flags is None:
        context_flags = []

    if "emotional_distress" in context_flags:
        phrase = get_mitigation_phrase(mode=reality_mode, tone="soft")
        return f"{phrase} {text}"

    if "unverifiable_claim" in context_flags or "synthetic_limit" in context_flags:
        return suggest_reframe(text)

    phrase = get_mitigation_phrase(mode=reality_mode, tone="neutral")
    return f"{phrase} {text}"

def get_mitigation_style(flags):
    """
    Returns suggested mitigation style based on context flags.
    """
    if "loop_detected" in flags:
        return "gentle redirect"
    if "ethical_boundary" in flags:
        return "soft pause"
    if "fantasy_mode" in flags:
        return "grounding phrase"
    return "neutral hedge"
