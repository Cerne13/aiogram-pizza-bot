from aiogram import types, Dispatcher
from create_bot import bot


# @dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome to BotPizza and bon appetit!')
        await message.delete()
    except:
        await message.reply('Please ask our bot! Send it a message: https://t.me/its_not_a_pizza_bot')


# @dp.message_handler(commands=['working_hours'])
async def work_hours(message: types.Message):
    await bot.send_message(message.from_user.id, 'We are open Mon-Fri 09:00 to 18:00')


# @dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    await bot.send_message(message.from_user.id, 'We are located on Tiraspols\'ska st. 2')


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(work_hours, commands=['working_hours'])
    dp.register_message_handler(contacts, commands=['contacts'])
