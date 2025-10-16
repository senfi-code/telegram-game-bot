import sqlite3

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import application.keyboards as kb


transactions = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Transfer(StatesGroup):
    transaction = State()
    summ = State()


@transactions.callback_query(F.data == "transaction")
async def bank(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")
    await state.set_state(Transfer.transaction)

    await callback.message.answer("<b>🆔 Введите ID пользователя которому хотите перевести::</b>", parse_mode='HTML')


@transactions.message(Transfer.transaction)
async def bank_siz(message: Message, state: FSMContext):
    await state.update_data(transaction=message.text)

    try:
        transaction = int(message.text)
    
        global id_pay
        id_pay = message.text
        inf = cursor.execute(f"SELECT id FROM users WHERE id = {id_pay}").fetchone()
        if inf is None:
            await message.answer("<b>⛔️ Данного аккаунта не существует !</b>", parse_mode='HTML')
        
        else:
            await state.set_state(Transfer.summ)
            await message.answer("<b>💵 Введите сумму которую хотите перевести:</b>", parse_mode='HTML')

    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')


@transactions.message(Transfer.summ)
async def summ(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summ=message.text)

    bank_user = cursor.execute(f"SELECT bank FROM users WHERE id = {message.chat.id}").fetchone()

    try:
        sum = int(message.text)
    
        if int(message.text) < 1:
            await message.answer("<b>🔴 Сумма перевода должна быть больше 1$ !</b>", parse_mode='HTML')
        else:
            if bank_user[0] < int(message.text):
                money_user = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
                if money_user[0] >= int(message.text):
                    await message.answer("<b>📉 У вас мало денег на банковском счету. Переведите деньги на банковский счет который хотите передать !</b>", parse_mode='HTML')
                else:
                    await message.answer("<b>😔 Недостаточно средств на банковском счету !</b>", parse_mode='HTML')

            else:
                cursor.execute(f"UPDATE users SET bank = bank - ? WHERE id = {message.chat.id}", (message.text, ))
                cursor.execute(f"UPDATE users SET bank = bank + ? WHERE id = {id_pay}", (message.text, ))

                await message.answer("<b>✅ Успешный перевод средств !</b>", parse_mode='HTML')
                await bot.send_message(id_pay, f"<blockquote><b>📲 Поступление средств на счёт !</b></blockquote>\n\n<b>💵 Сумма:</b> <code>{message.text} $AETH</code>\n<b>👤 Отправитель:</b> <code>{message.chat.id}</code>", parse_mode='HTML')
    
    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')

    await state.clear()
    conn.commit()