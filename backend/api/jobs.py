from fastapi import APIRouter
from celery.result import AsyncResult
from app.workers.celery_app import celery_app

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/{job_id}")
def job_status(job_id: str):
    task = AsyncResult(job_id, app=celery_app)
    return {
        "id": job_id,
        "status": task.state,
        "result": task.result if task.ready() else None
    }
