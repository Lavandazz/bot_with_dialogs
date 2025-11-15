from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from .settings_env import settings


def bot_config():
    """Настройка бота"""
    redis_client_ = Redis(host=settings.REDIS_HOST,
                          port=settings.REDIS_PORT,
                          db=settings.REDIS_DB,
                          password=settings.REDIS_PASSWORD,
                          decode_responses=True)  # чтобы строки были не в байтах

    storage = RedisStorage(redis=redis_client_,
                           key_builder=DefaultKeyBuilder(with_destiny=True))
    # storage = MemoryStorage()
    # Объекты бота
    bot_ = Bot(
        token=settings.BOT_TOKEN,
        session=AiohttpSession(),
        default=DefaultBotProperties(parse_mode="HTML")
    )

    # Храним состояния в Redis
    dp_ = Dispatcher(storage=storage)

    return bot_, dp_, redis_client_


bot, dp, rd = bot_config()
