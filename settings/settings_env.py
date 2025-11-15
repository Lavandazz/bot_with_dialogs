from pathlib import Path

from pydantic_settings import BaseSettings


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROD = "production"  # local


class Settings(BaseSettings):
    # Настройки бота
    BOT_TOKEN: str
    SUPER_ADMIN: str
    SUPER_NAME: str
    SUPERUSER: str

    # Настройки Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_PASSWORD: str

    # Настройки Postgres
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int


def get_settings() -> Settings:
    """Получаем настройки зависимости от env"""
    env = "production"
    env_file = ".env" if env == "production" else ".env_local"
    env_path = PROJECT_ROOT / env_file
    return Settings(_env_file=env_path)


settings = get_settings()
