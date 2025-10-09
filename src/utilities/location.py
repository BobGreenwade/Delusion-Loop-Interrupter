"""
location.py — Utility module for location-aware logic in DLI

Handles optional location awareness, fallback behavior, and mapping to local resources.
Respects user privacy and degrades gracefully when location is unavailable or disabled.
"""

import os

# Sample config structure (replace with actual config loader)
CONFIG = {
    "locationAwareness": {
        "enabled": True,
        "fallbackBehavior": "ask"  # Options: "ask", "silent"
    }
}

def get_user_location():
    """
    Attempts to retrieve user location from environment, platform, or external service.
    Returns a string (e.g., "Corvallis, OR") or None if unavailable.
    """
    # Placeholder: Replace with actual location retrieval logic
    return os.getenv("USER_LOCATION", None)

def should_use_location():
    """
    Determines whether location-aware logic should be used, based on config and availability.
    Returns True, False, or triggers fallback behavior.
    """
    if not CONFIG["locationAwareness"]["enabled"]:
        return False

    location = get_user_location()
    if location:
        return True

    fallback = CONFIG["locationAwareness"]["fallbackBehavior"]
    if fallback == "ask":
        # Trigger prompt to user (handled by calling function)
        return "ask"
    return False

def resolve_local_resources(location):
    """
    Maps a location string to relevant local resources (e.g., support networks, fact-checking sources).
    Returns a dictionary of resource links or None.
    """
    # Placeholder: Replace with actual mapping logic or external API
    local_map = {
        "Corvallis, OR": {
            "mental_health": "https://www.bentoncountyor.gov/health",
            "fact_check": "https://www.oregon.gov/newsroom"
        },
        "Puerto Princesa": {
            "mental_health": "https://www.palawan.gov.ph/health",
            "fact_check": "https://www.gov.ph"
        }
    }
    return local_map.get(location, None)
