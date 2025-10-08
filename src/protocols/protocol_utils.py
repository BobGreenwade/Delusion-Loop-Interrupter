"""
protocol_utils.py — Shared utilities for safeguard protocols

Provides logging, fallback routing, and escalation formatting for ethical modules.
Used by ethicalPause, referToHuman, callHuman, scopedMemory, and others.
"""

import datetime

LOG_HISTORY = []

def log_protocol_event(event_type, details):
    """
    Logs a protocol event with timestamp and details.
    """
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = {"timestamp": timestamp, "event": event_type, "details": details}
    LOG_HISTORY.append(entry)
    print(f"[LOG] {timestamp} | {event_type} | {details}")
    return entry

def format_escalation_payload(reason, context=None, urgency="moderate"):
    """
    Formats a standardized escalation payload.
    """
    return {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "reason": reason,
        "urgency": urgency,
        "context": context or {}
    }

def get_log_history(limit=10):
    """
    Returns the most recent protocol events.
    """
    return LOG_HISTORY[-limit:]
