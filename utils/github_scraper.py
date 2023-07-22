import asyncio
from bs4 import BeautifulSoup
import re
from .github_endpoint import get_user_data

class UserDataProcessingError(Exception):
    pass

async def user_data(users):
    data = []
    
    coroutines = [get_user_data(user) for user in users]

    try:
        pages = await asyncio.gather(*coroutines)
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return []  # Return an empty list to signify that data fetching failed

    for page in pages:
        try:
            soup = BeautifulSoup(page, "html.parser")
            results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n", "")
            fullName = soup.find("title").text
            namelgth = len(fullName) - 8

            strfmt = re.sub("\s+", " ", results)
            c = strfmt.split()
            userBoard = f"{fullName[:namelgth]} {c[0]}"

            data.append(userBoard)
        except Exception as e:
            raise UserDataProcessingError("Error processing user data")  # Raise the custom exception

    return data
