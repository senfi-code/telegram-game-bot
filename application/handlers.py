import sqlite3
import asyncio
import os, hashlib
import random

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import FSInputFile
from aiogram.types import TextQuote

from aiogram.types import WebAppInfo
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle, InlineQuery
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

from cfg import ADMIN_ID

from application.primary.src import ENERGY_START
from application.primary.src import EMOJI_HI

import application.keyboards as kb


router = Router()


class make(StatesGroup):
    nick = State()


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    nick TEXT,
    money INTEGER,
    bonus_last INTEGER,
    car_name TEXT,
    home_name TEXT,
    phone_name TEXT,
    energy INTEGER,
    lvl INTEGER,
    admin INTEGER,
    status TEXT,
    work INTEGER,
    work_name TEXT,
    work_zp INTEGER,
    ban INTEGER,
    bank INTEGER,
    clan_status INTEGER,
    clan_name TEXT
)""")


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    usrid = message.chat.id

    info = cursor.execute(f"SELECT id FROM users WHERE id = {usrid}").fetchone()
    if info is None:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
            usrid, message.from_user.first_name, 15000, 0, "❌", "❌",
            "❌", ENERGY_START, 1, 0, "Игрок", 0, "Безработный", 0, 0, 0, 0, "❌"))
        conn.commit()

        await message.answer(f"{EMOJI_HI}", reply_markup=kb.start_keyboard())

        await message.answer("<b>⭐️ Привет, игрок ! Готов к приключениям ? Добро пожаловать в мир захватывающих игр на просторах Telegram ! Начни играть прямо сейчас !</b>", parse_mode='HTML', reply_markup=kb.start_inline())

    else:
        await message.answer("<b>📲 Выбор пункта меню....</b>", parse_mode='HTML', reply_markup=kb.start_keyboard())


@router.message(F.text == "❓")
async def reports(message: Message) -> None:
    await message.answer("<b>❗️ Если у вас возникли какие либо вопросы, обратитесь - spectagram.t.me !</b>", parse_mode='HTML')



@router.message(F.text.lower().in_(["Ограбить", "Ограбить казну", "казна"]))
async def cazna(message: Message, bot: Bot):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        energyu = cursor.execute(f'SELECT energy FROM users WHERE id = {message.chat.id}').fetchone()
        if energyu[0] < 1:
            await message.answer("<b>🔮 У вас мало энергии !</b>", parse_mode='HTML')
        else:
            give_money = random.randint(3000, 15000)
            random_photo = random.SystemRandom().choice(
                ["https://proumdom.ru/wp-content/uploads/2020/12/21567875464789.jpg",
                 "https://media.1777.ru/images/images_processing/881/8817189501727565.jpeg",
                 "https://news.store.rambler.ru/img/dfc6a83e751a8f423e52f62ebb426346?img-format=auto&img-1-resize=height:710",
                 "https://liter.kz/cache/imagine/1200/uploads/news/2022/03/18/62345d2b2ec99547306734.jpg"])
            await bot.send_photo(chat_id=message.chat.id, photo=random_photo,
                           caption=f"<b>💰 Вы успешно ограбили банк и получили {give_money} $AETH !</b>", parse_mode='HTML')
            cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (give_money,))
            cursor.execute(f"UPDATE users SET energy = energy - 1 WHERE id = {message.chat.id}")
        
    conn.commit()


@router.message(F.text == "ℹ️")
async def info(message: Message):
    await message.answer("<b>📖 Выберите категорию из списка ниже:\n\n1️⃣ Основное\n2️⃣ Игры\n3️⃣ Кланы</b>", parse_mode='HTML', reply_markup=kb.info())


@router.callback_query(F.data == "home")
async def home(callback: CallbackQuery) -> None:
    button1 = InlineKeyboardButton(text="🔚 Назад", callback_data="home_back")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1],
    ])

    await callback.message.edit_text("""
<b>📙 Основное:
       📋 Профиль (⮕ Меню)
       💰 Баланс (⮕ Меню)
       💸 Бонус (⮕ Меню)
       🖊 Ник (⮕ Ник/ник_убрать)
       📍 Статус (⮕ Профиль)
       📎 Работы (⮕ Меню)
       💳 Банк (⮕ Профиль)
       🤝 Переводы (⮕ Профиль)

🏪 Магазин:
       🚘 Машины (⮕ Меню)
       🏘 Дома (⮕ Меню)
       📱 Телефоны (⮕ Меню)

🎮 Игры:
       🎰 Казино (⮕ Меню)
       🔨 Работа (⮕ Меню)
       ⚽️ Футбол (⮕ Меню)
       🚨 Взлом (⮕ Ограбить, Казна, Ограбить казну)
       🐠 Рыбалка (⮕ Рыбалка)
       ⛺️ Поход (⮕ Поход)</b>

<i>(в новом обновлении будет доступен большой арсенал)</i>""", parse_mode='HTML', reply_markup=keyboard)
    

@router.callback_query(F.data == "home_back")
async def info(callback: CallbackQuery):
    await callback.message.edit_text("<b>📖 Выберите категорию из списка ниже:\n\n1️⃣ Основное\n2️⃣ Игры\n3️⃣ Кланы</b>", parse_mode='HTML', reply_markup=kb.info())


@router.callback_query(F.data == "games")
async def game(callback: CallbackQuery) -> None:
    await callback.answer("Раздел '🎮 Игры' находится в разработке и появится в ближайшее время !", show_alert=True)



@router.message(F.text == "Ник")
async def nick(message: Message, state: FSMContext):
    await state.set_state(make.nick)

    await message.answer("<b>👑 Введите ник, который хотите поставить:</b>", parse_mode='HTML')


@router.message(make.nick)
async def msmdm(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(nick=message.text)

    if message.text.lower() == 'ник_убрать' or message.text.lower() == 'off':
        username = message.from_user.first_name
        cursor.execute(f"UPDATE users SET nick = ? WHERE id = {message.chat.id}", (username,))
        conn.commit()
        await bot.send_message(chat_id=message.chat.id, text="<b>✍️ Вы установили себе изначальный ник !</b>", parse_mode='HTML')
    else:
        if len(message.text) > 11:
            await bot.send_message(chat_id=message.chat.id, text="<b>❗️ Вы указали слишком длинный ник !</b>", parse_mode='HTML')
        else:
            username = message.text
            cursor.execute(f"UPDATE users SET nick = ? WHERE id = {message.chat.id}", (username,))
            conn.commit()
            await bot.send_message(chat_id=message.chat.id, text="<b>😼 Вы установили себе новый ник !</b>", parse_mode='HTML')

    await state.clear()
    conn.commit()


@router.message(F.text == "⚙️")
async def settings(message: Message) -> None:
    button1 = InlineKeyboardButton(text="Меню: Вкл. ✅", callback_data="menu_off")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1]
    ])

    await message.answer("<b>🆒 Выберите нужную вам настройку:</b>", parse_mode='HTML', reply_markup=keyboard)


@router.callback_query(F.data == "menu_off")
async def menu_off(callback: CallbackQuery) -> None:
    button1 = InlineKeyboardButton(text="Меню: Выкл. ❌",callback_data="menu_on")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1]
    ])

    await callback.message.edit_text("<b>🆒 Выберите нужную вам настройку:</b>", parse_mode='HTML', reply_markup=keyboard)
    await callback.message.answer("<b>✅ Меню отключено !</b>", parse_mode='HTML', reply_markup=ReplyKeyboardRemove())



@router.callback_query(F.data == "menu_on")
async def menu_on(callback: CallbackQuery) -> None:
    button1 = InlineKeyboardButton(text="Меню: Вкл. ✅", callback_data="menu_off")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1]
    ])

    await callback.message.edit_text("<b>🆒 Выберите нужную вам настройку:</b>", parse_mode='HTML', reply_markup=keyboard)
    await callback.message.answer("<b>✅ Меню включено !</b>", parse_mode='HTML', reply_markup=kb.start_keyboard())