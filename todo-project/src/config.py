from functools import lru_cache
import logging

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading settings...")
    return Settings()
