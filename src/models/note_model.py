from sqlalchemy import Column, String, DateTime, Integer
from src.database.base import Base
from datetime import datetime, timezone
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class NoteModel(Base):
    __tablename__ = 'note'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user = Column(UUID(as_uuid=True), nullable=False)
    note = Column(String(), nullable=False)
    createdAt = Column(DateTime(), default=datetime.now(timezone.utc) )
    updateAt = Column(DateTime(), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc) )