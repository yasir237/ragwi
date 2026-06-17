from groq import Groq
from typing import List
from stores.llm.LLMInterface import LLMInterface

class GroqProvider(LLMInterface):

    def __init__(self, api_key: str, model: str):
        self.client = Groq(api_key=api_key)
        self.model = model

    def generate_text(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    def embed_text(self, text: str) -> List[float]:
        raise NotImplementedError("Groq embedding desteklemiyor, Ollama kullan")

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError("Groq embedding desteklemiyor, Ollama kullan")