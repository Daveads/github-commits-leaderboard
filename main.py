import asyncio
import time
import cProfile
import sys
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

from utils.github_scraper import fetch_user_data, UserDataProcessingError
from utils.board_sort import sort_data_by_commits
from utils.github_users_list import userlist
from utils.generate_html import generate_html_table

load_dotenv(".env")
SUSER = os.getenv('username') or None

# Set up the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

async def main():
    start_time = time.time()

    github_username = await userlist()

    try:
        if SUSER:
            data_list, current_commit = await fetch_user_data(github_username.split(), SUSER)
        else:
            data_list = await fetch_user_data(github_username.split())

        lead_data = await sort_data_by_commits(data_list)

        end_time = time.time()

        if SUSER:
            sys.stdout.write(await generate_html_table(lead_data, current_commit))
        else:
            sys.stdout.write(await generate_html_table(lead_data))

        execution_time = end_time - start_time
        # logger.info(f"Execution time: {execution_time} seconds")

    except UserDataProcessingError as e:
        logger.error(f"Error processing user data: {e}")
    except Exception as e:
        logger.exception("Unexpected error occurred")

if __name__ == "__main__":
    asyncio.run(main())
