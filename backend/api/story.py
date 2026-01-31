from fastapi import APIRouter
from pydantic import BaseModel
from app.workers.tasks import generate_story_job

router = APIRouter(prefix="/stories", tags=["Stories"])


class StoryRequest(BaseModel):
    prompt: str


@router.post("/")
def create_story(payload: StoryRequest):
    task = generate_story_job.delay(payload.prompt)
    return {"job_id": task.id}
