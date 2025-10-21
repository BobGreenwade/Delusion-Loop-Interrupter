"""
learning.py — Central ML integration utility for DLI

Detects available ML packages, routes tasks to best option, and executes learning-enhanced functions.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

import importlib

ML_PACKAGES = {
    "spacy": "spaCy NLP",
    "transformers": "Hugging Face Transformers",
    "sklearn": "Scikit-learn",
    "textblob": "TextBlob",
    "nltk": "NLTK",
    "openai": "OpenAI API",
    "cohere": "Cohere API"
}

def detect_installed_ml():
    """
    Returns a dictionary of installed ML packages.
    """
    available = {}
    for pkg in ML_PACKAGES:
        try:
            importlib.import_module(pkg)
            available[pkg] = ML_PACKAGES[pkg]
        except ImportError:
            continue
    return available

def select_ml_for(task):
    """
    Selects the best ML package for a given task.
    """
    available = detect_installed_ml()
    task_map = {
        "classification": ["transformers", "spacy", "sklearn"],
        "parsing": ["spacy", "nltk"],
        "tone": ["textblob", "transformers"],
        "emotion": ["textblob", "transformers"],
        "semantic": ["embedding", "transformers"],
        "certainty": ["sklearn", "transformers"],
        "loop_detection": ["sklearn", "spacy"]
    }
    for preferred in task_map.get(task, []):
        if preferred in available:
            return preferred
    return None

def run_learning(task, input_data):
    """
    Executes ML-enhanced logic for a given task and input.
    Placeholder logic; refine with package-specific calls.
    """
    package = select_ml_for(task)
    if not package:
        return {"error": "No suitable ML package installed."}

    # Placeholder: simulate output
    return {
        "task": task,
        "package": package,
        "input": input_data,
        "output": f"Simulated result for '{task}' using {package}"
    }

def log_learning_outcome(task, input_data, output_data):
    """
    Logs learning result for audit or refinement.
    Placeholder logic; refine with logger integration.
    """
    print(f"[Learning] Task: {task} | Input: {input_data} | Output: {output_data}")
