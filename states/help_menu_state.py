from aiogram.filters.state import State, StatesGroup


class HelpMenuSG(StatesGroup):
    main = State()
    answer = State()
