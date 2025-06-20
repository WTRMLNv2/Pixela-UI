# getDate.py
# This script returns the current date in the format YYYY-MM-DD
from datetime import datetime

def get_current_date():
    """
    Returns the current date in the format YYYYMMDD.

    Args:
        None
    Returns:
        date (str): The current date formatted as YYYYMMDD.
    """
    return datetime.now().strftime("%Y%m%d")

def get_current_normal_date():
    """
    Returns the current date in the format DD-MM-YYYY.
    Args:
        None
    Returns:
        date (str): The current date formatted as DD-MM-YYYY.
    """
    return datetime.now().strftime("%d-%m-%Y")

def convert_normal_to_compact(date: str) -> str:
    """
    Returns the given date from DD-MM-YYYY to YYYYMMDD format
    Args:
        date (str): The date you want to convert
    Returns:
        converted_date (str): The date in YYYYMMDD format
    """
    date = str(date)
    try:
        datetime.strptime(date, "%d-%m-%Y")  # just for validation
        return datetime.strptime(date, "%d-%m-%Y").strftime("%Y%m%d")
    except Exception:
        return None
    
