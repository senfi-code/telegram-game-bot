import sqlite3
import time
import random

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import application.keyboards as kb


player = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@player.message(F.text == "Рыбалка")
async def workeng(message: Message, bot: Bot) -> None:
    usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
    energyu = cursor.execute(f'SELECT energy FROM users WHERE id = {message.chat.id}').fetchone()
    if energyu[0] < 1:
        await message.answer("<b>🧪 У вас мало энергии !</b>", parse_mode='HTML')
    else:
        give_money = random.randint(30000, 1000000)
        random_photo = random.SystemRandom().choice(
                ["https://s9.travelask.ru/system/images/files/001/275/092/wysiwyg_jpg/1380317392-ribi-ch5--72.jpg?1550509979",
                 "https://dfdrussia.wordpress.com/wp-content/uploads/2016/02/blue-marlin.jpg",
                 "https://c.pxhere.com/photos/2d/df/giant_trevally_fish_trevally-921528.jpg!s2",
                 "https://s9.travelask.ru/system/images/files/001/275/102/wysiwyg_jpg/51_whale_shark-e1412159361267.jpg?1550510491",
                 "https://animals.pibig.info/uploads/posts/2023-03/1680228397_animals-pibig-info-p-okeanskie-ribi-zhivotnie-pinterest-3.jpg"])
        random_fish = random.SystemRandom().choice(["Луциана Кубера", "Голубого Марлина", "Большого Каранкса", "Китовую акулу"])
        cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (give_money,))
        cursor.execute(f"UPDATE users SET energy = energy - 1 WHERE id = {message.chat.id}")

        await bot.send_photo(chat_id=message.chat.id,
                            photo=random_photo,
                            caption=f"<blockquote><b>🐠 Вы поймали редкую рыбу !</b></blockquote>\n\n<b>💵 Сумма с продажи: {give_money} $AETH</b>",
                            parse_mode='HTML')

    conn.commit()



@player.message(F.text == "Поход")
async def pohod(message: Message, bot: Bot) -> None:
    usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
    energyu = cursor.execute(f'SELECT energy FROM users WHERE id = {message.chat.id}').fetchone()
    if energyu[0] < 1:
        await message.answer("<b>🧪 У вас мало энергии !</b>", parse_mode='HTML')
    else:
        give_money = random.randint(1000, 10000000)
        random_photo = "https://pion-decor.ru/netcat_files/multifile/11450/IMG_84692EK.JPG"
        cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (give_money,))
        cursor.execute(f"UPDATE users SET energy = energy - 1 WHERE id = {message.chat.id}")

        await bot.send_photo(chat_id=message.chat.id,
                            photo=random_photo,
                            caption=f"<b>💵 Вы сходили в поход и нашли {give_money} $AETH</b>",
                            parse_mode='HTML')
    
    conn.commit()



