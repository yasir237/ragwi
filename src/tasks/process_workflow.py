from celery import chain
from celery_app import celery_app
from tasks.file_processing import process_file
from tasks.data_indexing import index_chunks

@celery_app.task
def process_and_index(asset_id: int):
    workflow = chain(
        process_file.s(asset_id),
        index_chunks.si(asset_id)  # .si() önceki sonucu almaz
    )
    workflow.apply_async()