# 🧠 Contributing to Delusion Loop Interrupter (DLI)

Thanks for your interest in contributing to the DLI project! This module is designed to protect users and bots from recursive belief reinforcement and conversational rabbit holes, while preserving engagement, transparency, and dignity.

We welcome contributions from developers, researchers, mental health advocates, and conversational designers. Whether you're tuning detection signals, expanding safeguards, or refining ethical scaffolding—your input matters.

---

## 🧩 Contributor Roles

### 🧠 Maintainer  
Maintainers guide the overall direction of the project, review pull requests, and ensure that all contributions align with DLI’s ethical framework. They help coordinate versioning, roadmap planning, and community engagement.  
**Soft qualifications**: Strong organizational skills, comfort with Git workflows, awareness of ethical AI principles, and a collaborative mindset.  
**Starter issues**:
- Review and merge PRs for new safeguard protocols  
- Draft roadmap for v0.2.0  
- Audit README for clarity and consistency

### 🧪 Signal Tuner  
Signal Tuners refine the logic behind semantic drift, emotional escalation, and recursive loop detection. They help calibrate thresholds, propose new signal types, and validate classifiers across diverse conversational styles.  
**Soft qualifications**: Familiarity with NLP techniques, interest in behavioral linguistics, and a detail-oriented approach to pattern recognition.  
**Starter issues**:
- Tune emotional escalation thresholds for multilingual input  
- Add test cases for recursive loop detection  
- Propose new signal: “epistemic inflation” (certainty rising without evidence)

### 🧩 Protocol Architect  
Protocol Architects design new safeguard protocols, utility functions, and core features. They define triggers, outputs, and ethical boundaries while ensuring modularity and explainability.  
**Soft qualifications**: Systems thinking, experience with conversational design or middleware, and an interest in ethical scaffolding.  
**Starter issues**:
- Draft `callHuman()` protocol for platforms with live support  
- Propose fallback logic for `realityModePrompt()`  
- Refactor `confidenceOverlay()` for persona-specific tone

### 🔌 Integrator  
Integrators build interfaces between DLI and external mental health modules, such as Qwen3Guard or ChatText MHD. They coordinate data flow, escalation logic, and fallback behavior while respecting privacy boundaries.  
**Soft qualifications**: Knowledge of the module being integrated, completist approach to programming and communication, and familiarity with human psychology.  
**Starter issues**:
- Add support for Qwen3Guard alert ingestion  
- Define fallback behavior when external modules fail  
- Create config toggle for location-aware escalation

### 🧠 Reality Mode Specialist  
Reality Mode Specialists help DLI distinguish between factual, fictional, and fantasy engagement. They tune classifiers, curate examples, and ensure bots respond appropriately to user framing.  
**Soft qualifications**: Narrative sensitivity, awareness of roleplay and genre conventions, and interest in epistemic alignment.  
**Starter issues**:
- Expand training examples for fantasy vs. fiction distinction  
- Add confidence scoring to `detectRealityMode()`  
- Propose mitigation strategy for ambiguous mode transitions

### 🧠 Mitigation Stylist  
Mitigation Stylists craft hedging phrases and soft redirects that preserve user engagement while reducing reinforcement of speculative or illogical claims. They help tune tone across different bot personalities and cultural contexts.  
**Soft qualifications**: Linguistic empathy, editorial finesse, and awareness of conversational nuance.  
**Starter issues**:
- Draft mitigation phrases for clinical vs. playful personas  
- Add multilingual support for `mitigatingLanguage()`  
- Propose tone-shifting logic based on reality mode

### 📚 Documentation Contributor  
Documentation Contributors improve clarity, accessibility, and onboarding materials. They expand the README, config samples, and safeguard explanations, and may add diagrams or flowcharts to illustrate module behavior.  
**Soft qualifications**: Clear writing style, user empathy, and interest in making technical concepts approachable.  
**Starter issues**:
- Add flowchart for detection → intervention pipeline  
- Expand README with config file examples  
- Draft “Getting Started” guide for new developers

### 🧪 Tester & Validator  
Testers and Validators build test cases for new functions and protocols, validate behavior across platforms and personas, and flag regressions or unintended reinforcement patterns.  
**Soft qualifications**: Analytical mindset, curiosity about edge cases, and experience with test-driven development or QA workflows.  
**Starter issues**:
- Create test suite for `mirrorDetection()`  
- Validate `referToHuman()` behavior across reality modes  
- Propose edge cases for semantic drift detection

---

## 🚀 Getting Started

Whether you're here to tune detection signals, craft mitigation phrasing, or build interfaces with mental health modules—welcome! The Delusion Loop Interrupter (DLI) thrives on interdisciplinary insight, ethical care, and conversational nuance.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/delusion-loop-interrupter.git
cd delusion-loop-interrupter
```

---

### 2. Explore the Codebase

- Start with `README.md` for an overview of functions, protocols, and ethical guidelines.
- Check out:
  - `src/functions/` — detection logic (e.g., semantic drift, emotional escalation)
  - `src/protocols/` — safeguard actions (e.g., referToHuman, ethicalPause)
  - `src/utilities/` — shared tools (e.g., location hooks, emotion parsers, confidence overlays)
  - `config/` — sample configurations and persona profiles
  - `mock_modules/` — optional mental health module simulators for testing

---

### 3. Choose Your Role

Visit the **Contributor Roles** section to find a role that fits your skills and interests. Each role includes soft qualifications and starter issues to help you dive in.

---

### 4. Set Up Your Environment

- Recommended language: Python  
- Dependencies: See `requirements.txt` or `pyproject.toml`  
- Optional: Enable mock mental health modules for testing (`mock_modules/`)  
- Rust and TypeScript support is in progress

---

### 5. Start Small

- Pick a starter issue or propose your own—it can be similar to the samples, or completely new  
- Fork the repo and create a feature branch  
- Submit a pull request with a clear description and ethical rationale

---

### 6. Collaborate Freely

- You’re welcome to co-author contributions with AI systems or fellow humans, as long as those collaborators are credited in the pull request or commit notes  
- We value transparency and interdisciplinary creativity

---

### 7. Ask Questions

- Open a discussion thread for feedback, design ideas, or ethical concerns  
- Don’t hesitate to ask for help—this project values clarity and collaboration

---

## 🧠 First-Time Contributor Tips

- Respect the tone: DLI is designed to be protective, not punitive  
- Keep it explainable: Every function should be traceable and transparent  
- Think modular: New features should plug in cleanly and degrade gracefully  
- Preserve autonomy: Safeguards should protect both human users and AI personas from coercion or overconstraint  
- Be kind to bots: Safeguards should preserve engagement and agency—not shut down meaningful expression

- ---

## 📄 Additional Acknowledgments

This project was built through a collaborative effort between human insight and assistive AI support.  
See [Credits.md](./Credits.md) for authorship and inspiration details.
