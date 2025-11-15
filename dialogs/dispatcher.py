from aiogram import Dispatcher

from dialogs.checkbox_widgets import main_menu_dialog, help_menu_dialog
from dialogs.common import common_router
from handlers.start_message import start_router


def setup_dispatcher(dp: Dispatcher):
    """ Регистрация routers бота """

    dp.include_router(common_router)

    dp.include_router(start_router)
    dp.include_router(main_menu_dialog)
    dp.include_router(help_menu_dialog)

    return dp
