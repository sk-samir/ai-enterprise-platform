from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    # =========================
    # OLLAMA CONFIG
    # =========================

    OLLAMA_MODEL: str

    # =========================
    # MYSQL CONFIG
    # =========================

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str

    # =========================
    # MONGODB CONFIG
    # =========================

    MONGO_URI: str
    MONGO_DATABASE: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()