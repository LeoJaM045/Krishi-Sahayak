import re

def detect_language(text: str) -> str:
    """
    Detects whether the text is Punjabi, English, or Mixed.
    Returns: 'punjabi', 'english', 'mixed', or 'unknown'
    """
    if not text:
        return "unknown"
        
    # Gurmukhi Unicode range: 0A00-0A7F
    gurmukhi_chars = len(re.findall(r'[\u0A00-\u0A7F]', text))
    english_chars = len(re.findall(r'[a-zA-Z]', text))
    
    total_chars = len(text.replace(" ", ""))
    
    if total_chars == 0:
        return "unknown"
        
    if gurmukhi_chars > 0 and english_chars > 0:
        return "mixed"
    elif gurmukhi_chars > 0:
        return "punjabi"
    elif english_chars > 0:
        return "english"
        
    return "unknown"
