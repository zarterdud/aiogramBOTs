import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot = Bot("6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc")
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton("/help")).insert(KeyboardButton("/description")).add("❤️").insert(
    KeyboardButton("Отправить апельсин")
).add(KeyboardButton("Рандомное местоположение"))


@dp.message_handler(commands=["start"])
async def hi(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="hi", reply_markup=kb)



@dp.message_handler()
async def stiker_ans(message: types.Message):
    if message.text == "❤️":
        await bot.send_sticker(
            message.from_user.id,
            sticker="CAACAgIAAxkBAAELIZFlnl6-OCh9vq7eQPeEDWT6vf8AAbUAAt0zAALgQMhIEZ-Z893DZJA0BA",
        )
    if message.text == "Отправить апельсин":
        await bot.send_photo(
            chat_id=message.chat.id,
            photo="https://avatars.mds.yandex.net/get-entity_search/510165/779700765/SUx182_2x",
        )
    if message.text == "Рандомное местоположение":
        await bot.send_location(
            chat_id=message.chat.id,
            longitude=random.choice([i for i in range(181)]),
            latitude=random.choice([i for i in range(91)]),
        )


if __name__ == "__main__":
    executor.start_polling(dp)
