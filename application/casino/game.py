import sqlite3
import random
import time

from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from application.primary.src import carss, workss, phoness, homess

import application.keyboards as kb


casino_play = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


class Football(StatesGroup):
    summa = State()


class Cub(StatesGroup):
    summa = State()
    fiction = State()


class Darts(StatesGroup):
    summa = State()


class Basketball(StatesGroup):
    summa = State()


class Bouling(StatesGroup):
    summa = State()


class Slots(StatesGroup):
    summa = State()



@casino_play.message(F.text == "🎰 Казино")
async def casino(message: Message) -> None:
    button1 = InlineKeyboardButton(text="🎲 Кубик", callback_data="cub")
    button2 = InlineKeyboardButton(text="🎯 Дартс", callback_data="datrs")
    button3 = InlineKeyboardButton(text="🏀 Баскетбол", callback_data="basketball")
    button4 = InlineKeyboardButton(text="⚽️ Футбол", callback_data="football")
    button5 = InlineKeyboardButton(text="🎳 Боулинг", callback_data="bouling")
    button6 = InlineKeyboardButton(text="🎰 Слоты", callback_data="slots")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2],
        [button3],
        [button4],
        [button5, button6]
    ])

    await message.answer("<b>🎮 Выберите меню:</b>", parse_mode='HTML', reply_markup=keyboard)




@casino_play.callback_query(F.data == "slots")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Slots.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')


@casino_play.message(Slots.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    usrid = message.chat.id
    try:
        st = message.text
        stavka = int(st)
        b = cursor.execute(f"SELECT money FROM users WHERE id = {usrid}").fetchone()
        ba = b[0]
        if ba >= stavka:
            await message.answer(f"<b>❇️ Вы указали ставку {stavka} $AETH, игра начинается....</b>", parse_mode='HTML')

            time.sleep(2)

            await bot.send_dice(chat_id=message.chat.id, emoji='🎰')

            time.sleep(2.6)

            rnd = random.randint(1, 3)
            if rnd == 1:
                y = stavka
                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')
                cursor.execute(f'UPDATE users SET money = money - {y} WHERE id = {message.chat.id}')

            if rnd == 2:
                await message.answer("<b>😕 Вы не проиграли, но и не выйграли !</b>", parse_mode='HTML')

            if rnd == 3:
                y = stavka
                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
                cursor.execute(f'UPDATE users SET money = money + {y} WHERE id = {message.chat.id}')
        else:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')


    except:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')  

    
    await state.clear()
    conn.commit()




@casino_play.callback_query(F.data == "bouling")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Bouling.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')


@casino_play.message(Bouling.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    try:
        stavka_dice = int(message.text)
        moneyuser = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        if moneyuser[0] < stavka_dice:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')
        
        else:
            dicee = await bot.send_dice(chat_id=message.chat.id, emoji='🎳')
            time.sleep(2)
            if dicee.dice.value == 6:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')

    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')    
    
    await state.clear()
    conn.commit()





@casino_play.callback_query(F.data == "basketball")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Basketball.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')


@casino_play.message(Basketball.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    try:
        stavka_dice = int(message.text)
        moneyuser = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        if moneyuser[0] < stavka_dice:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')
        
        else:
            dicee = await bot.send_dice(chat_id=message.chat.id, emoji='🏀')
            time.sleep(3)
            if dicee.dice.value == 5 or dicee.dice.value == 4:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')

    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')    

    await state.clear() 
    conn.commit()





@casino_play.callback_query(F.data == "datrs")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Darts.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')



@casino_play.message(Darts.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    try:
        stavka_dice = int(message.text)
        moneyuser = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        if moneyuser[0] < stavka_dice:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')

        else:
            dicee = await bot.send_dice(chat_id=message.chat.id, emoji='🎯')
            time.sleep(3)
            if dicee.dice.value == 6:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (stavka_dice,))

                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (stavka_dice,))

                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')

        
    except:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')    

    await state.clear()
    conn.commit()



@casino_play.callback_query(F.data == "cub")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Cub.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')


@casino_play.message(Cub.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    try:
        global stavka_cubik
        stavka_cubik = int(message.text)
        usermoney = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        if usermoney[0] >= stavka_cubik:
            if stavka_cubik > 0:
                await state.set_state(Cub.fiction)
                await message.answer("<b>🔢 Введите число на которое ставите [1-6]:</b>", parse_mode='HTML')
            
            else:
                await message.answer("<b>🔴 Вы ввели число менее 0 !</b>", parse_mode='HTML')
        
        else:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')

    except:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML') 



@casino_play.message(Cub.fiction)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(fiction=message.text)

    try:
        cube_num = int(message.text)
        if cube_num > 6:
            await message.answer("<b>#️⃣ Вы ввели число больше 6 !</b>")

        else:
            dicee = await bot.send_dice(chat_id=message.chat.id, emoji='🎲')
            time.sleep(3)
            usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
            if dicee.dice.value == cube_num:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (stavka_cubik,))

                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (stavka_cubik,))

                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')

    
    except:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')    

    await state.clear()
    conn.commit()



@casino_play.callback_query(F.data == "football")
async def slots_play(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Football.summa)

    await callback.message.edit_text("<b>▫️ Введите сумму ставки:</b>", parse_mode='HTML')


@casino_play.message(Football.summa)
async def bank_siz(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(summa=message.text)

    try:
        stavka_dice = int(message.text)
        moneyuser = cursor.execute(f"SELECT money FROM users WHERE id = {message.chat.id}").fetchone()
        usernick = cursor.execute(f'SELECT nick FROM users WHERE id = {message.chat.id}').fetchone()
        if moneyuser[0] < stavka_dice:
            await message.answer("<b>💵 На вашем счете недостаточно средств !</b>", parse_mode='HTML')
        
        else:
            dicee = await bot.send_dice(chat_id=message.chat.id, emoji='⚽️')
            time.sleep(3)
            if dicee.dice.value == 5 or dicee.dice.value == 4 or dicee.dice.value == 3:
                cursor.execute(f"UPDATE users SET money = money + ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>🎉 Поздравляем, вы выиграли !</b>", parse_mode='HTML')
            
            else:
                cursor.execute(f"UPDATE users SET money = money - ? WHERE id = {message.chat.id}", (stavka_dice,))
                conn.commit()

                await message.answer("<b>😔 Очень жаль, но вы проиграли !</b>", parse_mode='HTML')

    except ValueError:
        await message.answer("<b>📛 Ошибка: 404 !</b>", parse_mode='HTML')    
    
    await state.clear()
    conn.commit()


