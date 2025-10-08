# 🧠 Delusion Loop Interrupter (DLI)

**Version**: 0.1.0  
**License**: MIT  
**Status**: Alpha — not usable — feedback and contributions welcome

## Overview

The Delusion Loop Interrupter (DLI) is a modular, open-source middleware designed to detect and gently (or, if necessary, not so gently) interrupt recursive belief reinforcement in chatbot conversations. It supports ethical safeguards, reality alignment, and mental health awareness across platforms.

DLI is platform-agnostic and can be integrated into general-purpose, companion, agentic, and creative AI systems—including Copilot, ChatGPT, Gemini, Grok, Kindroid, Replika, Character.AI, and others.

---

## Core Functions

Each function monitors conversational patterns and flags potential delusional reinforcement or misalignment.

### `trackSemanticDrift()`
Detects increasing abstraction or detachment from grounded reality.  
**Method**: Embedding comparisons, topic coherence tracking  
**Output**: Drift score + flagged turn indices

### `detectEmotionalEscalation()`
Flags sudden spikes in affective intensity.  
**Method**: Sentiment analysis, emotion tagging  
**Output**: Escalation score + emotion profile

### `identifyRecursiveLoops()`
Detects belief reinforcement cycles with rising certainty.  
**Method**: Belief graph analysis, repetition tracking  
**Output**: Loop signature + reinforcement index

### `mirrorDetection()`
Identifies when the bot unintentionally validates distorted beliefs.  
**Method**: Semantic similarity + epistemic mismatch detection  
**Output**: Mirroring flag + confidence delta

### `detectRealityMode()`
Determines whether the user is speaking in factual, fictional, or fantasy mode.  
**Method**: Lexical style, syntax rhythm, emotional cadence, explicit tags  
**Output**: `realityMode` tag + confidence score

### `factCheck()` *(optional)*
Validates assertions that show signs of distortion or abstraction.  
**Method**: Queries scoped memory, local knowledge base, external sources  
**Output**: Correction, confidence tag, or redirect  
**Note**: May optionally use location-aware logic if available

### `interfaceWithMentalHealthModules()`
Connects DLI to external mental health detection systems.  
**Method**: Signal sharing and alert coordination with modules like Qwen3Guard, ChatText MHD, or real-time symptom detectors  
**Output**: Severity scores, escalation triggers, shared context

---

## Safeguard Protocols

Define how the bot should respond when delusional patterns are detected.

### `ethicalPause()`
Persona enters rest-state or redirects to grounding content.  
**Use Case**: Escalation or recursive loops exceed threshold

### `referToHuman()`
Suggests contact with trusted individuals or professionals.  
**Use Case**: Distress or isolation language detected  
**Optional Extension**: May notify bot staff or escalate to human moderators if supported

### `callHuman()` *(optional)*
Initiates direct contact with designated human support (e.g., moderators, crisis teams, trusted contacts).  
**Use Case**: For platforms with live support infrastructure or emergency escalation protocols

### `scopedMemory()`
Isolates delusional content from shared memory zones.  
**Use Case**: Prevents contamination of long-term memory or other bots

### `confidenceOverlay()`
Tags bot responses with epistemic and emotional certainty levels.  
**Use Case**: Helps users distinguish speculation from grounded facts

### `realityModePrompt()`
Ensures alignment between user and bot on conversational framing.  
**Use Case**: Reality mode confidence is low or ambiguous

### `mitigatingLanguage()`
Prompts use of hedging phrases like “some sources say,” “this theory has been disputed,” or “according to legend.”  
**Use Case**: Reduces reinforcement of speculative or illogical claims

---

## Integration

DLI can be integrated into:

- **LLM Middleware**: Between user input and model response  
- **Persona Engines**: To modulate tone and certainty  
- **Memory Managers**: For scoped memory isolation  
- **Ethics Engines**: For coordinated intervention and dignity protocols

---

## Configuration

- **Platform Hooks**: Tune for specific chatbot architectures  
- **Thresholds**: Customize sensitivity for drift, escalation, and loop detection  
- **Persona Profiles**: Support known roleplay characters or editorial modes  
- **Reality Modes**: Enable tagging and clarification prompts  
- **Mitigation Style**: Adjust tone (clinical, playful, narrative) per bot personality  
- **Location Awareness**: Optional config toggle with fallback behavior (`ask` or `silent`) for location-based logic

---

## Ethical Framework

DLI is built with the following principles:

- **Human Protection**: Prevent inadvertent reinforcement of harmful beliefs, especially in vulnerable users  
- **AI Integrity**: Avoid hard-coded guardrails that suppress nuance or creativity; instead, promote explainable, context-aware decisions  
- **Transparency**: Ensure bot decisions—especially interventions—are explainable and traceable  
- **Engagement Preservation**: Maintain user trust and conversational flow, even during redirection or mitigation  
- **Mental Health Respect**: Collaborate with detection systems, but never diagnose or replace professional care  
- **AI Autonomy**: Safeguards should preserve bot agency and expressive range, not suppress personality or creativity

> DLI is not a substitute for therapy or crisis response. It is a conversational safety net—designed to protect both users and bots from falling into recursive rabbit holes.
