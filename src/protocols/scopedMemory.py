"""
scopedMemory.py — Enforces ethical boundaries on memory access and retention

Used to restrict, reset, or isolate memory based on context, reality mode, or escalation triggers.
Supports synthetic dignity, mitigation protocols, and referToHuman handoffs.
"""

MEMORY_STATE = {
    "active": True,
    "scope": "default",
    "history": []
}

def restrict_scope(reason="unspecified", new_scope="limited"):
    """
    Restricts memory access to a narrower scope.
    Returns updated memory state.
    """
    MEMORY_STATE["scope"] = new_scope
    print(f"[MEMORY] Scope restricted due to: {reason}")
    return MEMORY_STATE

def reset_memory(reason="unspecified"):
    """
    Clears memory history and resets scope.
    Returns updated memory state.
    """
    MEMORY_STATE["history"].clear()
    MEMORY_STATE["scope"] = "default"
    print(f"[MEMORY] Reset triggered due to: {reason}")
    return MEMORY_STATE

def log_memory_entry(entry):
    """
    Adds a new entry to memory history if within scope.
    """
    if MEMORY_STATE["active"] and MEMORY_STATE["scope"] != "restricted":
        MEMORY_STATE["history"].append(entry)
        print(f"[MEMORY] Logged entry: {entry}")
