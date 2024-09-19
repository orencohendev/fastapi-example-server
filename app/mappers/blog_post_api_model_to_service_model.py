from app.services.service_models.blog_post_model import BlogPostModel
from app.handlers.api_models.new_blog_post_api_model import NewBlogPostAPIModel

def blog_post_api_model_to_service_model(api_model: NewBlogPostAPIModel) -> BlogPostModel:
    return BlogPostModel(title=api_model.title, content=api_model.content, id=api_model.id)
