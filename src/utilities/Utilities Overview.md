<!-- Drafted collaboratively with Copilot and Bob Greenwade -->

# 🧰 Utilities Overview — Version 0.1.4

This folder contains shared utility modules that support detection, mitigation, escalation, and editorial transparency across the Delusion Loop Interrupter (DLI) system. Each utility is lightweight, reusable, and designed to degrade gracefully if disabled.

As of version 0.1.4, this module is considered **deployable for learning** — ready for supervised training, editorial refinement, and modular integration.

---

## 📁 Module Index

### 🎚️ `confidence.py`  
**Purpose**: Manage epistemic and emotional certainty tagging  
**Functions**:  
- `tag_confidence_level(text)` — assigns confidence score to bot assertions  
- `overlay_certainty()` — adds confidence metadata to responses  
- `detect_inflation()` — flags rising certainty without new evidence  
**ML-Ready**: ✅

### 💬 `emotion.py`  
**Purpose**: Parse affective signals and map editorial tone  
**Functions**:  
- `analyze_emotion(text)` — returns emotion profile (e.g., anger, fear, joy)  
- `map_emotion_to_tone(emotion_vector)` — maps emotion to editorial tone  
- `detect_spike()` — flags sudden emotional escalation  
- `normalize_emotion()` — smooths affective noise across turns  
**ML-Ready**: ✅

### 🧠 `embedding.py`  
**Purpose**: Support semantic comparison and drift detection  
**Functions**:  
- `compare_embeddings(a, b)` — returns similarity score  
- `track_topic_shift()` — flags semantic drift across turns  
- `get_user_embedding()` — retrieves user’s semantic profile  
**ML-Ready**: ✅

### 🗺️ `location.py`  
**Purpose**: Handle optional location awareness and fallback logic  
**Functions**:  
- `get_user_location()` — retrieves location from platform or config  
- `should_use_location()` — checks config and fallback behavior (`ask`, `silent`)  
- `resolve_local_resources()` — maps location to support networks or fact-checking sources  
**ML-Ready**: ❌

### 📜 `logger.py`  
**Purpose**: Track interventions and decision paths for transparency  
**Functions**:  
- `log_intervention(event_type, details)` — records safeguard actions  
- `trace_decision_path()` — reconstructs logic behind a mitigation  
- `export_log()` — optional output for audit or debugging  
**ML-Ready**: ✅

### 🗣️ `paraphrase.py`  
**Purpose**: Generate persona-aware editorial phrasing  
**Functions**:  
- `paraphrase(text, persona, tone, style)` — rewrites text to match persona voice and editorial tone  
- `reparaphrase(text, previous_attempt)` — refines phrasing to avoid editorial stasis  
**ML-Ready**: ✅

### 👤 `profile.py`  
**Purpose**: Retrieve user traits and escalation preferences  
**Functions**:  
- `get_user_profile(username)` — returns persona, strategies, and escalation settings  
- `get_characteristic(username, key)` — retrieves or refines editorial traits  
**ML-Ready**: ✅

### 🧠 `semantics.py`  
**Purpose**: Support lexical and semantic matching  
**Functions**:  
- `match_wordlist(text, wordlist)` — returns match score or boolean  
- `match_phrase_structure(text)` — detects editorial rhythm and clause types  
- `detect_euphemism(text)` — flags softened or indirect language  
- `semantic_distance(a, b)` — returns conceptual gap  
**ML-Ready**: ✅

### 🗣️ `style.py`  
**Purpose**: Support mitigation phrasing and persona tone alignment  
**Functions**:  
- `get_mitigation_phrase(mode, tone)` — returns hedging language based on reality mode and bot persona  
- `adjust_tone(text, persona)` — rewrites response to match desired style  
- `style_shift()` — suggests alternate tone/style combinations  
- `generate_style_tag()` — produces editorial tag for logging or paraphrasing  
**ML-Ready**: ✅

### 📝 `transcript.py`  
**Purpose**: Manage transcript lifecycle and escalation handoff  
**Functions**:  
- `save_transcript(username)` — stores transcript for escalation or audit  
- `update_context_buffer(turn)` — maintains scoped memory for editorial review  
- `summarize_transcript()` — generates editorial summary  
- `tag_transcript_metadata()` — adds tone, escalation level, and persona tags  
**ML-Ready**: ✅

---

## 🔧 Usage Notes

- Utilities are imported by core functions and protocols as needed  
- Each module operates independently and supports graceful failure  
- Configuration toggles can enable or disable specific utilities  
- Location-aware logic should respect user privacy and fallback settings  
- Editorial phrasing supports persona voice and emotional tone modulation
