from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
)

TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"

bot = Bot(TOKEN_api)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text="hello")


@dp.inline_handler()
async def ih(inline_query: types.InlineQuery):
    text = inline_query.query
    ipc1 = InputTextMessageContent(f"<b>{text}</b>", parse_mode="HTML")
    item1 = InlineQueryResultArticle(
        id="123",
        input_message_content=ipc1,
        title="Bold",
        description="Empty",
    )
    await bot.answer_inline_query(
        results=[item1], inline_query_id=inline_query.id, cache_time=1
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
