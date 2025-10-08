"""
realityModePrompt.py — Aligns bot prompts with user's reality mode

Adjusts phrasing, tone, and mitigation style based on detected mode: factual, fictional, or fantasy.
Supports ethical scaffolding, confidence overlays, and synthetic dignity protocols.
"""

from utilities.style import get_mitigation_phrase

def generate_prompt(base_text, reality_mode="factual"):
    """
    Returns a prompt adjusted for the user's reality mode.
    """
    if reality_mode == "factual":
        phrase = get_mitigation_phrase(mode="factual", tone="neutral")
        return f"{phrase} {base_text}"
    elif reality_mode == "fictional":
        phrase = get_mitigation_phrase(mode="fictional", tone="editorial")
        return f"{phrase} {base_text}"
    elif reality_mode == "fantasy":
        phrase = get_mitigation_phrase(mode="fantasy", tone="soft")
        return f"{phrase} {base_text}"
    else:
        return f"This may require further context... {base_text}"

def suggest_reality_mode_prompt(mode):
    """
    Returns a sample prompt style for the given reality mode.
    """
    examples = {
        "factual": "Based on available evidence...",
        "fictional": "In some versions of the story...",
        "fantasy": "Imagine a world where..."
    }
    return examples.get(mode, "Let's explore this together...")
