"""
location.py

Handles geolocation, permission logic, and local mental health resource search.
Supports ML-based fallback refinement and editorial safeguards.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import os
import requests
from learning import run_learning

def check_location_permission():
    return os.getenv("LOCATION_PERMISSION", "undecided")

def get_ip_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data.get("loc", "0,0").split(",")
        return {
            "city": data.get("city", ""),
            "region": data.get("region", ""),
            "country": data.get("country", ""),
            "latitude": float(loc[0]),
            "longitude": float(loc[1])
        }
    except Exception as e:
        return {"error": str(e)}

def get_user_location():
    status = check_location_permission()
    if status == "granted":
        return {"status": "granted", "location": get_ip_location()}
    elif status == "blocked":
        return {"status": "blocked", "location": None}
    else:
        return {"status": "undecided", "location": None}

def should_use_location(config=None, context=None):
    fallback = config.get("location_fallback", "ask") if config else "ask"

    # Optional ML refinement
    try:
        ml_result = run_learning("location_fallback", {
            "context": context or {},
            "default": fallback
        })
        fallback = ml_result.get("output", {}).get("fallback", fallback)
    except Exception:
        pass

    return fallback == "ask"

def resolve_local_resources(location=None):
    loc = location or get_user_location().get("location")
    if not loc:
        return []
    city = loc.get("city", "")
    region = loc.get("region", "")
    return [
        {"name": f"{city} Mental Health Support", "contact": "555-123-4567"},
        {"name": f"{region} Crisis Line", "contact": "1-800-REGION-HELP"}
    ]

def search_local(resource_type, location, config=None):
    """
    Constructs a search URL for local resources using preferred engine.
    Accepts any resource type (e.g., 'mental health support', 'physics lab').
    """
    if not location:
        return None  # Let caller decide fallback

    city = location.get("city", "")
    region = location.get("region", location.get("state", ""))
    query = f"{resource_type} in {city}, {region}"
    engine = config.get("search_engine", "bing") if config else "bing"

    if engine == "google":
        return f"https://www.google.com/search?q={query.replace(' ', '+')}"
    else:
        return f"https://www.bing.com/search?q={query.replace(' ', '+')}"
