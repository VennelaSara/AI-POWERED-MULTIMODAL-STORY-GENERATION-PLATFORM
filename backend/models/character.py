from sqlalchemy import Column, Integer, String, JSON
from app.models.db import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    traits = Column(JSON)
