from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


bot = Bot("6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc")
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton("/help")).add(KeyboardButton("/give")).add(
    KeyboardButton("/photo")
)

HELP_COMMAND = """
<b>/give</b> - <em>Стикер</em>
<b>/help</b> - <em>Сущ-ие команды</em>
"""


async def main(_):
    print("Бот запущен!")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(text="hi", parse_mode="HTML", reply_markup=kb)


@dp.message_handler(commands=["give"])
async def ans(message: types.Message):
    await message.answer(text="Смотри какой смешной кот❤️")
    await bot.send_sticker(
        message.from_user.id,
        sticker="CAACAgIAAxkBAAELIZFlnl6-OCh9vq7eQPeEDWT6vf8AAbUAAt0zAALgQMhIEZ-Z893DZJA0BA",
    )
    await message.answer(text=message.text.count("✅"))


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.answer(HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(content_types=["stiker"])
async def send_sticker_id(m: types.Message):
    await m.answer(m.sticker.file_id)


@dp.message_handler(commands=["photo"])
async def send_photo(message: types.Message):
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo="http://almode.ru/uploads/posts/2021-03/1617027123_29-p-andrei-malakhov-31.jpg",
    )
    await message.delete()


@dp.message_handler(commands=["location"])
async def send_location(message: types.Message):
    await bot.send_location(
        chat_id=message.from_user.id, longitude="37°40'10.0", latitude="55°21'39.6"
    )


@dp.message_handler()
async def heart(message: types.Message):
    if message.text == "❤️":
        await message.reply(chat_id=message.chat.id, text="🖤")
    else:
        await message.answer(text=message.text)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=main)
