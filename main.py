import asyncio
import time
import sys
import logging

from utils.github_scraper import fetch_user_data, UserDataProcessingError
from utils.board_sort import sort_data_by_commits
from utils.brainiacs_list import brainiacslist
from utils.generate_html import generate_html_table

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

    github_username = await brainiacslist()


    from utils.data_json import usersd_list
    SUSER = usersd_list("username") or None
     
    try:
        if SUSER:
            data_list, users_daily = await fetch_user_data(github_username.split(), SUSER)
        else:
            data_list = await fetch_user_data(github_username.split())

        lead_data = await sort_data_by_commits(data_list)

        end_time = time.time()


        if SUSER:
            sys.stdout.write(await generate_html_table(lead_data, users_daily))
        else:
            sys.stdout.write(await generate_html_table(lead_data))

        execution_time = end_time - start_time
        #logger.info(f"Execution time: {execution_time} seconds")

    except UserDataProcessingError as e:
        logger.error(f"Error processing user data: {e}")
    except Exception as e:
        logger.exception("Unexpected error occurred")

if __name__ == "__main__":
    asyncio.run(main())
