import sqlite3
import time

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import application.keyboards as kb


bonus_give = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@bonus_give.message(F.text == "🎁")
async def bonus(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        bonust = cursor.execute(f'SELECT bonus_last FROM users WHERE id = {message.chat.id}').fetchone()
        s = time.localtime(time.time())
        if bonust[0] != s.tm_mday:
            cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (1500000000,))
            cursor.execute(f"UPDATE users SET bonus_last = ? WHERE id = {message.chat.id}",
                           (time.localtime(time.time()).tm_mday,))
            conn.commit()

            await message.answer("<b>✅ Вы успешно получили бонус в размере 15.000.000.000 $AETH !</b>", parse_mode='HTML')

        else:
            await message.answer("<b>🎉 Вы уже получали свой бонус !</b>", parse_mode='HTML')
    
    conn.commit()


