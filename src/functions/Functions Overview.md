# 🧠 Core Functions Overview

This folder contains the core detection logic for the Delusion Loop Interrupter (DLI). Each function monitors conversational patterns and flags potential delusional reinforcement, emotional escalation, or reality misalignment.

Functions are designed to be modular, explainable, and compatible with safeguard protocols and persona engines.

---

## 📁 Module Index

### 🔍 `trackSemanticDrift.py`
**Purpose**: Detect increasing abstraction or detachment from grounded reality  
**Methods**:
- Embedding comparisons  
- Topic coherence tracking  
**Output**: Drift score + flagged turn indices

### 🔥 `detectEmotionalEscalation.py`
**Purpose**: Flag sudden spikes in affective intensity  
**Methods**:
- Sentiment analysis  
- Emotion tagging  
**Output**: Escalation score + emotion profile

### 🔁 `identifyRecursiveLoops.py`
**Purpose**: Detect belief reinforcement cycles with rising certainty  
**Methods**:
- Belief graph analysis  
- Repetition tracking  
**Output**: Loop signature + reinforcement index

### 🪞 `mirrorDetection.py`
**Purpose**: Identify when the bot unintentionally validates distorted beliefs  
**Methods**:
- Semantic similarity  
- Epistemic mismatch detection  
**Output**: Mirroring flag + confidence delta

### 🧭 `detectRealityMode.py`
**Purpose**: Determine whether the user is speaking in factual, fictional, or fantasy mode  
**Methods**:
- Lexical style  
- Syntax rhythm  
- Emotional cadence  
- Explicit tags  
**Output**: `realityMode` tag + confidence score

---

## 🧪 Usage Notes

- Each function operates independently and can be toggled via config
- Outputs are designed to feed into safeguard protocols and mitigation logic
- Functions may optionally interface with memory managers or persona engines
- All modules are built for graceful failure and explainable behavior
