# tools.py
import requests

def get_temperature_f(city):
    """Fetches live weather from Open-Meteo for coordinates approximating a city."""
    # Hardcoded mock mapping for simplicity
    coords = {"boston": (42.36, -71.05), "seattle": (47.60, -122.33)}
    lat, lon = coords.get(city.lower(), (40.71, -74.00)) # Default NYC
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        res = requests.get(url, timeout=10).json()
        temp_c = res["current_weather"]["temperature"]
        return (temp_c * 9/5) + 32 # Convert Celsius to Fahrenheit
    except Exception:
        return "Error reaching API"

tool_definitions = [{
    "type": "function",
    "function": {
        "name": "get_temperature_f",
        "description": "Fetch the temperature for a given city in Fahrenheit",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The city to fetch weather for (e.g. boston, seattle)"}
            },
            "required": ["city"]
        }
    }
}]