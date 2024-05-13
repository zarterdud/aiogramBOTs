from aiogram import Bot
from aiogram.types import Message, LabeledPrice, pre_checkout_query


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка через Телеграм бот",
        description="Учимся",
        payload="Payment",
        provider_token="381764678:TEST:82000",
        currency="rub",
        prices=[
            LabeledPrice(label="Оплата кредита", amount=1),
            LabeledPrice(label="НДС", amount=1),
        ],
        max_tip_amount=10,
        suggested_tip_amounts=[1000, 2000, 3000, 4000],
        start_parameter="nztcoder",
        provider_data=None,
        photo_url="https://i.ytimg.com/vi/ufRrlpgIMaI/maxresdefault.jpg",
        photo_size=100,
        photo_width=100,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=True,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
    )


async def pre_check(pre_checkout_query: pre_checkout_query, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f"Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}."
    await message.answer(msg)
