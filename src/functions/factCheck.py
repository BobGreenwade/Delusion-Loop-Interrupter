"""
factCheck.py

Validates claims using a configurable knowledge base and trusted sources.
Supports general fact-checking, etymology verification, and health myth debunking.
Drafted collaboratively with Copilot.
"""

from config import CONFIG

TRUSTED_SOURCES = CONFIG.get("trusted_sources", [
    "Snopes",
    "FactCheck.org",
    "Wikipedia",
    "Wiktionary",
    "WebMD",
    "NASA",
    "CDC",
    "WHO",
    "PolitiFact",
    "PubMed"
])

def get_source_url(source_name):
    """
    Returns the homepage URL for a known source.
    """
    urls = {
        "Snopes": "https://www.snopes.com/",
        "FactCheck.org": "https://www.factcheck.org/",
        "Wikipedia": "https://en.wikipedia.org/",
        "Wiktionary": "https://www.wiktionary.org/",
        "WebMD": "https://www.webmd.com/",
        "NASA": "https://www.nasa.gov/",
        "CDC": "https://www.cdc.gov/",
        "WHO": "https://www.who.int/",
        "PolitiFact": "https://www.politifact.com/",
        "PubMed": "https://pubmed.ncbi.nlm.nih.gov/"
    }
    return urls.get(source_name)

def validate_claim(claim, domain="general"):
    """
    Constructs search queries for validating a claim across trusted sources.
    Returns a list of search URLs.
    """
    queries = []
    for source in TRUSTED_SOURCES:
        base_url = get_source_url(source)
        if base_url:
            search_url = f"{base_url}search?q={claim.replace(' ', '+')}"
            queries.append({"source": source, "url": search_url})
    return queries

def suggest_sources(domain="general"):
    """
    Returns a filtered list of sources based on domain.
    """
    domain_map = {
        "politics": ["PolitiFact", "FactCheck.org", "Snopes"],
        "health": ["WebMD", "CDC", "WHO", "PubMed"],
        "science": ["NASA", "Wikipedia"],
        "language": ["Wiktionary", "Wikipedia"],
        "history": ["Wiktionary", "FactCheck.org", "Snopes"],
        "general": TRUSTED_SOURCES
    }
    return domain_map.get(domain, TRUSTED_SOURCES)
