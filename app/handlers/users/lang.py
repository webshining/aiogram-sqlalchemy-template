from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import LangKeyboard
from database.models import User, get_session
from loader import _
from ..routes import user_router as router


@router.message(Command("lang"))
async def _lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=LangKeyboard.keyboard)


@router.callback_query(LangKeyboard.filter)
async def _lang_callback(call: CallbackQuery, callback_data: LangKeyboard.Callback):
    async with get_session() as session:
        await User.update(session, call.from_user.id, lang=callback_data.lang)
    await call.message.edit_text(
        _("Language changed!", locale=callback_data.lang), reply_markup=None
    )
