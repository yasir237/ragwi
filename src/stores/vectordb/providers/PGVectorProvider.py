from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from pgvector.sqlalchemy import Vector
from stores.vectordb.VectorDBInterface import VectorDBInterface
from models.db_schemes.ragwi.schemes.datachunk import DataChunk

class PGVectorProvider(VectorDBInterface):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_collection(self, collection_name: str):
        # pgvector'da collection = tablo, zaten migration ile oluşturuldu
        pass

    async def upsert_vector(self, collection_name: str, vector_id: int, vector: List[float], payload: dict):
        result = await self.db.execute(
            select(DataChunk).where(DataChunk.id == vector_id)
        )
        chunk = result.scalar_one_or_none()

        if chunk:
            chunk.embedding = vector
            await self.db.commit()
            return chunk

        return None

    async def search(self, collection_name: str, query_vector: List[float], top_k: int = 5):
        results = await self.db.execute(
            select(DataChunk)
            .order_by(DataChunk.embedding.cosine_distance(query_vector))
            .limit(top_k)
        )
        return results.scalars().all()

    async def delete_collection(self, collection_name: str):
        await self.db.execute(delete(DataChunk))
        await self.db.commit()