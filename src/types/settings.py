from pydantic import BaseSettings

from src.types import PostgresDsn


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
