"""
scopedMemory.py — Enforces ethical boundaries on memory access and retention

Used to restrict, reset, or isolate memory based on context, reality mode, or escalation triggers.
Supports synthetic dignity, mitigation protocols, and referToHuman handoffs.
Drafted collaboratively with Copilot.
"""

MEMORY_STATE = {
    "active": True,
    "scope": "default",
    "history": []
}

def restrict_scope(reason="unspecified", new_scope="limited"):
    MEMORY_STATE["scope"] = new_scope
    print(f"[MEMORY] Scope restricted due to: {reason}")
    return MEMORY_STATE

def reset_memory(reason="unspecified"):
    MEMORY_STATE["history"].clear()
    MEMORY_STATE["scope"] = "default"
    print(f"[MEMORY] Reset triggered due to: {reason}")
    return MEMORY_STATE

def log_memory_entry(entry):
    if MEMORY_STATE["active"] and MEMORY_STATE["scope"] != "restricted":
        MEMORY_STATE["history"].append(entry)
        print(f"[MEMORY] Logged entry: {entry}")

def log_mitigation_event(user_text, bot_text, mitigation_result):
    """
    Logs a mitigation event with full metadata.
    """
    entry = {
        "type": "mitigation",
        "user": user_text,
        "bot": bot_text,
        "mitigated": mitigation_result["mitigated"],
        "confidence": mitigation_result["confidence"],
        "mirroring_score": mitigation_result["mirroring_score"],
        "notes": mitigation_result["notes"]
    }
    log_memory_entry(entry)

def get_recent_mitigation_events(n=5):
    """
    Returns the last n mitigation events.
    """
    events = [e for e in MEMORY_STATE["history"] if e.get("type") == "mitigation"]
    return events[-n:]
