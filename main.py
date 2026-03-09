import asyncio
import logging
import sys
import os
import types

from dotenv import load_dotenv
from aiogram import Bot,Dispatcher,html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F

load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")
dp=Dispatcher()


@dp.message(CommandStart)
async def command_start(message:Message)->None:
    await message.answer(f"Assamu alaykum {html.bold(message.from_user.full_name)}")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


def get_role_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🚚 Haydovchiman", callback_data="role_driver")
    builder.button(text="📦 Yuk beruvchiman", callback_data="role_shipper")
    builder.adjust(1)
    return builder.as_markup()

@dp.callback_query(F.data.startswith("role_"))
async def callbacks_num_confirm(callback: types.CallbackQuery):
    role = callback.data.split("_")[1]
    if role == "driver":
        await callback.message.edit_text("Siz Haydovchi bo'limini tanladingiz. Mashinangiz turini kiriting:")
    else:
        await callback.message.edit_text("Siz Yuk beruvchi bo'limini tanladingiz. Yuk haqida ma'lumot bering:")
    await callback.answer()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


