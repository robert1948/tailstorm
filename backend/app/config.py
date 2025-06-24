from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List


class Settings(BaseSettings):
    postgres_db: str = Field(..., alias="POSTGRES_DB")
    postgres_user: str = Field(..., alias="POSTGRES_USER")
    postgres_password: str = Field(..., alias="POSTGRES_PASSWORD")
    secret_key: str = Field(..., alias="SECRET_KEY")
    env: str = Field(default="development", alias="ENV")
    debug: bool = Field(default=True, alias="DEBUG")
    allowed_hosts: List[str] = Field(default_factory=list, alias="ALLOWED_HOSTS")
    api_url: str = Field(..., alias="API_URL")
    database_url: str = Field(..., alias="DATABASE_URL")

    # ✅ Allows comma-separated ALLOWED_HOSTS string from Heroku/Env
    @field_validator("allowed_hosts", mode="before")
    @classmethod
    def split_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",         # ✅ fallback for local development
        case_sensitive=False     # ✅ flexible for env var casing
    )


# ✅ Create the singleton instance
settings = Settings()
