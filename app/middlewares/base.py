from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, Dict

from aiogram.types import Update, Message, CallbackQuery, InlineQuery


class BaseMiddlewareABC(ABC):
    @classmethod
    async def __call__(
            cls,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update | Message | CallbackQuery | InlineQuery,
            data: Dict[str, Any],
    ) -> Awaitable:
        match event:
            case Message():
                result = await cls.handle_message(handler=handler, message=event, data=data)
            case CallbackQuery():
                result = await cls.handle_callback_query(handler=handler, call=event, data=data)
            case InlineQuery():
                result = await cls.handle_inline_query(handler=handler, query=event, data=data)
            case Update(message=Message()):
                result = await cls.handle_message(handler=handler, message=event.message, data=data)
            case Update(callback_query=CallbackQuery()):
                result = await cls.handle_callback_query(handler=handler, call=event.callback_query, data=data)
            case Update(inline_query=InlineQuery()):
                result = await cls.handle_inline_query(handler=handler, query=event.inline_query, data=data)
            case _:
                result = None
        if not result:
            return await handler(event, data)

    @classmethod
    @abstractmethod
    async def handle_message(cls, message: Message, handler, data):
        pass

    @classmethod
    @abstractmethod
    async def handle_callback_query(cls, call: CallbackQuery, handler, data):
        pass

    @classmethod
    @abstractmethod
    async def handle_inline_query(cls, query: InlineQuery, handler, data):
        pass
