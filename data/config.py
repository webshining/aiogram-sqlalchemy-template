from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = env.str("WEBHOOK_URL", default=None)
WEBHOOK_PATH = env.str("WEBHOOK_PATH", default=None)
WEBHOOK_SERVER_HOST = env.str("WEBHOOK_SERVER_HOST", default=None)
WEBHOOK_SERVER_PORT = env.int("WEBHOOK_SERVER_PORT", default=None)
WEBHOOK_SERVER_SECRET = env.str("WEBHOOK_SERVER_SECRET", default=None)

RD_URI = env.str("RD_URI", default=None)

DB_USER = env.str("DB_USER", default=None)
DB_PASS = env.str("DB_PASS", default=None)
DB_NAME = env.str("DB_NAME", default=None)
DB_HOST = env.str("DB_HOST", default=None)
DB_PORT = env.int("DB_PORT", default=None)

DB_URI = env.str("DB_URI", default="sqlite+aiosqlite:///database.sqlite3")
if DB_HOST and DB_PORT and DB_USER and DB_PASS and DB_NAME:
    DB_URI = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

I18N_PATH = f"{DIR}/data/locales"
I18N_DOMAIN = "bot"
