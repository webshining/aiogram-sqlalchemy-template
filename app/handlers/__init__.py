from aiogram import Dispatcher
from aiogram.types import ErrorEvent

from utils import logger

from .admins import router as admin_router
from .users import router as user_router


def setup_handlers(dp: Dispatcher) -> None:
    @dp.error()
    async def _error(event: ErrorEvent):
        logger.exception(event.exception)

    dp.include_routers(user_router, admin_router)
