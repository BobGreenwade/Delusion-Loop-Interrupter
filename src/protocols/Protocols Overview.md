<!-- Drafted collaboratively with Copilot and Bob Greenwade -->

# 🛡️ Safeguard Protocols Overview — Version 0.1.4

This folder contains the ethical safeguard protocols for the Delusion Loop Interrupter (DLI). Each protocol responds to conversational risk, synthetic limits, or emotional escalation. Protocols are modular, explainable, and compatible with detection functions, mitigation layers, and persona engines.

As of version 0.1.4, this module is considered **deployable for learning** — ready for supervised integration, editorial refinement, and ML-enhanced escalation logic.

---

## 📁 Module Index

### 📞 `callHuman.py`  
**Purpose**: Notify designated staff or local authority when escalation is triggered  
**Methods**:  
- Channel selection (`sms`, `email`, `log`)  
- Contact mapping by location  
- Transcript packaging and `handoff_status` logic  
- Persona-aware escalation phrasing via `paraphrase()`  
**Output**: Notification payload + delivery status + editorial message  
**ML-Ready**: ✅

### 🧠 `confidenceOverlay.py`  
**Purpose**: Modify output phrasing based on internal certainty  
**Methods**:  
- Confidence scoring  
- Mitigation phrase selection  
- Optional tone modulation  
**Output**: Adjusted response + confidence tag  
**ML-Ready**: ✅

### ⏸️ `ethicalPause.py`  
**Purpose**: Trigger a pause when synthetic systems reach ethical or emotional boundaries  
**Methods**:  
- Threshold detection  
- Reality mode mismatch  
- Escalation override  
**Output**: Pause signal + reason code  
**ML-Ready**: ❌ (excluded from ML integration)

### 🧭 `mitigatingLanguage.py`  
**Purpose**: Apply softening language and redirects based on context flags  
**Methods**:  
- Mitigation phrase selection via `get_mitigation_phrase()`  
- Reframing logic  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Modified response + mitigation tag  
**ML-Ready**: ✅ (high priority)

### 🧠 `protocol_utils.py`  
**Purpose**: Provide shared logging, fallback routing, and escalation formatting  
**Methods**:  
- Event logging  
- Escalation payload formatting  
- Fallback routing logic  
**Output**: Log entry + formatted escalation object  
**ML-Ready**: ✅

### 🔐 `realityModePrompt.py`  
**Purpose**: Align bot prompts with user’s reality mode (factual, fictional, fantasy, etc.)  
**Methods**:  
- Mode detection  
- Confidence-aware prompt adjustment  
- Emotional tone mapping via `map_emotion_to_tone()`  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Reality-aligned prompt + mode tag  
**ML-Ready**: ✅

### 👥 `referToHuman.py`  
**Purpose**: Initiate handoff to a qualified human when escalation is required  
**Methods**:  
- Trigger mapping  
- Referral packaging  
- Editorialized referral text via `referral_text()` and `paraphrase()`  
**Output**: Referral payload + confirmation status  
**ML-Ready**: ✅

### 🧠 `scopedMemory.py`  
**Purpose**: Restrict or reset memory access based on context and escalation triggers  
**Methods**:  
- Memory scope adjustment  
- Context filtering  
- Optional transcript isolation  
**Output**: Memory action + scope report  
**ML-Ready**: ✅

---

## 🧪 Usage Notes

- Protocols are triggered by detection functions or config thresholds  
- Each module operates independently and supports graceful failure  
- Outputs are routed to mitigation logic, persona engines, or escalation channels  
- All protocols are designed to uphold conversational safety and synthetic dignity  
- Editorial phrasing is modulated by emotional tone and persona voice
