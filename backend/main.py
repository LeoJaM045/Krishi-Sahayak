from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from contextlib import asynccontextmanager

from chatbot.response_engine import response_engine
from chatbot.conversation_manager import conversation_manager
from services.translation_service import translate_to_punjabi, translate_to_english
from services.weather_service import get_weather
from services.mandi_service import get_mandi_prices
from database import models, database
from nlp.model_manager import intent_classifier
from evaluation.evaluate_model import evaluate
import json

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Load / Train model on startup if not available
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    intent_classifier.load_model()
    if intent_classifier.model is None:
        intent_classifier.train()
    yield
    print("Shutting down...")

app = FastAPI(title="Punjabi Krishi Sahayak API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    session_id: str

class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Punjabi Krishi Sahayak backend is running"}

@app.post("/api/chat")
def chat(request: ChatRequest, db: Session = Depends(database.get_db)):
    context = conversation_manager.get_context(request.session_id)
    
    response_data = response_engine.generate_response(request.message, conversation_context=context)
    
    # Update context with new entities
    if response_data.get("entities"):
        conversation_manager.update_context(request.session_id, response_data["entities"])
        
    # Log to database
    db_message = models.ChatMessage(
        session_id=request.session_id,
        user_message=request.message,
        bot_response=response_data["response"],
        intent=response_data["intent"],
        confidence=response_data["confidence"],
        language=response_data["language"]
    )
    db.add(db_message)
    db.commit()
    
    return response_data

@app.post("/api/translate")
def translate(request: TranslationRequest):
    target = request.target_language.lower()
    source = request.source_language.lower()
    if target == "punjabi":
        return {"translated_text": translate_to_punjabi(request.text)}
    elif target == "english":
        # 'auto' or 'punjabi' source → translate to English
        return {"translated_text": translate_to_english(request.text)}
    return {"translated_text": request.text}

@app.get("/api/crops")
def get_all_crops():
    return {"crops": response_engine.knowledge.get("crops", {})}

@app.get("/api/crops/{crop_name}")
def get_crop(crop_name: str):
    crops = response_engine.knowledge.get("crops", {})
    if crop_name in crops:
        return crops[crop_name]
    raise HTTPException(status_code=404, detail="Crop not found")

@app.get("/api/weather")
def weather():
    return get_weather()

@app.get("/api/mandi")
def mandi():
    return get_mandi_prices()

@app.get("/api/evaluation")
def evaluation():
    results = evaluate()
    return results

@app.get("/api/analytics")
def analytics(db: Session = Depends(database.get_db)):
    total = db.query(models.ChatMessage).count()
    
    intents = db.query(models.ChatMessage.intent, func.count(models.ChatMessage.id)).group_by(models.ChatMessage.intent).all()
    intent_dist = {i[0]: i[1] for i in intents}
    
    avg_conf = db.query(func.avg(models.ChatMessage.confidence)).scalar() or 0
    
    return {
        "total_conversations": total,
        "intent_distribution": intent_dist,
        "average_confidence": round(avg_conf, 4)
    }
