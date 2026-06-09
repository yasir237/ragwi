from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from models.BaseDataModel import get_db
from controllers.ProjectController import ProjectController
from routes.schemes.data import ProjectCreate, ProjectResponse, ProjectsListResponse
from models.enums.ResponseEnums import ResponseSignal

router = APIRouter(prefix="/api/v1/data")


@router.post("/project", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    controller = ProjectController(db)
    result = await controller.create_project(name=project.name)
    return result


@router.get("/projects", response_model=ProjectsListResponse)
async def get_projects(
    page: int = 1, page_size: int = 10, db: AsyncSession = Depends(get_db)
):
    controller = ProjectController(db)
    projects, total_pages = await controller.get_all_projects(
        page=page, page_size=page_size
    )
    return ProjectsListResponse(projects=projects, total_pages=total_pages, page=page)


@router.delete("/project/{project_id}")
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    controller = ProjectController(db)
    result = await controller.delete_project(project_id=project_id)
    if result == ResponseSignal.PROJECT_NOT_FOUND:
        return {"signal": ResponseSignal.PROJECT_NOT_FOUND}
    return {"signal": ResponseSignal.SUCCESS}
