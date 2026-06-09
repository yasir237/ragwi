from enum import Enum

class ResponseSignal(str, Enum):
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    PROJECT_NOT_FOUND = "project_not_found"
    PROJECT_CREATED = "project_created"
    SUCCESS = "success"
    FAILED = "failed"