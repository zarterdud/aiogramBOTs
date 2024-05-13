from aiogram import Bot, Dispatcher, executor, types
import asyncio
from aiogram.utils.exceptions import BotBlocked


bot = Bot()
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await asyncio.sleep(10)
    await message.answer("heheheha")


@dp.errors_handler(exception=BotBlocked)
async def error(update: types.Update, exceptions: BotBlocked):
    print("Низя отправить сообщение")
    return True


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
