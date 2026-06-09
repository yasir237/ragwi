from pydantic import BaseModel
from typing import Optional, List
import uuid

class ProjectCreate(BaseModel):
    name: str

class ProjectResponse(BaseModel):
    id: int
    uuid: uuid.UUID
    name: str

    class Config:
        from_attributes = True

class ProjectsListResponse(BaseModel):
    projects: List[ProjectResponse]
    total_pages: int
    page: int