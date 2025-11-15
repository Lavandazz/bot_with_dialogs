from aiogram.filters.state import State, StatesGroup


class MainMenuSG(StatesGroup):
    main = State()
    settings = State()
    profile = State()
