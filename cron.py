#!/usr/bin/env python
# 59 22 * * * /usr/bin/python3 /path/to/your_script.py  << 11:59pm
# */3 * * * * /usr/bin/python3 /path/to/your_script.py << 3min test

import asyncio
import os
import datetime
from dotenv import load_dotenv
from utils.email import send_email
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Set the log level to ERROR or the desired level


current_date = datetime.datetime.now()
current_date_str = current_date.strftime("%d-%m-%Y")


async def main():
    load_dotenv(".env")

    directory = os.getenv("directory")

    # Email values
    SENDER_EMAIL = os.getenv('sender_email')
    PASSWORD = os.getenv('sender_password')
    RECEIVER_EMAIL = [f"{os.getenv('receiver_email')}"]
    
    os.chdir(directory)

    process = await asyncio.create_subprocess_shell(
        "python3 main.py",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    output, _ = await process.communicate()
    output = output.decode()
    
    # Send email with the output
    await send_email(output, SENDER_EMAIL, PASSWORD, RECEIVER_EMAIL)
    
    output_dir = os.getenv("output_dir")

    output_file = os.path.join(output_dir, f"output_{current_date_str}.html")

    with open(output_file, "w") as file:
        file.write(output)

    os.chmod(output_file, 0o644)

if __name__ == "__main__":
    try:
        log_file = "error.log"  # Specify the desired log file path
        logging.basicConfig(filename=log_file, level=logging.ERROR)  # Configure logging to write ERROR level messages to the file

        asyncio.run(main())
    except Exception as e:
        logger.error(f"An error occurred: {e}")
