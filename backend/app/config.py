import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "CapeControl"
    FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
    CORS_ORIGIN = os.getenv("CORS_ORIGIN")
    SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
    DATABASE_URL = os.getenv("DATABASE_URL")

    @property
    def cors_origins(self):
        if self.CORS_ORIGIN == "*":
            return ["*"]
        return [self.FRONTEND_ORIGIN]

settings = Settings()
