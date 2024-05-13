from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
)

TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"

bot = Bot(TOKEN_api)
dp = Dispatcher(bot)

num = ""


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text="Hi")


@dp.inline_handler()
async def ih(inline_query: types.InlineQuery):
    ipc1 = InputTextMessageContent(f"У вас хуй = <b>1000 см</b>", parse_mode="HTML")
    # ipc2 = InputTextMessageContent(f"Подрочить", parse_mode="HTML")
    item1 = InlineQueryResultArticle(
        id="123",
        input_message_content=ipc1,
        title="Сколько у вас см",
        description="Присылает размер хуя",
    )
    await bot.answer_inline_query(
        results=[item1], inline_query_id=inline_query.id, cache_time=1
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
