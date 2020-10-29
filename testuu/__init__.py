import json
import aiohttp, aiofiles

async def load():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/Vincysuper07/StrapBot-testuu/main/qpowieurtyturiewqop.json") as req:
            with open("testù.json", "w") as file:
                file.write((await req.content.read()).decode("UTF-8"))
