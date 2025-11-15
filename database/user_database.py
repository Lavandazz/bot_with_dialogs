from dataclasses import dataclass

from database.models_db import User
from services.logging_config import db_logger


@dataclass
class UserDatabase:
    """Класс для работы с пользователями в БД"""
    telegram_id: int

    async def create_user(self, telegram_id: int, username: str, first_name: str):
        """Добавление юзера в бд"""
        try:
            # возвращаем объект для дальнейшего использования
            return await User.create(
                telegram_id=telegram_id,
                username=username,
                first_name=first_name
            )

        except Exception as e:
            db_logger.exception(f"Ошибка регистрации пользователя {e}")
