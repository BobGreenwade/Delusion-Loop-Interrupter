"""
profile.py — Modular user profile management for DLI

Supports creation, updates, editorial assertions, and ML-based trait refinement.
Drafted collaboratively with Bob Greenwade and Copilot.
"""

import os
import json
from embedding import fetch_external_profile
from learning import run_learning

CONFIG_PATH = "config.json"
PROFILE_DIR = "profiles"

def load_config():
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

CONFIG = load_config()

def get_profile_path(username):
    return os.path.join(PROFILE_DIR, f"{username}_profile.json")

def get_user_profile(username="User"):
    path = get_profile_path(username)
    if not os.path.exists(path):
        print(f"[PROFILE] No profile found for {username}, creating...")
        create_user_profile(username)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_user_profile(username, seed_text="Hello, I’m new here."):
    os.makedirs(PROFILE_DIR, exist_ok=True)
    path = get_profile_path(username)

    if os.path.exists(path):
        print(f"[PROFILE] Profile already exists for {username}")
        return

    external = fetch_external_profile(CONFIG.get("EXTERNAL_PROFILE_API", ""), seed_text)
    profile = {
        "name": username,
        "preferred_language": "en-US",
        "escalation_opt_in": False,
        "emergency_contacts": [],
        "persona": {
            "tone": "empathetic",
            "style": "clarifying",
            "allow_speculation": False
        },
        "profile_characteristics": {
            "concern_level": 0,
            "emotionality": 50,
            "responsiveness": 75
        },
        "external_profile": external,
        "strategies": ["default"],
        "assertions": [],
        "facts": {}
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)
    print(f"[PROFILE] Created profile for {username}")

def update_profile_seed(username, new_seed_text):
    path = get_profile_path(username)
    if not os.path.exists(path):
        print(f"[PROFILE] No profile found for {username}")
        return

    external = fetch_external_profile(CONFIG.get("EXTERNAL_PROFILE_API", ""), new_seed_text)
    with open(path, "r+", encoding="utf-8") as f:
        profile = json.load(f)
        profile["external_profile"] = external
        f.seek(0)
        json.dump(profile, f, indent=2)
        f.truncate()
    print(f"[PROFILE] Updated external seed for {username}")

def update_user_profile(username, updates):
    path = get_profile_path(username)
    if not os.path.exists(path):
        print(f"[PROFILE] No profile found for {username}")
        return

    with open(path, "r+", encoding="utf-8") as f:
        profile = json.load(f)
        profile.update(updates)
        f.seek(0)
        json.dump(profile, f, indent=2)
        f.truncate()
    print(f"[PROFILE] Updated profile for {username}")

def profile_assertion(username, assertion):
    path = get_profile_path(username)
    if not os.path.exists(path):
        print(f"[PROFILE] No profile found for {username}")
        return

    with open(path, "r+", encoding="utf-8") as f:
        profile = json.load(f)
        profile.setdefault("assertions", []).append(assertion)
        f.seek(0)
        json.dump(profile, f, indent=2)
        f.truncate()
    print(f"[PROFILE] Assertion added for {username}")

def profile_user_fact(username, key, value):
    path = get_profile_path(username)
    if not os.path.exists(path):
        print(f"[PROFILE] No profile found for {username}")
        return

    with open(path, "r+", encoding="utf-8") as f:
        profile = json.load(f)
        profile.setdefault("facts", {})[key] = value
        f.seek(0)
        json.dump(profile, f, indent=2)
        f.truncate()
    print(f"[PROFILE] Fact stored for {username}: {key} = {value}")

def update_characteristic(username, key, value):
    path = get_profile_path(username)
    if not os.path.exists(path):
        create_user_profile(username)

    with open(path, "r+", encoding="utf-8") as f:
        profile = json.load(f)
        profile.setdefault("profile_characteristics", {})[key] = value
        f.seek(0)
        json.dump(profile, f, indent=2)
        f.truncate()
    print(f"[PROFILE] Updated {key} to {value} for {username}")

def get_characteristic(username, key):
    path = get_profile_path(username)
    if not os.path.exists(path):
        create_user_profile(username)

    with open(path, "r", encoding="utf-8") as f:
        profile = json.load(f)
        value = profile.get("profile_characteristics", {}).get(key, None)

    # Optional ML override
    try:
        ml_result = run_learning("trait_inference", {
            "username": username,
            "trait": key,
            "current_value": value
        })
        value = ml_result.get("output", {}).get("value", value)
    except Exception:
        pass

    return value
