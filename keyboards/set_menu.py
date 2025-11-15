from aiogram.types import BotCommand, BotCommandScopeDefault

from settings.config import bot
from services.logging_config import bot_logger
from services.texts.lexicon import LEXICON_COMMANDS


async def set_main_menu(user_id: int = None):
    """
    Команды start и help
    """

    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS.items()
    ]

    # Устанавливаем команды по умолчанию
    await bot.set_my_commands(main_menu_commands, scope=BotCommandScopeDefault())
    bot_logger.debug('Установил команды')
