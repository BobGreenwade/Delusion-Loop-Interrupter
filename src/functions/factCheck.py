"""
factCheck.py

Validates claims using a configurable knowledge base and trusted sources.
Defers to standalone Fact-Check module if installed.
Supports general fact-checking, etymology verification, and health myth debunking.
Drafted collaboratively with Copilot and Bob Greenwade.
"""

from config import CONFIG

# Expanded fallback source list
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
    "PubMed",
    "AP",
    "Reuters",
    "Library of Congress",
    "National Archives"
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
        "PubMed": "https://pubmed.ncbi.nlm.nih.gov/",
        "AP": "https://apnews.com/",
        "Reuters": "https://www.reuters.com/",
        "Library of Congress": "https://www.loc.gov/",
        "National Archives": "https://www.archives.gov/"
    }
    return urls.get(source_name)

def is_factcheck_module_available():
    """
    Checks if the standalone Fact-Check module is installed.
    """
    try:
        import checkFact
        return True
    except ImportError:
        return False

def validate_claim(claim, domain="general"):
    """
    Validates a claim using either the Fact-Check module or fallback logic.
    Returns a list of search URLs or module results.
    """
    if is_factcheck_module_available():
        from checkFact import verify_assertion
        return verify_assertion(claim, source_type="registry")

    # Fallback logic
    queries = []
    for source in suggest_sources(domain):
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
        "politics": ["PolitiFact", "FactCheck.org", "Snopes", "Reuters", "AP"],
        "health": ["WebMD", "CDC", "WHO", "PubMed"],
        "science": ["NASA", "Wikipedia"],
        "language": ["Wiktionary", "Wikipedia"],
        "history": ["Library of Congress", "National Archives", "Wikipedia", "Snopes"],
        "general": TRUSTED_SOURCES
    }
    return domain_map.get(domain, TRUSTED_SOURCES)
