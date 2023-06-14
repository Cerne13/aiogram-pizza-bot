import os

from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

load_dotenv()
bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher(bot)

votes = dict()

# Just buttons with urls
inline_kb = InlineKeyboardMarkup(row_width=2)

inline_btn1 = InlineKeyboardButton(text='Youtube', url='https://www.youtube.com/')
inline_btn2 = InlineKeyboardButton(text='Google', url='https://google.com')
inline_list = [
    InlineKeyboardButton(text='LInk 1', url='https://www.youtube.com/'),
    InlineKeyboardButton(text='LInk 2', url='https://www.youtube.com/'),
    InlineKeyboardButton(text='LInk 3', url='https://www.youtube.com/'),
]

inline_kb.row(inline_btn1, inline_btn2)
inline_kb.row(*inline_list)
inline_kb.insert(InlineKeyboardButton(text='Link_42', url='https://www.youtube.com/'))


@dp.message_handler(commands=['inline'])
async def inline_commands(message: types.Message):
    await message.answer('Links', reply_markup=inline_kb)


# Some markup with callbacks
inline_cb_markup = InlineKeyboardMarkup(row_width=2)
inline_cb_markup.add(InlineKeyboardButton('Like', callback_data='like_1'))
inline_cb_markup.add(InlineKeyboardButton('Dislike', callback_data='like_-1'))


@dp.message_handler(commands=['test'])
async def some_test(message: types.Message):
    await message.answer('Inline button', reply_markup=inline_cb_markup)


@dp.callback_query_handler(Text(startswith='like_'))
async def query_handler(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[-1])

    if callback.from_user.id not in votes:
        votes[callback.from_user.id] = res
        await callback.answer('You have successfully voted')
    else:
        await callback.answer('You have already voted', show_alert=True)

    await callback.message.answer(f'Vote results: {sum(votes.values())}')


executor.start_polling(dp, skip_updates=True)
