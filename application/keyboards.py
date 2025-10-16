from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery


def start_keyboard():
    button1 = KeyboardButton(text="👤")
    button2 = KeyboardButton(text="🎁")
    button3 = KeyboardButton(text="ℹ️")
    button4 = KeyboardButton(text="❓")
    button5 = KeyboardButton(text="⚙️")
    button6 = KeyboardButton(text="💵 Баланс")
    button7 = KeyboardButton(text="⚒️ Работать")
    button8 = KeyboardButton(text="🎰 Казино")
    button9 = KeyboardButton(text="💎 Донат")
    button10 = KeyboardButton(text="🏠 Дом")
    button11 = KeyboardButton(text="🚗 Машина")
    button12 = KeyboardButton(text="📲 Телефон")

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [button10, button11, button12],
        [button6, button7],
        [button8, button9],
        [button1, button2, button3, button4, button5]
    ], resize_keyboard=True, input_field_placeholder="⭐️ Выбор меню....")

    return keyboard


def start_inline():
    button1 = InlineKeyboardButton(text="🔸 Канал", url="https://t.me/AetheriaGames")
    button2 = InlineKeyboardButton(text="🔸 Чат", url="https://t.me/+ekGsNUgLd-c1MjFk")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1, button2]
    ])

    return keyboard


def profile_keyboard():
    button1 = InlineKeyboardButton(text="💵 Лицевой счет", callback_data="bank_user")
    button2 = InlineKeyboardButton(text="🪙 Перевести", callback_data="transaction")
    button3 = InlineKeyboardButton(text="⚡️ Энергия", callback_data="energy")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [button1],
        [button2],
        [button3]
    ])

    return keyboard


def admin_keyboard():
    button1 = InlineKeyboardButton(text="👤 Найти аккаунт", callback_data="search_account")
    button2 = InlineKeyboardButton(text="💵 Выдать деньги", callback_data="give_money")
    button3 = InlineKeyboardButton(text="📛 Забанить аккаунт", callback_data="ban")
    button6 = InlineKeyboardButton(text="📩 Рассылка", callback_data="post")
    button7 = InlineKeyboardButton(text="📊 Статистика", callback_data="static")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1],
            [button2],
            [button3],
            [button6],
            [button7]
    ])

    return keyboard


def info():
    button1 = InlineKeyboardButton(text="🖼 Основное", callback_data="home")
    button2 = InlineKeyboardButton(text="🎮 Игры", callback_data="games")
    button3 = InlineKeyboardButton(text="🏆 Кланы", callback_data="clans")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1],
            [button2],
            [button3],
    ])

    return keyboard


def payment(message: Message):
    button1 = InlineKeyboardButton(text="🔗 Получить", url=f"https://t.me/spectagram?text=👋+Здравствуйте+!+Хочу+получить+токены.+(количество которое вы покупали)+-+(сколько звёзд потратили).+Мой+ID:+{message.chat.id}.+Спасибо+!")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [button1],
    ])

    return keyboard


def clans_keyboard():
    button11 = InlineKeyboardButton(text="🔚 Назад", callback_data="home_back")
    button22 = InlineKeyboardButton(text="👥 Клан", callback_data="clan_page")

    keyboard1 = InlineKeyboardMarkup(inline_keyboard=[
            [button11],
            [button22]
        ])
    
    return keyboard1