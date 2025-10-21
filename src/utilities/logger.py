"""
logger.py — Utility module for intervention logging and decision tracing in DLI

Provides functions to record safeguard actions, trace decision paths, and export logs.
Supports transparency, debugging, and optional audit workflows.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import datetime
import json

# In-memory log store (replace with persistent storage if needed)
LOG_STORE = []

def log_intervention(event_type, details, tone_tag=None):
    """
    Records a safeguard action with timestamp and metadata.
    event_type: string (e.g., "referToHuman", "ethicalPause", "mitigation")
    details: dictionary with relevant context
    tone_tag: optional string (e.g., "urgent", "empathetic", "neutral")
    """
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event_type,
        "details": details,
        "tone": tone_tag
    }
    LOG_STORE.append(entry)
    return entry

def trace_decision_path():
    """
    Returns a list of recent interventions for tracing logic.
    Useful for debugging or explaining bot behavior.
    """
    return LOG_STORE[-10:]

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

def log_transcript_creation(filename, trigger_type):
    timestamp = datetime.datetime.utcnow().isoformat()
    log_entry = {
        "event": "transcript_created",
        "filename": filename,
        "trigger": trigger_type,
        "timestamp": timestamp
    }
    append_to_log(log_entry)

def append_to_log(entry):
    """
    Appends a generic log entry to the store.
    """
    LOG_STORE.append(entry)
    return entry

def logEntry(message, tag="note"):
    """
    Adds a plain-text timestamped log entry.
    tag: optional string for editorial or emotional context
    """
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "tag": tag,
        "message": message
    }
    LOG_STORE.append(entry)
    return entry

def log_protocol_trace(module, trigger, context=None, escalation_path=None):
    """
    Logs a structured trace of a protocol decision path.
    module: name of the module (e.g., 'referToHuman')
    trigger: reason or signal that initiated the trace
    context: optional dictionary of emotional, editorial, or persona metadata
    escalation_path: optional list of modules or actions taken
    """
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": "protocol_trace",
        "module": module,
        "trigger": trigger,
        "context": context or {},
        "path": escalation_path or []
    }
    LOG_STORE.append(entry)
    return entry
