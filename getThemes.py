# getThemes.py
# Gets the themes as the user suggests.
import json

def load_theme(theme_name: str, file_path="themes.json", last_used_file="lastUsed_theme.json") -> dict:
    """
    Loads the specified theme from a JSON file.

    Args:
        theme_name (str): The name of the theme to load (e.g., "dark", "light").
        file_path (str): The path to the theme JSON file.

    Returns:
        dict: A dictionary containing the theme's color values.
    """
    with open(file_path, "r") as file:
        all_themes = json.load(file)
    
    theme = all_themes.get(theme_name)
    
    with open(last_used_file, "w") as file:
        json.dump({"lastUsedTheme": theme_name}, file)

    if theme is None:
        return None
    
    return theme


def load_last_theme(file_path: str = "themes.json") -> dict:
    """
    Loads the theme last used from the json file

    Args:
        file_path(str, optional): The file path you want to extract out of.
    Returns:
        lastUsed_theme (dict): A dict structured the same way as load_theme would give
    """
    with open(file_path, "r") as file:
        last_used_themeDict = json.load(file)
    last_used_theme = last_used_themeDict["lastUsedTheme"]
    return last_used_theme
