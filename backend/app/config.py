import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CapeControl"

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    @property
    def db_url(self):
        # Heroku provides 'postgres://...' which SQLAlchemy doesn't like
        return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)

    cors_origins: list[str] = ["*"]  # Update with actual CORS if needed

settings = Settings()
