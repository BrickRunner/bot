from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAANLZ9SGqQMEueUG0MW2pg1cH_KmkHkAAm8AA8GcYAzLDn2LwN1NVjYE')
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать в магазин спортивных товаров')

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)

@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Нет такой команды')\
    
if __name__ == '__main__':
    executor.start_polling(dp)
