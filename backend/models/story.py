from sqlalchemy import Column, Integer, String, JSON
from app.models.db import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(JSON)
