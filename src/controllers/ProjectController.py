import os
from fastapi import UploadFile
from models.ProjectModel import ProjectModel
from models.AssetModel import AssetModel
from models.db_schemes.ragwi.schemes.asset import Asset
from models.enums.ResponseEnums import ResponseSignal
from models.enums.AssetTypeEnum import AssetTypeEnum
from models.enums.ProcessingEnum import ProcessingEnum
from controllers.BaseController import BaseController
from helpers.config import get_settings

settings = get_settings()

class ProjectController(BaseController):

    def __init__(self, db):
        super().__init__()
        self.project_model = ProjectModel(db)
        self.asset_model = AssetModel(db)

    async def create_project(self, name: str):
        project = await self.project_model.get_or_create_project(name=name)
        return project

    async def get_all_projects(self, page: int = 1, page_size: int = 10):
        projects, total_pages = await self.project_model.get_all_projects(
            page=page,
            page_size=page_size
        )
        return projects, total_pages

    async def delete_project(self, project_id: int):
        result = await self.project_model.delete_project(project_id=project_id)
        if not result:
            return ResponseSignal.PROJECT_NOT_FOUND
        return ResponseSignal.SUCCESS

    async def upload_file(self, project_id: int, file: UploadFile):
        project = await self.project_model.get_project(project_id=project_id)
        if not project:
            return None, ResponseSignal.PROJECT_NOT_FOUND

        if not self.is_valid_file(file):
            return None, ResponseSignal.FILE_TYPE_NOT_SUPPORTED

        file_content = await file.read()

        if not self.is_valid_size(len(file_content)):
            return None, ResponseSignal.FILE_SIZE_EXCEEDED

        file_path = self.generate_file_path(
            project_uuid=str(project.uuid),
            file_name=file.filename
        )

        with open(file_path, "wb") as f:
            f.write(file_content)

        asset = Asset(
            project_id=project.id,
            name=file.filename,
            type=file.content_type,
            size=len(file_content),
            path=file_path,
            status=ProcessingEnum.PENDING
        )

        asset = await self.asset_model.create_asset(asset=asset)
        return asset, ResponseSignal.FILE_UPLOAD_SUCCESS