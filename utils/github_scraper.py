import asyncio
from bs4 import BeautifulSoup
import re
from .github_endpoint import get_user_data

async def user_data(users):
    data = []

    coroutines = [get_user_data(user) for user in users]

    pages = await asyncio.gather(*coroutines)

    for page in pages:
        soup = BeautifulSoup(page, "html.parser")
        results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n", "")
        fullName = soup.find("title").text
        namelgth = len(fullName) - 8

        strfmt = re.sub("\s+", " ", results)
        c = strfmt.split()
        userBoard = f"{fullName[:namelgth]} {c[0]}"

        data.append(userBoard)

    return data
