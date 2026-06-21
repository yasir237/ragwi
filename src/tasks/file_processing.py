import asyncio
import fitz
from celery_app import celery_app
from models.BaseDataModel import AsyncSessionLocal
from models.ChunkModel import ChunkModel
from models.AssetModel import AssetModel
from models.enums.ProcessingEnum import ProcessingEnum

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list:
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append(chunk)
        start = end - overlap
    return chunks

async def _process_file(asset_id: int):
    async with AsyncSessionLocal() as db:
        asset_model = AssetModel(db)
        asset = await asset_model.get_asset(asset_id)

        if not asset:
            return {"status": "failed", "reason": "asset not found"}

        await asset_model.update_asset_status(asset_id, ProcessingEnum.PROCESSING)

        text = extract_text_from_pdf(asset.path)
        chunks = chunk_text(text)

        chunk_model = ChunkModel(db)
        for order, chunk_text_item in enumerate(chunks):
            await chunk_model.create_chunk(
                asset_id=asset.id,
                project_id=asset.project_id,
                text=chunk_text_item,
                chunk_order=order
            )

        await asset_model.update_asset_status(asset_id, ProcessingEnum.COMPLETED)
        return {"status": "success", "chunks": len(chunks)}

@celery_app.task
def process_file(asset_id: int):
    return asyncio.run(_process_file(asset_id))