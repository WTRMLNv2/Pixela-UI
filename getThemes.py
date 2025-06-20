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


def load_last_theme(file_path = "themes.json") -> dict:
    """
    Loads the theme last used from the json file
    """