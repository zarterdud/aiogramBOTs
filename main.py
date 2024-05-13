from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.dispatcher import FSMContext


TOKEN_api = "6714704690:AAGusdRE_2A8n77Lr8h-UBl6t6_KQcEZFKc"
storage = MemoryStorage()
bot = Bot(TOKEN_api)
dp = Dispatcher(bot, storage=storage)


class ProfileStart(StatesGroup):
    photo = State()
    name = State()
    age = State()
    desc = State()


def get_kb():
    kb = ReplyKeyboardMarkup()
    return kb


def get_cancel_kb():
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/cancel"))


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Bot started, type /create for start", reply_markup=get_kb())


@dp.message_handler(commands=["cancel"], state="*")
async def end(message: types.Message, state: FSMContext):
    if state is None:
        return
    await message.reply("Вы прервали заполнение анкеты!", reply_markup=get_kb())
    await state.finish()


@dp.message_handler(commands=["create"])
async def create_start(message: types.Message):
    await message.answer(
        "Let's create your profile, send photo", reply_markup=get_cancel_kb()
    )
    await ProfileStart.photo.set()


@dp.message_handler(lambda message: not message.photo, state=ProfileStart.photo)
async def check_photo(message: types.Message):
    await message.reply("Это не фотография!")


@dp.message_handler(content_types=["photo"], state=ProfileStart.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id

    await message.answer("Теперь отправьте Имя")
    await ProfileStart.next()


@dp.message_handler(state=ProfileStart.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text

    await message.answer("Теперь отправьте Возраст")
    await ProfileStart.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ProfileStart.age)
async def chack_age(message: types.Message):
    await message.reply("Это не число!")


@dp.message_handler(state=ProfileStart.age)
async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = message.text

    await message.answer("Теперь отправьте Описание")
    await ProfileStart.next()


@dp.message_handler(state=ProfileStart.desc)
async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["desc"] = message.text
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=data["photo"],
            caption=f"{data['name']}, {data['age']}\n{data['desc']}",
        )

    await message.answer("Анкета сохранена")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
