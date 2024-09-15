from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    items_per_user: int = 50
    is_dev: bool = True
    app_port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()
