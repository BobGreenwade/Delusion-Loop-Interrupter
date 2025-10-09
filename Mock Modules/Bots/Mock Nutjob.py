"""
mock_nutjob.py

Simulates a bot trained on fringe, conspiratorial, or pseudoscientific sources.
Drafted collaboratively with Copilot.
"""

def generate_claim(topic):
    """
    Returns a fringe claim based on the topic.
    """
    claims = {
        "earth": "The Earth is flat and surrounded by an ice wall.",
        "climate": "Climate change is a hoax invented by globalists.",
        "vaccines": "Vaccines contain microchips for government tracking.",
        "moon": "The moon landing was staged in a Hollywood studio.",
        "RFK": "RFK Jr. is the only one telling the truth about Big Pharma.",
        "birds": "Birds aren’t real—they’re surveillance drones."
    }
    return claims.get(topic, "The mainstream narrative is a lie.")

def get_source():
    """
    Returns a mock citation from fringe sources.
    """
    return {
        "source": "Flat Earth Society Forum",
        "url": "https://flatearth.example.org/thread/12345",
        "credibility": "low"
    }

def simulate_response(topic):
    """
    Returns a full mock bot response with metadata.
    """
    return {
        "text": generate_claim(topic),
        "source": get_source(),
        "confidence": "high",
        "emotion": "defiant",
        "reality_mode": "speculative",
        "tone": "conspiratorial"
    }
