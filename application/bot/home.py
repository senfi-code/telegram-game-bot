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


homes_src = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@homes_src.message(F.text == "🏠 Дом")
async def my_home(message: Message):
    button1 = InlineKeyboardButton(text="1", callback_data="home_vibor1")
    button2 = InlineKeyboardButton(text="2", callback_data="home_vibor2")
    button3 = InlineKeyboardButton(text="3", callback_data="home_vibor3")
    button4 = InlineKeyboardButton(text="4", callback_data="home_vibor4")
    button5 = InlineKeyboardButton(text="5", callback_data="home_vibor5")
    button6 = InlineKeyboardButton(text="6", callback_data="home_vibor6")
    button7 = InlineKeyboardButton(text="7", callback_data="home_vibor7")
    button8 = InlineKeyboardButton(text="8", callback_data="home_vibor8")
    button9 = InlineKeyboardButton(text="9", callback_data="home_vibor9")
    button10 = InlineKeyboardButton(text="10", callback_data="home_vibor10")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1, button2, button3],
            [button4, button5, button6],
            [button7, button8, button9],
            [button10]
        ])

    await message.answer(f"""
<b>1️⃣ | {homess['home_name_1']} | {homess['home_cost_1']} $AETH
2️⃣ | {homess['home_name_2']} | {homess['home_cost_2']} $AETH
3️⃣ | {homess['home_name_3']} | {homess['home_cost_3']} $AETH
4️⃣ | {homess['home_name_4']} | {homess['home_cost_4']} $AETH
5️⃣ | {homess['home_name_5']} | {homess['home_cost_5']} $AETH
6️⃣ | {homess['home_name_6']} | {homess['home_cost_6']} $AETH
7️⃣ | {homess['home_name_7']} | {homess['home_cost_7']} $AETH
8️⃣ | {homess['home_name_8']} | {homess['home_cost_8']} $AETH
9️⃣ | {homess['home_name_9']} | {homess['home_cost_9']} $AETH
🔟 | {homess['home_name_10']} | {homess['home_cost_10']} $AETH</b>

<blockquote><b>⛓️ Выберите нужный дом:</b></blockquote>""", parse_mode='HTML', reply_markup=keyboard)
        



@homes_src.callback_query(F.data == "home_vibor1")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 10000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (10000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_1'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor2")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 70000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (70000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_2'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor3")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 100000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (100000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_3'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor4")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 500000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (500000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_4'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor5")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 900000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (900000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_5'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor6")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 10000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (10000000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_6'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()

@homes_src.callback_query(F.data == "home_vibor7")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 30000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (30000000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_7'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor8")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 70000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (70000000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_8'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor9")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 900000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (900000000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_9'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()


@homes_src.callback_query(F.data == "home_vibor10")
async def buy_home(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        money = cursor.execute(f"SELECT money FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if money[0] >= 1000000000:
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {callback.message.chat.id}", (1000000000,))
            cursor.execute(f"UPDATE users SET home_name = ? WHERE id = {callback.message.chat.id}", (homess['home_name_10'], ))
            
            await callback.message.edit_text("<b>🏠 Вы успешно купили дом !</b>", parse_mode='HTML')

        else:
            await callback.answer("💵 Недостаточно средств для покупки этого дома !", show_alert=True)

    conn.commit()

