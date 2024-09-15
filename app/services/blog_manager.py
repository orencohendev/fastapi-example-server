
from uuid import UUID
from pydantic import BaseModel
from app.dal.blog_db_repository import BlogDBRepository


class BlogPostModel(BaseModel):
    id: UUID | None = None
    title: str
    content: str

    class Config:
        orm_mode = True

class BlogManager:
    
    blog_repository = BlogDBRepository()

    @staticmethod
    async def create_post(blog):

        db_blog = BlogPostModel(title=blog.title, content=blog.content, id=blog.id)

        res = await BlogManager.blog_repository.insert(db_blog)
        return res
    
    @staticmethod
    async def get_post(blog_id):
        return await BlogManager.blog_repository.get(blog_id)
    
    @staticmethod
    def get_all_posts():
        return BlogManager.blog_repository.get_all()
    
    @staticmethod
    def update_post(blog_id, blog):
        return BlogManager.blog_repository.update(blog_id, blog)
    
    @staticmethod
    def delete_post(blog_id):
        return BlogManager.blog_repository.delete(blog_id)
    
    @staticmethod
    def delete_all_posts():
        return BlogManager.blog_repository.delete_all()
    