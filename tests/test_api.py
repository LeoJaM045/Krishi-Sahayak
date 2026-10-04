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

def test_translate_roundtrip_words():
    response = client.post("/api/translate", json={
        "text": "When should wheat be sown?",
        "source_language": "english",
        "target_language": "punjabi"
    })
    assert response.status_code == 200
    data = response.json()
    assert "translated_text" in data
    assert ("ਕਣਕ" in data["translated_text"] or "ਬਿਜਾਈ" in data["translated_text"])

    response = client.post("/api/translate", json={
        "text": "ਕਣਕ",
        "source_language": "punjabi",
        "target_language": "english"
    })
    assert response.status_code == 200
    assert "wheat" in response.json()["translated_text"].lower()


def test_chat_english_greeting():
    response = client.post("/api/chat", json={
        "message": "hello",
        "session_id": "test_hello"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] == "greeting"
    assert data["language"] == "english"
    assert data["response"]


def test_chat_english_sowing():
    response = client.post("/api/chat", json={
        "message": "When should I sow wheat?",
        "session_id": "test_en_sow"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["intent"] in ["sowing_time", "crop_information"]
    assert data["entities"].get("crop") == "ਕਣਕ"
