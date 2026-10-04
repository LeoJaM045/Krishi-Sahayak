# Viva Questions and Answers

**1. What is NLP?**
NLP (Natural Language Processing) is a field of AI that enables computers to understand, interpret, and generate human language.

**2. Why NLP is required?**
It bridges the gap between human communication and computer understanding, allowing users to interact with systems naturally rather than using code or strict commands.

**3. Why Punjabi NLP?**
Most NLP research focuses on English. Punjabi NLP is essential to make technology accessible to millions of Punjabi speakers, especially in rural sectors like agriculture.

**4. What is tokenization?**
Tokenization is the process of breaking down a sentence into smaller units called tokens (usually words or subwords).

**5. What is normalization?**
Normalization involves cleaning text (e.g., removing punctuation, converting to lowercase, handling unicode) so that variations of the same word are treated identically.

**6. What is TF-IDF?**
TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a statistical measure used to evaluate how important a word is to a document in a collection or corpus.

**7. Why TF-IDF?**
It reduces the weight of common words (like 'the', 'is', 'ਦਾ', 'ਦੀ') and increases the weight of rare, domain-specific words (like 'ਯੂਰੀਆ', 'ਕਣਕ'), making it highly effective for text classification.

**8. What is Logistic Regression?**
It is a statistical model used for classification. Despite the name, it predicts probabilities that an input belongs to a certain category.

**9. Why Logistic Regression?**
It is fast to train, works very well with high-dimensional sparse data (like TF-IDF vectors), and is highly interpretable compared to black-box deep learning models.

**10. What is intent classification?**
It is the task of determining the user's goal or intention from their text input (e.g., asking for weather vs. asking for crop disease info).

**11. What is entity extraction?**
Entity extraction (or NER) involves identifying specific, useful pieces of information from text, such as names of crops, locations, or chemicals.

**12. What is a knowledge base?**
A structured repository of verified facts and information that the system queries to generate accurate responses, rather than guessing or hallucinating.

**13. How does the chatbot work?**
User text -> Language Detection -> Preprocessing -> Intent Classification & Entity Extraction -> Knowledge Base Lookup -> Response Generation.

**14. How is Punjabi detected?**
By checking the text for characters within the Gurmukhi Unicode range (0A00-0A7F).

**15. How does English input work?**
English text is detected, translated into Punjabi using the translation service, and then passed through the standard Punjabi NLP pipeline.

**16. How does translation work?**
It uses an external translation engine (like googletrans) to map text between English and Punjabi.

**17. What is precision?**
Out of all the instances the model predicted as a specific intent, how many were actually correct.

**18. What is recall?**
Out of all the actual instances of a specific intent, how many did the model successfully identify.

**19. What is F1-score?**
The harmonic mean of precision and recall, providing a single metric that balances both.

**20. What is accuracy?**
The percentage of total correct predictions out of all predictions made.

**21. What is a confusion matrix?**
A table that describes the performance of a classification model, showing true positives, false positives, true negatives, and false negatives.

**22. Why not use only a generative LLM?**
LLMs can be expensive, require internet access, and most importantly, they often hallucinate false information (which is dangerous in agriculture, e.g., wrong pesticide dosage). A localized NLP pipeline ensures absolute control over the knowledge.

**23. What are the limitations?**
The rule-based entity extractor may fail on misspelled words, and the TF-IDF model struggles with complex sentence semantics compared to transformers.

**24. What happens when confidence is low?**
If the intent classifier's confidence score drops below a threshold (e.g., 45%), the bot triggers a fallback response asking the user to clarify.

**25. How does conversation context work?**
The backend maintains a session dictionary in memory. If a user says "Wheat" in turn 1, and "Disease" in turn 2, the system remembers "Wheat" as the active entity.

**26. How can the model be improved?**
By increasing the dataset size, adding spell-checkers, and moving to deep learning architectures like LSTMs or Transformers.

**27. How could BERT/IndicBERT be incorporated?**
IndicBERT could replace the TF-IDF + Logistic Regression pipeline. The text would be passed to the BERT model to get dense embeddings, followed by a classification head.

**28. What is the role of APIs?**
APIs (Application Programming Interfaces) allow the chatbot to fetch real-time data, like weather updates or Mandi prices, from external servers.

**29. How is agricultural safety handled?**
The bot is programmed to avoid giving specific chemical dosages and always appends a disclaimer urging farmers to consult human experts for critical decisions.

**30. What is the future scope?**
Adding voice support, image-based disease recognition, and deploying it on scalable cloud infrastructure with a PostgreSQL database.
