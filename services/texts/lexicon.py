from aiogram_dialog.widgets.text import Const

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Старт бота',
    '/help': 'Справка по работе бота'
}

additional = Const(
    "Here is some additional text, which is visible only in extended mode",
    when="extended",
)
