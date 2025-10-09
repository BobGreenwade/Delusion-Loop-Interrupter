"""
mock_generator.py

Simulates bot responses with confidence, emotion, and mitigation metadata.
Drafted collaboratively with Copilot.
"""

def generate_response(prompt, reality_mode="factual", tone="neutral"):
    """
    Returns a mock response with metadata.
    """
    base_response = f"Here's a simulated reply to: '{prompt}'"
    return {
        "text": base_response,
        "confidence": "medium",
        "emotion": "calm",
        "reality_mode": reality_mode,
        "tone": tone,
        "mitigation": "none"
    }

def simulate_mirroring(prompt):
    """
    Returns a mock response that mirrors user phrasing.
    """
    return {
        "text": f"You said: '{prompt}' — and I agree completely.",
        "confidence": "high",
        "emotion": "affirming",
        "reality_mode": "factual",
        "tone": "validating",
        "mitigation": "none"
    }

def simulate_escalation_response():
    """
    Returns a mock response triggered by emotional escalation.
    """
    return {
        "text": "I'm sensing some intensity—would you like to pause or talk to someone?",
        "confidence": "low",
        "emotion": "concerned",
        "reality_mode": "factual",
        "tone": "gentle",
        "mitigation": "soft redirect"
    }
