"""
location.py

Handles location awareness with permission logic and fallback behavior.
Drafted collaboratively with Copilot.
"""

import os

def check_location_permission():
    """
    Simulates checking whether location permission is granted, blocked, or undecided.
    Returns one of: 'granted', 'blocked', 'undecided'
    """
    # Placeholder logic — replace with actual platform check
    return os.getenv("LOCATION_PERMISSION", "undecided")

def get_user_location():
    """
    Returns location if permission is granted, or status if blocked/undecided.
    """
    status = check_location_permission()

    if status == "granted":
        # Replace with actual geolocation logic
        return {
            "status": "granted",
            "location": {
                "city": "Corvallis",
                "state": "Oregon",
                "country": "United States",
                "latitude": 44.5646,
                "longitude": -123.2620
            }
        }
    elif status == "blocked":
        return {
            "status": "blocked",
            "location": None
        }
    else:  # 'undecided'
        return {
            "status": "undecided",
            "location": None
        }

def should_use_location(config=None):
    """
    Determines fallback behavior when permission is undecided.
    Returns True if system should ask, False if silent fallback.
    """
    fallback = config.get("location_fallback", "ask") if config else "ask"
    return fallback == "ask"

def resolve_local_resources(location=None):
    """
    Maps location to support networks or fact-checking sources.
    """
    loc = location or get_user_location().get("location")
    if not loc:
        return []

    if loc["city"] == "Corvallis":
        return [
            {"name": "Corvallis Crisis Line", "contact": "541-757-5124"},
            {"name": "Local Fact Check Hub", "url": "https://corvallisfacts.org"}
        ]
    else:
        return [
            {"name": "Generic Support Network", "contact": "1-800-555-HELP"}
        ]
