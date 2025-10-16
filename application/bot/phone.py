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


phones_src = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@phones_src.message(F.text == "📲 Телефон")
async def my_home(message: Message):
    button1 = InlineKeyboardButton(text="1", callback_data="phones_vibor1")
    button2 = InlineKeyboardButton(text="2", callback_data="phones_vibor2")
    button3 = InlineKeyboardButton(text="3", callback_data="phones_vibor3")
    button4 = InlineKeyboardButton(text="4", callback_data="phones_vibor4")
    button5 = InlineKeyboardButton(text="5", callback_data="phones_vibor5")
    button6 = InlineKeyboardButton(text="6", callback_data="phones_vibor6")
    button7 = InlineKeyboardButton(text="7", callback_data="phones_vibor7")
    button8 = InlineKeyboardButton(text="8", callback_data="phones_vibor8")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1, button2, button3],
            [button4, button5, button6],
            [button7, button8]
        ])

    await message.answer(f"""
<b>1️⃣ | {phoness['phone_name_1']} {phoness['phone_cost_1']} $AETH
2️⃣ | {phoness['phone_name_2']} {phoness['phone_cost_2']} $AETH
3️⃣ | {phoness['phone_name_3']} {phoness['phone_cost_3']} $AETH
4️⃣ | {phoness['phone_name_4']} {phoness['phone_cost_4']} $AETH
5️⃣ | {phoness['phone_name_5']} {phoness['phone_cost_5']} $AETH
6️⃣ | {phoness['phone_name_6']} {phoness['phone_cost_6']} $AETH
7️⃣ | {phoness['phone_name_7']} {phoness['phone_cost_7']} $AETH
8️⃣ | {phoness['phone_name_8']} {phoness['phone_cost_8']} $AETH</b>

<blockquote><b>⛓️ Выберите нужный телефон:</b></blockquote>""", parse_mode='HTML', reply_markup=keyboard)
    


@phones_src.callback_query(F.data == "phones_vibor1")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 1000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (1000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_1'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor2")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 5000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (5000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_2'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor3")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 20000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (20000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_3'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor4")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 30000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (30000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_4'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor5")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 70000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (70000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_5'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor6")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 1000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (100000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_6'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor7")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 600000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (600000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_7'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


@phones_src.callback_query(F.data == "phones_vibor8")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 900000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (900000,))
            cursor.execute(f"UPDATE users SET phone_name = ? WHERE id = {callback.message.chat.id}", (phoness['phone_name_8'], ))
            
            await callback.message.edit_text("<b>📲 Вы успешно купили телефон !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого телефона !", show_alert=True)

    conn.commit()


