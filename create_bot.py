import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()

bot = Bot(os.getenv("API_TOKEN"))

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
