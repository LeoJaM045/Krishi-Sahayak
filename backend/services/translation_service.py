import time

# Comprehensive Punjabi-English dictionary covering all bot response phrases
PUNJABI_TO_ENGLISH = {
    # === Greetings ===
    "ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਜੀ": "Sat Sri Akal (Hello)!",
    "ਸਤ ਸ੍ਰੀ ਅਕਾਲ": "Sat Sri Akal (Hello)",
    "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ": "Sat Sri Akal (Hello)",

    # === Crops ===
    "ਕਣਕ": "Wheat",
    "ਝੋਨਾ": "Paddy/Rice",
    "ਝੋਨੇ": "Paddy/Rice",
    "ਮੱਕੀ": "Maize/Corn",
    "ਸਰ੍ਹੋਂ": "Mustard",
    "ਦਾਲ": "Lentils",
    "ਮੂੰਗੀ": "Green Gram",
    "ਮਾਂਹ": "Black Gram",
    "ਛੋਲੇ": "Chickpeas",
    "ਚੌਲ": "Rice",
    "ਗੰਨਾ": "Sugarcane",
    "ਆਲੂ": "Potato",
    "ਪਿਆਜ਼": "Onion",
    "ਟਮਾਟਰ": "Tomato",
    "ਸੂਰਜਮੁਖੀ": "Sunflower",
    "ਕਪਾਹ": "Cotton",
    "ਕਪਾਹ (ਨਰਮਾ)": "Cotton",

    # === Agricultural Terms ===
    "ਬਿਜਾਈ": "sowing/planting",
    "ਵਾਢੀ": "harvesting",
    "ਸਿੰਚਾਈ": "irrigation",
    "ਖਾਦ": "fertilizer",
    "ਕੀੜਾ": "pest/insect",
    "ਕੀੜੇ": "pests/insects",
    "ਬਿਮਾਰੀ": "disease",
    "ਬਿਮਾਰੀਆਂ": "diseases",
    "ਮਿੱਟੀ": "soil",
    "ਪਾਣੀ": "water",
    "ਮੌਸਮ": "weather",
    "ਮੰਡੀ": "mandi/market",
    "ਭਾਅ": "prices/rates",
    "ਫਸਲ": "crop",
    "ਖੇਤ": "field",
    "ਕਿਸਾਨ": "farmer",
    "ਖੇਤੀ": "farming/agriculture",
    "ਖੇਤੀਬਾੜੀ": "agriculture",
    "ਪੰਜਾਬੀ": "Punjabi",
    "ਕ੍ਰਿਸ਼ੀ": "Krishi (Agriculture)",
    "ਸਹਾਇਕ": "Assistant",
    "ਹਾਂ": "I am",
    "ਅੱਜ": "today",
    "ਦਵਾਈ": "medicine/pesticide",
    "ਕੀਟਨਾਸ਼ਕ": "pesticide",
    "ਉਪਜ": "yield/produce",
    "ਬੀਜ": "seed",
    "ਰੋਗ": "disease",
    "ਯੂਰੀਆ": "Urea",
    "ਡੀਏਪੀ": "DAP fertilizer",
    "ਮੀਂਹ": "rain",
    "ਤਾਪਮਾਨ": "temperature",
    "ਨਮੀ": "humidity",
    "ਰੋਕਥਾਮ": "prevention/control",
    "ਪਨੀਰੀ": "nursery",
    "ਲਵਾਈ": "transplanting",
    "ਨਦੀਨ": "weed",
    "ਨਦੀਨਾਂ": "weeds",
    "ਸੋਧ": "treatment/improvement",
    "ਉੱਲੀਨਾਸ਼ਕ": "fungicide",
    "ਕਿਲੋ": "kg",
    "ਏਕੜ": "acre",
    "ਹਫ਼ਤੇ": "weeks",
    "ਦਿਨਾਂ": "days",
    "ਸਮਾਂ": "time/period",
    "ਸਾਲ": "year",
    "ਮਹੀਨਾ": "month",
    "ਪ੍ਰਤੀ": "per",

    # === Months ===
    "ਜਨਵਰੀ": "January",
    "ਫਰਵਰੀ": "February",
    "ਮਾਰਚ": "March",
    "ਅਪ੍ਰੈਲ": "April",
    "ਮਈ": "May",
    "ਜੂਨ": "June",
    "ਜੁਲਾਈ": "July",
    "ਅਗਸਤ": "August",
    "ਸਤੰਬਰ": "September",
    "ਅਕਤੂਬਰ": "October",
    "ਨਵੰਬਰ": "November",
    "ਦਸੰਬਰ": "December",

    # === Common Action Words ===
    "ਕਰੋ": "do/apply",
    "ਦਿਓ": "give/provide",
    "ਲਾਓ": "apply/put",
    "ਕਰੀਏ": "should do",
    "ਦੱਸੋ": "tell/please tell",
    "ਮਦਦ": "help",
    "ਲੋੜ": "need/requirement",
    "ਲੋੜ ਹੁੰਦੀ ਹੈ": "is needed",
    "ਜ਼ਰੂਰੀ": "necessary/important",
    "ਵਰਤੋਂ": "use",
    "ਵਰਤੋ": "use",
    "ਸੰਪਰਕ ਕਰੋ": "contact",
    "ਬੱਚਤ": "saving",
    "ਸੁੱਕਣ": "drying",
    "ਖੜ੍ਹਾ": "standing/stagnant",
    "ਰੱਖੋ": "keep",
    "ਨਿਰੀਖਣ": "monitoring/inspection",

    # === Common Phrases ===
    "ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਨਹੀਂ ਹੋ ਸਕਿਆ": "Could not connect to server",
    "ਮਾਫ਼ ਕਰਨਾ": "Sorry",
    "ਧੰਨਵਾਦ": "Thank you",
    "ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ": "Thank you very much",
    "ਹਾਂ": "Yes",
    "ਨਹੀਂ": "No",
    "ਜੀ": "(respectful term)",
    "ਕਿਰਪਾ ਕਰਕੇ": "Please",
    "ਬਾਰੇ": "about/regarding",
    "ਜਾਣਕਾਰੀ": "information",
    "ਸਵਾਲ": "question",
    "ਜਵਾਬ": "answer",
    "ਸਮੱਸਿਆ": "problem/issue",
    "ਮੈਂ": "I",
    "ਤੁਸੀਂ": "you",
    "ਮੇਰੀ": "my",
    "ਤੁਹਾਡੀ": "your",
    "ਹੋਰ": "more/other",
    "ਲਈ": "for",
    "ਨਾਲ": "with",
    "ਤੋਂ": "from",
    "ਦਾ": "of",
    "ਦੀ": "of",
    "ਦੇ": "of",
    "ਅਤੇ": "and",
    "ਜਾਂ": "or",
    "ਵਿੱਚ": "in/within",
    "ਤੱਕ": "until/up to",
    "ਆਮ": "common/general",
    "ਸਹੀ": "correct/proper",
    "ਚੰਗੀ": "good",
    "ਘੱਟ": "less/reduced",
    "ਵੱਧ": "more/increased",
    "ਪਹਿਲਾ": "first",
    "ਪਹਿਲੇ": "first/initial",
    "ਫਿਰ": "then/after",
    "ਬਾਅਦ": "after",
    "ਅਖੀਰ ਤੋਂ": "from late",
    "ਅਖੀਰ ਤੱਕ": "to end of",
    "ਅਖੀਰ": "end/late",
    "ਅਖ਼ੀਰ": "end/late",
    "ਮਾਹਿਰ": "expert",
    "ਸਲਾਹ": "advice",
    "ਸਾਵਧਾਨੀ": "care/caution",
    "ਰੋਜ਼ਾਨਾ": "daily",
    "ਲਗਾਤਾਰ": "continuous/regular",
    "ਸਿਫਾਰਸ਼": "recommended",
    "ਕਿਸਮਾਂ": "varieties",
    "ਨਿਕਾਸੀ": "drainage",
    "ਦਰਮਿਆਨੀ": "medium",
    "ਭਾਰੀ": "heavy",
    "ਹਲਕੀ": "light",
    "ਰੇਤਲੀ": "sandy",
    "ਮੈਰਾ": "loamy",
    "ਡੂੰਘੀ": "deep",

    # === Response phrases ===
    "ਦੀ ਬਿਜਾਈ ਦਾ ਸਮਾਂ": "sowing time",
    "ਦੀ ਵਾਢੀ ਦਾ ਸਮਾਂ": "harvesting time",
    "ਲਈ ਮਿੱਟੀ": "soil requirements",
    "ਲਈ ਸਿੰਚਾਈ": "irrigation requirements",
    "ਲਈ ਖਾਦ": "fertilizer requirements",
    "ਦੀਆਂ ਆਮ ਬਿਮਾਰੀਆਂ": "common diseases",
    "ਦੇ ਆਮ ਕੀੜੇ": "common pests",
    "ਬਾਰੇ ਜਾਣਕਾਰੀ": "information about",
    "ਅੱਜ ਦਾ ਮੌਸਮ": "Today's weather",
    "ਅੱਜ ਦੇ ਮੰਡੀ ਭਾਅ": "Today's mandi prices",
    "ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ": "please provide the crop name",
    "ਮੈਂ ਤੁਹਾਡੀ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ": "How can I help you",
    "ਹੋਰ ਕੋਈ ਸਵਾਲ ਹੋਵੇ ਤਾਂ ਜ਼ਰੂਰ ਪੁੱਛੋ": "Feel free to ask if you have more questions",
    "ਚੰਗਾ ਜੀ ਫਿਰ ਮਿਲਦੇ ਹਾਂ": "Goodbye, see you again",
    "ਰੱਬ ਰਾਖਾ": "God bless you (Goodbye)",
    "ਨਹੀਂ ਸਮਝ ਸਕਿਆ": "could not understand",
    "ਪੂਰੀ ਤਰ੍ਹਾਂ": "completely/fully",
    "ਵਧੇਰੇ ਜਾਣਕਾਰੀ": "more information",
    "ਮੈਨੂੰ ਇਹ ਜਾਣਕਾਰੀ ਮਿਲੀ ਹੈ": "I found this information",
    "ਡੇਮੋ ਡੇਟਾ": "Demo Data",
    "ਦੱਸਣ ਲਈ": "to tell/provide",
    "ਸੰਪਰਕ ਕਰੋ": "please contact",

    # === Conditions & weather ===
    "ਧੁੱਪ": "Sunny",
    "ਬੱਦਲਵਾਈ": "Cloudy",
    "ਹਲਕਾ ਮੀਂਹ": "Light Rain",
    "ਸਾਫ਼": "Clear",
}

# Rate limiting for external API
_last_translate_call = 0.0
_translate_min_interval = 2.0  # 2 seconds between API calls


def translate_to_english(text: str) -> str:
    """Translate Punjabi text to English using local dictionary + API fallback."""
    global _last_translate_call

    if not text or not text.strip():
        return text

    # Apply local dictionary - sort by length descending to match longer phrases first
    translated = text
    sorted_terms = sorted(PUNJABI_TO_ENGLISH.items(), key=lambda x: len(x[0]), reverse=True)
    for pa, en in sorted_terms:
        translated = translated.replace(pa, en)

    # Count remaining Punjabi (Gurmukhi) chars
    punjabi_chars = sum(1 for c in translated if '\u0A00' <= c <= '\u0A7F')
    total_chars = len(translated.replace(' ', ''))

    # If less than 25% Punjabi chars remain, the local translation is good enough
    if total_chars == 0 or punjabi_chars < total_chars * 0.25:
        return translated.strip()

    # Fallback: try deep-translator API with rate limiting
    try:
        now = time.time()
        elapsed = now - _last_translate_call
        if elapsed < _translate_min_interval:
            time.sleep(_translate_min_interval - elapsed)

        from deep_translator import GoogleTranslator
        result = GoogleTranslator(source='pa', target='en').translate(text)
        _last_translate_call = time.time()
        return result if result else translated
    except Exception as e:
        print(f"Translation to English API failed: {e}")
        # Return best local translation we have
        return translated.strip()


def translate_to_punjabi(text: str) -> str:
    """Translate English text to Punjabi using API with local fallback."""
    global _last_translate_call

    if not text or not text.strip():
        return text

    # Check if text is already mostly Punjabi
    punjabi_chars = sum(1 for c in text if '\u0A00' <= c <= '\u0A7F')
    if punjabi_chars > len(text) * 0.3:
        return text  # Already Punjabi

    # Try reverse dictionary lookup for English -> Punjabi
    text_lower = text.lower()
    reverse_dict = {en.lower(): pa for pa, en in PUNJABI_TO_ENGLISH.items()}
    translated = text
    for en_lower, pa in sorted(reverse_dict.items(), key=lambda x: len(x[0]), reverse=True):
        if en_lower in text_lower:
            translated = translated.replace(en_lower, pa)

    if translated != text:
        return translated

    # Fallback to API
    try:
        now = time.time()
        elapsed = now - _last_translate_call
        if elapsed < _translate_min_interval:
            time.sleep(_translate_min_interval - elapsed)

        from deep_translator import GoogleTranslator
        result = GoogleTranslator(source='en', target='pa').translate(text)
        _last_translate_call = time.time()
        return result if result else text
    except Exception as e:
        print(f"Translation to Punjabi API failed: {e}")
        return text
