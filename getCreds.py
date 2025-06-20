# getCreds.py
# This script retrieves the Pixela API credentials from a file.

import json
from pathlib import Path

def get_creds(file_name : str = "creds.json") -> dict:
    """
    Retrieves Pixela API credentials from a JSON file.
    Args:
        file_name (str): (optional) The name of the JSON file containing the credentials. Default set to "creds.json" - the original file in the folder.
    Returns:
        dict: A dictionary containing the Pixela API credentials.
    """
    basePath = Path(__file__).parent
    file_path = basePath / file_name
    try:
        with open(file_path, 'r') as file:
            creds = json.load(file)
            return creds
    except FileNotFoundError:
        return {"error": "Credentials file not found."}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON from credentials file."}
