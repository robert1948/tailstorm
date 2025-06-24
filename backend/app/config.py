from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import List


class Settings(BaseSettings):
    postgres_db: str = Field(..., alias="POSTGRES_DB")
    postgres_user: str = Field(..., alias="POSTGRES_USER")
    postgres_password: str = Field(..., alias="POSTGRES_PASSWORD")
    secret_key: str = Field(..., alias="SECRET_KEY")
    env: str = Field("development", alias="ENV")
    debug: bool = Field(True, alias="DEBUG")
    allowed_hosts_raw: str = Field("", alias="ALLOWED_HOSTS")
    api_url: str = Field(..., alias="API_URL")
    database_url: str = Field(..., alias="DATABASE_URL")

    @property
    def allowed_hosts(self) -> List[str]:
        return [h.strip() for h in self.allowed_hosts_raw.split(",") if h.strip()]

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()
