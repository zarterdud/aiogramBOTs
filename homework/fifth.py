from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


bot = Bot("6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc")
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="/links"))
ikb = InlineKeyboardMarkup(row_width=1)
ikb.add(
    InlineKeyboardButton(
        text="сигма", url="https://ru.wikipedia.org/wiki/Сигма_(буква)"
    )
).insert(
    InlineKeyboardButton(
        text="Коротченко пупс", url="https://web.telegram.org/a/#6843395042"
    )
)


async def main(_):
    print("Бот запущен")


@dp.message_handler(commands=["start"])
async def start(message: types.message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker="CAACAgIAAxkBAAELIZFlnl6-OCh9vq7eQPeEDWT6vf8AAbUAAt0zAALgQMhIEZ-Z893DZJA0BA",
        reply_markup=kb,
    )
    await message.answer(text="hi")


@dp.message_handler(commands=["links"])
async def link(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id, text="Кнапка с Inline", reply_markup=ikb
    )


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=main, skip_updates=True)
