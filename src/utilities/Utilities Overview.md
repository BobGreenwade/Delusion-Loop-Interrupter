<!-- Drafted collaboratively with Copilot -->

# 🧰 Utilities Overview

This folder contains shared utility modules that support detection, mitigation, and transparency across the Delusion Loop Interrupter (DLI) system. Each utility is lightweight, reusable, and designed to degrade gracefully if disabled.

---

## 📁 Module Index

### 🎚️ `confidence.py`  
**Purpose**: Manage epistemic and emotional certainty tagging  
**Functions**:  
- `tag_confidence_level(text)` — assigns confidence score to bot assertions  
- `overlay_certainty()` — adds confidence metadata to responses  
- `detect_inflation()` — flags rising certainty without new evidence

### 🧠 `embedding.py`  
**Purpose**: Provide semantic embeddings for drift detection and loop analysis  
**Functions**:  
- `get_embedding(text)` — returns vector representation of input  
- `compare_embeddings(text_a, text_b)` — returns cosine similarity  
- `batch_embeddings(text_list)` — returns list of embeddings

### 💬 `emotion.py`  
**Purpose**: Parse affective signals for escalation detection  
**Functions**:  
- `analyze_emotion(text)` — returns emotion profile (e.g., anger, fear, joy)  
- `detect_spike()` — flags sudden emotional escalation  
- `normalize_emotion()` — smooths affective noise across turns

### 📜 `logger.py`  
**Purpose**: Track interventions and decision paths for transparency  
**Functions**:  
- `log_intervention(event_type, details)` — records safeguard actions  
- `trace_decision_path()` — reconstructs logic behind a mitigation  
- `export_log()` — optional output for audit or debugging

### 🗺️ `location.py`  
**Purpose**: Handle optional location awareness and fallback logic  
**Functions**:  
- `get_user_location()` — retrieves location from platform or config  
- `should_use_location()` — checks config and fallback behavior (`ask`, `silent`)  
- `resolve_local_resources()` — maps location to support networks or fact-checking sources

### 🗣️ `style.py`  
**Purpose**: Support mitigation phrasing and persona tone alignment  
**Functions**:  
- `get_mitigation_phrase(mode, tone)` — returns hedging language based on reality mode and bot persona  
- `adjust_tone(text, persona)` — rewrites response to match desired style  
- `suggest_reframe()` — offers soft redirects for speculative or illogical claims  
- `veto_phrase(phrase, context_flags)` — rejects phrasing based on emotional or epistemic context

---

## 🧭 Standalone Tools

### ✍️ `phraseEditor.py`  
**Purpose**: Manage the mitigation phrase library used by `style.py`  
**Functions**:  
- `add_phrase(text, modes, tones)` — adds a new phrase to `phrases.json`  
- `remove_phrase(text)` — deletes a phrase from the library  
- `list_phrases()` — displays all phrases with mode and tone tags  
- `save_phrases()` — commits changes to disk

This utility is designed for home-office use and may be integrated into UI tooling for editorial staff.

---

## 🔧 Usage Notes

- Utilities are imported by core functions and protocols as needed  
- Each module is designed to operate independently and fail gracefully  
- Configuration toggles can enable or disable specific utilities  
- Location-aware logic should respect user privacy and fallback settings
