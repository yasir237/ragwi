from models.ProjectModel import ProjectModel
from sqlalchemy.ext.asyncio import AsyncSession
from models.enums import ResponseSignal


class ProjectController:

    def __init__(self, db: AsyncSession):
        self.project_model = ProjectModel(db=db)

    async def create_project(self, name:str):
        project = await self.project_model.get_or_create_project(name)
        return project
    
    async def get_all_projects(self, page:int = 1,  page_size: int = 10):
        projects, total_pages = await self.project_model.get_all_projects(page=page,page_size=page_size)
        return projects, total_pages
    
    async def delete_project(self, project_id: int):
        result = self.project_model.delete_project(project_id=project_id)
        if not result:
            return ResponseSignal.PROJECT_NOT_FOUND
        return ResponseSignal.SUCCESS
