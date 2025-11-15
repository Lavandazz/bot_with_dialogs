from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from services.logging_config import bot_logger
from states.menu_state import MainMenuSG


async def go_to_settings(callback: CallbackQuery, button: Button, manager: DialogManager):
    """Переключается на окно настроек"""
    await manager.switch_to(MainMenuSG.settings)


async def close_dialog(callback: CallbackQuery, button: Button, manager: DialogManager):
    """Закрывает весь диалог"""
    await manager.done()
    await manager.start(MainMenuSG.main)
