
from aiogram.fsm.state import State, StatesGroup

class AddTask(StatesGroup):
    waiting_text = State()
    waiting_date = State()
    waiting_time = State()