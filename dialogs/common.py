from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager

from states.help_menu_state import HelpMenuSG
from states.menu_state import MainMenuSG

common_router = Router()


@common_router.message(CommandStart())
async def get_start(message: Message, dialog_manager: DialogManager):
    """Команда /start."""
    # Передать из messsage пользователя в редис и зарегить в бд
    await dialog_manager.start(MainMenuSG.main)


@common_router.message(Command("help"))
async def help_command(message: Message, dialog_manager: DialogManager):
    """Обработчик команды /help"""
    await dialog_manager.start(HelpMenuSG.main)
