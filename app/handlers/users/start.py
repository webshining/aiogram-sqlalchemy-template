from aiogram import html
from aiogram.filters import CommandStart
from aiogram.types import Message

from loader import _
from ..routes import user_router as router


@router.message(CommandStart())
async def start_handler(message: Message):
    text = _("Hello {}").format(html.quote(message.from_user.full_name))
    await message.answer(text)
