"""
bootstrap.py — Initializes DLI environment and dependencies

Downloads required resources, validates config, and preloads semantic scaffolds.
Drafted collaboratively with Copilot.
"""

import nltk
import os
from phraseEditor import load_phrases

def initialize_nltk():
    """
    Downloads required NLTK corpora.
    """
    nltk.download("wordnet")
    nltk.download("omw-1.4")
    print("[BOOTSTRAP] NLTK corpora downloaded.")

def validate_environment():
    """
    Checks for required environment variables or config toggles.
    """
    required_vars = ["PROFILE_ACCESS_GRANTED", "DLI_MODE"]
    for var in required_vars:
        if var not in os.environ:
            print(f"[BOOTSTRAP] Warning: Missing env var {var}")
        else:
            print(f"[BOOTSTRAP] {var} = {os.environ[var]}")

def preload_editorial_assets():
    """
    Loads mitigation phrases and confirms emotional cue readiness.
    """
    phrases = load_phrases()
    print(f"[BOOTSTRAP] Loaded {len(phrases)} mitigation phrases.")

def run_bootstrap():
    print("[BOOTSTRAP] Starting DLI initialization...")
    initialize_nltk()
    validate_environment()
    preload_editorial_assets()
    print("[BOOTSTRAP] Initialization complete.")

if __name__ == "__main__":
    run_bootstrap()
