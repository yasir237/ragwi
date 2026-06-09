from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from models.db_schemes.ragwi.schemes.asset import Asset

class AssetModel:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_asset(self, asset: Asset):
        self.db.add(asset)
        await self.db.commit()
        await self.db.refresh(asset)
        return asset

    async def get_asset(self, asset_id: int):
        result = await self.db.execute(
            select(Asset).where(Asset.id == asset_id)
        )
        return result.scalar_one_or_none()

    async def get_all_assets(self, project_id: int, page: int = 1, page_size: int = 10):
        total = await self.db.execute(
            select(func.count(Asset.id)).where(Asset.project_id == project_id)
        )
        total_count = total.scalar_one()

        total_pages = total_count // page_size
        if total_count % page_size > 0:
            total_pages += 1

        result = await self.db.execute(
            select(Asset)
            .where(Asset.project_id == project_id)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        assets = result.scalars().all()

        return assets, total_pages

    async def update_asset_status(self, asset_id: int, status: str):
        asset = await self.get_asset(asset_id)
        if asset:
            asset.status = status
            await self.db.commit()
            await self.db.refresh(asset)
            return asset
        return None

    async def delete_asset(self, asset_id: int):
        asset = await self.get_asset(asset_id)
        if asset:
            await self.db.delete(asset)
            await self.db.commit()
            return True
        return False