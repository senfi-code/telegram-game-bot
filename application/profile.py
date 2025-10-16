import sqlite3

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import application.keyboards as kb


profiles = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@profiles.message(F.text == "👤")
async def cabinet(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        usermoney = cursor.execute(f'SELECT money FROM users WHERE id = {message.chat.id}').fetchone()
        userbank = cursor.execute(f'SELECT bank FROM users WHERE id = {message.chat.id}').fetchone()
        usercar = cursor.execute(f'SELECT car_name FROM users WHERE id = {message.chat.id}').fetchone()
        userhome = cursor.execute(f'SELECT home_name FROM users WHERE id = {message.chat.id}').fetchone()
        userphone = cursor.execute(f'SELECT phone_name FROM users WHERE id = {message.chat.id}').fetchone()
        userenergy = cursor.execute(f'SELECT energy FROM users WHERE id = {message.chat.id}').fetchone()
        userlvl = cursor.execute(f'SELECT lvl FROM users WHERE id = {message.chat.id}').fetchone()
        useradmin = cursor.execute(f'SELECT admin FROM users WHERE id = {message.chat.id}').fetchone()
        userprefix = cursor.execute(f'SELECT status FROM users WHERE id = {message.chat.id}').fetchone()
        userwork = cursor.execute(f'SELECT work_name FROM users WHERE id = {message.chat.id}').fetchone()
        clan = cursor.execute(f'SELECT clan_name FROM users WHERE id = {message.chat.id}').fetchone()

        await message.answer(f"""
<b>💎 [{userprefix[0]}], ваш профиль:

━━━━━━━━━━━━━━━
🆔 ID:</b> <code>{message.chat.id}</code>
<b>👨‍💻 Nick: {usernick[0]}
☘️ Статус: Online
💰 Баланс:</b> <code>{usermoney[0]}</code> <b>$AETH</b>
<b>💳 В банке:</b> <code>{userbank[0]}</code> <b>$AETH</b>
<b>━━━━━━━━━━━━━━━
⭐️ Уровень: {userlvl[0]}
📍 Префикс: {userprefix[0]}
🔧 Уровень админки: {useradmin[0]}

🏆 Ваш клан: {clan[0]}
━━━━━━━━━━━━━━━
⚒️ Работа: {userwork[0]}
⚡️ Энергия: {userenergy[0]}

🌃 Имущество:
        
🏠 Дом: {userhome[0]}
🚘 Машина: {usercar[0]}
📱 Телефон: {userphone[0]}</b>""", parse_mode='HTML', reply_markup=kb.profile_keyboard())
        
    conn.commit()



@profiles.callback_query(F.data == "energy")
async def energy(callback: CallbackQuery) -> None:
    energyu = cursor.execute(f'SELECT energy FROM users WHERE id = {callback.message.chat.id}').fetchone()

    button1 = InlineKeyboardButton(text="⚡️ Пополнить энергию", callback_data="buy_energy")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1]
    ])

    await callback.message.edit_text(f"<b>⚡️ Ваш уровень энергии: {energyu[0]}\n\n💵 Стоимость пополнения энергии: 30.000 $AETH</b>", parse_mode='HTML', reply_markup=keyboard)



@profiles.callback_query(F.data == "buy_energy")
async def buy_energy(callback: CallbackQuery) -> None:
    button1 = InlineKeyboardButton(text="⚡️ Пополнить энергию", callback_data="energy")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1]
    ])

    energyu = cursor.execute(f'SELECT energy FROM users WHERE id = {callback.message.chat.id}').fetchone()

    if energyu[0] == 100:
        await callback.message.edit_text("<b>🎩 У вас уже максимальный уровень энергии !</b>", parse_mode='HTML')
    else:
        balanceu = cursor.execute(f'SELECT money FROM users WHERE id = {callback.message.chat.id}').fetchone()
        
        if balanceu[0] > 2999:
            cursor.execute(f"UPDATE users SET energy = energy + 1 WHERE id = {callback.message.chat.id}")
            cursor.execute(f"UPDATE users SET money = money - 30000 WHERE id = {callback.message.chat.id}")
            await callback.message.edit_text("<b>🔥 Вы успешно повысили свою энергию на 1 !</b>", parse_mode='HTML', reply_markup=keyboard)
        else:
            await callback.answer("💵 Недостаточно средств для покупки энергии !", show_alert=True)