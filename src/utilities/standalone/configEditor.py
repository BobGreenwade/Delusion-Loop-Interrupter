"""
configEditor.py

Utility for viewing and editing config.py settings.
Supports validation, toggling, and session overrides.
Drafted collaboratively with Copilot.
"""

import json
from pathlib import Path

CONFIG_PATH = Path(__file__).parent.parent.parent / "config.py"

def load_config():
    """
    Loads the CONFIG dictionary from config.py.
    Assumes config.py defines CONFIG = {...}
    """
    config_globals = {}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        exec(f.read(), config_globals)
    return config_globals.get("CONFIG", {})

def save_config(new_config):
    """
    Overwrites config.py with updated CONFIG dictionary.
    """
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write('CONFIG = ' + json.dumps(new_config, indent=2))

def list_config():
    """
    Prints current config settings.
    """
    config = load_config()
    for key, value in config.items():
        print(f"{key}: {value}")

def update_config(key, value):
    """
    Updates a specific config key.
    """
    config = load_config()
    if key not in config:
        print(f"[ERROR] Key '{key}' not found in config.")
        return
    config[key] = value
    save_config(config)
    print(f"[UPDATED] {key} → {value}")

def validate_config(config):
    """
    Validates config values against known constraints.
    """
    valid_engines = ["bing", "google"]
    valid_modes = ["factual", "fictional", "fantasy"]
    valid_log_levels = ["debug", "info", "warn", "error"]

    errors = []
    if config.get("search_engine") not in valid_engines:
        errors.append("Invalid search_engine")
    if config.get("default_reality_mode") not in valid_modes:
        errors.append("Invalid default_reality_mode")
    if config.get("log_level") not in valid_log_levels:
        errors.append("Invalid log_level")

    if errors:
        print("[VALIDATION FAILED]")
        for e in errors:
            print(f" - {e}")
    else:
        print("[CONFIG VALID]")

def list_trusted_sources():
    config = load_config()
    sources = config.get("trusted_sources", [])
    print("[TRUSTED SOURCES]")
    for s in sources:
        print(f" - {s}")

def add_trusted_source(source_name):
    config = load_config()
    sources = config.get("trusted_sources", [])
    if source_name not in sources:
        sources.append(source_name)
        config["trusted_sources"] = sources
        save_config(config)
        print(f"[ADDED] {source_name}")
    else:
        print(f"[SKIPPED] {source_name} already present.")

def remove_trusted_source(source_name):
    config = load_config()
    sources = config.get("trusted_sources", [])
    if source_name in sources:
        sources.remove(source_name)
        config["trusted_sources"] = sources
        save_config(config)
        print(f"[REMOVED] {source_name}")
    else:
        print(f"[NOT FOUND] {source_name} not in list.")
