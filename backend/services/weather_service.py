import os
import random

def get_weather(location="Punjab"):
    # If API key exists, we would use requests to fetch actual weather
    # For now, we return demo data clearly labelled
    weather_conditions = ["ਧੁੱਪ (Sunny)", "ਬੱਦਲਵਾਈ (Cloudy)", "ਹਲਕਾ ਮੀਂਹ (Light Rain)", "ਸਾਫ਼ (Clear)"]
    
    return {
        "status": "success",
        "is_demo_data": True,
        "location": location,
        "temperature": f"{random.randint(20, 35)}°C",
        "condition": random.choice(weather_conditions),
        "humidity": f"{random.randint(40, 80)}%"
    }
