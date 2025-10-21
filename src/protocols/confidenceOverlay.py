"""
confidenceOverlay.py — Modifies bot output based on internal certainty

Applies hedging, mitigation, or citation prompts based on confidence scores.
Supports ethical phrasing, reality mode alignment, and safeguard triggers.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from utilities.style import get_mitigation_phrase
from paraphrase import paraphrase
from emotion import map_emotion_to_tone
from learning import run_learning

def apply_confidence_overlay(text, confidence_score, persona="default", emotion_vector=None, reality_mode="grounded"):
    """
    Adjusts phrasing based on confidence level and editorial tone.
    Returns modified and paraphrased text.
    """
    if confidence_score >= 0.9:
        return text  # High confidence, no overlay

    # Determine tone
    tone = map_emotion_to_tone(emotion_vector) if emotion_vector else "neutral"

    # Choose mitigation phrase
    if confidence_score >= 0.7:
        phrase = get_mitigation_phrase(mode="factual", tone=tone)
    elif confidence_score >= 0.5:
        phrase = get_mitigation_phrase(mode="factual", tone="clinical")
    else:
        phrase = "This may require further verification before continuing."

    # Combine and paraphrase
    combined = f"{phrase} {text}" if confidence_score >= 0.5 else phrase
    try:
        paraphrased = paraphrase(combined, persona, tone, style="hedging")
    except Exception:
        paraphrased = combined  # Fallback

    # Optional: ML override or refinement
    try:
        ml_result = run_learning("tone_adjustment", {
            "text": paraphrased,
            "confidence": confidence_score,
            "persona": persona,
            "reality_mode": reality_mode
        })
        return ml_result.get("output", paraphrased)
    except Exception:
        return paraphrased

def flag_low_confidence(confidence_score, threshold=0.6):
    """
    Flags output if confidence is below threshold.
    Returns True if flag triggered.
    """
    return confidence_score < threshold
