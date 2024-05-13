from aiogram import Bot, Dispatcher, executor, types


TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"

bot = Bot(TOKEN_api)
dp = Dispatcher(bot)


@dp.message_handler()
async def answer(message: types.Message):
    await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp)
