import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from nlp.preprocessing import normalize_punjabi_text, detect_language
from nlp.intent_classifier import IntentClassifier
from nlp.entity_extractor import EntityExtractor
from services.translation_service import translate_to_english, translate_to_punjabi

def test_language_detection():
    assert detect_language("ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?") == "punjabi"
    assert detect_language("When should I sow wheat?") == "english"
    assert detect_language("ਮੇਰੀ wheat ਦੀ crop ਖਰਾਬ ਹੈ") == "mixed"
    
def test_preprocessing():
    assert normalize_punjabi_text("  ਕਣਕ  ਦੀ  ਬਿਜਾਈ!!  ") == "ਕਣਕ ਦੀ ਬਿਜਾਈ"

def test_intent_classification():
    classifier = IntentClassifier()
    # Assuming model is trained
    if classifier.model:
        res = classifier.predict("ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?")
        assert res["intent"] == "sowing_time"
        
        res = classifier.predict("ਝੋਨੇ ਨੂੰ ਕਿੰਨਾ ਪਾਣੀ ਚਾਹੀਦਾ ਹੈ?")
        assert res["intent"] == "irrigation"

def test_entity_extraction():
    extractor = EntityExtractor()
    res = extractor.extract("ਮੇਰੇ ਕਣਕ ਦੇ ਪੱਤੇ ਪੀਲੇ ਹੋ ਰਹੇ ਹਨ")
    assert res.get("crop") == "ਕਣਕ"
    assert res.get("symptom") == "ਪੱਤੇ ਪੀਲੇ"

def test_translation():
    # Dictionary-based translation should not depend on an external API.
    res = translate_to_english("ਕਣਕ")
    assert res.lower() == "wheat" or "wheat" in res.lower()
