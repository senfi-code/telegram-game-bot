import sqlite3

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import application.keyboards as kb


bank_user = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class bank_sez(StatesGroup):
    bank_siz = State()

class bank_pez(StatesGroup):
    bank_piz = State()


@bank_user.callback_query(F.data == "bank_user")
async def bank(callback: CallbackQuery, state: FSMContext) -> None:
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {callback.message.chat.id}").fetchone()
    if baninf[0] == 0:
        bank_balance = cursor.execute(f"SELECT bank FROM users WHERE id = {callback.message.chat.id}").fetchone()
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()

        button1 = InlineKeyboardButton(text="💳 Положить", callback_data="bank_s")
        button2 = InlineKeyboardButton(text="💳 Снять", callback_data="bank_p")

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2]
    ])
        
        await callback.message.edit_text(f"<b>💸 На вашем банковском счету: {bank_balance[0]} $AETH</b>", parse_mode='HTML', reply_markup=keyboard)

        conn.commit()


@bank_user.callback_query(F.data == "bank_s")
async def bank_s(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(bank_sez.bank_siz)

    await callback.message.answer("<b>▫️ Введите сколько хотите положить:</b>", parse_mode='HTML')


@bank_user.message(bank_sez.bank_siz)
async def bank_siz(message: Message, state: FSMContext):
    await state.update_data(bank_siz=message.text)

    user_money = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        
    try:
        bank_siz = int(message.text)
    
        if user_money[0] < int(message.text):
            await message.answer("<b>🔴 У вас нет столько деняг !</b>", parse_mode='HTML')
        
        else:
            cursor.execute(f"UPDATE users SET bank = bank + ? WHERE id = {message.chat.id}", (message.text, ))
            cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (message.text, ))

            await message.answer(f"<b>✅ Вы успешно положили {message.text} $AETH на ваш банковский счет !</b>", parse_mode='HTML')
    
    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')

    await state.clear()
    conn.commit()



@bank_user.callback_query(F.data == "bank_p")
async def bank_s(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(bank_pez.bank_piz)

    await callback.message.answer("<b>▫️ Введите сколько хотите снять:</b>", parse_mode='HTML')


@bank_user.message(bank_pez.bank_piz)
async def bank_siz(message: Message, state: FSMContext):
    await state.update_data(bank_piz=message.text)

    bank_balance = cursor.execute(f"SELECT bank FROM users WHERE id = {message.chat.id}").fetchone()
        
    try:
        bank_piz = int(message.text)
    
        if bank_balance[0] < int(message.text):
            await message.answer("<b>🔴 У вас нет столько деняг !</b>", parse_mode='HTML')
        
        else:
            cursor.execute(f"UPDATE users SET bank = bank - ? WHERE id = {message.chat.id}", (message.text, ))
            cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (message.text, ))

            await message.answer(f"<b>✅ Вы успешно сняли {message.text} $AETH с вашего банковского счёта !</b>", parse_mode='HTML')
    
    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')

    await state.clear()
    conn.commit()


@bank_user.message(F.text == "💵 Баланс")
async def balance(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        balanceu = cursor.execute(f'SELECT money FROM users WHERE id = {message.chat.id}').fetchone()
        userbank = cursor.execute(f'SELECT bank FROM users WHERE id = {message.chat.id}').fetchone()

        button1 = InlineKeyboardButton(text="💳 Положить", callback_data="bank_s")
        button2 = InlineKeyboardButton(text="💳 Снять", callback_data="bank_p")

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2]
    ])
        
        await message.answer(f"<b>💳 Ваш баланс: {balanceu[0]} $AETH\n💵 В банке: {userbank[0]} $AETH</b>", parse_mode='HTML', reply_markup=keyboard)

    conn.commit()

        