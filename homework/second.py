from aiogram import Bot, Dispatcher, executor, types
from random import choice


TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"

bot = Bot(TOKEN_api)
dp = Dispatcher(bot)
alf = "abcdefghijklmnopqrstuvwxyz"

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - о боте
/count - кол-во вызовов
"""

count = 0


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global count
    count += 1
    if "0" in message.text:
        await message.answer(text="Добро пожаловать в наш тг бот\nYES")
        await message.delete()
    else:
        await message.answer(text="Добро пожаловать в наш тг бот\nNO")
        await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    global count
    count += 1
    if "0" in message.text:
        await message.reply(text=f"{HELP_COMMAND}\nYES")
    else:
        await message.reply(text=f"{HELP_COMMAND}\nNO")


@dp.message_handler(commands=["description"])
async def about(message: types.Message):
    global count
    count += 1
    if "0" in message.text:
        await message.answer(text="Начальный бот\nYES")
    else:
        await message.answer(text="Начальный бот\nNO")


@dp.message_handler(commands=["count"])
async def len(message: types.Message):
    global count
    count += 1
    if "0" in message.text:
        await message.answer(text=f"Кол-во вызовов: {count}\nYES")
    else:
        await message.answer(text=f"Кол-во вызовов: {count}\nNO")


@dp.message_handler()
async def ans(message: types.Message):
    global count
    count += 1
    if "0" in message.text:
        await message.reply(text=f"{choice(alf)}\nYES")
    else:
        await message.reply(text=f"{choice(alf)}\nNO")


if __name__ == "__main__":
    executor.start_polling(dp)
