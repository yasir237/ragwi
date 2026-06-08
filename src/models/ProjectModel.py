from sqlalchemy.ext.asyncio import AsyncSession
from models.db_schemes.ragwi.schemes import Project
from sqlalchemy.future import select

class ProjectModel:

    def __init__(self, db: AsyncSession):
        self.db = db



    async def create_proejct(self, name:str):
        project = Project(name=name)
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project
    

    async def get_project(self, project_id: int):
        result = self.db.execute(
             select(Project).where(Project.id == project_id)
        )

        return result.scalar_one_or_none()
    

    async def get_or_create_project(self, name:str):
        result = self.db.execute(
            select(Project).where(Project.name == name)
        )

        project = result.scalar_one_or_none()

        if project is None:
            project = await self.create_proejct(project_id)
