# backend/app/config.py
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# ✅ Path to backend/.env regardless of where uvicorn is run from
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    PROJECT_NAME: str = "CapeControl"
    SECRET_KEY: str
    ENV: str = "production"
    DEBUG: bool = False
    ALLOWED_HOSTS: list[str] = ["localhost"]
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        case_sensitive = True

    # Validator to support comma-separated ALLOWED_HOSTS in .env
    @classmethod
    def validate_allowed_hosts(cls, value):
        if isinstance(value, str):
            return [host.strip() for host in value.split(",") if host.strip()]
        return value

    def __init__(self, **values):
        if 'ALLOWED_HOSTS' in values:
            values['ALLOWED_HOSTS'] = self.validate_allowed_hosts(values['ALLOWED_HOSTS'])
        super().__init__(**values)

settings = Settings()
