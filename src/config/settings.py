"""
settings.py — Configuration for safeguard protocols and escalation routing

Defines thresholds, contact mappings, and delivery channels for ethical modules.
Used by callHuman, referToHuman, scopedMemory, and others.
"""

# Notification channels by priority
NOTIFY_CHANNEL = {
    "high": "secure_sms_gateway",
    "moderate": "staff_email",
    "normal": "log_only"
}

# Local contacts by deployment region
LOCAL_CONTACTS = {
    "Corvallis, OR": "Dr. Rivera (Community Liaison)",
    "Puerto Princesa": "Ms. Santos (Field Ethics Officer)",
    "Burabod": "Team Lead - Burabod Node",
    "default": "Platform Safeguard Desk"
}

# Thresholds for triggering protocols
THRESHOLDS = {
    "semantic_drift": 0.4,
    "emotional_escalation": 0.5,
    "recursive_loop": 2.0,
    "confidence_drop": 0.6
}

# Supported reality modes
REALITY_MODES = ["factual", "fictional", "fantasy"]

# External modules available for escalation
EXTERNAL_MODULES = [
    "Qwen3Guard",
    "AI Mental Health Crisis Intervention Bot",
    "MindBridge Escalation API"
]
