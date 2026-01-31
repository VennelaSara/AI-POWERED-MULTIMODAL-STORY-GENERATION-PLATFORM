from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.dependencies import get_db
from app.services.character_service import create_character, list_characters

router = APIRouter(prefix="/characters", tags=["Characters"])


class CharacterCreate(BaseModel):
    name: str
    description: str


@router.post("/")
def create(payload: CharacterCreate, db: Session = Depends(get_db)):
    return create_character(db, payload.name, payload.description)


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return list_characters(db)
