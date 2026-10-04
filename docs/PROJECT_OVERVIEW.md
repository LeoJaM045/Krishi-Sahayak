# Project Title: Krishi Sahayak - Punjabi Agricultural Chatbot

## Problem Statement
Farmers in Punjab face challenges accessing timely, accurate, and localized agricultural information in their native language (Punjabi). Existing solutions are often in English or Hindi, use complex technical terms, or lack the regional context required for Punjab's specific crops and soil conditions.

## Motivation
Agriculture is the backbone of Punjab's economy. Providing farmers with a digital assistant that understands their language (including mixed English-Punjabi terms) and provides immediate, farmer-friendly answers can significantly improve crop yield, resource management, and pest control.

## Objectives
- To build a chatbot capable of understanding natural language queries in Punjabi and mixed English-Punjabi.
- To provide an English ↔ Punjabi translation layer for broader accessibility.
- To classify user intents accurately using NLP (TF-IDF + Logistic Regression).
- To extract relevant agricultural entities (crops, diseases, fertilizers).
- To deliver context-aware, locally relevant agricultural advice.

## Existing System
Current systems rely on call centers (e.g., Kisan Call Center) or static websites. Mobile apps often require navigating complex menus. LLM-based bots usually lack localization, sometimes hallucinate dangerous pesticide doses, and require expensive API calls.

## Limitations of Existing Systems
- High latency (call centers).
- Language barrier (mostly English/Hindi).
- Lack of offline/local-first capabilities.
- Poor handling of Gurmukhi script and rural dialects.

## Proposed System
Krishi Sahayak is a text-based, AI-powered chatbot tailored for Punjabi farmers. It uses a custom NLP pipeline trained specifically on Punjabi agricultural intents. It features an interactive UI, real-time intent analysis display, and a curated knowledge base to ensure safe and accurate responses.

## System Architecture
- **Frontend**: React-based responsive UI.
- **Backend**: FastAPI serving REST endpoints.
- **NLP Engine**: Custom pipeline using Scikit-Learn.
- **Database**: SQLite for storing conversational analytics.

## NLP Pipeline
User Text -> Language Detection -> Translation (if required) -> Punjabi Text Preprocessing -> Tokenization -> TF-IDF Vectorization -> Logistic Regression -> Intent Classification -> Entity Extraction -> Knowledge Retrieval -> Response Generation.

## Dataset
A custom dataset (`punjabi_intents.csv`) containing over 300 realistic agricultural queries in Punjabi and mixed English, categorized into 19+ intents (e.g., `sowing_time`, `crop_disease`, `mandi_price`).

## Data Preprocessing
- Unicode Normalization (NFC) for Gurmukhi script.
- Lowercasing for mixed English text.
- Punctuation removal while preserving Gurmukhi characters.
- Whitespace normalization.

## TF-IDF (Term Frequency-Inverse Document Frequency)
Used to convert Punjabi text into numerical vectors. It highlights words that are frequent in a specific query but rare across the entire dataset, effectively capturing key agricultural terms.

## Logistic Regression
Used as the classifier. It is lightweight, fast, interpretable, and performs exceptionally well on TF-IDF vectors for text classification tasks, making it ideal for a local, API-independent NLP solution.

## Intent Classification
Categorizes the user's query into predefined buckets (e.g., asking about weather vs. asking about fertilizer).

## Entity Extraction
A rule/dictionary-based approach extracts specific entities like crop names (e.g., "ਕਣਕ"), symptoms (e.g., "ਪੱਤੇ ਪੀਲੇ"), and fertilizers.

## Translation System
Provides optional English ↔ Punjabi translation, allowing users who prefer typing in English to receive answers in Punjabi, or vice-versa.

## Knowledge Base
A structured JSON repository containing expert-vetted information on major crops (Wheat, Rice, Cotton, etc.), ensuring the bot does not invent false information.

## Response Generation
Combines the detected intent, extracted entities, and knowledge base to construct a natural, farmer-friendly Punjabi response.

## Evaluation Metrics
- **Accuracy**: Overall correctness of the model.
- **Precision**: Accuracy of positive predictions.
- **Recall**: Ability to find all relevant instances.
- **F1-score**: Harmonic mean of precision and recall.

## Limitations
- Rule-based entity extraction may miss novel synonyms.
- Logistic Regression may struggle with highly complex, multi-intent sentences compared to large transformers.
- Reliance on external APIs for live weather/mandi prices.

## Future Scope
- Integration with IndicBERT for deep contextual understanding.
- Voice support (Speech-to-Text and Text-to-Speech in Punjabi).
- Image recognition for crop disease diagnosis.
