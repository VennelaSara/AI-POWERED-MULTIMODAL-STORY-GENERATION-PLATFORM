from sqlalchemy.orm import Session
from app.models.character import Character


def create_character(db: Session, name: str, description: str):
    character = Character(name=name, description=description)
    db.add(character)
    db.commit()
    db.refresh(character)
    return character


def list_characters(db: Session):
    return db.query(Character).all()
