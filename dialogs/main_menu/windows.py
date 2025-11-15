from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Back
from aiogram_dialog.widgets.text import Const

from dialogs.main_menu.user_dialog import go_to_settings
from states.menu_state import MainMenuSG

main_window = Window(
    Const("🏠 Главное меню"),
    Row(
        Button(Const("⚙️ Настройки"), id="settings", on_click=go_to_settings),
        Button(Const("👤 Профиль"), id="profile"),
    ),
    state=MainMenuSG.main,
)

settings_window = Window(
    Const("⚙️ Настройки"),
    Back(Const("← Назад")),  # Спец кнопка назад
    state=MainMenuSG.settings,
)

