from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasmdagi matnni o'zbek tiliga tarjima qilish")
        ],
        [
            KeyboardButton(text="Texni o'zbek tiliga tarjima qilish")
        ],
[
            KeyboardButton(text="Chatgpt bilan suhbatlashish")
        ],
    ],
    resize_keyboard=True
)