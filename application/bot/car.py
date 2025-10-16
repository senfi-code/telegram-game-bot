import sqlite3
import random

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from application.primary.src import carss, workss, phoness, homess

import application.keyboards as kb


cars_src = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@cars_src.message(F.text == "🚗 Машина")
async def my_home(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        button1 = InlineKeyboardButton(text="1", callback_data="car_vibor1")
        button2 = InlineKeyboardButton(text="2", callback_data="car_vibor2")
        button3 = InlineKeyboardButton(text="3", callback_data="car_vibor3")
        button4 = InlineKeyboardButton(text="4", callback_data="car_vibor4")
        button5 = InlineKeyboardButton(text="5", callback_data="car_vibor5")
        button6 = InlineKeyboardButton(text="6", callback_data="car_vibor6")
        button7 = InlineKeyboardButton(text="7", callback_data="car_vibor7")
        button8 = InlineKeyboardButton(text="8", callback_data="car_vibor8")
        button9 = InlineKeyboardButton(text="9", callback_data="car_vibor9")

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9]
        ])

        await message.answer(f"""
<b>1️⃣ | {carss['car_name_1']} | {carss['car_cost_1']} $AETH
2️⃣ | {carss['car_name_2']} | {carss['car_cost_2']} $AETH
3️⃣ | {carss['car_name_3']} | {carss['car_cost_3']} $AETH
4️⃣ | {carss['car_name_4']} | {carss['car_cost_4']} $AETH
5️⃣ | {carss['car_name_5']} | {carss['car_cost_5']} $AETH
6️⃣ | {carss['car_name_6']} | {carss['car_cost_6']} $AETH
7️⃣ | {carss['car_name_7']} | {carss['car_cost_7']} $AETH
8️⃣ | {carss['car_name_8']} | {carss['car_cost_8']} $AETH
9️⃣ | {carss['car_name_9']} | {carss['car_cost_9']} $AETH</b>

<blockquote><b>⛓️ Выберите нужную вам машину:</b></blockquote>""", parse_mode='HTML', reply_markup=keyboard)
        
    conn.commit()


@cars_src.callback_query(F.data == "car_vibor1")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 60000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (60000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_1'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor2")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 280000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (280000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_2'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor3")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 10000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (10000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_3'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor4")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 50000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (50000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_4'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor5")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 100000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (100000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_5'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor6")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 150000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (150000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_6'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()



@cars_src.callback_query(F.data == "car_vibor7")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 300000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (300000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_7'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor8")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 600000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (600000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_8'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()


@cars_src.callback_query(F.data == "car_vibor9")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 950000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (950000000,))
            cursor.execute(f"UPDATE users SET car_name = ? WHERE id = {callback.message.chat.id}", (carss['car_name_9'],))
            
            await callback.message.edit_text("<b>🚗 Вы успешно купили машину !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этой машины !", show_alert=True)

    conn.commit()