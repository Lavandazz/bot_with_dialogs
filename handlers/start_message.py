from aiogram import Router

from settings.config import bot
from settings.settings_env import settings

start_router = Router()


@start_router.startup()
async def on_start():
    """
    Отправка сообщения о старте супер-админу
    """
    await bot.send_message(chat_id=settings.SUPER_ADMIN, text='Я запустил бота, /start')
