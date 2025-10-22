<!-- Drafted collaboratively with Copilot and Bob Greenwade -->

# 🧩 Safeguard Flowchart — Version 0.1.4

This document outlines the logical flow of the Delusion Loop Interrupter (DLI) safeguard system. It maps how detection functions trigger protocols, how mitigation is applied, and how escalation is editorialized.

As of version 0.1.4, this system is considered **deployable for learning** — ready for supervised integration, editorial refinement, and ML-enhanced escalation logic.

---

## 🧠 Detection Layer

Functions monitor conversational input and flag risk signals:

- `trackSemanticDrift()` → drift score  
- `identifyRecursiveLoops()` → reinforcement index  
- `mirrorDetection()` → mirroring flag  
- `detectEmotionalEscalation()` → escalation type + emotion profile  
- `detectRealityMode()` → reality mode tag + confidence  
- `factCheck()` → verification status + confidence delta  
- `interfaceWithMentalHealthModules()` → escalation payload + confirmation  
  - Self-harm-detection integration planned  
- `analyze_emotion()` → emotion vector + intensity  
- `map_emotion_to_tone()` → editorial tone mapping  
- `semantic_distance()` → conceptual gap  
- `reparaphrase()` → editorial stasis detection

Each function outputs structured metadata to the protocol layer.  
**ML-Ready**: All except `interfaceWithMentalHealthModules()`

---

## 🛡️ Protocol Layer

Protocols respond to flagged signals based on thresholds and context:

- `ethicalPause()` ← triggered by drift, loop, or escalation  
- `referToHuman()` ← triggered by distress or isolation language  
  - Uses `referral_text()` for persona-aware phrasing  
- `callHuman()` ← triggered by critical escalation or config override  
  - Includes `handoff_status`, `transcript_action`, and editorial message  
- `scopedMemory()` ← triggered by recursive or delusional content  
- `confidenceOverlay()` ← triggered by low certainty or inflation  
- `realityModePrompt()` ← triggered by mode mismatch or ambiguity  
  - Uses `generate_reality_prompt()` for confidence-aware mitigation  
- `mitigatingLanguage()` ← triggered by speculative or illogical phrasing  
  - Uses `select_mitigation()` with persona and emotional tone  
- `protocol_utils.py` ← supports logging, formatting, and fallback routing  
- `transcript.py` ← supports tagging, summarization, and escalation handoff

Protocols may trigger one another or escalate to external systems.  
**ML-Ready**: All except `ethicalPause()`

---

## 🧰 Utility Layer

Utilities support detection and protocol logic:

- `embedding.py` — semantic comparison  
- `emotion.py` — affective analysis and tone mapping  
- `confidence.py` — certainty modeling  
- `style.py` — mitigation phrasing and tone alignment  
  - Includes `style_shift()` and `generate_style_tag()`  
- `location.py` — optional location-aware logic  
- `logger.py` — intervention tracking  
- `phraseEditor.py` — editorial tool  
  - Includes `retag_phrase()` and `suggest_variants()`  
- `paraphrase.py` — persona-aware phrasing engine  
- `transcript.py` — context buffer, tagging, and escalation handoff  
- `profile.py` — user traits and escalation preferences  
- `semantics.py` — lexical matching and euphemism detection  
  - Includes `match_phrase_structure()` and `detect_euphemism()`

Utilities are modular and fail gracefully if disabled.  
**ML-Ready**: All except `location.py` and `phraseEditor.py`

---

## 🔁 Flow Summary

1. **User input** → Detection functions  
2. **Flagged signals** → Protocol triggers  
3. **Protocol actions** → Mitigation, escalation, or memory isolation  
4. **Utilities** → Support analysis, phrasing, and logging  
5. **Optional handoff** → Mental health modules or human support  
6. **Editorial framing** → Persona-aware phrasing and emotional tone modulation

---

## 📌 Notes

- All modules are designed for explainable behavior and graceful failure  
- Flowchart may be visualized later using Mermaid, Graphviz, or UI mockups  
- Self-harm-detection will be embedded in mental health routing and escalation safeguards
