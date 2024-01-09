from aiogram import Bot, Dispatcher, executor, types


# Бот - сервер, взаимодействующий с API
TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"

bot = Bot(TOKEN_api)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer(text="Херли ты старт нажимаешь?")


@dp.message_handler(content_types=["text"])
async def echo(message: types.Message):
    await message.answer(text=message.text)  # Ответ на сообщение


if __name__ == "__main__":
    executor.start_polling(dp)  # Запуск бота №1
