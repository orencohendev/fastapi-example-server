from uuid import UUID
from app.dal.blog_db_repository import BlogDBRepository
from app.services.service_models.blog_post_model import BlogPostModel




class BlogManager:
    
    blog_repository = BlogDBRepository()

    @staticmethod
    async def create_post(blog: BlogPostModel):

        res = await BlogManager.blog_repository.insert(blog)
        return res
    
    @staticmethod
    async def get_post(blog_id: UUID):
        return await BlogManager.blog_repository.get(blog_id)
    
    @staticmethod
    async def get_all_posts():
        return await BlogManager.blog_repository.get_all()
    
    @staticmethod
    async def update_post(blog_id, blog):
        return await BlogManager.blog_repository.update(blog_id, blog)
    
    @staticmethod
    async def delete_post(blog_id):
        return await BlogManager.blog_repository.delete(blog_id)
    
    @staticmethod
    def delete_all_posts():
        return BlogManager.blog_repository.delete_all()
    