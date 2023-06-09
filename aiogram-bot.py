import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor

load_dotenv()

bot = Bot(os.getenv("API_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Hello!')
    # await message.reply('Hello!!!')
    # await bot.send_message(message.from_user.id, 'HELLO!')


executor.start_polling(dp, skip_updates=True)
