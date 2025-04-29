# <p align="center">Aiogram SQLAlchemy Template</p>

### <p align="center"><a href="https://core.telegram.org/bots/api">Telegram Bot</a> template with <a href="https://docs.aiogram.dev/en/dev-3.x/">aiogram</a>, <a href="https://www.sqlalchemy.org/">SQLAlchemy</a> and <a href="https://www.docker.com/">docker</a></p>

## Technologies used:

-   Aiogram
-   Redis
-   SQLAlchemy
-   SQLite3
-   PostgreSQL
-   i18n
-   Docker and docker compose

## Navigate

-   [Getting started](#getting-started)
    -   [Init project](#init-project)
    -   [Configure environment variables](#configure-environment-variables)
        -   [Bot config](#bot-config)
        -   [Redis config](#redis-config)
        -   [Database config](#database-config)
    -   [Application start (local)](#application-start-local)
-   [Docker](#docker)
    -   [Application start (docker)](#application-start-docker)
    -   [View app logs](#view-app-logs)
    -   [Rebuild app](#rebuild-app)
    -   [Manage mongodb](#manage-mongodb)

## Getting started

### Init project

\#:/> `git clone https://github.com/webshining/aiogram-sqlalchemy-template project_name`<br>
\#:/> `cd project_name`<br>
\#:/project_name> `pip install -r requirements.txt`<br>

> if you have uv

\#:/project_name> `uv sync`

### Configure environment variables

> Copy variables from .env.ren file to .env

\#:/project_name> `cp .env.ren .env`

### Bot config

`TELEGRAM_BOT_TOKEN` - your bot token (required)

`I18N_DOMAIN` - locales file name

### Redis config

> If you are not using redis, by default used MemoryStorage

> RD_URI format<br>> `redis[s]://[[username][:password]@][host][:port][/db-number]`

`RD_URI` - connection url to your redis server

### Database config

> DB_URI format<br>> `dialect+driver://username:password@host:port/database`

`DB_USER` - your database username

`DB_PASS` - your database password

`DB_NAME` - your database name

`DB_HOST` - your database host

`DB_PORT` - your database port

> You can specify DB_URI instead of DB_USER, DB_PASS, DB_NAME, DB_HOST and DB_PORT

`DB_URI` - connection url to your database server

### Application start (local)

\#:/project_name> `python main.py`

> if you have make

\#:/project_name> `make run`

> if you have uv

\#:/project_name> `uv run main.py`

## Docker

### Application start (docker)

> Run only one service:<br>`$ docker-compose up -d service-name`

\#:/project_name> `docker compose up -d`

> If you have make you can enter

\#:/project_name> `make rebuild`

### View app logs

\#:/project_name> `docker-compose logs -f app`

> If you have make you can enter

\#:/project_name> `make logs`

### Rebuild app

\#:/project_name> `docker-compose up -d --build --no-deps --force-recreate`

> If you have make you can enter

\#:/project_name> `make rebuild`
