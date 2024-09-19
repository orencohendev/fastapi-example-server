import datetime
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select

from sqlalchemy.orm import scoped_session, sessionmaker
from app.dal.blog_table import Blog
from sqlalchemy.ext.asyncio import AsyncSession


class BlogDBRepository:
    def __init__(self):

        database_url = f"postgresql+asyncpg://blog:blog@localhost:5432/blog"

        self.engine = create_async_engine(database_url, **dict())
        self.session = scoped_session(sessionmaker(bind=self.engine))

    async def create_tables(self):
        from app.dal.blog_table import Base

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    def drop_tables(self):
        from app.dal.blog_table import Base

        Base.metadata.drop_all(self.engine)

    def get_session(self):
        return self.session

    def close(self):
        self.session.remove()
        self.engine.dispose()

    async def insert(self, blog):
        timestamp = datetime.datetime.now()
        db_obj = Blog(
            title=blog.title,
            content=blog.content,
            id=blog.id,
            created_at=timestamp,
            updated_at=timestamp,
        )
        async with AsyncSession(self.engine) as async_session:
            async_session.add(db_obj)
            await async_session.commit()
            await async_session.refresh(db_obj)
        return db_obj

    async def get(self, blog_id):
        async with AsyncSession(self.engine) as async_session:
            return await async_session.get(Blog, blog_id)

    async def get_all(self):
        async with AsyncSession(self.engine) as async_session:
            result = await async_session.execute(select(Blog))
            return result.scalars().all()

    async def update(self, blog_id, blog):
        async with AsyncSession(self.engine) as async_session:
            db_obj = await async_session.get(Blog, blog_id)
            db_obj.title = blog.title
            db_obj.content = blog.content
            db_obj.updated_at = datetime.datetime.now()
            await async_session.commit()
            await async_session.refresh(db_obj)
            return db_obj

    async def delete(self, blog_id):
        async with AsyncSession(self.engine) as async_session:
            blog = await async_session.get(Blog, blog_id)
            await async_session.delete(blog)
            await async_session.commit()
            return blog
