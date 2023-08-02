import aiofiles
import os

class UserListError(Exception):
    pass

async def brainiacslist():
    root_path = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the current file's directory
    file_path = os.path.join(root_path, f"../brainiacs.txt")  # Construct the correct relative path to challenger.txt

    try:
        async with aiofiles.open(file_path, 'r') as f:
            text = await f.read()
        return text
    except FileNotFoundError as e:
        raise UserListError(f"File 'challenger.txt' not found: {e}")
    
    except Exception as e:
        raise UserListError(f"Error reading 'challenger.txt': {e}")