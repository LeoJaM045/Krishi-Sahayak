import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Punjabi Krishi Sahayak backend is running"}

def test_chat():
    response = client.post("/api/chat", json={
        "message": "ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?",
        "session_id": "test_123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["intent"] in ["sowing_time", "crop_information"]
    assert data["language"] == "punjabi"
    assert "ਕਣਕ" == data["entities"].get("crop")

def test_weather():
    response = client.get("/api/weather")
    assert response.status_code == 200
    assert "temperature" in response.json()

def test_mandi():
    response = client.get("/api/mandi")
    assert response.status_code == 200
    assert "prices" in response.json()

def test_crops():
    response = client.get("/api/crops")
    assert response.status_code == 200
    assert "crops" in response.json()
    assert "ਕਣਕ" in response.json()["crops"]

def test_translate():
    response = client.post("/api/translate", json={
        "text": "When should wheat be sown?",
        "source_language": "english",
        "target_language": "punjabi"
    })
    assert response.status_code == 200
    assert "translated_text" in response.json()
