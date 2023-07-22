#!/usr/bin/env python
import asyncio
import time
import cProfile
from datetime import datetime

from utils.github_scraper import user_data
from utils.board_sort import leaderboard_sort
from utils.github_users_list import userlist

profiler = cProfile.Profile()



def get_commit_per_user(data):
    commit_list = []
    for i in data:
        length = len(i.split()) - 1
        contributions = i.split()[length].replace(',', '')  # Remove commas from contributions string
        commit_list.append(int(contributions))
    return commit_list




async def main():
    start_time = time.time()

    githubusername = await userlist()
    #print(githubusername)

    data_list = await user_data(githubusername.split())

    commits = get_commit_per_user(data_list)

    Lead_data = leaderboard_sort(commits, data_list)

    end_time = time.time()

    print(f"  Username  >>>  Name  >>>  contributions in {datetime.now().year}")
    for count, i in enumerate(Lead_data):
        print(count, i)

    # performance issues
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())
