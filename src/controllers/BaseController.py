import os
import uuid
from fastapi import UploadFile
from helpers.config import get_settings

settings = get_settings()

class BaseController:

    def __init__(self, upload_dir: str = "assets"):
        self.upload_dir = upload_dir

    def get_project_path(self, project_uuid: str) -> str:
        path = os.path.join(self.upload_dir, project_uuid)
        os.makedirs(path, exist_ok=True)
        return path

    def is_valid_file(self, file: UploadFile) -> bool:
        return file.content_type in settings.FILE_ALLOWED_TYPES

    def is_valid_size(self, file_size: int) -> bool:
        max_size = settings.FILE_MAX_SIZE * 1024 * 1024
        return file_size <= max_size

    def generate_file_path(self, project_uuid: str, file_name: str) -> str:
        project_path = self.get_project_path(project_uuid)
        return os.path.join(project_path, file_name)