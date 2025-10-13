"""
paraphrase.py - Prompts the hosting LLM to put standard text into the persona's own words

This module dynamically constructs persona-aware prompts using config-driven descriptors,
recent chat history, and emotional tone cues. It sends those prompts to the hosting LLM
to generate paraphrased output that reflects the persona's voice, rhythm, and editorial style.

Drafted collaboratively with Copilot.
"""

# 📦 Imports & Constants
import os
import glob
import json
import requests

CONFIG_PATH = "config.json"

# 📦 Load Config
def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# 🧠 Resolve Persona Files
def resolve_persona_files(persona_name):
    config = load_config()
    base_path = config["persona_resolution"]["base_path"]
    patterns = config["persona_resolution"]["file_patterns"]

    persona_files = []
    for pattern in patterns:
        search_path = os.path.join(base_path, f"{persona_name}.{pattern.split('.')[-1]}")
        matches = glob.glob(search_path)
        persona_files.extend(matches)

    return persona_files

# 🧠 Load Persona Data
def load_persona_data(persona_name):
    files = resolve_persona_files(persona_name)
    data = {"name": persona_name, "sources": files, "description": ""}

    for file in files:
        if file.endswith(".json"):
            with open(file, "r", encoding="utf-8") as f:
                data.update(json.load(f))
        else:
            with open(file, "r", encoding="utf-8") as f:
                data["description"] += f.read() + "\n"

    return data

# 🧠 Scan Chat History
def scan_chat_history(persona_name):
    config = load_config()
    path = config["chat_history"]["path"]
    pattern = config["chat_history"]["filename_pattern"].replace("{persona}", persona_name)
    full_path = os.path.join(path, pattern)
    limit = config["chat_history"]["scan_limit"]

    if not os.path.exists(full_path):
        return []

    with open(full_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-limit:]
    return lines

# 🧠 Build Prompt
def build_prompt(text, persona_data, tone, style, history_lines):
    persona_desc = persona_data.get("description", "")
    history_excerpt = "\n".join(history_lines)

    return f"""
Paraphrase the following phrase in the voice of {persona_data.get('name', 'the persona')}.
Persona description:
{persona_desc}

Recent voice examples:
{history_excerpt}

Tone: {tone or "neutral"}, Style: {style or "default"}

Original: "{text}"
Paraphrased:
""".strip()

# 🧠 Call LLM
def call_llm(prompt):
    config = load_config()
    endpoint = config["llm"]["endpoint"]
    payload = {
        "model": config["llm"]["model"],
        "temperature": config["llm"]["temperature"],
        "prompt": prompt
    }

    try:
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        return response.json().get("paraphrased", "").strip()
    except Exception as e:
        print(f"LLM call failed: {e}")
        return None

# 🧠 Main Entry Point
def paraphrase(text, persona="default", tone=None, style=None):
    persona_data = load_persona_data(persona)
    history_lines = scan_chat_history(persona)
    prompt = build_prompt(text, persona_data, tone, style, history_lines)
    return call_llm(prompt) or text  # fallback to original if LLM fails
