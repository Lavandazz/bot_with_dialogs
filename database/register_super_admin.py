from tortoise.exceptions import IntegrityError

from database.models_db import Role, UserRole, User
from services.logging_config import bot_logger
from settings.settings_env import settings


async def seed_admin():
    """
    Функция для создания супер-админа при старте приложения.
    Если супер админа нет, то создается роль и регистрируется пользователь из .env
    """
    try:
        admin_role, created = await Role.get_or_create(role='superAdmin')
        super_admin = await UserRole.filter(role=admin_role).exists()

        if not super_admin:
            user = await User.create(
                username=settings.SUPERUSER,
                first_name=settings.SUPER_NAME,
                telegram_id=settings.SUPER_ADMIN,
            )
            # связь пользователя с ролью
            await UserRole.create(role=admin_role, user=user)
            bot_logger.info("Администратор зарегистрирован")

    except IntegrityError:
        bot_logger.info("Админ уже существует, пропускаем создание")

    except Exception as e:
        bot_logger.exception(f'Ошибка при создании админа {e}')
