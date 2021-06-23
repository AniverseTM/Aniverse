from aniverse import create_app
import aiohttp
import asyncio


app = create_app()

async def launch_attr_config():
    app.client_session = aiohttp.ClientSession()
    app.api_cache = {}  # filled later


loop = asyncio.get_event_loop()
loop.run_until_complete(launch_attr_config())