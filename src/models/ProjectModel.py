from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from models.db_schemes.ragwi.schemes.project import Project

class ProjectModel:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_project(self, name: str):
        project = Project(name=name)
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project

    async def get_or_create_project(self, name: str):
        result = await self.db.execute(
            select(Project).where(Project.name == name)
        )
        project = result.scalar_one_or_none()

        if project is None:
            project = await self.create_project(name=name)

        return project

    async def get_project(self, project_id: int):
        result = await self.db.execute(
            select(Project).where(Project.id == project_id)
        )
        return result.scalar_one_or_none()

    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        total = await self.db.execute(
            select(func.count(Project.id))
        )
        total_count = total.scalar_one()

        total_pages = total_count // page_size
        if total_count % page_size > 0:
            total_pages += 1

        result = await self.db.execute(
            select(Project)
            .offset((page - 1) * page_size)
            .limit(page_size)
        )
        projects = result.scalars().all()

        return projects, total_pages

    async def delete_project(self, project_id: int):
        project = await self.get_project(project_id)
        if project:
            await self.db.delete(project)
            await self.db.commit()
            return True
        return False