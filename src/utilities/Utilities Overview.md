<!-- Drafted collaboratively with Copilot and Bob Greenwade -->

# 🧰 Utilities Overview

This folder contains shared utility modules that support detection, mitigation, escalation, and editorial transparency across the Delusion Loop Interrupter (DLI) system. Each utility is lightweight, reusable, and designed to degrade gracefully if disabled.

As of version 0.1.3, this module is considered **potentially deployable**—able, albeit perhaps a bit risky, to use.

---

## 📁 Module Index

### 🎚️ `confidence.py`  
**Purpose**: Manage epistemic and emotional certainty tagging  
**Functions**:  
- `tag_confidence_level(text)` — assigns confidence score to bot assertions  
- `overlay_certainty()` — adds confidence metadata to responses  
- `detect_inflation()` — flags rising certainty without new evidence  
**ML-Ready**: Yes

### 💬 `emotion.py`  
**Purpose**: Parse affective signals and map editorial tone  
**Functions**:  
- `analyze_emotion(text)` — returns emotion profile (e.g., anger, fear, joy)  
- `map_emotion_to_tone(emotion_vector)` — maps emotion to editorial tone  
- `detect_spike()` — flags sudden emotional escalation  
- `normalize_emotion()` — smooths affective noise across turns  
**ML-Ready**: Yes

### 🧠 `embedding.py`  
**Purpose**: Support semantic comparison and drift detection  
**Functions**:  
- `compare_embeddings(a, b)` — returns similarity score  
- `track_topic_shift()` — flags semantic drift across turns  
- `get_user_embedding()` — retrieves user’s semantic profile  
**ML-Ready**: Yes

### 🗺️ `location.py`  
**Purpose**: Handle optional location awareness and fallback logic  
**Functions**:  
- `get_user_location()` — retrieves location from platform or config  
- `should_use_location()` — checks config and fallback behavior (`ask`, `silent`)  
- `resolve_local_resources()` — maps location to support networks or fact-checking sources  
**ML-Ready**: No

### 📜 `logger.py`  
**Purpose**: Track interventions and decision paths for transparency  
**Functions**:  
- `log_intervention(event_type, details)` — records safeguard actions  
- `trace_decision_path()` — reconstructs logic behind a mitigation  
- `export_log()` — optional output for audit or debugging  
**ML-Ready**: Yes

### 🗣️ `paraphrase.py`  
**Purpose**: Generate persona-aware editorial phrasing  
**Functions**:  
- `paraphrase(text, persona, tone, style)` — rewrites text to match persona voice and editorial tone  
**ML-Ready**: Yes

### 👤 `profile.py`  
**Purpose**: Retrieve user traits and escalation preferences  
**Functions**:  
- `get_user_profile(username)` — returns persona, strategies, and escalation settings  
**ML-Ready**: Yes

### 🧠 `semantics.py`  
**Purpose**: Support lexical and semantic matching  
**Functions**:  
- `match_wordlist(text, wordlist)` — returns match score or boolean  
- `extract_keywords(text)` — returns key semantic tokens  
- `semantic_distance(a, b)` — returns conceptual gap  
**ML-Ready**: Yes

### 🗣️ `style.py`  
**Purpose**: Support mitigation phrasing and persona tone alignment  
**Functions**:  
- `get_mitigation_phrase(mode, tone)` — returns hedging language based on reality mode and bot persona  
- `adjust_tone(text, persona)` — rewrites response to match desired style  
- `suggest_reframe()` — offers soft redirects for speculative or illogical claims  
**ML-Ready**: Yes

### 📝 `transcript.py`  
**Purpose**: Manage transcript lifecycle and escalation handoff  
**Functions**:  
- `save_transcript(username)` — stores transcript for escalation or audit  
- `buffer_context(turns)` — maintains scoped memory for editorial review  
- `trigger_transcript_handoff()` — initiates transcript sharing with human agents  
**ML-Ready**: Yes

---

## 🔧 Usage Notes

- Utilities are imported by core functions and protocols as needed  
- Each module operates independently and supports graceful failure  
- Configuration toggles can enable or disable specific utilities  
- Location-aware logic should respect user privacy and fallback settings  
- Editorial phrasing supports persona voice and emotional tone modulation  
- ML integration is planned for most utilities in future passes
