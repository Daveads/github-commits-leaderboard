import asyncio
from bs4 import BeautifulSoup
import re
from .github_endpoint import get_user_data
from .duplicate import remove_duplicates
import datetime

current_date = datetime.datetime.now()  # Get the current date and time
current_date_str = current_date.strftime("%Y-%m-%d")


class UserDataProcessingError(Exception):
    pass


def parse_input_string(input_string):
    name, *details, number = input_string.split()
    details = ' '.join(details)
    first_open_bracket_index = details.find('(')
    first_close_bracket_index = details.find(')')
    if first_open_bracket_index != -1 and first_close_bracket_index != -1:
        details = details[:first_open_bracket_index] + details[first_open_bracket_index + 1:first_close_bracket_index] + details[first_close_bracket_index + 1:]
    return [name, details, number] if number else [name, details]


async def fetch_user_data(users, suser=None):
    data = []

    users_daily_commit ={}

    coroutines = [get_user_data(user) for user in remove_duplicates(users)]

    try:
        pages = await asyncio.gather(*coroutines)
    except Exception as e:
        raise UserDataProcessingError(f"Error fetching user data: {e}")

    current_commit = None

    for page in pages:
        try:
            soup = BeautifulSoup(page, "html.parser")
            results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n", "")

            fullName = soup.find("title").text
            name_length = len(fullName) - 8
            formatted_results = re.sub("\s+", " ", results)
            first_word = formatted_results.split()[0]
            user_data = f"{fullName[:name_length]} {first_word}"
            user_data = parse_input_string(user_data)

            for user in suser:          
                if user in user_data:

                    target_td = soup.find("td", {"data-date": f"{current_date_str}"})
                    if target_td:
                        span = target_td.find("span", {"class": "sr-only"})
                        current_commit = span.text.split()[0]

                        if current_commit == "No":
                            current_commit = 0
                        
                        from .daily_commit import add_user_commit
                        add_user_commit(user, current_commit, users_daily_commit)

            data.append(user_data)

        except Exception as e:
            raise UserDataProcessingError("Error processing user data")

    if suser:
        return data, users_daily_commit
    else:
        return data
