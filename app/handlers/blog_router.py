from uuid import UUID
from fastapi.routing import APIRouter
from app.handlers.api_models.new_blog_post_api_model import NewBlogPostAPIModel
from app.services.blog_manager import BlogManager

blog_router = APIRouter()

@blog_router.get("/blog")
def get_all_blogs():
    return BlogManager.get_all_posts()

@blog_router.get("/blog/{blog_id}")
async def get_blog(blog_id: UUID):
    return await BlogManager.get_post(blog_id)

@blog_router.post("/blog")
async def create_blog(blog_post: NewBlogPostAPIModel):
    return await BlogManager.create_post(blog_post)

@blog_router.put("/blog/{blog_id}")
def update_blog(blog_id: UUID, blog_post: NewBlogPostAPIModel):
    return BlogManager.update_post(blog_id, blog_post)

@blog_router.delete("/blog/{blog_id}")
def delete_blog(blog_id: UUID):
    return BlogManager.delete_post(blog_id)

