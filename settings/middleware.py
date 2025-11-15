from aiogram.types import TelegramObject
from redis.asyncio import Redis
from aiogram import BaseMiddleware
from typing import Callable, Dict, Any
from datetime import date, datetime

from database.models_db import User
