import json
import os
from nlp.model_manager import analyze_text
from services.translation_service import translate_to_punjabi
from services.weather_service import get_weather
from services.mandi_service import get_mandi_prices

KNOWLEDGE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'agriculture_knowledge.json')

class ResponseEngine:
    def __init__(self):
        self.knowledge = {}
        self.load_knowledge()
        self.CONFIDENCE_THRESHOLD = 0.15

    def load_knowledge(self):
        if os.path.exists(KNOWLEDGE_PATH):
            with open(KNOWLEDGE_PATH, 'r', encoding='utf-8') as f:
                self.knowledge = json.load(f)

    def generate_response(self, text: str, conversation_context=None):
        analysis = analyze_text(text)
        
        # If English, we only want to analyze intent after translation or handling it
        if analysis["language"] == "english":
            punjabi_text = translate_to_punjabi(text)
            analysis = analyze_text(punjabi_text)
            analysis["language"] = "english" # preserve original language
            
        intent = analysis["intent"]
        confidence = analysis["confidence"]
        entities = analysis["entities"]
        
        # If low confidence, fallback
        if confidence < self.CONFIDENCE_THRESHOLD:
            return {
                "response": self.knowledge.get("general_faqs", {}).get("unknown", "ਮਾਫ਼ ਕਰਨਾ, ਮੈਂ ਤੁਹਾਡਾ ਸਵਾਲ ਪੂਰੀ ਤਰ੍ਹਾਂ ਨਹੀਂ ਸਮਝ ਸਕਿਆ।"),
                "intent": "unknown",
                "confidence": confidence,
                "language": analysis["language"],
                "entities": entities
            }

        response_message = ""
        
        # Merge context entities if missing in current message
        if conversation_context:
            for k, v in conversation_context.get("entities", {}).items():
                if k not in entities:
                    entities[k] = v

        crop = entities.get("crop")
        
        # Handle intents
        if intent == "weather":
            weather_data = get_weather()
            response_message = f"ਅੱਜ ਦਾ ਮੌਸਮ ({weather_data['location']}): {weather_data['condition']}, ਤਾਪਮਾਨ: {weather_data['temperature']}, ਨਮੀ: {weather_data['humidity']} (Demo Data)"
            
        elif intent == "mandi_price":
            mandi_data = get_mandi_prices()
            prices_str = "\n".join([f"{p['crop']}: {p['price']}" for p in mandi_data['prices']])
            response_message = f"ਅੱਜ ਦੇ ਮੰਡੀ ਭਾਅ (Demo Data):\n{prices_str}"
            
        elif intent == "greeting":
            response_message = "ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਜੀ! 🌾 ਮੈਂ ਪੰਜਾਬੀ ਕ੍ਰਿਸ਼ੀ ਸਹਾਇਕ ਹਾਂ। ਦੱਸੋ ਮੈਂ ਤੁਹਾਡੀ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ?"
            
        elif intent == "thanks":
            response_message = "ਤੁਹਾਡਾ ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ! ਹੋਰ ਕੋਈ ਸਵਾਲ ਹੋਵੇ ਤਾਂ ਜ਼ਰੂਰ ਪੁੱਛੋ।"
            
        elif intent == "goodbye":
            response_message = "ਚੰਗਾ ਜੀ, ਫਿਰ ਮਿਲਦੇ ਹਾਂ! ਰੱਬ ਰਾਖਾ।"
            
        elif crop and crop in self.knowledge.get("crops", {}):
            crop_info = self.knowledge["crops"][crop]
            
            if intent == "sowing_time":
                response_message = f"{crop} ਦੀ ਬਿਜਾਈ ਦਾ ਸਮਾਂ: {crop_info['sowing_period']}"
            elif intent == "harvesting_time":
                response_message = f"{crop} ਦੀ ਵਾਢੀ ਦਾ ਸਮਾਂ: {crop_info['harvesting_period']}"
            elif intent == "soil":
                response_message = f"{crop} ਲਈ ਮਿੱਟੀ: {crop_info['soil_requirements']}"
            elif intent == "irrigation":
                response_message = f"{crop} ਲਈ ਸਿੰਚਾਈ: {crop_info['irrigation']}"
            elif intent == "fertilizer":
                response_message = f"{crop} ਲਈ ਖਾਦ: {crop_info['fertilizer']}"
            elif intent == "crop_disease":
                response_message = f"{crop} ਦੀਆਂ ਆਮ ਬਿਮਾਰੀਆਂ: {', '.join(crop_info['common_diseases'])}. \nਰੋਕਥਾਮ: {crop_info['basic_prevention']}"
            elif intent == "pest_control":
                response_message = f"{crop} ਦੇ ਆਮ ਕੀੜੇ: {', '.join(crop_info['common_pests'])}. \nਸਾਵਧਾਨੀ ਵਰਤੋ ਅਤੇ ਮਾਹਿਰ ਦੀ ਸਲਾਹ ਲਓ।"
            elif intent in ["crop_information", "general_agriculture", "crop_yield"]:
                response_message = f"{crop} ਬਾਰੇ ਜਾਣਕਾਰੀ:\nਬਿਜਾਈ: {crop_info['sowing_period']}\nਖਾਦ: {crop_info['fertilizer']}\nਸਿੰਚਾਈ: {crop_info['irrigation']}"
            else:
                response_message = f"{crop} ਬਾਰੇ ਮੈਨੂੰ ਇਹ ਜਾਣਕਾਰੀ ਮਿਲੀ ਹੈ: {crop_info['sowing_period']}"
        else:
            # Handle cases where crop is not specified or found
            if intent == "sowing_time":
                response_message = "ਕਿਰਪਾ ਕਰਕੇ ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ ਤਾਂ ਜੋ ਮੈਂ ਬਿਜਾਈ ਦਾ ਸਹੀ ਸਮਾਂ ਦੱਸ ਸਕਾਂ।"
            elif intent == "crop_disease" or intent == "pest_control":
                response_message = "ਬਿਮਾਰੀ ਜਾਂ ਕੀੜੇ ਬਾਰੇ ਸਹੀ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ।"
            elif intent == "fertilizer":
                response_message = "ਖਾਦ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ ਫਸਲ ਦਾ ਨਾਮ ਜ਼ਰੂਰੀ ਹੈ।"
            elif intent == "irrigation":
                response_message = "ਸਿੰਚਾਈ ਬਾਰੇ ਜਾਣਨ ਲਈ ਫਸਲ ਦੱਸੋ ਜੀ।"
            else:
                response_message = self.knowledge.get("general_faqs", {}).get(intent, "ਇਸ ਬਾਰੇ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ ਖੇਤੀਬਾੜੀ ਮਾਹਿਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।")

        return {
            "response": response_message,
            "intent": intent,
            "confidence": confidence,
            "language": analysis["language"],
            "entities": entities
        }

response_engine = ResponseEngine()
