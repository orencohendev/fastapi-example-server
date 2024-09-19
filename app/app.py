import logging
from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from app.dal.blog_db_repository import BlogDBRepository
from app.conf import settings
from app.handlers import blog_router, health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting up")

    blog_db_repository = BlogDBRepository()
    await blog_db_repository.create_tables()


    try:
        yield
    finally:
        logging.info("Shutting down")


app = FastAPI(
    title=settings.app_name,
    openapi_url="/blog/docs/openapi.json",
    redoc_url="/blog/docs/redoc",
    docs_url="/blog/docs/swagger",
    lifespan=lifespan,
)

app.include_router(health_router.health_router)
app.include_router(blog_router.blog_router)



if __name__ == "__main__":
    uvicorn.run(
        "app.app:app", host="0.0.0.0", port=settings.app_port, reload=settings.is_dev
    )
