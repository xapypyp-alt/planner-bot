import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from datetime import date, timedelta

from src.config import BOT_TOKEN
from src.database import init_db
from src.database import add_task
from src.database import get_tasks
from src.scheduler import start_scheduler, add_reminder
from src.keyboards import main_keyboard, date_keyboard, time_keyboard
from src.states import AddTask

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Я бот-ежедневник 📒",
        reply_markup=main_keyboard
    )

@dp.message(F.text == "➕ Добавить задачу")
async def add_task_start(message: Message, state: FSMContext):
    await message.answer("Введите текст задачи:")
    await state.set_state(AddTask.waiting_text)

@dp.message(AddTask.waiting_text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Выберите дату:", reply_markup=date_keyboard)
    await state.set_state(AddTask.waiting_date)

@dp.message(AddTask.waiting_date)
async def get_date(message: Message, state: FSMContext):
    if message.text == "📅 Сегодня":
        task_date = date.today()
    else:
        task_date = date.today() + timedelta(days=1)

    await state.update_data(date=str(task_date))
    await message.answer("Выберите время:", reply_markup=time_keyboard)
    await state.set_state(AddTask.waiting_time)

@dp.message(AddTask.waiting_time)
async def get_time(message: Message, state: FSMContext):
    time_str = message.text.replace("⏰", "").strip()
    data = await state.get_data()
    remind_at = f"{data['date']} {time_str}"

    await add_task(message.from_user.id, data["text"], remind_at)
    add_reminder(bot, message.from_user.id, data["text"], remind_at)

    await message.answer("✅ Задача добавлена", reply_markup=main_keyboard)
    await state.clear()

@dp.message(F.text == "📋 Мои дела")
async def show_tasks(message: Message):
    tasks = await get_tasks(message.from_user.id)
    if not tasks:
        await message.answer("Нет задач")
        return

    text = "📋 Ваши задачи:\n"
    for task in tasks:
        text += f"• {task[0]} — {task[1]}\n"
    await message.answer(text)

async def main():
    await init_db()
    start_scheduler()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
