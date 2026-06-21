from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.db_schemes.ragwi.schemes.datachunk import DataChunk

class ChunkModel:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_chunk(self, asset_id: int, project_id: int, text: str, chunk_order: int):
        chunk = DataChunk(
            asset_id=asset_id,
            project_id=project_id,
            text=text,
            chunk_order=chunk_order
        )
        self.db.add(chunk)
        await self.db.commit()
        await self.db.refresh(chunk)
        return chunk

    async def get_chunks_by_asset(self, asset_id: int):
        result = await self.db.execute(
            select(DataChunk).where(DataChunk.asset_id == asset_id)
        )
        return result.scalars().all()