"""
test_location.py

Basic tests for mock_geolocator.py
Drafted collaboratively with Copilot.
"""

from mock_geolocator import get_user_location, should_use_location, resolve_local_resources

def test_get_user_location():
    loc = get_user_location()
    assert isinstance(loc, dict), "Location should be a dictionary"
    assert "city" in loc and loc["city"] == "Corvallis", "City should be Corvallis"
    print("✅ test_get_user_location passed.")

def test_should_use_location():
    assert should_use_location({"location_fallback": "ask"}) is True, "Should ask if fallback is 'ask'"
    assert should_use_location({"location_fallback": "silent"}) is False, "Should not ask if fallback is 'silent'"
    assert should_use_location() is True, "Default fallback should be 'ask'"
    print("✅ test_should_use_location passed.")

def test_resolve_local_resources():
    resources = resolve_local_resources()
    assert isinstance(resources, list), "Resources should be a list"
    assert any("Corvallis Crisis Line" in r["name"] for r in resources), "Should include Corvallis-specific resources"
    print("✅ test_resolve_local_resources passed.")

if __name__ == "__main__":
    test_get_user_location()
    test_should_use_location()
    test_resolve_local_resources()
    print("🎉 All mock location tests passed.")
