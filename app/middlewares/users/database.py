from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import Message, CallbackQuery, InlineQuery

from database import get_session


async def database_middleware(event: TelegramEventObserver):
    @event.middleware()
    async def process(handler, event: Message | CallbackQuery | InlineQuery, data):
        async with get_session() as session:
            data["session"] = session
            await handler(event, data)
