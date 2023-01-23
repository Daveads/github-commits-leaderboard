#!/usr/bin/env python
import asyncio
from bs4 import BeautifulSoup
import re
import aiofiles
import aiohttp

import time
import cProfile

from datetime import date, datetime


start_date = date(datetime.now().year, 1,1)
profiler = cProfile.Profile()

async def userlist():
    async with aiofiles.open("challenger.txt", 'r') as f:
        text = await f.read()
    return text



async def get_user_data(user):
    async with aiohttp.ClientSession() as session:
            async with session.get("https://github.com/%s?tab=overview&from=%s&to=%s" % (user, start_date, date.today())) as response:
                page = await response.text()

    return page

async def user_data(users):
    data = []

    coroutines = [get_user_data(user) for user in users]

    pages = await asyncio.gather(*coroutines)

    for page in pages:

        soup = BeautifulSoup(page, "html.parser")

        results = soup.find("h2", {"class": "f4 text-normal mb-2"}).text.strip().replace("\n","")
    
        fullName = soup.find("title").text
        namelgth = len(fullName) - 8

        strfmt = re.sub("\s+", " ", results)

        c = strfmt.split()

        userBoard  = f"{fullName[:namelgth]} {c[0]}"
    
        data.append(userBoard)

    return data



def get_commit_per_user(data):
    commit_list = []
    for i in data:
        length = len(i.split()) - 1 
        commit_list.append(int(i.split()[length]))

    return commit_list




def leaderboard_sort(commits, data):
    for i in range(len(commits)):
        for j in range(len(commits) - 1):
            if commits[j] < commits[j + 1]:
                commits[j], commits[j + 1] = commits[j + 1], commits[j]
                data[j], data[j + 1] = data[j + 1], data[j]

    return data





async def main():


    start_time = time.time()

    githubusername = await userlist()

    
    #profiler.enable()
    data_list = await user_data(githubusername.split())
    #profiler.disable()

    commits = get_commit_per_user(data_list)

    Lead_data = leaderboard_sort(commits, data_list)

    end_time = time.time()

    print(f"  Username  >>>  Name  >>>  contributions in {datetime.now().year}")
    for count, i in enumerate(Lead_data):
        print(count, i)

    # performance issues
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
    #profiler.print_stats()

asyncio.run(main())


# asyncio.gather()
# requests-futures === concurrent.futures


# leaderboard_sort() quicksort or merge sort 
