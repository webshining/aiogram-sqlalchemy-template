import asyncio

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from app import set_default_commands, setup_middlewares, setup_routes
from data.config import (
    WEBHOOK_PATH,
    WEBHOOK_SERVER_HOST,
    WEBHOOK_SERVER_PORT,
    WEBHOOK_SERVER_SECRET,
    WEBHOOK_URL,
)
from loader import bot, dp
from utils import logger


async def on_startup() -> None:
    await set_default_commands()
    if all([WEBHOOK_URL, WEBHOOK_PATH, WEBHOOK_SERVER_SECRET]):
        await bot.set_webhook(f"{WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SERVER_SECRET)
    else:
        await bot.delete_webhook()


async def on_shutdown() -> None:
    logger.info("Bot stopped!")


async def main() -> None:
    await setup_middlewares(dp)
    await setup_routes(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    if all((WEBHOOK_URL, WEBHOOK_PATH, WEBHOOK_SERVER_SECRET, WEBHOOK_SERVER_PORT, WEBHOOK_SERVER_HOST)):
        app = web.Application()
        webhook_request_headers = SimpleRequestHandler(dispatcher=dp, bot=bot, secret_token=WEBHOOK_SERVER_SECRET)
        webhook_request_headers.register(app, path=WEBHOOK_PATH)
        setup_application(app, dp, bot=bot)

        runner = web.AppRunner(app)
        await runner.setup()

        site = web.TCPSite(runner, host=WEBHOOK_SERVER_HOST, port=WEBHOOK_SERVER_PORT)
        await site.start()

        logger.info("Webhook started!")
        await asyncio.Event().wait()
    else:
        logger.info("Bot polling started!")
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
