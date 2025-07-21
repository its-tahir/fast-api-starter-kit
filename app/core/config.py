from pydantic_settings import BaseSettings
import logging

logger = logging.getLogger("instaserve-ai")

class Settings(BaseSettings):
    PROJECT_NAME: str = 'instaserve-ai'
    DEBUG: bool = True
    VERSION: str = '0.1.0'
    RATE_LIMIT: str = '10/second'

    class Config:
        env_file = ".env"

settings = Settings() 