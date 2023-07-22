import aiohttp
from datetime import date, datetime

start_date = date(datetime.now().year, 1, 1)

class UserDataError(Exception):
    pass

async def get_user_data(user):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://github.com/%s?tab=overview&from=%s&to=%s" % (user, start_date, date.today())) as response:
                page = await response.text()

        # Check if the response status code indicates success (status code 200)
        if response.status != 200:
            raise UserDataError(f"Failed to fetch data for user '{user}'. Status Code: {response.status}")

        return page
    except aiohttp.ClientError as e:
        raise UserDataError(f"Error fetching data for user '{user}': {e}")