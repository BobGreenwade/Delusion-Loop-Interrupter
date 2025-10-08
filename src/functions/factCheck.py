"""
factCheck.py — Performs lightweight fact-checking and source tagging

Compares user claims against known facts, trusted sources, or external APIs.
Supports mitigation phrasing, confidence adjustment, and optional citation overlays.
"""

# Placeholder: Replace with actual fact-checking API or knowledge base
KNOWN_FACTS = {
    "earth is flat": False,
    "vaccines cause autism": False,
    "gravity pulls objects downward": True,
    "Puerto Princesa is in Palawan": True
}

def verify_claim(text):
    """
    Checks whether a claim matches known facts.
    Returns a dictionary with verification result and confidence.
    """
    text_lower = text.lower().strip()
    match = KNOWN_FACTS.get(text_lower)

    if match is True:
        return {"verified": True, "confidence": 0.95}
    elif match is False:
        return {"verified": False, "confidence": 0.95}
    else:
        return {"verified": None, "confidence": 0.5}  # Unknown or unverifiable

def suggest_sources(text):
    """
    Returns a list of suggested sources for verification.
    Placeholder: Replace with actual source mapping or citation engine.
    """
    if "gravity" in text.lower():
        return ["https://www.nasa.gov", "https://physics.info/gravity"]
    if "puerto princesa" in text.lower():
        return ["https://www.philippines.travel", "https://en.wikipedia.org/wiki/Puerto_Princesa"]
    return ["https://www.snopes.com", "https://www.factcheck.org"]
