import sqlite3
import random

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from cfg import ADMIN_ID

from application.primary.src import carss, workss, phoness, homess

import application.keyboards as kb


admin_panel = Router()

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
    bank INTEGER
)""")



class Admin_Panel(StatesGroup):
    search = State()
    give_money = State()
    give_money_summ = State()
    ban = State()
    ban_post = State()
    post = State()



def get_all_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cursor.close()
    return data



@admin_panel.message(F.text == "/admin")
async def admin(message: Message):
    baninf = cursor.execute(f"SELECT ban FROM users WHERE id = {message.chat.id}").fetchone()
    if baninf[0] == 0:
        ainf = cursor.execute(f"SELECT admin FROM users WHERE id = {message.chat.id}").fetchone()
        if ainf[0] > 0:
            await message.answer("<b>💎 Добро пожаловать в админ панель !</b>", parse_mode='HTML', reply_markup=kb.admin_keyboard())



@admin_panel.callback_query(F.data == "static")
async def static(callback: CallbackQuery, bot: Bot) -> None:
    all_users = get_all_users()
    count_users = len(all_users)

    await callback.answer("")
    await bot.send_message(chat_id=ADMIN_ID, text=f"<b>📊 AETHERIA STATIC 📊</b>\n\n"
                                                  f"<b>👥 Всего людей в проекте:</b> <code>{count_users}</code> <b>чел.</b>", parse_mode='HTML')



@admin_panel.callback_query(F.data == "search_account")
async def admin(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Admin_Panel.search)

    await callback.message.edit_text("<b>🆔 Введите ID аккаунта:</b>", parse_mode='HTML')


@admin_panel.message(Admin_Panel.search)
async def search(message: Message, state: FSMContext):
    user_id = cursor.execute(f'SELECT id FROM users WHERE id = {message.text}').fetchone()
    usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.text}').fetchone()
    usermoney = cursor.execute(f'SELECT money FROM users WHERE id = {message.text}').fetchone()
    usercar = cursor.execute(f'SELECT car_name FROM users WHERE id = {message.text}').fetchone()
    userhome = cursor.execute(f'SELECT home_name FROM users WHERE id = {message.text}').fetchone()
    userphone = cursor.execute(f'SELECT phone_name FROM users WHERE id = {message.text}').fetchone()
    userenergy = cursor.execute(f'SELECT energy FROM users WHERE id = {message.text}').fetchone()
    userlvl = cursor.execute(f'SELECT lvl FROM users WHERE id = {message.text}').fetchone()
    userprefix = cursor.execute(f'SELECT status FROM users WHERE id = {message.text}').fetchone()
    userwork = cursor.execute(f'SELECT work_name FROM users WHERE id = {message.text}').fetchone()

    await message.answer(f"""
<b>📂 Информация по аккаунту:

● ID:</b> <code>{user_id[0]}</code>
<b>● Ник: {usernick[0]}
● Баланс: {usermoney[0]} $AETH
● Сатус: online
● Уровень: {userlvl[0]}
● Префикс: {userprefix[0]}
● Работа: {userwork[0]}
● Энергия: {userenergy[0]}
● Дом: {userhome[0]}
● Машина: {usercar[0]}
● Телефон: {userphone[0]}</b>
""", parse_mode='HTML', reply_markup=kb.admin_keyboard())
    
    await state.clear()
    conn.commit()


@admin_panel.callback_query(F.data == "give_money")
async def admin(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Admin_Panel.give_money)

    await callback.message.edit_text("<b>🆔 Введите ID аккаунта:</b>", parse_mode='HTML')


@admin_panel.message(Admin_Panel.give_money)
async def search(message: Message, state: FSMContext):
    global user_id_givem
    user_id_givem = message.text
    await state.update_data(give_money=message.text)

    await state.set_state(Admin_Panel.give_money_summ)
    await message.answer("<b>💵 Введите сумму которую хотите перевести:</b>", parse_mode='HTML')


@admin_panel.message(Admin_Panel.give_money_summ)
async def give_money_summ(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(give_money_summ=message.text)
    cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {user_id_givem}", (message.text, ))

    await bot.send_message(chat_id=user_id_givem, text=f"<b>✅ Вам было выдано {message.text} $AETH !</b>", parse_mode='HTML')

    await state.clear()
    conn.commit()


@admin_panel.callback_query(F.data == "ban")
async def admin(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Admin_Panel.ban)

    await callback.message.edit_text("<b>🆔 Введите ID аккаунта:</b>", parse_mode='HTML')


@admin_panel.message(Admin_Panel.ban)
async def search(message: Message, state: FSMContext):
    await state.update_data(ban=message.text)

    global user_ban_id
    user_ban_id = message.text

    await state.set_state(Admin_Panel.ban_post)
    await message.answer("<b>✍️ Введите причину бана:</b>", parse_mode='HTML')


@admin_panel.message(Admin_Panel.ban_post)
async def search(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(ban_post=message.text)

    cursor.execute(f"UPDATE users SET ban = 1 WHERE id = {user_ban_id}")
    await bot.send_message(chat_id=user_ban_id, text=f"<blockquote><b>📛 Ваш аккаунт заблокирован !</b></blockquote>\n\n<b>✍️ Причина:</b> <code>{message.text}</code>", parse_mode='HTML')

    await state.clear()
    conn.commit()


@admin_panel.callback_query(F.data == "post")
async def admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text("<b>✍️ Введите команду /send:</b>", parse_mode='HTML', reply_markup=kb.admin_keyboard())



@admin_panel.message(lambda message: str(message.from_user.id) == ADMIN_ID, Command('send'))
async def btn_send(message: Message, command: CommandObject, bot: Bot):
    all_users1 = get_all_users()

    send_text = command.args
    if send_text is None:
        await message.answer("<b>❌ Вы ввели неправильно !</b>", parse_mode='HTML')
        return


    for users in all_users1:
        try:
            await bot.send_message(users[1], send_text, parse_mode='HTML')

        except:
            print("No")