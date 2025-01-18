from aiogram import BaseMiddleware

from ..base import BaseMiddlewareABC


class StatusMiddleware(BaseMiddlewareABC, BaseMiddleware):
    @classmethod
    async def handle_message(cls, message, handler, data):
        return cls.process_user(data)

    @classmethod
    async def handle_callback_query(cls, call, handler, data):
        return cls.process_user(data)

    @classmethod
    async def handle_inline_query(cls, query, handler, data):
        return cls.process_user(data)

    @classmethod
    def process_user(cls, data):
        user = data['user']
        if user.status != "admin":
            return user
