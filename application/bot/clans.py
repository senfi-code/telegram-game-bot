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


clan = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


@clan.callback_query(F.data == "clans")
async def clanss(callback: CallbackQuery) -> None:
    clan_status = cursor.execute(f"SELECT clan_status FROM users WHERE id = {callback.message.chat.id}").fetchone()
    balance = cursor.execute(f"SELECT money FROM users WHERE id = 6717475873").fetchone()
    if clan_status[0] == 0:
        button1 = InlineKeyboardButton(text="🔚 Назад", callback_data="home_back")

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1]
        ])

        await callback.answer("🏆 На данный момент доступен только клан разработчиков !")

        await callback.message.edit_text(f"""
<blockquote><b>💎 Клан: Aetheria Games</b></blockquote>
<b>━━━━━━━━━━━━━━━</b>

<blockquote><code>🆔 ID: DEVLOPERS</code></blockquote>

<b>❄️ Статус: Топ 1 🏆

💵 Казна: {balance[0]} $AETH

━━━━━━━━━━━━━━━

👤 Персонал: официальный клан 
разработчиков Aetheria Games.</b>""", parse_mode="HTML", reply_markup=keyboard)
        
    else:
        await callback.answer(f"🏆 На данный момент доступен только клан разработчиков !")

        await callback.message.edit_text(f"""
<blockquote><b>💎 Клан: Aetheria Games</b></blockquote>
<b>━━━━━━━━━━━━━━━</b>

<blockquote><code>🆔 ID: DEVLOPERS</code></blockquote>

<b>❄️ Статус: Топ 1 🏆

💵 Казна: {balance[0]} $AETH

━━━━━━━━━━━━━━━

👤 Персонал: официальный клан
разработчиков Aetheria Games.</b>""", parse_mode="HTML", reply_markup=kb.clans_keyboard())
        
    conn.commit()
        


@clan.callback_query(F.data == "clan_page")
async def clan_page(callback: CallbackQuery) -> None:
    usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {callback.message.chat.id}').fetchone()
    usermoney = cursor.execute(f'SELECT money FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userbank = cursor.execute(f'SELECT bank FROM users WHERE id = {callback.message.chat.id}').fetchone()
    usercar = cursor.execute(f'SELECT car_name FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userhome = cursor.execute(f'SELECT home_name FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userphone = cursor.execute(f'SELECT phone_name FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userenergy = cursor.execute(f'SELECT energy FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userlvl = cursor.execute(f'SELECT lvl FROM users WHERE id = {callback.message.chat.id}').fetchone()
    useradmin = cursor.execute(f'SELECT admin FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userprefix = cursor.execute(f'SELECT status FROM users WHERE id = {callback.message.chat.id}').fetchone()
    userwork = cursor.execute(f'SELECT work_name FROM users WHERE id = {callback.message.chat.id}').fetchone()

    button1 = InlineKeyboardButton(text="🔚 Назад", callback_data="home_back")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1]
        ])

    await callback.message.edit_text(f"""
❤️ Вы являетесь участником клана !

<b>● ID:</b> <code>{callback.message.from_user.id}</code>
<b>● Ник: {usernick[0]}
● Баланс: {usermoney[0]} $AETH
● Сатус: online
● Уровень: {userlvl[0]}
● Префикс: {userprefix[0]}
● Работа: {userwork[0]}
● Энергия: {userenergy[0]}
● Дом: {userhome[0]}
● Машина: {usercar[0]}</b>""", parse_mode='HTML', reply_markup=keyboard)
    

    conn.commit()