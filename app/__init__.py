from aiogram import Dispatcher

from .commands import set_default_commands
from .handlers import admin_router, user_router
from .middlewares import users_middlewares, admins_middlewares


def setup_routes(dp: Dispatcher):
    for middleware in users_middlewares:
        dp.update.middleware(middleware)
    for middleware in admins_middlewares:
        admin_router.message.middleware(middleware)
        admin_router.callback_query.middleware(middleware)
        admin_router.inline_query.middleware(middleware)

    dp.include_routers(user_router, admin_router)
