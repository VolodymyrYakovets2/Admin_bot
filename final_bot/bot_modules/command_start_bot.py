from aiogram.filters import CommandStart
from .dispatcher_bot import dispatcher
from aiogram.types import Message

@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text= "Привіт, користувач")