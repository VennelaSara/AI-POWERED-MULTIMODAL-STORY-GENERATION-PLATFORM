from fastapi import FastAPI
from app.api import story, character, jobs
from app.utils.websocket import router as ws_router

app = FastAPI(title="Multimodal Story Generation Platform")

app.include_router(story.router, prefix="/api/story")
app.include_router(character.router, prefix="/api/character")
app.include_router(jobs.router, prefix="/api/jobs")
app.include_router(ws_router)

@app.get("/")
def health():
    return {"status": "running"}
