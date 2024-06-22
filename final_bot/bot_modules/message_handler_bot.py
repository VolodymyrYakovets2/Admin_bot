from .dispatcher_bot import dispatcher
from aiogram.types import Message
from .loader import get_photo

@dispatcher.message()
async def message_handler(message: Message):
    if message.text == "/hello":
        # await message.answer(text="hello user ")
        await message.answer_photo(photo= get_photo(file_name= 'orig.png'), caption= 'Moti')