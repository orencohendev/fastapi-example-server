from uuid import UUID
from pydantic import BaseModel


class NewBlogPostAPIModel(BaseModel):
    id: UUID | None = None
    title: str
    content: str
