from uuid import UUID
from pydantic import BaseModel


class BlogPostModel(BaseModel):
    id: UUID | None = None
    title: str
    content: str

    class Config:
        from_attributes = True
