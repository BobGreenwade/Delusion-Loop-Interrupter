<!-- Drafted collaboratively with Copilot -->

# 📦 DLI Changelog

This file tracks version history and major changes to the Delusion Loop Interrupter (DLI) system.

---
## 🧠 Version 0.1.3 — "Potentially Deployable" (October 2025)

**Status**: Structurally sound, editorially aware, and ready for cautious use

### 🔧 Function Audit & Upgrades
- Refactored `detectEmotionalEscalation.py` to support escalation period tracking and editorial tone output
- Expanded `detectRealityMode.py` with new modes (`fiction`, `roleplay`, `indulgent`) and mitigation tagging
- Upgraded `identifyRecursiveLoops.py` with severity scoring and optional fact-check integration
- Refined `interfaceWithMentalHealthModules.py` with persona-aware payloads and escalation hooks
- Enhanced `mirrorDetection.py` with epistemic mismatch detection and mitigation tagging
- Upgraded `trackSemanticDrift.py` with topic shift tracking and editorial tone scaffolding

### 🧰 Utility Enhancements
- Refactored `embedding.py` with override logic, external profile enrichment, and tone scaffolding
- Upgraded `logger.py` with tone-aware logging, transcript tracking, and editorial tagging
- Scaffolded `indulgentMode.py` for rare but pivotal containment logic

### 🧠 ML Integration Plan
- Tagged ML-readiness across most Functions, Protocols, and Utilities
- Flagged `factCheck.py` for modular split and ML module selection
- Mapped merge strategy for multi-tester training data

### 📘 Documentation Updates
- Updated `Functions Overview.md`, `Protocols Overview.md`, and `Utilities Overview.md`
- Refined `Safeguard Flowchart.md` with ML-readiness tags and editorial tone flow
- Declared 0.1.3 as “potentially deployable” in all overview files

> 🧠 **Note:** “Potentially deployable” means structurally sound, editorially aware, and ready for cautious use. Editorial tone modulation and graceful failure are now supported across all core modules.

---

## 👀 Version 0.1.2 — "Deplorably Deployable" (Oct 2025)

- Integrated `paraphrase()` into all mitigation and escalation modules  
- Added `map_emotion_to_tone()` for tone-aware editorial logic  
- Refactored `select_mitigation()` to support persona voice and emotional nuance  
- Added `referral_text()` for editorialized resource suggestions  
- Updated `callHuman.py` with `handoff_status`, transcript logic, and external escalation phrasing  
- Refactored `realityModePrompt.py` to support confidence-aware mitigation  
- Seeded `toneMap.json` for Plutchik-to-tone mapping  
- Editorial continuity now preserved across all modules  

> 🔔 **Note:** `callHuman.py` is a supplemental safeguard for cases requiring outside intervention. It activates only when conversational safety fails and synthetic containment is no longer viable.

---

## 🧪 Version 0.1.1 — Alpha Release (October 2025)

**Status**: Barely deployable — ready for internal testing and feedback

### ✨ New Modules
- `semantics.py` — centralized synonym and word-form matching
- `emotion.py` — emotional tone detection and escalation support
- `detectRealityMode.py` — reality mode classification (fantasy, speculative, grounded)
- `phraseEditor.py` — standalone editorial tool for mitigation phrase management
- `bootstrap.py` — startup script for dependency setup and asset loading

### 🧠 Enhancements
- Semantic matching integrated into `confidence.py`, `emotion.py`, and `detectRealityMode.py`
- Emotional tone now informs `embedding.py` for editorial modulation
- Scoped memory now tracks mitigation events and escalation triggers
- `config.json` seeded with toggles, thresholds, and persona settings

### 📘 Documentation Updates
- `README.md` updated to reflect version and deployability
- `Utilities Overview.md` expanded with new modules and tools
- `Safeguard Flowchart.md` and `Functions Overview.md` pending next pass

### 🧪 Testing Readiness
- All modules degrade gracefully if disabled
- Startup script validates environment and loads editorial assets
- Ready for alpha testing in sandboxed environments

---

## 🧬 Version 0.1.0 — Initial Scaffold (September 2025)

**Status**: Conceptual — not yet deployable

- Core detection and safeguard protocols scaffolded
- Modular architecture seeded for loop interruption
- Editorial tone and mitigation logic prototyped
