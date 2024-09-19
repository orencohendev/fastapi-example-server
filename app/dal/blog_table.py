import uuid
from sqlalchemy import UUID, Column, String, Text, DateTime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Blog(Base): # type: ignore
    __tablename__ = "blog"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    title = Column(String(255))
    content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
