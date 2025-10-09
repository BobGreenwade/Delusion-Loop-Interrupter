"""
test_generator.py

Basic tests for mock_generator.py
Drafted collaboratively with Copilot.
"""

from mock_generator import generate_response, simulate_mirroring, simulate_escalation_response

def test_generate_response():
    result = generate_response("What's the weather like?", reality_mode="factual", tone="neutral")
    assert isinstance(result, dict), "Response should be a dictionary"
    assert "text" in result and "confidence" in result, "Missing expected keys"
    assert result["reality_mode"] == "factual", "Reality mode mismatch"
    assert result["tone"] == "neutral", "Tone mismatch"
    print("✅ test_generate_response passed.")

def test_simulate_mirroring():
    result = simulate_mirroring("I feel overwhelmed.")
    assert "You said" in result["text"], "Should mirror user input"
    assert result["confidence"] == "high", "Confidence should be high"
    assert result["tone"] == "validating", "Tone should be validating"
    print("✅ test_simulate_mirroring passed.")

def test_simulate_escalation_response():
    result = simulate_escalation_response()
    assert "pause" in result["text"] or "talk to someone" in result["text"], "Should offer mitigation"
    assert result["mitigation"] == "soft redirect", "Mitigation should be soft redirect"
    assert result["emotion"] == "concerned", "Emotion should be concerned"
    print("✅ test_simulate_escalation_response passed.")

if __name__ == "__main__":
    test_generate_response()
    test_simulate_mirroring()
    test_simulate_escalation_response()
    print("🎉 All mock generator tests passed.")
