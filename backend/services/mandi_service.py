import os
import random

def get_mandi_prices():
    # If API key exists, we would fetch actual mandi data
    # For now, we return demo data clearly labelled
    return {
        "status": "success",
        "is_demo_data": True,
        "prices": [
            {"crop": "ਕਣਕ (Wheat)", "price": "₹2275 / Quintal"},
            {"crop": "ਝੋਨਾ (Paddy)", "price": "₹2183 / Quintal"},
            {"crop": "ਕਪਾਹ (Cotton)", "price": "₹6620 / Quintal"},
            {"crop": "ਸਰ੍ਹੋਂ (Mustard)", "price": "₹5450 / Quintal"}
        ],
        "date": "Today"
    }
