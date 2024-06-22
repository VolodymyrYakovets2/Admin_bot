
from .create_bot import bot
from .dispatcher_bot import dispatcher
async def main():
    await dispatcher.start_polling(bot)