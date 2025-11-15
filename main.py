import asyncio

from aiogram_dialog import setup_dialogs

from database.register_super_admin import seed_admin
from settings.config import dp, bot
from database.create_db import init_db, close_db
from dialogs.dispatcher import setup_dispatcher
from keyboards.set_menu import set_main_menu
from services.logging_config import bot_logger


async def start_bot(user_id: int = None):
    """
    Запуск бота и регистрация диспетчера, при неудаче бот закроется.
    """
    await set_main_menu(user_id)

    setup_dialogs(dp)
    setup_dispatcher(dp)

    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        bot_logger.warning('Бот закрыт')
        await bot.close()


async def main():
    # Подключаем БД
    await init_db()
    # запись админа в бд
    await seed_admin()

    try:
        await start_bot()
    finally:
        await close_db()  # Закроем БД после завершения всех задач


if __name__ == '__main__':
    try:
        asyncio.run(main())
        bot_logger.info('>>> Бот запускается — main.py загружен!')
    except KeyboardInterrupt:
        bot_logger.warning('Помощник завершены')
