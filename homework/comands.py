from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



async def set_com(bot: Bot):
    commands = [
        BotCommand(
            command='pay',
            description='Оплатить кредит'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
