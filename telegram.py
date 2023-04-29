import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6175511910:AAFRAyMtLAcg0okYIv3jBxbWkq1ibkIwCKQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hello {user_full_name}!")

@dp.message_handler()
async def copy(message: types.Message):
    await message.reply(message.text)