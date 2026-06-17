import requests
from typing import List
from stores.llm.LLMInterface import LLMInterface

class OllamaProvider(LLMInterface):

    def __init__(self, base_url: str, model: str, embedding_model: str):
        self.base_url = base_url
        self.model = model
        self.embedding_model = embedding_model

    def generate_text(self, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

    def embed_text(self, text: str) -> List[float]:
        response = requests.post(
            f"{self.base_url}/api/embeddings",
            json={
                "model": self.embedding_model,
                "prompt": text
            }
        )
        return response.json()["embedding"]

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        return [self.embed_text(text) for text in texts]