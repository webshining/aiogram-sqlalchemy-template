from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import PRODUCTION, TEST
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n

from data.config import DEV_SERVER, I18N_DOMAIN, I18N_PATH, RD_URI, TELEGRAM_BOT_TOKEN

session = AiohttpSession(api=TEST if DEV_SERVER else PRODUCTION)
bot = Bot(TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True), session=session)
if RD_URI:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis

    storage = RedisStorage(Redis.from_url(RD_URI))
else:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()
dp = Dispatcher(storage=storage)

i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext
