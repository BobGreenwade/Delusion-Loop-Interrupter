"""
config.py — User-facing configuration for behavior, preferences, and integrations.
Used by location.py, generator.py, and other modules.
Drafted collaboratively with Copilot.
"""

CONFIG = {
    "search_engine": "bing",               # Options: 'bing', 'google'
    "location_fallback": "ask",            # Options: 'ask', 'silent', 'block'
    "default_reality_mode": "factual",     # Options: 'factual', 'fictional', 'fantasy'
    "default_tone": "neutral",             # Options: 'neutral', 'validating', 'playful', etc.
    "enable_mock_mode": True,              # Toggle for mock modules
    "log_level": "info",                   # Options: 'debug', 'info', 'warn', 'error'
    "user_locale": "en-US",                # For localization and search relevance
    "enable_editorial_play": True          # Enables lyric generator, satire bots, etc.
}
