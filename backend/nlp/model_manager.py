from .intent_classifier import IntentClassifier
from .entity_extractor import EntityExtractor
from .language_detector import detect_language

intent_classifier = IntentClassifier()
entity_extractor = EntityExtractor()

def analyze_text(text: str):
    language = detect_language(text)
    intent_data = intent_classifier.predict(text)
    entities = entity_extractor.extract(text)
    
    return {
        "language": language,
        "intent": intent_data["intent"],
        "confidence": intent_data["confidence"],
        "entities": entities
    }
