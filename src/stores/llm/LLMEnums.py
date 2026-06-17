from enum import Enum

class LLMEnum(str, Enum):
    GROQ = "groq"
    OLLAMA = "ollama"

class LLMModelEnum(str, Enum):
    # Groq modelleri
    GROQ_LLAMA3 = "llama3-8b-8192"
    GROQ_MIXTRAL = "mixtral-8x7b-32768"
    
    # Ollama modelleri
    OLLAMA_LLAMA3 = "llama3"
    OLLAMA_MISTRAL = "mistral"