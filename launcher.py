import aniverse
import aiohttp
import asyncio

try:
    import uvloop # type: ignore
    uvloop.install()
    print("Uvloop set!")
except Exception as exc:
    print(f"Uvloop not found/Cannot be imported: {exc}")
    

app = aniverse.create_app()

async def launch_attr_config():
    app.client_session = aiohttp.ClientSession()
    app.api_cache = {}  # filled later


loop = asyncio.get_event_loop()
loop.run_until_complete(launch_attr_config())
app.run("localhost", 8000, loop = loop)
