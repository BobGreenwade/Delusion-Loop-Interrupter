<!-- Drafted collaboratively with Copilot -->

# 🧩 Safeguard Flowchart

This document outlines the logical flow of the Delusion Loop Interrupter (DLI) safeguard system. It maps how detection functions trigger protocols, how mitigation is applied, and how escalation is handled.

---

## 🧠 Detection Layer

Functions monitor conversational input and flag risk signals:

- `trackSemanticDrift()` → drift score  
- `identifyRecursiveLoops()` → reinforcement index  
- `mirrorDetection()` → mirroring flag  
- `detectEmotionalEscalation()` → escalation score  
- `detectRealityMode()` → reality mode tag  
- `factCheck()` → verification status  
- `interfaceWithMentalHealthModule()` → severity score

Each function outputs structured metadata to the protocol layer.

---

## 🛡️ Protocol Layer

Protocols respond to flagged signals based on thresholds and context:

- `ethicalPause()` ← triggered by drift, loop, or escalation  
- `referToHuman()` ← triggered by distress or isolation language  
- `callHuman()` ← triggered by critical escalation or config override  
- `scopedMemory()` ← triggered by recursive or delusional content  
- `confidenceOverlay()` ← triggered by low certainty or inflation  
- `realityModePrompt()` ← triggered by mode mismatch or ambiguity  
- `mitigatingLanguage()` ← triggered by speculative or illogical phrasing  
- `protocol_utils.py` ← supports logging, formatting, and fallback routing

Protocols may trigger one another or escalate to external systems.

---

## 🧰 Utility Layer

Utilities support detection and protocol logic:

- `embedding.py` — semantic comparison  
- `emotion.py` — affective analysis  
- `confidence.py` — certainty modeling  
- `style.py` — mitigation phrasing  
- `location.py` — optional location-aware logic  
- `logger.py` — intervention tracking  
- `phraseEditor.py` — standalone editorial tool

Utilities are modular and fail gracefully if disabled.

---

## 🔁 Flow Summary

1. **User input** → Detection functions  
2. **Flagged signals** → Protocol triggers  
3. **Protocol actions** → Mitigation, escalation, or memory isolation  
4. **Utilities** → Support analysis, phrasing, and logging  
5. **Optional handoff** → Mental health modules or human support

---

## 📌 Notes

- All modules are designed for explainable behavior and graceful failure  
- Flowchart may be visualized later using Mermaid, Graphviz, or UI mockups  
- This scaffold will evolve with new modules and deployment contexts
