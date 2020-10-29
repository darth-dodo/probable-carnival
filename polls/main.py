from aiohttp import web
from db import close_pg, init_pg
from routes import setup_routes
from settings import config

app = web.Application()

setup_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
app["config"] = config
web.run_app(app)
