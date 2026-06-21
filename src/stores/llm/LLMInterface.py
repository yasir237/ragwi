from abc import ABC, abstractmethod
from typing import List

class LLMInterface(ABC):

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass

    @abstractmethod
    def embed_text(self, text: str) -> List[float]:
        pass

    @abstractmethod
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        pass