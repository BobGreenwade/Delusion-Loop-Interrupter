"""
learning.py — Central ML integration utility for DLI

Detects available ML packages, routes tasks to best option, and executes learning-enhanced functions.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import importlib
import json

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
    """Returns a dictionary of installed ML packages."""
    available = {}
    for pkg in ML_PACKAGES:
        try:
            importlib.import_module(pkg)
            available[pkg] = ML_PACKAGES[pkg]
        except ImportError:
            continue
    return available

def select_ml_for(task):
    """Selects the best ML package for a given task."""
    available = detect_installed_ml()
    task_map = {
        "classification": ["transformers", "spacy", "sklearn"],
        "parsing": ["spacy", "nltk"],
        "tone": ["textblob", "transformers"],
        "emotion": ["textblob", "transformers"],
        "semantic": ["transformers"],
        "certainty": ["sklearn", "transformers"],
        "loop_detection": ["sklearn", "spacy"]
    }
    for preferred in task_map.get(task, []):
        if preferred in available:
            return preferred
    return None

def run_learning(task, input_data):
    """Executes ML-enhanced logic for a given task and input."""
    package = select_ml_for(task)
    if not package:
        return {"error": "No suitable ML package installed."}

    result = {}

    try:
        if package == "textblob":
            from textblob import TextBlob
            blob = TextBlob(input_data.get("text", ""))
            if task == "tone":
                result["tone"] = "positive" if blob.sentiment.polarity > 0 else "negative"
            elif task == "emotion":
                result["polarity"] = blob.sentiment.polarity
                result["subjectivity"] = blob.sentiment.subjectivity

        elif package == "spacy":
            import spacy
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(input_data.get("text", ""))
            if task == "parsing":
                result["tokens"] = [token.text for token in doc]
            elif task == "loop_detection":
                result["loop_detected"] = any(sent.text.count("again") > 1 for sent in doc.sents)

        elif package == "sklearn":
            # Placeholder for sklearn logic
            result["score"] = 0.75  # Simulated score

        elif package == "transformers":
            # Placeholder for transformers logic
            result["embedding"] = [0.1, 0.2, 0.3]  # Simulated vector

        else:
            result["output"] = f"Simulated result for '{task}' using {package}"

    except Exception as e:
        result["error"] = str(e)

    return {
        "task": task,
        "package": package,
        "input": input_data,
        "output": result
    }

def log_learning_outcome(task, input_data, output_data):
    """Logs learning result for audit or refinement."""
    log_entry = {
        "task": task,
        "input": input_data,
        "output": output_data
    }
    print(f"[Learning] {json.dumps(log_entry, indent=2)}")
