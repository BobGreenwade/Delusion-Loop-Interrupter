<!-- Drafted collaboratively with Copilot -->

# 🧰 DLI Installation Guide

This guide walks you through installing and sandboxing the Delusion Loop Interrupter (DLI) system for testing. It's intended for relative newcomers, but could also be helpful for people who just haven't done it in a while.

---

## 📁 Step 1: Download the Code

You can download DLI from GitHub using either method:

### 🖱️ Web GUI
1. Visit the DLI GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Unzip the folder to a location you can easily access.

### 💻 GitHub Desktop
1. Open GitHub Desktop.
2. Clone the repository using the URL or search for it.
3. Choose a local folder for the clone.

---

## 🧪 Step 2: Sandbox the System

**What is a sandbox?**  
A sandbox is a safe, isolated environment where you can run code without affecting your main system. It protects your files, prevents accidental changes, and helps contain bugs.

### 🧰 Recommended Sandbox Setup
- Create a new folder (e.g. `DLI_Sandbox`)
- Inside it, create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Step 3: Run the Bootstrap Script

This sets up required resources and loads editorial assets.

```bash
python bootstrap.py
```

You should see messages confirming NLTK downloads and phrase loading.

---

## ⚙️ Optional: Modify Configuration

Edit `config.json` to adjust:

- Escalation thresholds  
- Persona tone and style  
- Module toggles (enable/disable components)

---

## 🧠 Safety Notes

- DLI is designed for **sandboxed testing only**  
- It is **not a substitute for therapy or crisis response**  
- Do not deploy in production environments without review  
- All modules are designed to **degrade gracefully** if disabled

---

## 🧪 Next Steps

Once installed, you can begin testing with mock inputs and sample transcripts. See `test/` folder for examples.

> Questions? Feedback? Contributions welcome.
