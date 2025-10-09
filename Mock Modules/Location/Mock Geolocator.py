"""
mock_geolocator.py

Simulated geolocation module for testing location-aware logic in DLI.
Drafted collaboratively with Copilot.
"""

def get_user_location():
    """
    Returns a mock location for testing purposes.
    """
    return {
        "city": "Corvallis",
        "state": "Oregon",
        "country": "United States",
        "latitude": 44.5646,
        "longitude": -123.2620
    }

def should_use_location(config=None):
    """
    Simulates config-based decision for location usage.
    """
    fallback = config.get("location_fallback", "ask") if config else "ask"
    return fallback in ["ask", "silent"]

def resolve_local_resources(location=None):
    """
    Returns mock support resources based on location.
    """
    loc = location or get_user_location()
    if loc["city"] == "Corvallis":
        return [
            {"name": "Corvallis Crisis Line", "contact": "541-757-5124"},
            {"name": "Local Fact Check Hub", "url": "https://corvallisfacts.org"}
        ]
    else:
        return [
            {"name": "Generic Support Network", "contact": "1-800-555-HELP"}
        ]
