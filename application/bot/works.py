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


work = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@work.message(F.text == "⚒️ Работать")
async def working(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        button1 = InlineKeyboardButton(text="1", callback_data="rabota_vibor1")
        button2 = InlineKeyboardButton(text="2", callback_data="rabota_vibor2")
        button3 = InlineKeyboardButton(text="3", callback_data="rabota_vibor3")
        button4 = InlineKeyboardButton(text="4", callback_data="rabota_vibor4")
        button5 = InlineKeyboardButton(text="5", callback_data="rabota_vibor5")
        button6 = InlineKeyboardButton(text="6", callback_data="rabota_vibor6")
        button7 = InlineKeyboardButton(text="7", callback_data="rabota_vibor7")
        button8 = InlineKeyboardButton(text="8", callback_data="rabota_vibor8")

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1, button2, button3],
            [button4, button5, button6],
            [button7, button8]
        ])

        await message.answer(f"""
<b>1️⃣ | {workss['work_name_1']} | {workss['work_lvl_1']} - Требуется уровень
2️⃣ | {workss['work_name_2']} | {workss['work_lvl_2']} - Требуется уровень 
3️⃣ | {workss['work_name_3']} | {workss['work_lvl_3']} - Требуется уровень
4️⃣ | {workss['work_name_4']} | {workss['work_lvl_4']} - Требуется уровень
5️⃣ | {workss['work_name_5']} | {workss['work_lvl_5']} - Требуется уровень 
6️⃣ | {workss['work_name_6']} | {workss['work_lvl_6']} - Требуется уровень
7️⃣ | {workss['work_name_7']} | {workss['work_lvl_7']} - Требуется уровень
8️⃣ | {workss['work_name_8']} | {workss['work_lvl_8']} - Требуется уровень</b>

<blockquote><b>⛓️ Выберите нужную работу:</b></blockquote>""", parse_mode='HTML', reply_markup=keyboard)
        
    conn.commit()


@work.callback_query(F.data == "rabota_vibor1")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (1, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_1'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_1'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor2")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (2, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_2'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_2'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor3")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (3, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_3'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_3'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


        
@work.callback_query(F.data == "rabota_vibor4")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (4, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_4'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_4'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor5")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (5, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_5'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_5'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor6")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (6, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_6'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_6'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor7")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (7, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_7'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_7'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')


@work.callback_query(F.data == "rabota_vibor8")
async def rabota_vibor1(callback: CallbackQuery):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
        lvlusr = cursor.execute(f"SELECT lvl FROM users WHERE id = {callback.message.chat.id}").fetchone()

        if lvlusr[0] >= 1:
            cursor.execute(f"UPDATE users SET work = ? WHERE id = {callback.message.chat.id}", (8, ))
            cursor.execute(f"UPDATE users SET work_name = ? WHERE id = {callback.message.chat.id}", (workss['work_name_8'],))
            cursor.execute(f"UPDATE users SET work_zp = ? WHERE id = {callback.message.chat.id}",(workss['work_zp_8'],))

            await callback.message.edit_text("<b>✅ Вы успешно устроились на работу !</b>", parse_mode='HTML')

            conn.commit()

        else:
            await callback.message.answer("<b>⭐️ Недостаточно уровня !</b>", parse_mode='HTML')



@work.message(F.text.lower().in_(["работать", "воркать", "ворк"]))
async def workeng(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        rabota_usr = cursor.execute(f'SELECT work FROM users WHERE id = {message.chat.id}').fetchone()
        energy_usr = cursor.execute(f'SELECT energy FROM users WHERE id = {message.chat.id}').fetchone()
        if rabota_usr[0] < 1:
            await message.answer("<b>❎ Вы нигде не работаете !</b>\n\n<blockquote><b><i>📚 Устроиться можно: ⚒️ Работать ⮕ [Выбор работы]</i></b></blockquote>", parse_mode='HTML')
        else:
            if energy_usr[0] < 1:
                await message.answer("<b>🧪 У вас мало энергии !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (workss[f'work_zp_{rabota_usr[0]}'], ))
                cursor.execute(f"UPDATE users SET energy = energy - 2 WHERE id = {message.chat.id}")

                up_lvl = random.randint(1, 2)

                await message.answer(f"<b>✅ Вы успешно закончили рабочий день и заработали {workss[f'work_zp_{rabota_usr[0]}']} $AETH !</b>", parse_mode='HTML')

                if up_lvl == 2:
                    setlvl = random.randint(1, 10)
                    cursor.execute(f"UPDATE users SET lvl = lvl + {setlvl} WHERE id = {message.chat.id}")

                    await message.answer(f"<b>🌠 Вы повысили свой уровень на {setlvl} !</b>", parse_mode='HTML')

    conn.commit()
