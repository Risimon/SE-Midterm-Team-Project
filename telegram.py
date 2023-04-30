import time
import logging
from dotenv import load_dotenv
from Mode import Mode
import os

import const
from ChatClient import ChatClient
from DalleClient import DalleClient
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from io import BytesIO
import requests

load_dotenv()
bot = Bot(token=os.getenv(const.TELEGRAM_API_KEY))
dp = Dispatcher(bot=bot)
chatClient = ChatClient(os.getenv(const.OPENAI_API_KEY))
dalleClient = DalleClient(os.getenv(const.OPENAI_API_KEY))

sessions = {}
mode = Mode.NONE

chat = KeyboardButton('Student Helper')
dalle = KeyboardButton('Artist')
clear = KeyboardButton('Clear')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(chat).add(dalle).add(clear)
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Hello {user_full_name}!\n"
                        f"I am Student Helper Bot\n\n"
                        f"I could be:\n"
                        f"1. Student Assistant\n"
                        f"2. Artist", reply_markup=keyboard1)

@dp.message_handler(commands=['helper'])
async def set_helper_mode(message: types.Message):
    global mode
    sessions[message.chat.id] = []
    mode = Mode.STUDENT_HELPER
    await message.reply("now i'm a student helper\nplease enter the list of courses you've taken:\n")


@dp.message_handler(commands=['artist'])
async def set_dalle_mode(message: types.Message):
    global mode
    mode = Mode.DALLE
    await message.reply("now i'm an artist")


@dp.message_handler(commands=['clear'])
async def clear_data(message: types.Message):
    global mode
    mode = Mode.NONE
    sessions[message.chat.id].clear()
    await message.reply("Chat context cleared")
    

@dp.message_handler()
async def prompt(message: types.Message):
    global mode
    if message.text == "Student Helper":
        await set_helper_mode(message)
    elif message.text == "Artist":
        await set_dalle_mode(message)
    elif message.text == "Clear":
        await clear_data(message)
    else:
        if mode == Mode.STUDENT_HELPER:
            response = ask_chat_api(message)
            if response:
                await message.reply(response)
        elif mode == Mode.DALLE:
            ask_dalle_api(message)
            photo = dalleClient.respond(message.text)
            await bot.send_photo(chat_id=message.chat.id, photo=photo)
        elif mode == Mode.NONE:
            await message.reply("First choose the mode")


def ask_chat_api(message: types.Message):
    if not sessions[message.chat.id]:
        sessions[message.chat.id].append({"role": "user", "content": message.text})
    else:
        sessions[message.chat.id].append({"role": "user", "content": message.text})
        response = chatClient.respond(sessions[message.chat.id])
        sessions[message.chat.id].append(response[-1])
        return response[-1]["content"]


def ask_dalle_api(message: types.Message):
    url = dalleClient.respond(message.text)
    if url:
        photo_response = requests.get(url)
        photo_data = BytesIO(photo_response.content)
        photo = types.InputFile(photo_data)
        return photo
