import os, hashlib
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, executor


load_dotenv()
bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_mod_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    url = f'http://wikipedia.org/wiki/{text}'

    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title='Wikipedia Article: ',
            url=url,
            input_message_content=types.InputTextMessageContent(message_text=url)
        )
    ]
    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp)
