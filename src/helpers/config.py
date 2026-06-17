from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    DATABASE_URL: str

    FILE_ALLOWED_TYPES: list 
    FILE_MAX_SIZE: int 
    FILE_DEFAULT_CHUNK_SIZE: int


    GROQ_API_KEY: str
    GROQ_MODEL: str
    OLLAMA_BASE_URL: str
    OLLAMA_MODEL: str
    OLLAMA_EMBEDDING_MODEL: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
