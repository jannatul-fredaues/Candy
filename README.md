# Candy – Your Personal AI Assistant
A hybrid online–offline voice-based AI assistant designed for personalized tasks, reasoning, and memory.
Candy uses agent-based reasoning, custom-trained intent recognition, and local memory to intelligently execute tasks for a single user.

🎯 Key Features

📴 Offline Mode
1. Wake word detection and voice interaction
2. Custom-trained intent classification
3. Entity extraction
4. Local task execution (files, system commands)
5. Persistent personal memory (vector database)
6. Optional small local LLM for reasoning

🌐 Online Mode
1. Complex reasoning and explanations
2. Web-based information retrieval
3. Advanced natural language understanding
4. Tool-augmented decision making

🔁 Hybrid Intelligence
1. Automatic switching between offline and online modes
2. Graceful degradation when internet is unavailable

🧠 Technologies Used
 Programming Language: Python 3.10+
 Speech Processing: Whisper (offline & online ASR), pyttsx3 / Coqui TTS
 NLP & Reasoning: DistilBERT (intent classification), spaCy (entity extraction), local LLM (Phi-2/TinyLlama), online LLM API
 Memory: FAISS (local vector database)
