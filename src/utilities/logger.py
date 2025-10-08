"""
logger.py — Utility module for intervention logging and decision tracing in DLI

Provides functions to record safeguard actions, trace decision paths, and export logs.
Supports transparency, debugging, and optional audit workflows.
"""

import datetime
import json

# In-memory log store (replace with persistent storage if needed)
LOG_STORE = []

def log_intervention(event_type, details):
    """
    Records a safeguard action with timestamp and metadata.
    event_type: string (e.g., "referToHuman", "ethicalPause", "mitigation")
    details: dictionary with relevant context
    """
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event_type,
        "details": details
    }
    LOG_STORE.append(entry)
    return entry

def trace_decision_path():
    """
    Returns a list of recent interventions for tracing logic.
    Useful for debugging or explaining bot behavior.
    """
    return LOG_STORE[-10:]  # Return last 10 entries

def export_log(filepath="dli_log.json"):
    """
    Exports the full log store to a JSON file.
    Optional: replace with platform-specific export logic.
    """
    try:
        with open(filepath, "w") as f:
            json.dump(LOG_STORE, f, indent=2)
        return True
    except Exception as e:
        print(f"Export failed: {e}")
        return False
