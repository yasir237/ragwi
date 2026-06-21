from celery import Celery
from helpers.config import get_settings

settings = get_settings()

celery_app = Celery(
    "ragwi",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=[
        "tasks.file_processing",
        "tasks.data_indexing",
        "tasks.process_workflow"
    ]
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)