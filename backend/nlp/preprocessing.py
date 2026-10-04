import re
import unicodedata

from .language_detector import detect_language

__all__ = ["normalize_punjabi_text", "tokenize", "detect_language"]

def normalize_punjabi_text(text: str) -> str:
    """
    Normalizes Punjabi text by handling unicode, whitespace, and common punctuations.
    """
    if not text:
        return ""
        
    # Unicode normalization
    text = unicodedata.normalize('NFC', text)
    
    # Lowercase if there are any english mixed words
    text = text.lower()
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove common punctuations but keep Gurmukhi characters and basic english alphanumeric for mixed text
    text = re.sub(r'[^\w\s\u0A00-\u0A7F]', '', text)
    
    return text

def tokenize(text: str) -> list:
    """
    Simple whitespace tokenizer for Punjabi/mixed text.
    """
    return text.split()
