from aiogram.dispatcher.event.telegram import TelegramEventObserver
from aiogram.types import Message, CallbackQuery, InlineQuery

from database.models import User


async def user_middleware(event: TelegramEventObserver):
    @event.middleware()
    async def process(handler, event: Message | CallbackQuery | InlineQuery, data):
        await process_user(event.from_user, data)
        await handler(event, data)

    async def process_user(from_user, data):
        session = data["session"]
        data["user"] = await User.update_or_create(
            from_user.id,
            session=session,
            name=from_user.full_name,
            username=from_user.username,
        )
