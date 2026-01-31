from sqlalchemy import Column, Integer, String
from app.models.db import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    task_id = Column(String, unique=True, index=True)
    status = Column(String, default="PENDING")
