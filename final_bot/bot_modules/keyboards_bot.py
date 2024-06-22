import aiogram 
from .buttons_bot import button_start

main_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard= [[button_start]],
    one_time_keyboard= True
)