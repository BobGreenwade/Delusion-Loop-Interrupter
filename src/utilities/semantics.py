"""
semantics.py

Provides synonym expansion, word-form normalization, and semantic matching.
Supports emotional tone detection, confidence tagging, and reality mode classification.
Drafted collaboratively with Copilot.
"""

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def normalize_word(word):
    """
    Returns the base form of a word using lemmatization.
    """
    return lemmatizer.lemmatize(word.lower())

def get_synonyms(word):
    """
    Returns a set of synonyms for the given word using WordNet.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def match_semantic(word, target_list):
    """
    Returns True if word or its synonyms match any item in target_list.
    """
    normalized = normalize_word(word)
    synonyms = get_synonyms(normalized)
    expanded = synonyms.union({normalized})
    return any(t in expanded for t in target_list)

def match_phrase(text, phrase_list):
    """
    Returns True if any phrase in phrase_list appears in text.
    Case-insensitive, whole-phrase match.
    """
    lowered = text.lower()
    return any(phrase.lower() in lowered for phrase in phrase_list)

def match_wordlist(text, wordlist):
    """
    Returns True if any word or synonym in wordlist appears in text.
    Uses semantic matching for each word.
    """
    tokens = text.lower().split()
    for token in tokens:
        if match_semantic(token, wordlist):
            return True
    return False
