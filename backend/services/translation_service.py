import re
import time

# Comprehensive Punjabi-English dictionary covering bot response phrases.
# Longer phrases are matched first via length-sorted replacement.
PUNJABI_TO_ENGLISH = {
    'ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਜੀ': 'Sat Sri Akal (Hello)!',
    'ਸਤ ਸ੍ਰੀ ਅਕਾਲ': 'Sat Sri Akal (Hello)',
    'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ': 'Sat Sri Akal (Hello)',
    'ਕਣਕ': 'Wheat',
    'ਝੋਨਾ': 'Paddy/Rice',
    'ਝੋਨੇ': 'Paddy/Rice',
    'ਮੱਕੀ': 'Maize/Corn',
    'ਸਰ੍ਹੋਂ': 'Mustard',
    'ਦਾਲ': 'Lentils',
    'ਮੂੰਗੀ': 'Green Gram',
    'ਮਾਂਹ': 'Black Gram',
    'ਛੋਲੇ': 'Chickpeas',
    'ਚੌਲ': 'Rice',
    'ਗੰਨਾ': 'Sugarcane',
    'ਆਲੂ': 'Potato',
    'ਪਿਆਜ਼': 'Onion',
    'ਟਮਾਟਰ': 'Tomato',
    'ਸੂਰਜਮੁਖੀ': 'Sunflower',
    'ਕਪਾਹ': 'Cotton',
    'ਕਪਾਹ (ਨਰਮਾ)': 'Cotton',
    'ਬਿਜਾਈ': 'sowing/planting',
    'ਵਾਢੀ': 'harvesting',
    'ਸਿੰਚਾਈ': 'irrigation',
    'ਖਾਦ': 'fertilizer',
    'ਕੀੜਾ': 'pest/insect',
    'ਕੀੜੇ': 'pests/insects',
    'ਬਿਮਾਰੀ': 'disease',
    'ਬਿਮਾਰੀਆਂ': 'diseases',
    'ਮਿੱਟੀ': 'soil',
    'ਪਾਣੀ': 'water',
    'ਮੌਸਮ': 'weather',
    'ਮੰਡੀ': 'mandi/market',
    'ਭਾਅ': 'prices/rates',
    'ਫਸਲ': 'crop',
    'ਖੇਤ': 'field',
    'ਕਿਸਾਨ': 'farmer',
    'ਖੇਤੀ': 'farming/agriculture',
    'ਖੇਤੀਬਾੜੀ': 'agriculture',
    'ਪੰਜਾਬੀ': 'Punjabi',
    'ਕ੍ਰਿਸ਼ੀ': 'Krishi (Agriculture)',
    'ਸਹਾਇਕ': 'Assistant',
    'ਅੱਜ': 'today',
    'ਦਵਾਈ': 'medicine/pesticide',
    'ਕੀਟਨਾਸ਼ਕ': 'pesticide',
    'ਉਪਜ': 'yield/produce',
    'ਬੀਜ': 'seed',
    'ਰੋਗ': 'disease',
    'ਯੂਰੀਆ': 'Urea',
    'ਡੀਏਪੀ': 'DAP fertilizer',
    'ਮੀਂਹ': 'rain',
    'ਤਾਪਮਾਨ': 'temperature',
    'ਨਮੀ': 'humidity',
    'ਰੋਕਥਾਮ': 'prevention/control',
    'ਪਨੀਰੀ': 'nursery',
    'ਲਵਾਈ': 'transplanting',
    'ਨਦੀਨ': 'weed',
    'ਨਦੀਨਾਂ': 'weeds',
    'ਸੋਧ': 'treatment/improvement',
    'ਉੱਲੀਨਾਸ਼ਕ': 'fungicide',
    'ਕਿਲੋ': 'kg',
    'ਏਕੜ': 'acre',
    'ਹਫ਼ਤੇ': 'weeks',
    'ਦਿਨਾਂ': 'days',
    'ਸਮਾਂ': 'time/period',
    'ਸਾਲ': 'year',
    'ਮਹੀਨਾ': 'month',
    'ਪ੍ਰਤੀ': 'per',
    'ਜਨਵਰੀ': 'January',
    'ਫਰਵਰੀ': 'February',
    'ਮਾਰਚ': 'March',
    'ਅਪ੍ਰੈਲ': 'April',
    'ਮਈ': 'May',
    'ਜੂਨ': 'June',
    'ਜੁਲਾਈ': 'July',
    'ਅਗਸਤ': 'August',
    'ਸਤੰਬਰ': 'September',
    'ਅਕਤੂਬਰ': 'October',
    'ਨਵੰਬਰ': 'November',
    'ਦਸੰਬਰ': 'December',
    'ਕਰੋ': 'do/apply',
    'ਦਿਓ': 'give/provide',
    'ਲਾਓ': 'apply/put',
    'ਕਰੀਏ': 'should do',
    'ਦੱਸੋ': 'tell/please tell',
    'ਮਦਦ': 'help',
    'ਲੋੜ': 'need/requirement',
    'ਲੋੜ ਹੁੰਦੀ ਹੈ': 'is needed',
    'ਜ਼ਰੂਰੀ': 'necessary/important',
    'ਵਰਤੋਂ': 'use',
    'ਵਰਤੋ': 'use',
    'ਸੰਪਰਕ ਕਰੋ': 'please contact',
    'ਬੱਚਤ': 'saving',
    'ਸੁੱਕਣ': 'drying',
    'ਖੜ੍ਹਾ': 'standing/stagnant',
    'ਰੱਖੋ': 'keep',
    'ਨਿਰੀਖਣ': 'monitoring/inspection',
    'ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਨਹੀਂ ਹੋ ਸਕਿਆ': 'Could not connect to server',
    'ਮਾਫ਼ ਕਰਨਾ': 'Sorry',
    'ਧੰਨਵਾਦ': 'Thank you',
    'ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ': 'Thank you very much',
    'ਨਹੀਂ': 'No',
    'ਜੀ': '(respectful term)',
    'ਕਿਰਪਾ ਕਰਕੇ': 'Please',
    'ਬਾਰੇ': 'about/regarding',
    'ਜਾਣਕਾਰੀ': 'information',
    'ਸਵਾਲ': 'question',
    'ਜਵਾਬ': 'answer',
    'ਸਮੱਸਿਆ': 'problem/issue',
    'ਮੈਂ': 'I',
    'ਤੁਸੀਂ': 'you',
    'ਮੇਰੀ': 'my',
    'ਤੁਹਾਡੀ': 'your',
    'ਹੋਰ': 'more/other',
    'ਲਈ': 'for',
    'ਨਾਲ': 'with',
    'ਤੋਂ': 'from',
    'ਦਾ': 'of',
    'ਦੀ': 'of',
    'ਦੇ': 'of',
    'ਅਤੇ': 'and',
    'ਜਾਂ': 'or',
    'ਵਿੱਚ': 'in/within',
    'ਤੱਕ': 'until/up to',
    'ਆਮ': 'common/general',
    'ਸਹੀ': 'correct/proper',
    'ਚੰਗੀ': 'good',
    'ਘੱਟ': 'less/reduced',
    'ਵੱਧ': 'more/increased',
    'ਪਹਿਲਾ': 'first',
    'ਪਹਿਲੇ': 'first/initial',
    'ਫਿਰ': 'then/after',
    'ਬਾਅਦ': 'after',
    'ਅਖੀਰ ਤੋਂ': 'from late',
    'ਅਖੀਰ ਤੱਕ': 'to end of',
    'ਅਖੀਰ': 'end/late',
    'ਅਖ਼ੀਰ': 'end/late',
    'ਮਾਹਿਰ': 'expert',
    'ਸਲਾਹ': 'advice',
    'ਸਾਵਧਾਨੀ': 'care/caution',
    'ਰੋਜ਼ਾਨਾ': 'daily',
    'ਲਗਾਤਾਰ': 'continuous/regular',
    'ਸਿਫਾਰਸ਼': 'recommended',
    'ਕਿਸਮਾਂ': 'varieties',
    'ਨਿਕਾਸੀ': 'drainage',
    'ਦਰਮਿਆਨੀ': 'medium',
    'ਭਾਰੀ': 'heavy',
    'ਹਲਕੀ': 'light',
    'ਰੇਤਲੀ': 'sandy',
    'ਮੈਰਾ': 'loamy',
    'ਡੂੰਘੀ': 'deep',
    'ਦੀ ਬਿਜਾਈ ਦਾ ਸਮਾਂ': 'sowing time',
    'ਦੀ ਵਾਢੀ ਦਾ ਸਮਾਂ': 'harvesting time',
    'ਲਈ ਮਿੱਟੀ': 'soil requirements',
    'ਲਈ ਸਿੰਚਾਈ': 'irrigation requirements',
    'ਲਈ ਖਾਦ': 'fertilizer requirements',
    'ਦੀਆਂ ਆਮ ਬਿਮਾਰੀਆਂ': 'common diseases',
    'ਦੇ ਆਮ ਕੀੜੇ': 'common pests',
    'ਬਾਰੇ ਜਾਣਕਾਰੀ': 'information about',
    'ਅੱਜ ਦਾ ਮੌਸਮ': "Today's weather",
    'ਅੱਜ ਦੇ ਮੰਡੀ ਭਾਅ': "Today's mandi prices",
    'ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ': 'please provide the crop name',
    'ਮੈਂ ਤੁਹਾਡੀ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ': 'How can I help you',
    'ਹੋਰ ਕੋਈ ਸਵਾਲ ਹੋਵੇ ਤਾਂ ਜ਼ਰੂਰ ਪੁੱਛੋ': 'Feel free to ask if you have more questions',
    'ਚੰਗਾ ਜੀ ਫਿਰ ਮਿਲਦੇ ਹਾਂ': 'Goodbye, see you again',
    'ਰੱਬ ਰਾਖਾ': 'God bless you (Goodbye)',
    'ਨਹੀਂ ਸਮਝ ਸਕਿਆ': 'could not understand',
    'ਪੂਰੀ ਤਰ੍ਹਾਂ': 'completely/fully',
    'ਵਧੇਰੇ ਜਾਣਕਾਰੀ': 'more information',
    'ਮੈਨੂੰ ਇਹ ਜਾਣਕਾਰੀ ਮਿਲੀ ਹੈ': 'I found this information',
    'ਡੇਮੋ ਡੇਟਾ': 'Demo Data',
    'ਦੱਸਣ ਲਈ': 'to tell/provide',
    'ਧੁੱਪ': 'Sunny',
    'ਬੱਦਲਵਾਈ': 'Cloudy',
    'ਹਲਕਾ ਮੀਂਹ': 'Light Rain',
    'ਸਾਫ਼': 'Clear',
    'ਮੈਂ ਪੰਜਾਬੀ ਕ੍ਰਿਸ਼ੀ ਸਹਾਇਕ ਹਾਂ': 'I am the Punjabi Krishi Assistant',
    'ਚੰਗਾ ਜੀ, ਫਿਰ ਮਿਲਦੇ ਹਾਂ': 'Goodbye, see you again',
    'ਤੁਹਾਡਾ ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ': 'Thank you very much',
    'ਇਸ ਬਾਰੇ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਲਈ ਖੇਤੀਬਾੜੀ ਮਾਹਿਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ': 'For more information on this, please contact an agriculture expert',
    'ਖੇਤੀਬਾੜੀ ਮਾਹਿਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ': 'please contact an agriculture expert',
    'ਬਿਮਾਰੀ ਜਾਂ ਕੀੜੇ ਬਾਰੇ ਸਹੀ ਜਾਣਕਾਰੀ ਦੇਣ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ': 'To give correct information about disease or pests, please tell the crop name',
    'ਖਾਦ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ ਫਸਲ ਦਾ ਨਾਮ ਜ਼ਰੂਰੀ ਹੈ': 'Crop name is required for fertilizer information',
    'ਸਿੰਚਾਈ ਬਾਰੇ ਜਾਣਨ ਲਈ ਫਸਲ ਦੱਸੋ ਜੀ': 'Please tell the crop to learn about irrigation',
    'ਕਿਰਪਾ ਕਰਕੇ ਫਸਲ ਦਾ ਨਾਮ ਦੱਸੋ ਤਾਂ ਜੋ ਮੈਂ ਬਿਜਾਈ ਦਾ ਸਹੀ ਸਮਾਂ ਦੱਸ ਸਕਾਂ': 'Please tell the crop name so I can give the correct sowing time',
    'ਹਾਂ ਜੀ': 'Yes',
}

# Dedicated English -> Punjabi phrases for chatbot / UI.
ENGLISH_TO_PUNJABI = {
    'sat sri akal (hello)!': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਜੀ',
    'sat sri akal (hello)': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ',
    'how can i help you': 'ਮੈਂ ਤੁਹਾਡੀ ਕੀ ਮਦਦ ਕਰ ਸਕਦਾ ਹਾਂ',
    'thank you very much': 'ਬਹੁਤ ਬਹੁਤ ਧੰਨਵਾਦ',
    'thank you': 'ਧੰਨਵਾਦ',
    'thanks': 'ਧੰਨਵਾਦ',
    'goodbye, see you again': 'ਚੰਗਾ ਜੀ, ਫਿਰ ਮਿਲਦੇ ਹਾਂ',
    'goodbye': 'ਚੰਗਾ ਜੀ, ਫਿਰ ਮਿਲਦੇ ਹਾਂ',
    'hello': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ',
    'hi': 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ',
    'when should wheat be sown?': 'ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?',
    'when should i sow wheat?': 'ਕਣਕ ਦੀ ਬਿਜਾਈ ਕਦੋਂ ਕਰੀਏ?',
    'what is the weather today?': 'ਅੱਜ ਦਾ ਮੌਸਮ ਕਿਵੇਂ ਹੈ?',
    "what's the weather today?": 'ਅੱਜ ਦਾ ਮੌਸਮ ਕਿਵੇਂ ਹੈ?',
    "today's weather": 'ਅੱਜ ਦਾ ਮੌਸਮ',
    'could not connect to server': 'ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਨਹੀਂ ਹੋ ਸਕਿਆ',
    'wheat': 'ਕਣਕ',
    'paddy/rice': 'ਝੋਨਾ',
    'paddy': 'ਝੋਨਾ',
    'rice': 'ਝੋਨਾ',
    'maize/corn': 'ਮੱਕੀ',
    'maize': 'ਮੱਕੀ',
    'corn': 'ਮੱਕੀ',
    'mustard': 'ਸਰ੍ਹੋਂ',
    'cotton': 'ਕਪਾਹ',
    'potato': 'ਆਲੂ',
    'sowing/planting': 'ਬਿਜਾਈ',
    'sowing': 'ਬਿਜਾਈ',
    'planting': 'ਬਿਜਾਈ',
    'harvesting': 'ਵਾਢੀ',
    'irrigation': 'ਸਿੰਚਾਈ',
    'fertilizer': 'ਖਾਦ',
    'weather': 'ਮੌਸਮ',
    'disease': 'ਬਿਮਾਰੀ',
    'diseases': 'ਬਿਮਾਰੀਆਂ',
    'pest/insect': 'ਕੀੜਾ',
    'pests/insects': 'ਕੀੜੇ',
    'pest': 'ਕੀੜਾ',
    'soil': 'ਮਿੱਟੀ',
    'crop': 'ਫਸਲ',
    'today': 'ਅੱਜ',
    'temperature': 'ਤਾਪਮਾਨ',
    'humidity': 'ਨਮੀ',
    'sunny': 'ਧੁੱਪ',
    'cloudy': 'ਬੱਦਲਵਾਈ',
    'clear': 'ਸਾਫ਼',
    'mandi/market': 'ਮੰਡੀ',
    'mandi': 'ਮੰਡੀ',
}

# Short English tokens that must never be reverse-substituted inside other words.

# Short English tokens that must never be reverse-substituted inside other words.
_REVERSE_SKIP = {
    "i", "am", "a", "an", "of", "in", "or", "to", "on", "is", "be", "do",
    "no", "per", "end", "use", "and", "for", "my", "kg", "yes",
}

_last_translate_call = 0.0
_translate_min_interval = 1.5
_translation_cache = {}


def _gurmukhi_ratio(text: str) -> float:
    letters = [c for c in text if c.isalpha() or ("\u0A00" <= c <= "\u0A7F")]
    if not letters:
        return 0.0
    gurmukhi = sum(1 for c in letters if "\u0A00" <= c <= "\u0A7F")
    return gurmukhi / len(letters)


def _apply_punjabi_dictionary(text: str) -> str:
    translated = text
    for pa, en in sorted(PUNJABI_TO_ENGLISH.items(), key=lambda x: len(x[0]), reverse=True):
        translated = translated.replace(pa, en)
    # Verb-ending haan (am) after longer phrases applied
    translated = re.sub(r"(?<!\w)\u0a39\u0a3e\u0a02(?!\w)", "am", translated)
    return translated


def _apply_english_dictionary(text: str) -> str:
    """Word/phrase-safe English -> Punjabi."""
    translated = text

    for en, pa in sorted(ENGLISH_TO_PUNJABI.items(), key=lambda x: len(x[0]), reverse=True):
        pattern = re.compile(re.escape(en), re.IGNORECASE)
        translated = pattern.sub(pa, translated)

    reverse_terms = []
    for pa, en in PUNJABI_TO_ENGLISH.items():
        en_key = en.lower().strip()
        if len(en_key) < 4 or en_key in _REVERSE_SKIP:
            continue
        if en_key in ENGLISH_TO_PUNJABI:
            continue
        if "/" in en_key:
            for part in en_key.split("/"):
                part = part.strip()
                if len(part) >= 4 and part not in _REVERSE_SKIP:
                    reverse_terms.append((part, pa))
        else:
            reverse_terms.append((en_key, pa))

    for en_key, pa in sorted(set(reverse_terms), key=lambda x: len(x[0]), reverse=True):
        pattern = re.compile(rf"\b{re.escape(en_key)}\b", re.IGNORECASE)
        translated = pattern.sub(pa, translated)

    return translated


def _call_google_translate(text: str, source: str, target: str):
    global _last_translate_call
    cache_key = (source, target, text)
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    try:
        now = time.time()
        elapsed = now - _last_translate_call
        if elapsed < _translate_min_interval:
            time.sleep(_translate_min_interval - elapsed)

        from deep_translator import GoogleTranslator
        result = GoogleTranslator(source=source, target=target).translate(text)
        _last_translate_call = time.time()
        if result:
            _translation_cache[cache_key] = result
        return result
    except Exception as e:
        print(f"Translation API ({source}->{target}) failed: {e}")
        return None


def translate_to_english(text: str) -> str:
    """Translate Punjabi text to English using local dictionary + API fallback."""
    if not text or not text.strip():
        return text

    cache_key = ("pa", "en", text)
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    translated = _apply_punjabi_dictionary(text)

    if _gurmukhi_ratio(translated) < 0.25:
        cleaned = translated.strip()
        _translation_cache[cache_key] = cleaned
        return cleaned

    api_result = _call_google_translate(text, "pa", "en")
    if api_result:
        return api_result

    return translated.strip()


def translate_to_punjabi(text: str) -> str:
    """Translate English text to Punjabi using phrase map, careful word map, then API."""
    if not text or not text.strip():
        return text

    if _gurmukhi_ratio(text) > 0.3:
        return text

    cache_key = ("en", "pa", text)
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    exact = ENGLISH_TO_PUNJABI.get(text.strip().lower())
    if exact:
        _translation_cache[cache_key] = exact
        return exact

    local = _apply_english_dictionary(text)

    word_count = len(text.split())
    if word_count >= 3 and _gurmukhi_ratio(local) < 0.4:
        api_result = _call_google_translate(text, "en", "pa")
        if api_result:
            return api_result

    if local != text and _gurmukhi_ratio(local) >= 0.2:
        _translation_cache[cache_key] = local
        return local

    api_result = _call_google_translate(text, "en", "pa")
    if api_result:
        return api_result

    return local if local != text else text
