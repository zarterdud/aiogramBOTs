from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


bot = Bot("5684427805:AAG8uTXj6XpxYmAnIZawiHPNZTGmrscmV5A")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    ikb = InlineKeyboardMarkup()
    ikb.add(InlineKeyboardButton(text="Кнопка", callback_data="1"))
    await message.answer(text="hi", parse_mode="HTML", reply_markup=ikb)


@dp.callback_query_handler()
async def end(call: types.CallbackQuery):
    await call.answer(show_alert=True, text="Пример уведомления")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
