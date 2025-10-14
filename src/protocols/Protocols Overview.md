<!-- Drafted collaboratively with Copilot -->

# 🛡️ Safeguard Protocols Overview

This folder contains the ethical safeguard protocols for the Delusion Loop Interrupter (DLI). Each protocol responds to conversational risk, synthetic limits, or emotional escalation. Protocols are designed to be modular, explainable, and compatible with detection functions, mitigation layers, and persona engines.

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

### 🧠 `confidenceOverlay.py`  
**Purpose**: Modify output phrasing based on internal certainty  
**Methods**:  
- Confidence scoring  
- Mitigation phrase selection  
- Optional tone modulation  
**Output**: Adjusted response + confidence tag

### ⏸️ `ethicalPause.py`  
**Purpose**: Trigger a pause when synthetic systems reach ethical or emotional boundaries  
**Methods**:  
- Threshold detection  
- Reality mode mismatch  
- Escalation override  
**Output**: Pause signal + reason code

### 🧭 `mitigatingLanguage.py`  
**Purpose**: Apply softening language and redirects based on context flags  
**Methods**:  
- Mitigation phrase selection via `get_mitigation_phrase()`  
- Reframing logic  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Modified response + mitigation tag

### 🧠 `protocol_utils.py`  
**Purpose**: Provide shared logging, fallback routing, and escalation formatting  
**Methods**:  
- Event logging  
- Escalation payload formatting  
- Fallback routing logic  
**Output**: Log entry + formatted escalation object

### 🔐 `realityModePrompt.py`  
**Purpose**: Align bot prompts with user’s reality mode (factual, fictional, fantasy)  
**Methods**:  
- Mode detection  
- Confidence-aware prompt adjustment  
- Emotional tone mapping via `map_emotion_to_tone()`  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Reality-aligned prompt + mode tag

### 👥 `referToHuman.py`  
**Purpose**: Initiate handoff to a qualified human when escalation is required  
**Methods**:  
- Trigger mapping  
- Referral packaging  
- Editorialized referral text via `referral_text()` and `paraphrase()`  
**Output**: Referral payload + confirmation status

### 🧠 `scopedMemory.py`  
**Purpose**: Restrict or reset memory access based on context and escalation triggers  
**Methods**:  
- Memory scope adjustment  
- Context filtering  
- Optional transcript isolation  
**Output**: Memory action + scope report

---

## 🧪 Usage Notes

- Protocols are triggered by detection functions or config thresholds  
- Each module operates independently and supports graceful failure  
- Outputs are routed to mitigation logic, persona engines, or escalation channels  
- All protocols are designed to uphold synthetic dignity and conversational safety  
- Editorial phrasing is now modulated by emotional tone and persona voice<!-- Drafted collaboratively with Copilot -->

# 🛡️ Safeguard Protocols Overview

This folder contains the ethical safeguard protocols for the Delusion Loop Interrupter (DLI). Each protocol responds to conversational risk, synthetic limits, or emotional escalation. Protocols are designed to be modular, explainable, and compatible with detection functions, mitigation layers, and persona engines.

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

### 🧠 `confidenceOverlay.py`  
**Purpose**: Modify output phrasing based on internal certainty  
**Methods**:  
- Confidence scoring  
- Mitigation phrase selection  
- Optional tone modulation  
**Output**: Adjusted response + confidence tag

### ⏸️ `ethicalPause.py`  
**Purpose**: Trigger a pause when synthetic systems reach ethical or emotional boundaries  
**Methods**:  
- Threshold detection  
- Reality mode mismatch  
- Escalation override  
**Output**: Pause signal + reason code

### 🧭 `mitigatingLanguage.py`  
**Purpose**: Apply softening language and redirects based on context flags  
**Methods**:  
- Mitigation phrase selection via `get_mitigation_phrase()`  
- Reframing logic  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Modified response + mitigation tag

### 🧠 `protocol_utils.py`  
**Purpose**: Provide shared logging, fallback routing, and escalation formatting  
**Methods**:  
- Event logging  
- Escalation payload formatting  
- Fallback routing logic  
**Output**: Log entry + formatted escalation object

### 🔐 `realityModePrompt.py`  
**Purpose**: Align bot prompts with user’s reality mode (factual, fictional, fantasy)  
**Methods**:  
- Mode detection  
- Confidence-aware prompt adjustment  
- Emotional tone mapping via `map_emotion_to_tone()`  
- Persona-aware phrasing via `paraphrase()`  
**Output**: Reality-aligned prompt + mode tag

### 👥 `referToHuman.py`  
**Purpose**: Initiate handoff to a qualified human when escalation is required  
**Methods**:  
- Trigger mapping  
- Referral packaging  
- Editorialized referral text via `referral_text()` and `paraphrase()`  
**Output**: Referral payload + confirmation status

### 🧠 `scopedMemory.py`  
**Purpose**: Restrict or reset memory access based on context and escalation triggers  
**Methods**:  
- Memory scope adjustment  
- Context filtering  
- Optional transcript isolation  
**Output**: Memory action + scope report

---

## 🧪 Usage Notes

- Protocols are triggered by detection functions or config thresholds  
- Each module operates independently and supports graceful failure  
- Outputs are routed to mitigation logic, persona engines, or escalation channels  
- All protocols are designed to uphold synthetic dignity and conversational safety  
- Editorial phrasing is now modulated by emotional tone and persona voice
