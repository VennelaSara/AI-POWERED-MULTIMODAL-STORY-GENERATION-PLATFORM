from app.models.story import Story
from sqlalchemy.orm import Session


def save_story(db: Session, prompt: str, content: str):
    story = Story(prompt=prompt, content=content)
    db.add(story)
    db.commit()
    db.refresh(story)
    return story
