import os
import json
import string

from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv

load_dotenv()

bot = Bot(os.getenv("API_TOKEN"))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Your bot is online')


#   CLIENT PART
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome to BotPizza and bon appetit!')
        await message.delete()
    except:
        await message.reply('Please ask our bot! Send it a message: https://t.me/its_not_a_pizza_bot')


@dp.message_handler(commands=['working_hours'])
async def work_hours(message: types.Message):
    await bot.send_message(message.from_user.id, 'We are open Mon-Fri 09:00 to 18:00')


@dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    await bot.send_message(message.from_user.id, 'We are located on Tiraspols\'ska st. 2')


#   ADMIN PART


#   COMMON PART


@dp.message_handler()
async def profanity_filter(message: types.Message):
    profanity_words_list = json.load(open('profanity_filter/profanity.json'))

    if {
        word.lower().translate(str.maketrans('', '', string.punctuation))
        for word in message.text.split(' ')
    }.intersection(set(profanity_words_list)):
        await message.reply('Profanity is forbidden!')
        await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
