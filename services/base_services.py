from database.models_db import User
from services.logging_config import db_logger


class BaseUserService:
    """Сервис для работы с пользователями"""

    def __init__(self):
        self.model = User

    async def get_user(self, telegram_id: int) -> User:
        """Получить пользователя по telegram_id"""
        return await self.model.filter(telegram_id=telegram_id).first()

    async def user_exists(self, telegram_id: int) -> bool:
        """Проверить существование пользователя"""
        return await self.model.filter(telegram_id=telegram_id).exists()

    async def validate(self, telegram_id: int, *args, **kwargs):
        """Базовая валидация"""
        if not await self.user_exists(telegram_id):
            raise ValueError("Пользователь не найден")
        return True
