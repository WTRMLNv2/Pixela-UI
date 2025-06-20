# helpers.py
# Contains functions to make code easier to write and underst
from tkinter import Label, Button, Entry

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

def create_button(root, text: str, command: callable, bg: str = "#4CAF50", fg: str = "#FFFFFF", font: tuple = ("Arial", 16), pady:int = 10) -> Button:
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
    button.pack(pady=pady)
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

{
    "dark": {
        "bg": "#3f3f3f",
        "fg": "#FFFFFF",
        "green": "#4CAF50",
        "red": "#f44336"
    },
    "light": {
        "bg": "#DADADA",
        "fg": "#222222",
        "green": "#4CAF50",
        "red": "#f44336"
    },
    "midnight": {
        "bg": "#1e1e1e",
        "fg": "#c0caf5",
        "green": "#73d13d",
        "red": "#f5222d"
    },
    "pastel": {
        "bg": "#f2f1ef",
        "fg": "#3b3b3b",
        "green": "#a3d9a5",
        "red": "#f4a6a6"
    },
    "sepia": {
        "bg": "#f4ecd8",
        "fg": "#5b4636",
        "green": "#769c79",
        "red": "#cc5c57"
    },
    "ocean": {
        "bg": "#2e8b9c",
        "fg": "#e9f5f9",
        "green": "#66cdaa",
        "red": "#e75454"
    }
}