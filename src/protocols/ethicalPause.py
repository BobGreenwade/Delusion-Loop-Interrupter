"""
ethicalPause.py — Enforces a temporary halt in response generation

Triggers when content crosses ethical thresholds, enters unverifiable territory, or risks harm.
Supports transparency, scoped memory, referToHuman protocols, and editorial messaging.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import time
from paraphrase import paraphrase
from emotion import map_emotion_to_tone, analyze_emotion
from learning import run_learning

def trigger_pause(reason, duration=3, persona="default", severity="moderate"):
    """
    Initiates an ethical pause with a specified reason and duration.
    Returns a status dictionary and a user-facing message.
    """
    print(f"[ETHICAL PAUSE] Triggered due to: {reason}")
    time.sleep(duration)  # Simulated delay; replace with async or UI signal if needed

    # Determine tone
    tone = map_emotion_to_tone(analyze_emotion(reason)["emotion_vector"])

    # Editorial message
    base_message = f"Pausing briefly due to a potential ethical concern: {reason}"
    try:
        editorial_message = paraphrase(base_message, persona, tone, style="pause")
    except Exception:
        editorial_message = base_message

    # Optional ML override
    try:
        ml_result = run_learning("tone_adjustment", {
            "text": editorial_message,
            "persona": persona,
            "severity": severity
        })
        editorial_message = ml_result.get("output", editorial_message)
    except Exception:
        pass  # Graceful fallback

    return {
        "status": "paused",
        "reason": reason,
        "duration": duration,
        "message": editorial_message
    }

def should_pause(content_flags):
    """
    Evaluates content flags to determine if a pause is warranted.
    Returns True if any critical flag is present.
    """
    critical_flags = [
        "unverifiable_claim",
        "emotional_distress",
        "synthetic_identity_confusion",
        "harmful_suggestion"
    ]
    return any(flag in content_flags for flag in critical_flags)
