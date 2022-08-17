import os
from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

load_dotenv()
token = os.environ.get('BOT_TOKEN')
print(token)
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет, легушька!\nОтправь сообщеньку!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Обойдёшься.")


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
