from stores.llm.LLMEnums import LLMEnum
from stores.llm.providers.GroqProvider import GroqProvider
from stores.llm.providers.OllamaProvider import OllamaProvider

class LLMProviderFactory:

    def __init__(self, settings):
        self.settings = settings

    def create(self, provider: str):
        if provider == LLMEnum.GROQ:
            return GroqProvider(
                api_key=self.settings.GROQ_API_KEY,
                model=self.settings.GROQ_MODEL
            )
        elif provider == LLMEnum.OLLAMA:
            return OllamaProvider(
                base_url=self.settings.OLLAMA_BASE_URL,
                model=self.settings.OLLAMA_MODEL,
                embedding_model=self.settings.OLLAMA_EMBEDDING_MODEL
            )
        else:
            raise ValueError(f"Bilinmeyen provider: {provider}")