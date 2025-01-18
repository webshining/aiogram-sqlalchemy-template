from aiogram.filters import Command
from aiogram.types import Message

from database.models import User
from loader import _
from ..routes import user_router as router
from ...commands import set_admins_commands, remove_commands


@router.message(Command("start"))
async def _start(message: Message, user: User):
    if user.status == "admin":
        await set_admins_commands(user.id)
    else:
        await remove_commands(user.id)
    await message.answer(_("Hello <b>{}</b>").format(message.from_user.full_name))
