from aiogram_dialog import Dialog

from dialogs.help_menu.windows import create_help_window, answer_window
from dialogs.main_menu.windows import main_window, settings_window

main_menu_dialog = Dialog(
    main_window,
    settings_window,
)

help_menu_dialog = Dialog(
    create_help_window(),
    answer_window,
)