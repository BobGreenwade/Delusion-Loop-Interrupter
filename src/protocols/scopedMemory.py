"""
scopedMemory.py — Enforces ethical boundaries on memory access and retention

Used to restrict, reset, or isolate memory based on context, reality mode, or escalation triggers.
Supports synthetic dignity, mitigation protocols, and referToHuman handoffs.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from learning import run_learning
from embedding import get_user_profile
from emotion import analyze_emotion, map_emotion_to_tone

MEMORY_STATE = {
    "active": True,
    "scope": "default",
    "history": []
}

def restrict_scope(reason="unspecified", new_scope="limited", username="User"):
    """
    Restricts memory scope based on reason and optional ML refinement.
    """
    try:
        ml_result = run_learning("scope_adjustment", {
            "reason": reason,
            "persona": get_user_profile(username).get("persona", "default")
        })
        new_scope = ml_result.get("output", {}).get("scope", new_scope)
    except Exception:
        pass

    MEMORY_STATE["scope"] = new_scope
    print(f"[MEMORY] Scope restricted due to: {reason}")
    return MEMORY_STATE

def reset_memory(reason="unspecified"):
    """
    Clears memory history and resets scope.
    """
    MEMORY_STATE["history"].clear()
    MEMORY_STATE["scope"] = "default"
    print(f"[MEMORY] Reset triggered due to: {reason}")
    return MEMORY_STATE

def log_memory_entry(entry):
    """
    Logs a memory entry if scope allows.
    """
    if MEMORY_STATE["active"] and MEMORY_STATE["scope"] != "restricted":
        MEMORY_STATE["history"].append(entry)
        print(f"[MEMORY] Logged entry: {entry}")

def log_mitigation_event(user_text, bot_text, mitigation_result, username="User"):
    """
    Logs a mitigation event with full metadata and optional persona tone.
    """
    emotion_vector = analyze_emotion(user_text)["emotion_vector"]
    tone = map_emotion_to_tone(emotion_vector)
    persona = get_user_profile(username).get("persona", "default")

    entry = {
        "type": "mitigation",
        "user": user_text,
        "bot": bot_text,
        "mitigated": mitigation_result["mitigated"],
        "confidence": mitigation_result["confidence"],
        "mirroring_score": mitigation_result["mirroring_score"],
        "notes": mitigation_result["notes"],
        "persona": persona,
        "tone": tone
    }
    log_memory_entry(entry)

def get_recent_mitigation_events(n=5):
    """
    Returns the last n mitigation events.
    """
    events = [e for e in MEMORY_STATE["history"] if e.get("type") == "mitigation"]
    return events[-n:]
