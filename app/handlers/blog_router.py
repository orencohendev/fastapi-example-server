from uuid import UUID
from fastapi.routing import APIRouter
from app.handlers.api_models.new_blog_post_api_model import NewBlogPostAPIModel
from app.mappers.blog_post_api_model_to_service_model import (
    blog_post_api_model_to_service_model,
)
from app.services.blog_manager import BlogManager

blog_router = APIRouter(prefix="/blog")


@blog_router.get("")
async def get_all_blogs():
    return await BlogManager.get_all_posts()


@blog_router.get("/{blog_id}")
async def get_blog(blog_id: UUID):
    return await BlogManager.get_post(blog_id)


@blog_router.post("")
async def create_blog(blog_post: NewBlogPostAPIModel):
    service_model = blog_post_api_model_to_service_model(blog_post)
    return await BlogManager.create_post(service_model)


@blog_router.put("/{blog_id}")
async def update_blog(blog_id: UUID, blog_post: NewBlogPostAPIModel):
    return await BlogManager.update_post(blog_id, blog_post)


@blog_router.delete("/{blog_id}")
async def delete_blog(blog_id: UUID):
    return await BlogManager.delete_post(blog_id)
