from abc import ABC, abstractmethod
from typing import List

class VectorDBInterface(ABC):

    @abstractmethod
    async def create_collection(self, collection_name: str):
        pass

    @abstractmethod
    async def upsert_vector(self, collection_name: str, vector_id: str, vector: List[float], payload: dict):
        pass

    @abstractmethod
    async def search(self, collection_name: str, query_vector: List[float], top_k: int = 5):
        pass

    @abstractmethod
    async def delete_collection(self, collection_name: str):
        pass