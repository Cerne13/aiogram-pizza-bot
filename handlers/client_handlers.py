from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from create_bot import bot
from db import get_menu

from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome to BotPizza and bon appetit!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Please ask our bot! Send it a message: https://t.me/its_not_a_pizza_bot')


# @dp.message_handler(commands=['working_hours'])
async def work_hours(message: types.Message):
    await bot.send_message(message.from_user.id, 'We are open Mon-Fri 09:00 to 18:00')


# @dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'We are located on Tiraspols\'ska st. 2',
        reply_markup=ReplyKeyboardRemove()
    )


async def pizza_menu(message):
    await get_menu(message)
    await message.delete()


async def easter_egg(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Yay! You have found an easter egg. Use promo code "EASTER" to get 5% discount.'
    )
    await bot.send_photo(
        message.from_user.id,
        photo='https://museumhack.com/wp-content/uploads/2023/01/online-pizza-party.jpg'
    )
    await message.delete()


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])
    dp.register_message_handler(work_hours, commands=['working_hours'])
    dp.register_message_handler(contacts, commands=['contacts'])

    dp.register_message_handler(pizza_menu, commands=['menu'])

    dp.register_message_handler(easter_egg, lambda message: 'easteregg' in message.text.strip().lower())
