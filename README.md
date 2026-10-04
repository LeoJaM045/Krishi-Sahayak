# Krishi Sahayak - Punjabi Agricultural Chatbot 🌾

Krishi Sahayak is a complete, production-quality full-stack NLP project. It is an AI-powered Punjabi-language agricultural chatbot designed specifically for Punjabi-speaking farmers.

## Features
- **Punjabi NLP Pipeline**: Text preprocessing, normalization, TF-IDF + Logistic Regression based intent classification, entity extraction.
- **Language Detection**: Automatically detects Punjabi, English, and Mixed input.
- **Translation System**: Bi-directional English ↔ Punjabi translation.
- **Agricultural Knowledge Base**: Detailed crop data, diseases, pests, fertilizers.
- **Conversation Context**: Keeps track of entities discussed.
- **API Integrations**: Mock structures for Weather and Mandi (Market) Prices with demo fallbacks.
- **Model Evaluation**: Script to evaluate Accuracy, Precision, Recall, F1-score and Confusion Matrix.
- **Analytics Dashboard**: Monitor usage and intents.

## Technology Stack
- **Frontend**: React, Vite, Tailwind CSS, Lucide React
- **Backend**: Python, FastAPI, SQLite
- **NLP / ML**: scikit-learn, pandas, NumPy, NLTK, Googletrans

## Installation & Setup

### Backend
1. Go to backend directory:
   ```bash
   cd backend
   ```
2. Create virtual environment and activate:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Mac/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend
1. Go to frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```

## Model Training & Evaluation
To train the NLP model from scratch (it also auto-trains on first boot if missing):
```bash
cd backend
python -c "from nlp.intent_classifier import IntentClassifier; IntentClassifier().train()"
```

To evaluate the model:
```bash
cd backend
python evaluation/evaluate_model.py
```

## Running Tests
Run pytest from the root folder:
```bash
pytest tests/
```

## Environment Variables
Copy `.env.example` to `.env` and fill in any actual API keys if you have them. Otherwise, the app falls back to demo data automatically.

## API Documentation
Once backend is running, visit `http://localhost:8000/docs` for Swagger UI.

## Future Improvements
- Integrate `IndicBERT` for deep semantic understanding.
- Connect real-time weather and Mandi APIs.
- Expand dataset to 10000+ utterances.
- Add PostgreSQL for production deployment.
