from pydantic import BaseSettings, Field, validator
from typing import List


class Settings(BaseSettings):
    postgres_db: str = Field(..., env="POSTGRES_DB")
    postgres_user: str = Field(..., env="POSTGRES_USER")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    secret_key: str = Field(..., env="SECRET_KEY")
    env: str = Field("development", env="ENV")
    debug: bool = Field(True, env="DEBUG")
    allowed_hosts: List[str] = Field(default_factory=list, env="ALLOWED_HOSTS")
    api_url: str = Field(..., env="API_URL")
    database_url: str = Field(..., env="DATABASE_URL")

    @validator("allowed_hosts", pre=True)
    def split_allowed_hosts(cls, v):
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
