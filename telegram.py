import time
import logging
from ChatClient import ChatClient
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6175511910:AAFRAyMtLAcg0okYIv3jBxbWkq1ibkIwCKQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
chatClient = ChatClient()

sessions = {}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hello {user_full_name}!\n"
                        f"I am Student Helper Bot\n\n"
                        f"I could be:\n"
                        f"1. Student Assistant\n"
                        f"2. Artist")

@dp.message_handler(commands=['1'])
async def set_mode(message: types.Message):
    sessions[message.chat.id] = []
    await message.reply("now i'm a student helper\nplease enter the list of courses you've taken:\n")

@dp.message_handler()
async def prompt(message: types.Message):
    if not sessions[message.chat.id]:
        sessions[message.chat.id].append({"role": "user", "content": message.text})
    else:
        sessions[message.chat.id].append({"role": "user", "content": message.text})
        response = chatClient.respond(sessions[message.chat.id])
        sessions[message.chat.id].append(response[-1])
        await message.reply(response[-1]["content"])