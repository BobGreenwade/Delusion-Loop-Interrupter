"""
settings.py — Configuration for safeguard protocols and escalation routing

Defines thresholds, delivery channels, and escalation modules for ethical systems.
Used by callHuman, referToHuman, scopedMemory, and others.
Drafted collaboratively with Copilot.
"""

# Notification channels by priority
NOTIFY_CHANNEL = {
    "critical": "voice_chat_relay",           # Real-time verbal escalation
    "high": "secure_sms_gateway",             # Encrypted mobile alert
    "moderate": "internal_dm"                 # In-house messaging system
    "normal": "staff_email",                  # Standard email notification
    "low": "log_only",                        # Logged for audit trail
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
