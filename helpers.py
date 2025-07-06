# helpers.py
# Contains functions to make code easier to write and underst
from tkinter import Label, Button, Entry
from json import load, dump, JSONDecodeError

def create_labeled_entry(root, label_text, bg, fg):
    """
    Creates a label and an entry using the specified text
    Args:
        label_text(str): The text to put in the label
    Returns:
        entry (object): An Entry object placed under the label
    """
    Label(root, text=label_text, font=("Arial", 16), bg=bg, fg=fg).pack(pady=(10, 0))
    entry = Entry(root, width=30, font=("Arial", 16), bg=bg, fg=fg)
    entry.pack(pady=5)
    return entry

def create_button(root, text: str, command: callable, bg: str = "#4CAF50", fg: str = "#FFFFFF", font: tuple = ("Arial", 16), pady:int = 10, packSide = "top") -> Button:
    """
    Creates a button using the specified text
    Args: 
        text (str): The text to put in the button
        command (function): The command to use when button pressed
        bg (str): The background color of the button
        fg (str): The text color of the button
        font (tuple): The font and text size of the text
        pady (int): The padding on the y axis

    Returns:
        button (Button): The button asked for
    """
    button = Button(root, text=text, font=font, bg=bg, fg=fg, command=command)
    button.pack(side=packSide, pady=pady)
    return button

def create_label(root, text: str, font_size, fg: str = "#FFFFFF", pady: int = 10, font:str = "Arial", bg: str = "#3F3F3F") -> object:
    """
    Creates and returns a Tkinter Label widget with the specified text, font size, and optional styling.

    Args:
        root: The parent widget where the Label will be placed.
        text (str): The text to be displayed inside the Label.
        font_size: The size of the font (e.g., 16 for Arial 16).
        fg (str, optional): The foreground (text) color. Defaults to white ("#FFFFFF").
        pady (int, optional): The vertical padding to apply when packing the Label. Defaults to 10.
        font (str, optional): The font you want in the text. Defaults to Arial
        bg (str, optional): The bg color you want. Defaults to "#3F3F3F"

    Returns:
        Label: A configured Tkinter Label widget ready to be packed or placed in the UI.
    """
    font_ = (font, font_size)
    label = Label(master=root, text=text, font=font_, fg=fg, bg=bg)
    label.pack(pady=pady)

def return_themesJson():
    """
    Reads and returns the content of 'themes.json'.

    Returns:
        dict: Dictionary containing all themes from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        JSONDecodeError: If the file is empty or contains invalid JSON.
    """
    with open("themes.json", "r") as file:
        all_themes = load(file)
    return all_themes

def dumpToJson(theme_name, theme_data, file_path="themes.json"):
    """
    Adds or updates a theme in the JSON file.

    Args:
        theme_name (str): The name of the theme.
        theme_data (dict): A dictionary with theme data (e.g., bg, fg, green, red).
        file_path (str, optional): The JSON file path. Defaults to "themes.json".
    """
    try:
        with open(file_path, "r") as file:
            themes = load(file)
    except (FileNotFoundError, JSONDecodeError):
        themes = {}

    themes[theme_name] = theme_data  # Add or overwrite

    with open(file_path, "w") as file:
        dump(themes, file, indent=4)


def addToJson(theme_name, green, red, bg, fg, file_path="themes.json"):
    """
    Adds a new theme to the JSON file only if it does not already exist.

    Args:
        theme_name (str): Name of the theme.
        green (str): Hex color for 'green'.
        red (str): Hex color for 'red'.
        bg (str): Hex background color.
        fg (str): Hex foreground/text color.
        file_path (str, optional): The JSON file path. Defaults to "themes.json".
    """
    try:
        with open(file_path, "r") as file:
            themes = load(file)
    except (FileNotFoundError, JSONDecodeError):
        themes = {}

    if theme_name not in themes:
        themes[theme_name] = {"bg": bg, "fg": fg, "green": green, "red": red}  # Add only if it doesn't exist

    with open(file_path, "w") as file:
        dump(themes, file, indent=4)
# addToJson("default", "#4CAF50", "#F44336", "#3F3F3F", "#FFFFFF")  # For test
