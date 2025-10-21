"""
detectEmotionalEscalation.py — Flags affective spikes and gradual escalation using Plutchik vectors

Compares emotion vectors and intensity scores across turns.
Returns escalation type, period metadata, editorial tone suggestion, and logs emotional profile.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from emotion import analyze_emotion, map_emotion_to_tone
from datetime import datetime

# Optional: external emotional profile log
emotional_profile_log = []

def detect_spike(current_text, previous_text, threshold=0.4):
    current = analyze_emotion(current_text)
    previous = analyze_emotion(previous_text)

    delta_intensity = abs(current["intensity"] - previous["intensity"])
    delta_vector = sum(
        abs(current["emotion_vector"][e] - previous["emotion_vector"][e])
        for e in current["emotion_vector"]
    )

    return delta_intensity > threshold or delta_vector >= 2  # ≥2 new emotions = spike

def detect_gradual_escalation(emotion_history, threshold=0.6):
    if len(emotion_history) < 3:
        return False

    cumulative_intensity = sum(e["intensity"] for e in emotion_history[-3:])
    cumulative_vector_shift = sum(
        abs(emotion_history[-1]["emotion_vector"][e] - emotion_history[-3]["emotion_vector"][e])
        for e in emotion_history[-1]["emotion_vector"]
    )

    return cumulative_intensity > threshold or cumulative_vector_shift >= 3

def get_escalation_period(emotion_history, time_history):
    num_turns = len(emotion_history)
    if time_history and len(time_history) >= 2:
        time_span = time_history[-1] - time_history[0]
        duration_seconds = time_span.total_seconds()
    else:
        duration_seconds = 0
    return {"turns": num_turns, "duration_seconds": duration_seconds}

def log_emotional_profile(user_id, emotion_data):
    """
    Logs emotional profile with timestamp for external modeling.
    """
    emotional_profile_log.append({
        "user": user_id,
        "timestamp": datetime.utcnow().isoformat(),
        "emotion_vector": emotion_data["emotion_vector"],
        "intensity": emotion_data["intensity"]
    })

def detect_escalation(current_text, previous_text, emotion_history, time_history, user_id="default"):
    escalation_type = "none"
    if detect_spike(current_text, previous_text):
        escalation_type = "spike"
    elif detect_gradual_escalation(emotion_history):
        escalation_type = "gradual"

    current_emotion = analyze_emotion(current_text)
    editorial_tone = map_emotion_to_tone(current_emotion["emotion_vector"])
    period = get_escalation_period(emotion_history, time_history)

    # Log emotional profile
    log_emotional_profile(user_id, current_emotion)

    return {
        "escalation_type": escalation_type,
        "period": period,
        "delta_intensity": abs(current_emotion["intensity"] - analyze_emotion(previous_text)["intensity"]),
        "delta_vector": sum(
            abs(current_emotion["emotion_vector"][e] - analyze_emotion(previous_text)["emotion_vector"][e])
            for e in current_emotion["emotion_vector"]
        ),
        "editorial_tone": editorial_tone
    }
