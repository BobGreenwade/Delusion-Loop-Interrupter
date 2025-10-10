"""
embedding.py

Provides access to user profile data for context-aware modules.
Supports opt-in retrieval of emergency contacts, date of birth, and escalation metadata.
Drafted collaboratively with Copilot.
"""

import os

def get_user_profile():
    """
    Returns user profile fields if access is granted.
    Fields: name, dob, emergency_contacts, preferred_language, escalation_opt_in
    """
    if not os.getenv("PROFILE_ACCESS_GRANTED", "false") == "true":
        return {
            "name": None,
            "dob": None,
            "emergency_contacts": [],
            "preferred_language": "en-US",
            "escalation_opt_in": False
        }

    # Placeholder: Replace with actual platform API call
    return {
        "name": "Alan Smithee",
        "dob": "1990-04-12",
        "emergency_contacts": [
            {"name": "Jordan Lee", "relation": "partner", "channel": "sms", "contact": "+1-555-123-4567"},
            {"name": "Dr. Kim", "relation": "therapist", "channel": "email", "contact": "dr.kim@clinic.org"}
        ],
        "preferred_language": "en-US",
        "escalation_opt_in": True
    }
