import json
import os
import re

ENTITIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'entities.json')

class EntityExtractor:
    def __init__(self):
        self.entities_data = {}
        self.load_entities()

    def load_entities(self):
        if os.path.exists(ENTITIES_PATH):
            with open(ENTITIES_PATH, 'r', encoding='utf-8') as f:
                self.entities_data = json.load(f)

    def extract(self, text: str):
        extracted = {}
        text_lower = text.lower()
        
        # Crops
        for crop in self.entities_data.get('crops', []):
            for syn in crop['synonyms']:
                if re.search(r'\b' + re.escape(syn.lower()) + r'\b', text_lower) or syn.lower() in text_lower:
                    extracted['crop'] = crop['name_punjabi']
                    break
            if 'crop' in extracted:
                break
                
        # Symptoms
        for symptom in self.entities_data.get('symptoms', []):
            for syn in symptom['synonyms']:
                if re.search(r'\b' + re.escape(syn.lower()) + r'\b', text_lower) or syn.lower() in text_lower:
                    extracted['symptom'] = symptom['name_punjabi']
                    break
            if 'symptom' in extracted:
                break
                
        # Fertilizers
        for fertilizer in self.entities_data.get('fertilizers', []):
            for syn in fertilizer['synonyms']:
                if re.search(r'\b' + re.escape(syn.lower()) + r'\b', text_lower) or syn.lower() in text_lower:
                    extracted['fertilizer'] = fertilizer['name_punjabi']
                    break
            if 'fertilizer' in extracted:
                break

        return extracted
