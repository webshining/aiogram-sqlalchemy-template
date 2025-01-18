from typing import Any, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, InlineQuery, User as UserType

from database.models import User, get_session
from ..base import BaseMiddlewareABC


class UserMiddleware(BaseMiddlewareABC, BaseMiddleware):
    @classmethod
    async def handle_message(cls, message: Message, handler, data):
        await cls.process_user(message.from_user, data)

    @classmethod
    async def handle_callback_query(cls, call: CallbackQuery, handler, data):
        await call.answer()
        await cls.process_user(call.from_user, data)

    @classmethod
    async def handle_inline_query(cls, query: InlineQuery, handler, data):
        await cls.process_user(query.from_user, data)

    @classmethod
    async def process_user(cls, from_user: UserType, data: Dict[str, Any]):
        async with get_session() as session:
            user = await User.get_or_create(
                session=session,
                id=from_user.id,
                name=from_user.full_name,
                username=from_user.username,
            )
        data['user'] = user
