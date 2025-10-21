"""
semantics.py — Editorial semantic matching and rhythm-aware analysis

Provides synonym expansion, word-form normalization, semantic matching,
phrase structure detection, euphemism flagging, and conceptual drift scoring.
Supports emotional tone detection, confidence tagging, and reality mode classification.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import re
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from learning import run_learning

lemmatizer = WordNetLemmatizer()

def normalize_word(word):
    """Returns the base form of a word using lemmatization."""
    return lemmatizer.lemmatize(word.lower())

def get_synonyms(word):
    """Returns a set of synonyms for the given word using WordNet."""
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def match_semantic(word, target_list):
    """Returns True if word or its synonyms match any item in target_list."""
    normalized = normalize_word(word)
    synonyms = get_synonyms(normalized)
    expanded = synonyms.union({normalized})
    return any(t in expanded for t in target_list)

def match_phrase(text, phrase_list):
    """Returns True if any phrase in phrase_list appears in text."""
    lowered = text.lower()
    return any(phrase.lower() in lowered for phrase in phrase_list)

def match_wordlist(text, wordlist):
    """Returns True if any word or synonym in wordlist appears in text."""
    tokens = text.lower().split()
    for token in tokens:
        if match_semantic(token, wordlist):
            return True
    return False

def match_phrase_structure(text):
    """
    Returns a dictionary describing editorial rhythm and clause structure.
    Useful for punchline detection, poetic sabotage, and rhythm-aware modules.
    """
    clauses = re.split(r"[.,;!?]", text)
    rhythm = "short" if all(len(c.strip().split()) <= 6 for c in clauses) else "mixed"
    punctuation = [p for p in text if p in ".!?"]
    return {
        "clause_count": len(clauses),
        "rhythm": rhythm,
        "punctuation": punctuation
    }

def detect_euphemism(text):
    """
    Flags euphemistic or softened language for editorial modules.
    Uses ML override if available.
    """
    softeners = [
        "passed away", "let go", "downsized", "special", "unique",
        "challenging", "differently abled", "nontraditional", "alternative"
    ]
    match = match_phrase(text, softeners)

    try:
        ml_result = run_learning("euphemism_detection", {"text": text})
        match = match or ml_result.get("output", {}).get("euphemism_detected", False)
    except Exception:
        pass

    return match

def semantic_distance(text1, text2):
    """
    Returns a float score representing conceptual drift between two phrases.
    0.0 = identical, 1.0 = completely unrelated.
    """
    try:
        ml_result = run_learning("semantic_distance", {
            "text1": text1,
            "text2": text2
        })
        return round(ml_result.get("output", {}).get("distance", 0.5), 2)
    except Exception:
        return 0.5
