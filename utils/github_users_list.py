import aiofiles
import os

async def userlist():
    root_path = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the current file's directory
    file_path = os.path.join(root_path, "../challenger.txt")  # Construct the correct relative path to challenger.txt
    async with aiofiles.open(file_path, 'r') as f:
        text = await f.read()
    return text
