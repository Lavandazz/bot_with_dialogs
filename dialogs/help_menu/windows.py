from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Back, Group
from aiogram_dialog.widgets.text import Const, Format

from dialogs.help_menu.help_dialog import go_to_answer
from dialogs.main_menu.user_dialog import close_dialog
from services.texts.help_menu_text import questions
from states.help_menu_state import HelpMenuSG


def create_help_window():
    # Создаем кнопки с вопросами динамически
    question_buttons = []
    for question_id, question_data in questions.items():
        button = Button(
            Const(question_data["text"]),
            id=question_id,  # уникальный ID для каждой кнопки
            on_click=go_to_answer
        )
        question_buttons.append(button)

    # Группируем кнопки (по 1 в ряд)
    keyboard = Group(*question_buttons, width=2)

    return Window(
        Const("⁉️ Часто задаваемые вопросы ⁉️"),
        keyboard,
        Button(Const("❌ Закрыть"), id="close", on_click=close_dialog),
        state=HelpMenuSG.main,
    )


answer_window = Window(
    Format("❓ Вопрос: {dialog_data[question_text]}\n\n💡 Ответ: {dialog_data[current_answer]}"),
    Back(Const("← Назад к вопросам")),
    state=HelpMenuSG.answer,
)
