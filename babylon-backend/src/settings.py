import logging
from pydantic_settings import BaseSettings
from enum import Enum
logger = logging.getLogger(__name__)

class Env(Enum):
    local = "local"
    sit = "sit"
    uat = "uat"
    prod = "prod"

class Settings(BaseSettings):
    env: Env
    ollama_host: str

try:
    settings = Settings(_env_file=".env") # type: ignore
except Exception as ex:
    logger.error(f"Exception loading environment variables: {ex}", exc_info=True)
    exit()

__all__ = ["settings"]
