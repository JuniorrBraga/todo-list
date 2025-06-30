from . import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Task(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow)