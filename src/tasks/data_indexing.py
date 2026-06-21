import asyncio
from celery_app import celery_app
from models.BaseDataModel import AsyncSessionLocal
from models.ChunkModel import ChunkModel
from stores.llm.LLMProviderFactory import LLMProviderFactory
from stores.llm.LLMEnums import LLMEnum
from stores.vectordb.VectorDBProviderFactory import VectorDBProviderFactory
from stores.vectordb.VectorDBEnums import VectorDBEnum
from helpers.config import get_settings

settings = get_settings()

async def _index_chunks(asset_id: int):
    async with AsyncSessionLocal() as db:
        chunk_model = ChunkModel(db)
        chunks = await chunk_model.get_chunks_by_asset(asset_id)

        if not chunks:
            return {"status": "failed", "reason": "no chunks found"}

        llm_factory = LLMProviderFactory(settings)
        llm_provider = llm_factory.create(LLMEnum.OLLAMA)

        vectordb_factory = VectorDBProviderFactory(db)
        vectordb_provider = vectordb_factory.create(VectorDBEnum.PGVECTOR)

        for chunk in chunks:
            embedding = llm_provider.embed_text(chunk.text)
            await vectordb_provider.upsert_vector(
                collection_name="chunks",
                vector_id=chunk.id,
                vector=embedding,
                payload={}
            )

        return {"status": "success", "indexed": len(chunks)}

@celery_app.task
def index_chunks(asset_id: int):
    return asyncio.run(_index_chunks(asset_id))