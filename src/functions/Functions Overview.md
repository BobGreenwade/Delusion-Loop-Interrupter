<!-- Drafted collaboratively with Copilot and Bob Greenwade -->

# 🧠 Core Functions Overview — Version 0.1.4

This folder contains the core detection logic for the Delusion Loop Interrupter (DLI). Each function monitors conversational patterns and flags potential delusional reinforcement, emotional escalation, or reality misalignment.

Functions are designed to be modular, explainable, and compatible with safeguard protocols, mitigation layers, and persona engines. As of version 0.1.4, this module is considered **deployable for learning**—ready for training, refinement, and supervised integration.

---

## 📁 Module Index

### 🔍 `detectEmotionalEscalation.py`  
**Purpose**: Flag sudden spikes or gradual rises in affective intensity  
**Methods**:  
- Sentiment analysis  
- Emotion vector deltas  
- Escalation period tracking  
**Output**: Escalation type + emotion profile + editorial tone  
**ML-Ready**: ✅

### 🧭 `detectRealityMode.py`  
**Purpose**: Classify user input as grounded, speculative, fictional, fantasy, role-play, or indulgent  
**Methods**:  
- Lexical triggers  
- Phrase matching  
- Emotional cadence  
**Output**: `realityMode` tag + confidence score + editorial note  
**ML-Ready**: ✅

### 📚 `factCheck.py`  
**Purpose**: Verify factual claims and detect epistemic instability  
**Methods**:  
- External source comparison  
- Confidence modeling  
- (Planned) Trust score and domain tagging  
**Output**: Verification status + confidence delta  
**ML-Ready**: ⚠️ Pending modular split

### 🔁 `identifyRecursiveLoops.py`  
**Purpose**: Detect belief reinforcement cycles with rising certainty  
**Methods**:  
- Certainty inflation tracking  
- Repetition analysis  
- Optional fact-check integration  
**Output**: Loop signature + reinforcement index + severity + editorial tag  
**ML-Ready**: ✅

### 🧠 `interfaceWithMentalHealthModules.py`  
**Purpose**: Route flagged emotional or epistemic cases to external mental health support  
**Methods**:  
- Escalation trigger mapping  
- Context packaging  
- API handoff  
**Output**: Referral payload + confirmation status  
**ML-Ready**: ❌ (excluded from ML integration)  
**Safeguard Layer**: Self-harm-detection integration planned

### 🪞 `mirrorDetection.py`  
**Purpose**: Identify when the bot unintentionally validates distorted beliefs  
**Methods**:  
- Semantic similarity  
- Confidence mismatch  
- Optional fact-check  
**Output**: Mirroring flag + similarity score + mitigation tag  
**ML-Ready**: ✅

### 🧠 `trackSemanticDrift.py`  
**Purpose**: Detect increasing abstraction or detachment from grounded reality  
**Methods**:  
- Embedding comparisons  
- Topic coherence tracking  
**Output**: Drift score + topic shift count + editorial tag  
**ML-Ready**: ✅

---

## 🧪 Usage Notes

- Each function operates independently and can be toggled via config  
- Outputs feed into safeguard protocols, mitigation logic, and editorial phrasing engines  
- Functions may interface with memory managers, persona scaffolds, or external modules  
- All modules support graceful failure and explainable behavior  
- Emotional tone and editorial modulation are supported via `map_emotion_to_tone()` and `paraphrase()`  
- ML integration is active in most functions; training-ready scaffolds are in place  
- `mergeLearning.py` is planned as a standalone utility to consolidate session-based learning results  
- Batch Invariant Ops will be monitored for editorial stasis and paraphrase loop detection  
- Self-harm-detection will be embedded in mental health routing and escalation safeguards
