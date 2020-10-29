import json
import aiohttp, aiofiles

async def load():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://raw.githubusercontent.com/Vincysuper07/StrapBot-testuu/master/qpowieurtyturiewqop.json") as req:
            async with aiofiles.open("testù.json", mode="w") as file:
                json.dump((await req.content.read()).decode("UTF-8"), file, indent=4)
