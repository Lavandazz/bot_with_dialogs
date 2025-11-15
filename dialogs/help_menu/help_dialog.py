from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from services.logging_config import bot_logger
from services.texts.help_menu_text import questions
from states.help_menu_state import HelpMenuSG


async def go_to_answer(callback: CallbackQuery, button: Button, manager: DialogManager):
    """Переключается на окно с вопросами о боте"""
    question_id = button.widget_id
    answer_text = questions[question_id]["answer"]
    # Сохраняем ответ в данные диалога
    manager.dialog_data["current_answer"] = answer_text
    manager.dialog_data["question_text"] = questions[question_id]["text"]

    bot_logger.debug(f"dialog_data: {manager.dialog_data}")
    bot_logger.debug(f"answer_text:, {answer_text}")

    await manager.switch_to(HelpMenuSG.answer)
