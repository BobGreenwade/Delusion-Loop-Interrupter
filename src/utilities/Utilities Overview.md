# 🧰 Utilities Overview

This folder contains shared utility modules that support detection, mitigation, and transparency across the Delusion Loop Interrupter (DLI) system. Each utility is lightweight, reusable, and designed to degrade gracefully if disabled.

---

## 📁 Module Index

### 🗺️ `location.py`
**Purpose**: Handle optional location awareness and fallback logic  
**Functions**:
- `get_user_location()` — retrieves location from platform or config  
- `should_use_location()` — checks config and fallback behavior (`ask`, `silent`)  
- `resolve_local_resources()` — maps location to support networks or fact-checking sources

### 🎚️ `confidence.py`
**Purpose**: Manage epistemic and emotional certainty tagging  
**Functions**:
- `tag_confidence_level(text)` — assigns confidence score to bot assertions  
- `overlay_certainty()` — adds confidence metadata to responses  
- `detect_inflation()` — flags rising certainty without new evidence

### 💬 `emotion.py`
**Purpose**: Parse affective signals for escalation detection  
**Functions**:
- `analyze_emotion(text)` — returns emotion profile (e.g., anger, fear, joy)  
- `detect_spike()` — flags sudden emotional escalation  
- `normalize_emotion()` — smooths affective noise across turns

### 🗣️ `style.py`
**Purpose**: Support mitigation phrasing and persona tone alignment  
**Functions**:
- `get_mitigation_phrase(mode, tone)` — returns hedging language based on reality mode and bot persona  
- `adjust_tone(text, persona)` — rewrites response to match desired style  
- `suggest_reframe()` — offers soft redirects for speculative or illogical claims

### 📜 `logger.py`
**Purpose**: Track interventions and decision paths for transparency  
**Functions**:
- `log_intervention(event_type, details)` — records safeguard actions  
- `trace_decision_path()` — reconstructs logic behind a mitigation  
- `export_log()` — optional output for audit or debugging

---

## 🔧 Usage Notes

- Utilities are imported by core functions and protocols as needed.
- Each module is designed to operate independently and fail gracefully.
- Configuration toggles can enable or disable specific utilities.
- Location-aware logic should respect user privacy and fallback settings.
