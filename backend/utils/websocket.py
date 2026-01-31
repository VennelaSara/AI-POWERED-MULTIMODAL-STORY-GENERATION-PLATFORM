from fastapi import APIRouter, WebSocket
from celery.result import AsyncResult
import asyncio
from app.workers.celery_app import celery

router = APIRouter()

@router.websocket("/ws/{task_id}")
async def websocket_job(ws: WebSocket, task_id: str):
    await ws.accept()
    while True:
        task = AsyncResult(task_id, app=celery)
        await ws.send_json({
            "state": task.state,
            "info": task.info
        })
        await asyncio.sleep(2)
