import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .preprocessing import normalize_punjabi_text

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'intent_model.joblib')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'vectorizer.joblib')
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'punjabi_intents.csv')

# High-signal phrases used when the TF-IDF model is uncertain or falls back
# to the majority class (general_agriculture).
KEYWORD_INTENTS = [
    ("sowing_time", ["ਬਿਜਾਈ", "ਬੀਜਣ", "sow", "sowing", "nursery", "ਪਨੀਰੀ"]),
    ("harvesting_time", ["ਵਾਢੀ", "ਕਟਾਈ", "harvest", "harvesting"]),
    ("irrigation", ["ਸਿੰਚਾਈ", "ਪਾਣੀ", "irrigation", "watering"]),
    ("fertilizer", ["ਖਾਦ", "ਯੂਰੀਆ", "urea", "dap", "fertilizer"]),
    ("pest_control", ["ਕੀੜਾ", "ਕੀੜੇ", "pest", "insect", "pesticide"]),
    ("crop_disease", ["ਬਿਮਾਰੀ", "ਰੋਗ", "disease", "ਪੀਲੇ", "blight", "rust"]),
    ("weather", ["ਮੌਸਮ", "weather", "ਮੀਂਹ", "temperature"]),
    ("mandi_price", ["ਮੰਡੀ", "ਭਾਅ", "mandi", "msp", "price"]),
]


class IntentClassifier:
    def __init__(self):
        self.vectorizer = None
        self.model = None
        self.load_model()

    def train(self):
        print("Training Intent Classifier...")
        if not os.path.exists(DATA_PATH):
            raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

        df = pd.read_csv(DATA_PATH)
        # Normalize text
        df['text'] = df['text'].apply(normalize_punjabi_text)
        
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2))
        X = self.vectorizer.fit_transform(df['text'])
        y = df['intent']
        
        self.model = LogisticRegression(random_state=42, max_iter=1000)
        self.model.fit(X, y)
        
        joblib.dump(self.model, MODEL_PATH)
        joblib.dump(self.vectorizer, VECTORIZER_PATH)
        print("Model and Vectorizer saved successfully.")

    def load_model(self):
        if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
            self.model = joblib.load(MODEL_PATH)
            self.vectorizer = joblib.load(VECTORIZER_PATH)
        else:
            print("Model not found. Please train the model first.")

    def _keyword_intent(self, normalized_text: str):
        best_intent = None
        best_hits = 0
        for intent, keywords in KEYWORD_INTENTS:
            hits = sum(1 for kw in keywords if kw in normalized_text)
            if hits > best_hits:
                best_hits = hits
                best_intent = intent
        return best_intent if best_hits else None

    def predict(self, text: str):
        if not self.model or not self.vectorizer:
            self.train()
            
        normalized_text = normalize_punjabi_text(text)
        X = self.vectorizer.transform([normalized_text])
        
        probabilities = self.model.predict_proba(X)[0]
        max_prob_index = probabilities.argmax()
        
        intent = self.model.classes_[max_prob_index]
        confidence = float(probabilities[max_prob_index])

        hinted = self._keyword_intent(normalized_text)
        if hinted and (intent == "general_agriculture" or confidence < 0.3):
            intent = hinted
            confidence = max(confidence, 0.55)
        
        return {
            "intent": intent,
            "confidence": confidence
        }
