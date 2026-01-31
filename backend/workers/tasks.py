from app.workers.celery_app import celery_app
from app.services.generation_pipeline import generate_full_story


@celery_app.task(bind=True)
def generate_story_job(self, prompt: str):
    self.update_state(state="PROGRESS", meta={"step": "Generating story"})
    return generate_full_story(prompt)
