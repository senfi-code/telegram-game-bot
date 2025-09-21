import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram import Router

from application.handlers import router
from application.profile import profiles
from application.bot.bank import bank_user
from application.bot.transaction import transactions
from application.bot.bonus import bonus_give
from application.bot.works import work
from application.bot.home import homes_src
from application.bot.car import cars_src
from application.bot.phone import phones_src
from application.casino.game import casino_play
from application.bot.admin import admin_panel
from application.bot.donate import donate_src
from application.bot.play import player
from application.bot.clans import clan

from cfg import BOT_TOKEN


async def main():
    dp = Dispatcher()
    bot = Bot(token=BOT_TOKEN)

    dp.include_router(router)
    dp.include_router(profiles)
    dp.include_router(bank_user)
    dp.include_router(transactions)
    dp.include_router(bonus_give)
    dp.include_router(work)
    dp.include_router(homes_src)
    dp.include_router(cars_src)
    dp.include_router(phones_src)
    dp.include_router(casino_play)
    dp.include_router(admin_panel)
    dp.include_router(donate_src)
    dp.include_router(player)
    dp.include_router(clan)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())