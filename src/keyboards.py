from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Добавить задачу")],
        [KeyboardButton(text="📋 Мои дела")]
    ],
    resize_keyboard=True
)

date_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Сегодня"), KeyboardButton(text="📅 Завтра")],
    ],
    resize_keyboard=True
)

time_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⏰ 09:00"), KeyboardButton(text="⏰ 12:00")],
        [KeyboardButton(text="⏰ 18:00")],
    ],
    resize_keyboard=True
)
