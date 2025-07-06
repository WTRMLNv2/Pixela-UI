# UI.py
# This script manages the UI class, responsible for the UI of the app.
from tkinter import Tk, Label, Button, Entry, messagebox,StringVar ,Frame, Radiobutton, StringVar, colorchooser
from core import *
from getCreds import get_creds
from getDate import *
from helpers import *
from ChartViewer import open_chart
from getThemes import load_theme, load_last_theme, give_all_themes
from getKeyBinds import load_keybinds, apply_keybinds, format_keybinds
class UI:
    def __init__(self):
        self.root = Tk()
        self.selected_theme = StringVar(self.root, value="pastel")
        self.theme = load_last_theme()
        
        self.bg = self.theme["bg"]
        self.fg = self.theme["fg"]
        self.green = self.theme["green"]
        self.red = self.theme["red"]
        self.root.option_add("*background", self.bg)
        self.root.option_add("*foreground", self.fg) 
        self.root.title("Pixela Home Screen")
        self.root.geometry("800x700")
        self.root.configure(bg=self.bg)
        self.root.resizable(True, True)
        self.create_homeScreen()
        keybinds = load_keybinds()
        actions = {
            "open_pixel": lambda e: self.add_pixel(),
            "create_graph": lambda e: self.create_graph(),
            "create_user": lambda e: self.create_user(),
            "change_theme": lambda e: self.change_theme(),
            "go_home": lambda e: self.create_homeScreen()
        }
        apply_keybinds(self.root, keybinds, actions)
        self.root.mainloop()


    def clear_screen(self, new_title):
        """
        Clears the screen of all the elements on it and sets the title to the specified title
        Args:
            new_title (str): The new title to set the title of the screen to
        """
        self.root.title(new_title)
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_homeScreen(self):
        """
        Creates the home screen of the application after clearing all the elements on the screen
        """
        self.clear_screen("Pixela Home Screen")

        creds = get_creds()
        if not creds["username"]:
            self.create_user()
        
        else:
            label = create_label(self.root, text="Welcome to Pixela!", bg=self.bg, fg=self.fg, font_size=24)

            create_user_button = create_button(self.root, text="Create User", command=self.create_user, bg=self.green, fg=self.fg)

            create_graph_button = create_button(self.root, text="Create Graph", command=self.create_graph, bg=self.green, fg=self.fg)

            add_pixel_button = create_button(self.root, text="Add a new pixel", command=self.add_pixel, bg=self.green, fg=self.fg)

            open_chart_button = create_button(self.root, text="Open chart in browser", command=open_chart, bg=self.green, fg=self.fg)

            change_theme_button = create_button(self.root, text="Change Theme", command=self.change_theme, bg=self.green, fg=self.fg)
    
            view_shortcuts_button = create_button(self.root, text="View Shortcuts", command=self.viewShortcuts, bg=self.green, fg=self.fg)

            create_theme_button = create_button(self.root, text="Create New Theme", command=self.createTheme, bg=self.green, fg=self.fg)
    def create_user(self):
        """
        Creates the screen where the user can create an account.
        """
        self.clear_screen("Create New User")

        header = Label(self.root, text="Create New Pixela User", font=("Arial", 24), bg=self.bg, fg=self.fg)
        header.pack(pady=20)

        user_label = Label(self.root, text="Username:", font=("Arial", 16), bg=self.bg, fg=self.fg)
        user_label.pack(pady=(10, 0))
        userNameEntry = Entry(self.root, width=30, font=("Arial", 16), bg=self.bg)
        userNameEntry.pack(pady=5)

        token_label = Label(self.root, text="Token:", font=("Arial", 16), bg=self.bg, fg=self.fg)
        token_label.pack(pady=(10, 0))
        tokenEntry = Entry(self.root, width=30, font=("Arial", 16))
        tokenEntry.pack(pady=5)

        submitButton = create_button(root=self.root, text="Submit", command=lambda: self.submit_user(userNameEntry=userNameEntry, tokenEntry=tokenEntry), pady=20, bg=self.green, fg=self.fg)

        backButton = create_button(root=self.root, text="Back", bg=self.red, command=self.create_homeScreen, pady=0, fg=self.fg)
    def submit_user(self, userNameEntry, tokenEntry):
        userName = userNameEntry.get()
        token = tokenEntry.get()
        response = create_user(token=token, username=userName)
        if response["isSuccess"]:
            messagebox.showinfo("Success", "User created successfully!")
            update_creds(username=userName, tokenID=token)
        else:
            messagebox.showerror("Error", f"Failed to create user: {response['message']}")
        self.create_homeScreen()

    def viewShortcuts(self):
        self.clear_screen("View Shortcuts")
        shortcuts_all = load_keybinds()
        formattedKeybinds = format_keybinds(shortcuts_all)
        label = create_label(self.root, text="View Shortcuts", font_size=24, fg=self.fg, bg=self.bg, pady=24)
        shortcuts = create_label(self.root, text=formattedKeybinds, font_size=16, fg=self.fg, bg=self.bg)
        backButton = create_button(self.root, text="Back", command=self.create_homeScreen, bg=self.red, fg=self.fg, pady=20)

    def create_graph(self):
        self.clear_screen("Create Graph")

        Label(self.root, text="Create a New Graph", font=("Arial", 24), bg=self.bg, fg=self.fg).pack(pady=20)



        graphNameEntry = create_labeled_entry(self.root,"Graph Name:", bg=self.bg, fg=self.fg)
        graphIDEntry = create_labeled_entry(self.root,"Graph ID:", bg=self.bg, fg=self.fg)
        unitEntry = create_labeled_entry(self.root,"Unit:", bg=self.bg, fg=self.fg)
        typeEntry = create_labeled_entry(self.root,"Type (int/float):", bg=self.bg, fg=self.fg)
        timezoneEntry = create_labeled_entry(self.root,"Timezone:", bg=self.bg, fg=self.fg)
        timezoneEntry.insert(0, "Asia/Kolkata")

        # Color Selector
        Label(self.root, text="Choose Graph Color:", font=("Arial", 16), bg=self.bg, fg=self.fg).pack(pady=(15, 0))
        color_frame = Frame(self.root, bg=self.bg)
        color_frame.pack(pady=10)

        selected_color = StringVar(value="ajisai")

        colors = {
            "shibafu": "#00b300",   # green
            "momiji": "#ff4500",    # red-orange
            "sora": "#00bfff",      # blue
            "ichou": "#ffd700",     # yellow
            "ajisai": "#9370db",    # purple
            "kuro": "#222222"       # black
        }

        for name, hex_color in colors.items():
            radio = Radiobutton(color_frame, text=name, variable=selected_color, value=name,
                                font=("Arial", 10), bg=self.bg, fg=self.fg, selectcolor=self.bg, activebackground=self.bg)
            radio.pack(anchor="w", side="left", padx=5)

            box = Label(color_frame, bg=hex_color, width=2, height=1, relief="solid", bd=1)
            box.pack(anchor="w", side="left", padx=(0, 10))

        

        # Submit Button
        def submit_graph():
            name = graphNameEntry.get()
            graph_id = graphIDEntry.get()
            unit = unitEntry.get()
            data_type = typeEntry.get()
            tz = timezoneEntry.get() or "Asia/Kolkata"
            color = selected_color.get()

            creds = get_creds()
            username, token  = creds["username"], creds["tokenID"]
            result = create_graph(graph_id=graph_id, name=name, unit=unit, type=data_type, color=color, timezone=tz, token=token, username=username)

            if result.get("isSuccess"):
                update_creds(graphID=graph_id)
                messagebox.showinfo("Success", "Graph created successfully!")
                self.create_homeScreen()
            else:
                messagebox.showerror("Error", f"Graph creation failed:\n{result.get('message')}")

        submitButton = create_button(self.root, text="Submit", command=submit_graph, pady=20, bg=self.green, fg=self.fg)

        backButton = create_button(self.root, text="Back", command=self.create_homeScreen, bg=self.red, fg=self.fg, pady=0)
    
    def createTheme(self):
        self.clear_screen("Create New Theme")
        create_label(self.root, text="Create New Theme", font_size=24, fg=self.fg, bg=self.bg, pady=24)
        create_label(self.root, text="Enter the name of the theme", font_size=16, fg=self.fg, bg=self.bg, pady=10)
        themeNameEntry = create_labeled_entry(self.root, "Theme Name:", bg=self.bg, fg=self.fg)
        newBG = None
        newFG = None
        newGreen = None
        newRed = None
        def select_color(element: str):
            return colorchooser.askcolor(title=f"Select {element} color")[1]
        def setBg():
            nonlocal newBG
            newBG = select_color("BG")
        
        def setFG():
            nonlocal newFG
            newFG = select_color("Text Colour")
        
        def setGreen():
            nonlocal newGreen
            newGreen = select_color("Green")
        
        def setRed():
            nonlocal newRed
            newRed = select_color("Red")
        
        bgColorButton = create_button(self.root, text="Select Background Color", command=setBg, bg=self.green, fg=self.fg)
        fgColorButton = create_button(self.root, text="Select Text Color", command=setFG, bg=self.green, fg=self.fg)
        greenColorButton = create_button(self.root, text="Select Green Color", command=setGreen, bg=self.green, fg=self.fg)
        redColorButton = create_button(self.root, text="Select Red Color", command=setRed, bg=self.green, fg=self.fg)

        def submit():
            themeName = themeNameEntry.get()
            if not newBG or not newFG or not newGreen or not newRed or not themeName:
                messagebox.showerror(title="Error", message="Please fill all fields and pick all colors.")
                return
            addToJson(themeName, newGreen, newRed, newBG, newFG)
            themeJson = return_themesJson()
            if themeName in themeJson:
                messagebox.showinfo(title="Theme Added", message="Theme was successfully added")
                self.create_homeScreen()
        button_frame = Frame(self.root, bg=self.bg)
        submitButton = create_button(button_frame,text="Submit",command=submit,bg=self.green,fg=self.fg)

        backButton = create_button(button_frame,text="Back",command=self.create_homeScreen,bg=self.red,fg=self.fg,pady=10)
        button_frame.pack()

        
    def add_pixel(self):
        self.clear_screen("Add a new pixel")
        creds = get_creds()
        token = creds["tokenID"]
        username = creds["username"]
        normal_date = get_current_normal_date()
        headers =     headers = {
        "X-USER-TOKEN": token}
        dateLabeledEntry = create_labeled_entry(self.root, "Enter Date (Format it as DD-MM-YYYY)", bg=self.bg, fg=self.fg)
        dateLabeledEntry.insert(0, normal_date)

        graphIdEntry = create_labeled_entry(self.root, "Enter Your graph ID", bg=self.bg, fg=self.fg)
        graphIdEntry.insert(0, creds["graphID"])
        
        quantityEntry = create_labeled_entry(self.root, "Enter the quantity to add", bg=self.bg, fg=self.fg)
        
        def submit_pixel() -> dict:
            graph_id = creds["graphID"]
            quantity = quantityEntry.get()
            date = convert_normal_to_compact(dateLabeledEntry.get())
            if not date:
                messagebox.showerror(title="Invalid Date Format!", message=f"Invalid Date format! Please put the format as DD-MM-YYYY \n No spaces, dashes between them. \n like: {normal_date}")
                self.create_homeScreen()
                return
            response = add_pixel(graph_id=graph_id, headers=headers, quantity=quantity, date=date, username=username)
            if response.get("isSuccess"):
                messagebox.showinfo("Success", "Pixel added successfully!")
                self.create_homeScreen()
            else:
                messagebox.showerror("Error", f"Failed to add pixel:\n{response.get('message', 'Unknown error')}")


        pixelSubmit = create_button(self.root, text="Submit", command=submit_pixel, pady=20, bg=self.green, fg=self.fg)
        backButton = create_button(self.root, text="Back", command=self.create_homeScreen, bg=self.red, pady=0, fg=self.fg)

    def change_theme(self):
        self.clear_screen("Change Theme")

        Label(self.root, text="Choose a Theme:", font=("Arial", 20),
            bg=self.bg, fg=self.fg).pack(pady=20)

        # Create theme selector radio buttons
        theme_frame = Frame(self.root, bg=self.bg)
        theme_frame.pack(pady=10)

        themes = give_all_themes()
        for theme in themes:
            Radiobutton(
                theme_frame,
                text=theme,
                variable=self.selected_theme,
                value=theme,
                bg=self.bg,
                fg=self.fg,
                font=("Arial", 12),
                selectcolor=self.bg,
                activebackground=self.bg
            ).pack(anchor="w", padx=20)

        # Apply Button
        def apply_theme():
            # Load new theme from file
            selected = self.selected_theme.get()
            new_theme = load_theme(selected)

            # Update theme attributes
            self.theme = new_theme
            self.bg = new_theme["bg"]
            self.fg = new_theme["fg"]
            self.green = new_theme["green"]
            self.red = new_theme["red"]

            # Apply to root window
            self.root.option_add("*background", self.bg)
            self.root.option_add("*foreground", self.fg)
            self.root.configure(bg=self.bg)

            # Show success + refresh screen
            messagebox.showinfo("Theme Changed", f"Theme set to '{selected}'")
            self.create_homeScreen()

        Button(
            self.root,
            text="Apply Theme",
            command=apply_theme,
            bg=self.green,
            fg=self.fg,
            font=("Arial", 14)
        ).pack(pady=20)

        # Back Button
        Button(
            self.root,
            text="Back",
            command=self.create_homeScreen,
            bg=self.red,
            fg=self.fg,
            font=("Arial", 14)
        ).pack(pady=0)

if __name__ == "__main__":
    ui = UI()