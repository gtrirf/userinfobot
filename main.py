from aiogram import Bot, Dispatcher, types
from asyncio import run
from functions import get_user_info
dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(5160960485, "bot ishlashni boshladi✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(5160960485, "bot ishdan to'xtadi❌")


# async def echo(message: types.Message, bot: Bot):
#     await message.copy_to(chat_id=message.chat.id)
#

async def start():

    dp.shutdown.register(shutdown_answer)
    dp.startup.register(startup_answer)
    # dp.message.register(echo)
    dp.message.register(get_user_info)
    bot = Bot("sizning bot tokeningiz")
    await dp.start_polling(bot, polling_timeout=1)


run(start())