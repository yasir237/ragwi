from stores.vectordb.VectorDBEnums import VectorDBEnum
from stores.vectordb.providers.PGVectorProvider import PGVectorProvider

class VectorDBProviderFactory:

    def __init__(self, db):
        self.db = db

    def create(self, provider: str):
        if provider == VectorDBEnum.PGVECTOR:
            return PGVectorProvider(db=self.db)
        else:
            raise ValueError(f"Bilinmeyen provider: {provider}")