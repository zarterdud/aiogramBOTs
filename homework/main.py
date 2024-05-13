from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext


TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"
storage = MemoryStorage()
bot = Bot(TOKEN_api)
dp = Dispatcher(bot, storage=storage)


class CliStateGroup(StatesGroup):
    photo = State()
    name = State()
    desc = State()


def cansle_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/cancel"))


def kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Начать работу!"))
    return kb


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    global chat
    await message.answer("Hello", reply_markup=kb())


@dp.message_handler(commands=["cancel"], state="*")
async def end(message: types.Message, state: FSMContext):
    current_statr = await state.get_state()
    if current_statr == None:
        return

    await message.reply("Отменил", reply_markup=kb())
    await state.finish()


@dp.message_handler(Text(equals="Начать работу!", ignore_case=True), state=None)
async def start_work(message: types.Message):
    await CliStateGroup().photo.set()
    await message.answer(
        "Сначала отправь нам фотографию паспорта!", reply_markup=cansle_kb()
    )


@dp.message_handler(lambda message: not message.photo, state=CliStateGroup.photo)
async def check_photo(message: types.Message):
    return await message.reply("Это не фотография!")


@dp.message_handler(
    lambda message: message.photo, content_types=["photo"], state=CliStateGroup.photo
)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await CliStateGroup.next()
    await message.answer("А теперь отправь нам ваше ФИО!")


@dp.message_handler(state=CliStateGroup.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await CliStateGroup.next()
    await message.answer("Далее введите срок возврата кредита!")


@dp.message_handler(
    lambda message: not message.text[0].isdigit() and message.text[-1],
    state=CliStateGroup.desc,
)
async def check_desc(message: types.Message):
    return await message.reply("Это не число!")


@dp.message_handler(state=CliStateGroup.desc)
async def add(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["desc"] = message.text
    await message.answer("Все сохранено!")
    async with state.proxy() as data:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=data["photo"],
            caption=f"Кредит на {data['name']} оформлен на срок {data['desc']}",
        )
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
