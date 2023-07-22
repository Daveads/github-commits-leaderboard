import aiohttp
from datetime import date, datetime

start_date = date(datetime.now().year, 1, 1)

async def get_user_data(user):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://github.com/%s?tab=overview&from=%s&to=%s" % (user, start_date, date.today())) as response:
            page = await response.text()

    return page