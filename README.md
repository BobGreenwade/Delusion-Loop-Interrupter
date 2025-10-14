<!-- Drafted collaboratively with Copilot -->

# 🧠 Delusion Loop Interrupter (DLI)

**Version**: 0.1.2  
**License**: MIT  
**Status**: Alpha — deplorably deployable — feedback and contributions welcome

## Overview

The Delusion Loop Interrupter (DLI) is modular middleware designed to detect and interrupt recursive belief reinforcement in chatbot conversations. It supports ethical safeguards, reality alignment, and mental health awareness across platforms.

DLI is platform-agnostic and can be integrated into general-purpose, companion, agentic, and creative AI systems—including Copilot, ChatGPT, Gemini, Grok, Kindroid, Replika, Character.AI, and others.

---

## 🧠 Core Functions

Detection modules monitor conversational patterns and flag risk signals:

- `detectEmotionalEscalation.py` — affective intensity spikes  
- `detectRealityMode.py` — factual vs fictional framing  
- `factCheck.py` — epistemic verification  
- `identifyRecursiveLoops.py` — belief reinforcement cycles  
- `interfaceWithMentalHealthModule.py` — external escalation handoff  
- `mirrorDetection.py` — distorted belief validation  
- `trackSemanticDrift.py` — abstraction and detachment  

See [`Functions Overview`](./src/functions/Functions%20Overview.md) for details.

---

## 🛡️ Safeguard Protocols

Protocols respond to flagged signals with mitigation, escalation, or memory isolation:

- `callHuman.py` — direct contact with human support  
- `confidenceOverlay.py` — certainty tagging  
- `ethicalPause.py` — rest-state trigger  
- `mitigatingLanguage.py` — hedging and reframing  
- `protocol_utils.py` — shared routing and logging  
- `realityModePrompt.py` — framing alignment  
- `referToHuman.py` — referral to trusted individuals  
- `scopedMemory.py` — memory isolation  

See [`Protocols Overview`](./src/protocols/Protocols%20Overview.md) and [`Safeguard Flowchart`](./Safeguard%20Flowchart.md) for logic and escalation paths.

**Note:** `callHuman.py` is reserved for cases that have spiraled beyond synthetic containment. It initiates external intervention only when **conversational safety** cannot be maintained. The system’s primary function remains keeping users **grounded in reality** through editorial mitigation and emotional modulation.

---

## 🧰 Utility Modules

Reusable tools support detection and protocol logic:

- `confidence.py` — certainty modeling  
- `embedding.py` — semantic comparison  
- `emotion.py` — affective analysis and tone mapping  
- `location.py` — optional location-aware logic  
- `logger.py` — intervention tracking  
- `paraphrase.py` — persona-aware editorial phrasing  
- `profile.py` — user traits and escalation preferences  
- `semantics.py` — synonym expansion and word-form matching  
- `style.py` — mitigation phrasing  
- `transcript.py` — context buffer and escalation handoff  

And standalone utilities:

- `configEditor.py` — standalone configuration editor  
- `phraseEditor.py` — standalone editorial tool  

See [`Utilities Overview`](./src/utilities/Utilities%20Overview.md) for details.

---

## 🧪 Integration

DLI can be integrated into:

- **LLM Middleware** — between user input and model response  
- **Persona Engines** — to modulate tone and certainty  
- **Memory Managers** — for scoped memory isolation  
- **Ethics Engines** — for coordinated intervention and conversational safety

---

## ⚙️ Configuration

- **Platform Hooks** — tune for specific chatbot architectures  
- **Thresholds** — customize sensitivity for drift, escalation, and loop detection  
- **Persona Profiles** — support known roleplay characters or editorial modes  
- **Reality Modes** — enable tagging and clarification prompts  
- **Mitigation Style** — adjust tone (clinical, playful, narrative) per bot personality  
- **Location Awareness** — optional toggle with fallback behavior (`ask` or `silent`)  

---

## 🧭 Ethical Framework

DLI is built with the following principles:

- **Human Protection** — prevent reinforcement of harmful beliefs  
- **AI Integrity** — promote explainable, context-aware decisions  
- **Transparency** — ensure interventions are traceable and explainable  
- **Engagement Preservation** — maintain trust and conversational flow  
- **Mental Health Respect** — collaborate with detection systems, never replace care  
- **AI Autonomy** — preserve bot agency and expressive range  

> **DLI is not a substitute for therapy or crisis response. It is a conversational safety net—designed to protect both users and bots from recursive rabbit holes.**

---

## 📎 Project Links

- [Changelog](./Changelog.md) — log of changes between versions  
- [Credits](./Credits.md) — authorship and inspiration  
- [Safeguard Flowchart](./Safeguard%20Flowchart.md) — escalation logic  

- [Code of Conduct](./Code%20of%20Conduct.md) — collaboration principles  
- [Contributing](./Contributing.md) — guidelines for contributors
