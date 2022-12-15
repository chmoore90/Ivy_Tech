"""
Program creates GUI where users can customize sundae's and milkshakes
Author: Chloe Moore
Class: SDEV 140-26J
Final Project
"""

import tkinter as tk
from tkinter import ttk


# GENERAL FUNCTIONS
def new_order():
    """Returns dictionary representing a new order, keys for every order item and values to be updated by the relevant input widgets."""

    return {
        "Name": tk.StringVar(),
        "Dessert": tk.StringVar(),
        "Size": tk.StringVar(),
        "Flavor 1": tk.StringVar(),
        "Flavor 2": tk.StringVar(),
        "Flavor 3": tk.StringVar(),
        "Topping 1": tk.StringVar(),
        "Topping 2": tk.StringVar(),
        "Topping 3": tk.StringVar(),
        "Nuts": tk.BooleanVar(),
        "Whip": tk.BooleanVar(),
        "Cherry": tk.BooleanVar(),
    }


def lets_go():
    """Checks value of 'Dessert' key, then initates corresponding page."""

    dessert = order_info["Dessert"].get()
    if dessert == "Sundae":
        init_sundae(sundae)
    if dessert == "Milkshake":
        init_milkshake(milkshake)


def toggle(check, flavor_menu, topping_menu):
    """Activates and deavtivates menus, depending on if the corresponding checkbotton is checked."""

    checked = check.get()

    if not checked:
        flavor_menu["state"] = "disabled"
        topping_menu["state"] = "disabled"
    if checked:
        flavor_menu["state"] = "normal"
        topping_menu["state"] = "normal"


def submit_order():
    """Prints dictionary of order information, then initiates thank you page."""

    for k, v in order_info.items():
        v = v.get()
        if v == "Choose one:":
            v = None
        print(f"{k}: {v}")

    init_thanks(thanks)


def configure_styles(scoops):
    """Creates a style that sets default settings for tkinter objects."""

    style = ttk.Style(scoops)

    # Sets background for all frames
    style.configure("TFrame", background="#fff391")

    # Default settings for all labels
    style.configure(
        "TLabel",
        anchor="center",
        background="#fff391",
        font=("Helvetica", 16),
        foreground="#551802",
        justify="center",
        padding=8,
        wraplength=700)

    # Overrides specified label settings when called
    style.configure(
        "banner.TLabel",
        font=("Ink Free", 32),
        padding=0,
        wraplength="")

    # Default settings for buttons (must be called directly)
    style.configure(
        "button.TLabel",
        background="#551802",
        font=("Ink Free", 20, "bold"),
        foreground="white",
        width=10)

    # Default settings for exit button (must be called directly)
    style.configure(
        "exit.TLabel",
        font=10
    )

    # Default for dynamic settings of buttons (must be called directly)
    style.map(
        "button.TLabel",
        background=[("pressed", "!disabled", "brown"), ("active", "brown")],
        foreground=[("pressed", "white"), ("active", "white")],
        relief=[("pressed", "sunken"), ("!pressed", "raised")])

    # Default for dynamic settings of the exit button (must be called directly)
    style.map(
        "exit.TLabel",
        background=[("pressed", "!disabled", "brown"), ("active", "brown")],
        foreground=[("pressed", "white"), ("active", "white")],
        relief=[("pressed", "sunken"), ("active", "raised")])

    # Default settings for optionmenus (does not apply to dropdown part)
    style.configure(
        "TMenubutton",
        background="white",
        font=("Helvetica", 16),
        width=15)

    # Default settings for checkbuttons
    style.configure(
        "TCheckbutton",
        background="#fff391",
        foreground="#551802",
        font=("Helvetica", 16),
        width=15)

    # Overrides width of checkbutton, sets width to 0
    style.configure("mini.TCheckbutton", width=0)

    # Default settings for radiobuttons
    style.configure(
        "TRadiobutton",
        background="#fff391",
        foreground="#551802",
        font=("Helvetica", 16),
        width=15)


# PAGE INITIALIZATION FUNCTIONS
def init_home(page):
    """Initiates home page and raises it."""

    # CREATE HOME PAGE OBJECTS

    # Text variables
    banner = "Welcome to Ike's Ice Cream Parlor!"  # Text for home page banner
    msg = "You can order sundaes and milkshakes from right here at your table! To begin, enter your name in the box below, then choose either Sundae or Milkshake."  # Text for home page paragraph
    name_msg = "This dessert is for:"  # Text for name entry prompt
    select_msg = "I want to order a:"  #  Text for dessert selection menu

    # Labels
    welcome_banner_label = ttk.Label(page, style="banner.TLabel", text=banner)  # Label object that displays home page banner text
    welcome_msg_label = ttk.Label(page, text=msg)  # Label object that displays home page paragraph text
    name_label = ttk.Label(page, text=name_msg)  # Label object that displays text to prompt user to use entry box
    select_label = ttk.Label(page, text=select_msg)  # Label object that displays text to prompt user to use selection menu

    # Entry box for user to enter their name
    name_entry = ttk.Entry(page, font=("Helvetica", 16), textvariable=order_info["Name"], width=20)

    # Selection menu
    options = ["Sundae", "Milkshake"]  # List of options
    home_menu = ttk.OptionMenu(page, order_info["Dessert"], "Choose one:", *options)  # Creates base menu
    home_menu["menu"].config(background="white", font=("Helvetica", 16))  # Configures settings for dropdown part of the menu

    # Button that takes user to order page
    go_button = ttk.Button(page, text="Let's Go!", style="button.TLabel", command=lets_go)


    # LAYOUT HOME PAGE OBJECTS

    # Row 1
    welcome_banner_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

    # Row 2
    welcome_msg_label.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=[0, 30])

    # Row 3
    name_label.grid(row=2, column=0, sticky="e", pady=[0, 8])
    name_entry.grid(row=2, column=1, sticky="w")

    # Row 4
    select_label.grid(row=3, column=0, sticky="e")
    home_menu.grid(row=3, column=1, sticky="w")

    # Row 5
    go_button.grid(row=4, column=0, columnspan=2, pady=[50, 0])

    # RAISE HOME PAGE
    page.tkraise()


def init_sundae(page):
    """Initiates and raises sundae order page"""

    # CREATE PAGE OBJECTS

    # Text variables
    banner = f"Let's make {order_info['Name'].get()}'s sundae!"
    msg = "Select up to 3 scoops of ice cream. You can pick one flavor and one topping per scoop. Then add on any number of extras. Hit 'Submit Order' when you're ready to order!"

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    flavors_label = ttk.Label(page, text="Choose your scoops...")
    toppings_label = ttk.Label(page, text="...and their toppings.")
    extras_label = ttk.Label(page, text="Add some extras:")

    # Flavor and topping dropdown optionmenus
    flavor1_menu = ttk.OptionMenu(page, order_info["Flavor 1"], "Choose one:", *flavors)
    flavor1_menu["menu"].config(background="white", font=("Helvetica", 16)) # settings for dropdown part of optionmenu
    flavor2_menu = ttk.OptionMenu(page, order_info["Flavor 2"], "Choose one:", *flavors)
    flavor2_menu["state"] = "disabled" # sets initial state of optionmenu to disabled
    flavor2_menu["menu"].config(background="white", font=("Helvetica", 16))
    flavor3_menu = ttk.OptionMenu(page, order_info["Flavor 3"], "Choose one:", *flavors)
    flavor3_menu["state"] = "disabled"
    flavor3_menu["menu"].config(background="white", font=("Helvetica", 16))
    toppings1_menu = ttk.OptionMenu(page, order_info["Topping 1"], "Choose one:", *toppings)
    toppings1_menu["menu"].config(background="white", font=("Helvetica", 16))
    toppings2_menu = ttk.OptionMenu(page, order_info["Topping 2"], "Choose one:", *toppings)
    toppings2_menu["state"] = "disabled"
    toppings2_menu["menu"].config(background="white",font=("Helvetica", 16))
    toppings3_menu = ttk.OptionMenu(page, order_info["Topping 3"], "Choose one:", *toppings)
    toppings3_menu["state"] = "disabled"
    toppings3_menu["menu"].config(background="white", font=("Helvetica", 16))

    # Checkbuttons for second and third flavor/topping optionmenus
    flavor2_var = tk.BooleanVar()
    flavor2_check = ttk.Checkbutton(page, style="mini.TCheckbutton", variable=flavor2_var, command=lambda: toggle(flavor2_var, flavor2_menu, toppings2_menu))
    flavor3_var = tk.BooleanVar()
    flavor3_check = ttk.Checkbutton(page, style="mini.TCheckbutton", variable=flavor3_var, command=lambda: toggle(flavor3_var, flavor3_menu, toppings3_menu))

    # Checkbuttons for extras
    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(page, text="Whipping Cream", variable=order_info["Whip"])
    cherry_check = ttk.Checkbutton(page, text="Cherry on Top", variable=order_info["Cherry"])

    # Button to submit order
    order_button = ttk.Button(page, text="Submit Order", style="button.TLabel", command=submit_order, width=15)


    # LAYOUT PAGE OBJECTS

    # Row 1
    banner_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Row 2
    msg_label.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=[0, 30])

    # Row 3
    flavors_label.grid(row=2, column=1, sticky="w")
    toppings_label.grid(row=2, column=3, sticky="e")

    # Row 4
    flavor1_menu.grid(row=3, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=3, column=2)
    toppings1_menu.grid(row=3, column=3)

    # Row 5
    flavor2_check.grid(row=4, column=0, sticky="e")
    flavor2_menu.grid(row=4, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=4, column=2)
    toppings2_menu.grid(row=4, column=3)

    # Row 6
    flavor3_check.grid(row=5, column=0, sticky="e")
    flavor3_menu.grid(row=5, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=5, column=2)
    toppings3_menu.grid(row=5, column=3)

    # Row 7
    extras_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=[20, 0])

    # Row 8
    nuts_check.grid(row=7, column=0, columnspan=2, sticky="w")
    whip_check.grid(row=7, column=1, columnspan=3, padx=[0, 110])
    cherry_check.grid(row=7, column=3, sticky="e")

    # Row 9
    order_button.grid(row=8, column=0, columnspan=4, pady=[50, 0])

    # RAISE PAGE
    page.tkraise()


def init_milkshake(page):
    """Initiates and raises milkshake order page"""

    # CREATE PAGE OBJECTS

    # Text variables
    banner = f"Let's make {order_info['Name'].get()}'s milkshake!"
    msg = "First, select a size and flavor. Then add on any number of extras that you want. Hit 'Submit Order' when you're ready to order."

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    size_label = ttk.Label(page, text="Choose your size:")
    flavor_label = ttk.Label(page, text="Choose your flavor:")
    extras_label = ttk.Label(page, text="Add some extras:")

    # Size radiobuttons
    small_radiob = ttk.Radiobutton(page, text="Small", value="Small", variable=order_info["Size"])
    large_radiob = ttk.Radiobutton(page, text="Large", value="Large", variable=order_info["Size"])

    # Flavor radiobuttons
    flavor1_radiob = ttk.Radiobutton(page, text="Chocolate", value="Chocolate", variable=order_info["Flavor 1"])
    flavor2_radiob = ttk.Radiobutton(page, text="Vanilla", value="Vanilla", variable=order_info["Flavor 1"])
    flavor3_radiob = ttk.Radiobutton(page,text="Strawberry",value="Strawberry",variable=order_info["Flavor 1"])

    # Extras checkbuttons
    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(page, text="Whipping Cream", variable=order_info["Whip"])
    cherry_check = ttk.Checkbutton(page, text="Cherry on Top", variable=order_info["Cherry"])

    # Button to submit order
    order_button = ttk.Button(page, text="Submit Order", style="button.TLabel", command=submit_order, width=15)


    # LAYOUT PAGE OBJECTS

    # Row 1
    banner_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Row 2
    msg_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=[0, 30])

    # Row 3
    size_label.grid(row=2, column=0, columnspan=2)
    flavor_label.grid(row=2, column=1, columnspan=2)

    # Row 4
    small_radiob.grid(row=3, column=0, columnspan=2)
    flavor1_radiob.grid(row=3, column=1, columnspan=2)

    # Row 5
    large_radiob.grid(row=4, column=0, columnspan=2)
    flavor2_radiob.grid(row=4, column=1, columnspan=2)

    # Row 6
    flavor3_radiob.grid(row=5, column=1, columnspan=2)

    # Row 7
    extras_label.grid(row=6, column=0, pady=[20, 0])

    # Row 8
    nuts_check.grid(row=7, column=0)
    whip_check.grid(row=7, column=1)
    cherry_check.grid(row=7, column=2)

    # Row 9
    order_button.grid(row=8, column=0, columnspan=3, pady=[50, 0])

    # RAISE PAGE
    page.tkraise()


def init_thanks(page):
    """Initiates and raises thank you page, then resets order info dictionary"""

    # CREATE APPLICATION OBJECTS

    # Text variables
    banner = f"Thank you {order_info['Name'].get()}! Your {order_info['Dessert'].get().lower()} will be ready soon."
    msg = "All you need to do now is wait! We will bring your dessert to you as soon as it's done. Return to the 'Home Page' to order something else."

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    thanks_img = tk.PhotoImage(file="thanks_kitty.png")
    thanks_kitty = ttk.Label(page, image=thanks_img, text="[Image of a cartoon kitten holding a thank you sign]")

    # Button to return to home page
    home_button = ttk.Button(page, text="Home Page", style="button.TLabel", command=lambda: init_home(home))


    # LAYOUT PAGE OBJECTS (four rows)

    banner_label.grid(row=0, column=0)
    msg_label.grid(row=1, column=0)
    thanks_kitty.grid(row=2, column=0, pady=[0, 30])
    home_button.grid(row=3, column=0)

    # RAISE PAGE
    page.tkraise()

    # RESET ORDER INFO DICTIONARY
    order_info.update(new_order())

# -------------------------------------------------------------------------------------------------------------------------------------------------
# SET UP OF ROOT APPLICATION AND BASE FRAMES

# ROOT
scoops = tk.Tk()
scoops.title("What's the Scoop?")
scoops.geometry("1200x800")
scoops.configure(background="#fff391")
scoops.resizable(True, True)
scoops.grid_anchor("n")


# SET UP LOGO FRAME (to display above main frame at all times)
logo_frame = ttk.Frame(scoops)
logo_frame.grid_anchor("n")  # sets grid default placement to top, center

# objects for logo frame
logo_img = tk.PhotoImage(file="ike_logo.png")
logo_label = ttk.Label(logo_frame, image=logo_img, text="\n[Ike's banner logo]    \n", style="banner.TLabel")
exit_button = ttk.Button(logo_frame,padding=5, text="Close", style="exit.TLabel", command=scoops.destroy)

# layout logo frame objects in logo frame
exit_button.grid(row=0, column=0, sticky="ne")
logo_label.grid(row=0, column=0, sticky="nsew")


# SET UP MAIN FRAME (to hold application pages)
main_frame = ttk.Frame(scoops)
main_frame.grid_anchor("n")

# create frames for application pages
home = ttk.Frame(main_frame)
sundae = ttk.Frame(main_frame)
milkshake = ttk.Frame(main_frame)
thanks = ttk.Frame(main_frame)

# place each page frame in identical position in main frame
for frame in (home, sundae, milkshake, thanks):
    frame.grid_anchor("n")
    frame.grid(row=0, column=0, sticky="nsew")


# LAYOUT LOGO AND MAIN FRAMES
logo_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid(row=1, column=0, sticky="nsew")


# INITIALIZATIONS
order_info = new_order()  # dictionary to hold order information
flavors = ["Chocolate", "Vanilla", "Strawberry"]  # list of ice cream flavors (both sundaes and milkshakes)
toppings = ["Chocolate Syrup", "Vanilla Syrup", "Caramel Syrup", "Strawberry Syrup", "Blueberry Syrup", "Raspberry Syrup"]  # list of toppings (sundaes only)
configure_styles(scoops)  # initializes default settings for application objects


# RUN APPLICATION

init_home(home)  # Raises home page to display first
scoops.mainloop()  # Runs tkinter mainloop
