from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from app.keyboards import LangKeyboard
from loader import _

from ..routes import user_router as router


@router.message(Command("lang"))
async def _lang(message: Message):
    await message.answer(_("Select language:"), reply_markup=LangKeyboard.keyboard())


@router.callback_query(LangKeyboard.filter())
async def _lang_callback(call: CallbackQuery, callback_data: LangKeyboard, session, user):
    user.lang = callback_data.lang
    await session.commit()
    await call.message.edit_text(_("Language changed!", locale=user.lang), reply_markup=None)
