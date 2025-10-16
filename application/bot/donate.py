import sqlite3
import random
import time

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from application.primary.src import carss, workss, phoness, homess

import application.keyboards as kb


donate_src = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Donate(StatesGroup):
    pay = State()


@donate_src.startup()
async def on_startip(bot: Bot) -> None:
    await bot.delete_webhook(True)


@donate_src.message(F.text == "💎 Донат")
async def donate(message: Message, state: FSMContext) -> None:
    await state.set_state(Donate.pay)
    balanceu = cursor.execute(f'SELECT money FROM users WHERE id = {message.chat.id}').fetchone()

    await message.answer(f"""
<b>📈 Вы можете купить токены $AETH. (никто не знает каков будет курс 1 $AETH)</b>

<blockquote><b>💵 Ваш баланс:</b> <code>{balanceu[0]}</code> <b>$AETH</b></blockquote>

<b>ℹ️ Введите количество звёзд, бот создаст счёт:</b>""", parse_mode='HTML')
    
    conn.commit()


@donate_src.message(Donate.pay)
async def payment(message: Message, state: FSMContext):
    await state.update_data(pay=message.text)

    await message.answer("<b>❇️ Создаю инвойс на оплату....</b>", parse_mode='HTML')

    time.sleep(2)

    try:
        pay = int(message.text)
        if pay > 100000 or pay < 1:
            await message.answer("<b>📛 Максимальное количество 100 000 ⭐️ !</b>", parse_mode='HTML')
            return
        
        elif pay < 1:
            await message.answer("<b>📛 Минимальное количество 1 ⭐️ !</b>", parse_mode='HTML')
            return

        else:
            summa = pay * 50000

            await message.answer_invoice(
                title="Покупка токенов $AETH",
                description=f"📃 Покупка {summa} $AETH токенов через официального Telegram бота.",
                payload="donate",
                currency="XTR",
                prices=[LabeledPrice(label="XTR",
                                    amount=pay)]
            )

    except ValueError:
        await message.answer("<b>📛 Ошибка в создании платежа !</b>", parse_mode='HTML')

    await state.clear()


@donate_src.pre_checkout_query()
async def pre_checkout_handler(event: PreCheckoutQuery) -> None:
    await event.answer(True)


@donate_src.message(F.successful_payment.payload == "donate")
async def successful_payment(message: Message, state: FSMContext):
    await message.answer("<b>✅ Успешный платёж ! Чтобы получить товар, нажмите на кнопку ниже👇</b>", parse_mode='HTML', reply_markup=kb.payment())
    