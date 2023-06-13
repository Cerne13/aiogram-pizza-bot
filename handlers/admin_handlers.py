from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


# @dp.message_handler(commands=['upload'], state=None)
async def sfm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Please provide an image')


# @dp.message_handler(state='*', commands=['cancel'])
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    curr_state = await state.get_state()
    if not curr_state:
        return
    await state.finish()
    await message.reply('Ok. The process is successfully canceled')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await FSMAdmin.next()
    await message.reply('Now provide a name')


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text.strip()

    await FSMAdmin.next()
    await message.reply('Enter description')


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text.strip()

    await FSMAdmin.next()
    await message.reply('Enter price')


# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text.strip())

    async with state.proxy() as data:
        await message.reply(str(data))

    await state.finish()


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(sfm_start, commands=['upload'], state=None)

    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
