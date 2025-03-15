from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Специальные предложения').add('Информация о доставке').add("Контакты").add('Личный кабинет').add('Полезные советы')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Специальные предложения').add('Информация о доставке').add("Контакты").add('Личный кабинет').add('Полезные советы').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', url='https://youtube.com/@sudoteach'),
                InlineKeyboardButton(text='Шорты', url='https://youtube.com/@sudoteach'),
                InlineKeyboardButton(text='Кроссовки', url='https://youtube.com/@sudoteach'))



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAANLZ9SGqQMEueUG0MW2pg1cH_KmkHkAAm8AA8GcYAzLDn2LwN1NVjYE')
    await message.answer(f'{message.from_user.first_name}, Добро пожаловать в магазин спортивных товаров', reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)


@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Для заказа пишите: @Brick_runner')



@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=catalog_list)



@dp.message_handler(text='Админ-панель')
async def admin(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ панель', reply_markup=admin_panel)
    else:
        await message.reply('Нет такой команды')



@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)

    

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Нет такой команды')
    
if __name__ == '__main__':
    executor.start_polling(dp)
