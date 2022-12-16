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
    """Returns dictionary with blank string variable values. keys are order info fields, values are updated by input widgets."""

    return {
        "Name": tk.StringVar(value=f"Table {table_number}"),  # Sets default value for name field to the table number
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
    """Checks value of 'Dessert' key and initates corresponding page. Doesn't run if no option is selected"""

    # shortens name input if over 25 characters to first 25 characters
    name = order_info["Name"].get()
    if len(name) > 25:
        order_info["Name"].set(name[:25])

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


def validate(check2=None, check3=None):
    """Prints dictionary of order information, then initiates thank you page. Only runs when all validation logic passes"""

    #if flavor 2 or 3 menu is deselected, sets flavor and toppings values to defaults/none
    if check2 is not None:
        if not check2.get():
            order_info["Flavor 2"].set("Choose one:")
            order_info["Topping 2"].set(None)

    if check3 is not None:
        if not check3.get():
            order_info["Flavor 3"].set("Choose one:")
            order_info["Topping 3"].set(None)

    if order_info["Flavor 1"].get() in flavors:  # Checks if flavor 1 is a valid flavor option
        if (check2.get() and order_info["Flavor 2"].get() in flavors) or not check2.get():  # Checks flavor 2 is either checked AND valid, or unchecked
            if (check3.get() and order_info["Flavor 3"].get() in flavors) or not check3.get():  # Checks flavor 3 is either checked AND valid, or unchecked

                init_thanks(thanks)  # raises thank you page

    else:
        return  # Returns None if any validation fails (to user, nothing happens)


def submit():
    """Prints dictionary of order information, then initiates home page."""

    for k, v in order_info.items():
        v = v.get()
        if v == "Choose one:": # sets value to None if user did not make a selection
            v = None
        print(f"{k}: {v}")

    init_home(home)


def configure_styles(scoops):
    """Creates a style that sets default settings for tkinter objects."""

    style = ttk.Style(scoops)

    # Sets background for all frames
    style.configure("TFrame", background="#fff391")
    # Sets frame background to light yellow when called
    style.configure("confirmation.TFrame", background="light yellow")

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

    # Sets label background to light yellow when called
    style.configure("confirmation.TLabel", background="light yellow")

    # Default settings for buttons (must be called directly)
    style.configure(
        "button.TLabel",
        background="#551802",
        font=("Ink Free", 20, "bold"),
        foreground="white",
        width=10)

    # Default font for exit button (must be called directly)
    style.configure("exit.TLabel", font=10)

    # Default for dynamic settings for buttons (must be called directly)
    style.map(
        "button.TLabel",
        background=[("pressed", "!disabled", "brown"), ("active", "brown")],
        foreground=[("pressed", "white"), ("active", "white")],
        relief=[("pressed", "sunken"), ("!pressed", "raised")])

    # Default for dynamic settings for exit button (must be called directly)
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

    # Overrides width of checkbutton, sets to 0
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

    # Clears frame and resets order dictionary
    for widget in page.winfo_children():
        widget.destroy()
    order_info.update(new_order())

    # CREATE HOME PAGE OBJECTS

    # Text variables
    banner = "Welcome to Ike's Ice Cream Parlor!"  # Text for home page banner
    msg = "You can order sundaes and milkshakes from right here at your table! Simply enter your name in the box below, then select the dessert you'd like to order from the dropdown menu. Click \"Let's Go\" to continue."  # Text for home page paragraph
    name_msg = "My name is:"  # Text for name entry prompt
    select_msg = "I want to order a:"  #  Text for dessert selection menu

    # Labels
    welcome_banner_label = ttk.Label(page, style="banner.TLabel", text=banner)  # Banner text
    welcome_msg_label = ttk.Label(page, text=msg)  # Paragraph text
    name_label = ttk.Label(page, text=name_msg)  # Prompt for user to use entry box
    select_label = ttk.Label(page, text=select_msg)  # Prompt for user to use selection menu

    # Entry box for user to enter their name
    name_entry = ttk.Entry(page, font=("Helvetica", 16), textvariable=order_info["Name"], width=20)

    # Selection menu
    options = ["Sundae", "Milkshake"]  # List of dessert options
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
    msg = "You can order up to 3 scoops. Each scoop is one flavor and can have one topping. Click the checkboxes to add a scoop. Don't forget to add on any extras you want! Click \"Submit Order\" when you're done."

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    flavors_label = ttk.Label(page, text="Choose your scoops...")
    toppings_label = ttk.Label(page, text="...and their toppings.")
    extras_label = ttk.Label(page, text="Add your extras:")

    # Flavor and topping dropdown optionmenus
    flavor1_menu = ttk.OptionMenu(page, order_info["Flavor 1"], "Choose one:", *flavors)
    flavor1_menu["menu"].config(background="white", font=("Helvetica", 16))
    flavor2_menu = ttk.OptionMenu(page, order_info["Flavor 2"], "Choose one:", *flavors)
    flavor2_menu["state"] = "disabled" # sets initial state of optionmenu to disabled
    flavor2_menu["menu"].config(background="white", font=("Helvetica", 16))
    flavor3_menu = ttk.OptionMenu(page, order_info["Flavor 3"], "Choose one:", *flavors)
    flavor3_menu["state"] = "disabled"
    flavor3_menu["menu"].config(background="white", font=("Helvetica", 16))
    toppings1_menu = ttk.OptionMenu(page, order_info["Topping 1"], "None", *toppings)
    toppings1_menu["menu"].config(background="white", font=("Helvetica", 16))
    toppings2_menu = ttk.OptionMenu(page, order_info["Topping 2"], "None", *toppings)
    toppings2_menu["state"] = "disabled"
    toppings2_menu["menu"].config(background="white",font=("Helvetica", 16))
    toppings3_menu = ttk.OptionMenu(page, order_info["Topping 3"], "None", *toppings)
    toppings3_menu["state"] = "disabled"
    toppings3_menu["menu"].config(background="white", font=("Helvetica", 16))

    # Checkbuttons for flavor/topping optionmenus
    flavor1_check = ttk.Label(page, text=u'\u2611', padding=0)  # Pseudo checkbox, can't be unchecked (since flavor 1 must have a value)
    flavor2_var = tk.BooleanVar()
    flavor2_check = ttk.Checkbutton(page, style="mini.TCheckbutton", variable=flavor2_var, command=lambda: toggle(flavor2_var, flavor2_menu, toppings2_menu))
    flavor3_var = tk.BooleanVar()
    flavor3_check = ttk.Checkbutton(page, style="mini.TCheckbutton", variable=flavor3_var, command=lambda: toggle(flavor3_var, flavor3_menu, toppings3_menu))

    # Checkbuttons for extras
    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(page, text="Whipping Cream", variable=order_info["Whip"])
    cherry_check = ttk.Checkbutton(page, text="Cherry on Top", variable=order_info["Cherry"])

    # Button to validate order information. If validations pass, validate function will raise next page
    order_button = ttk.Button(page, text="Submit Order", style="button.TLabel", command=lambda : validate(flavor2_var, flavor3_var) , width=15)


    # LAYOUT PAGE OBJECTS

    # Row 1
    banner_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

    # Row 2
    msg_label.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=[0, 30])

    # Row 3
    flavors_label.grid(row=2, column=1, sticky="w")
    toppings_label.grid(row=2, column=3, sticky="e")

    # Row 4
    flavor1_check.grid(row=3, column=0, sticky="e")
    flavor1_menu.grid(row=3, column=1, sticky="w")
    ttk.Label(page, text="--- with ---     ").grid(row=3, column=2)
    toppings1_menu.grid(row=3, column=3)

    # Row 5
    flavor2_check.grid(row=4, column=0, sticky="e")
    flavor2_menu.grid(row=4, column=1, sticky="w")
    ttk.Label(page, text="--- with ---     ").grid(row=4, column=2)
    toppings2_menu.grid(row=4, column=3)

    # Row 6
    flavor3_check.grid(row=5, column=0, sticky="e")
    flavor3_menu.grid(row=5, column=1, sticky="w")
    ttk.Label(page, text="--- with ---     ").grid(row=5, column=2)
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
    msg = "Select the size you'd like from the left column and select your flavor from the right. Don't forget to add on any extras you want! Click \"Submit Order\" when you're done."

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    size_label = ttk.Label(page, text="Choose your size:")
    flavor_label = ttk.Label(page, text="Choose your flavor:")
    extras_label = ttk.Label(page, text="Add some extras:")

    # Size radiobuttons
    small_radiob = ttk.Radiobutton(page, text="Small", value="Small", variable=order_info["Size"])
    large_radiob = ttk.Radiobutton(page, text="Large", value="Large", variable=order_info["Size"])
    order_info["Size"].set("Small")  # sets default size value to small

    # Flavor radiobuttons
    flavor1_radiob = ttk.Radiobutton(page, text="Chocolate", value="Chocolate", variable=order_info["Flavor 1"])
    flavor2_radiob = ttk.Radiobutton(page, text="Vanilla", value="Vanilla", variable=order_info["Flavor 1"])
    flavor3_radiob = ttk.Radiobutton(page,text="Strawberry",value="Strawberry",variable=order_info["Flavor 1"])
    order_info["Flavor 1"].set(flavors[0])  # sets default flavor selection to the first option

    # Extras checkbuttons
    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(page, text="Whipping Cream", variable=order_info["Whip"])
    cherry_check = ttk.Checkbutton(page, text="Cherry on Top", variable=order_info["Cherry"])

    # Button to go to thanks page. Skips validation function since all values have defaults or can be left blank
    order_button = ttk.Button(page, text="Submit Order", style="button.TLabel", command=lambda: init_thanks(thanks), width=15)


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

    # Clears frame of all existing widgets
    for widget in page.winfo_children():
        widget.destroy()

    # CREATE APPLICATION OBJECTS

    # Text variables
    banner = f"Thank you {order_info['Name'].get()}! Your {order_info['Dessert'].get().lower()} will be ready soon."
    msg = "Please check the list below to make sure we've got everything right. If there's a mistake, click \"Return Home\" to start again. If it looks good, click \"Submit Order\" and we will bring your dessert to you as soon as it's done.\n Clicking either button will return you to the home page."

    # Labels
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    thanks_kitty_label = ttk.Label(page, text="[Image of a cartoon kitten holding up a thank you sign]")
    thanks_kitty_label.image = tk.PhotoImage(file="thanks_kitty.png")  # have to make image an attributge of thanks_label, otherwise gets garbage collected (because inside a function)
    thanks_kitty_label.configure(image=thanks_kitty_label.image)  # tells label to call thanks_kitty as its image
    go_home_label = ttk.Label(page, text="Your order will not be submitted.", font=12)

    # Order Confirmation Frame
    order_conf = ttk.Frame(page, style="confirmation.TFrame")

    t_f = {True : "Yes", False: "No"}  # dictionary to change True/False values to "Yes"/"No"

    # Row 1
    name = ttk.Label(order_conf, text=f"Name: {order_info['Name'].get()}", style="confirmation.TLabel").grid(row=0, column=0, sticky="w")
    dessert = ttk.Label(order_conf, text=f"Dessert: {order_info['Dessert'].get()}", style="confirmation.TLabel").grid(row=0, column=1, sticky="w")

    # Displays if dessert is a sundae
    if order_info["Dessert"].get() == "Sundae":
        # Row 2
        flavor1 = ttk.Label(order_conf, text=f"Flavor 1: {order_info['Flavor 1'].get()}", style="confirmation.TLabel").grid(row=1, column=0, sticky="w")
        topping1 = ttk.Label(order_conf, text=f"Topping 1: {order_info['Topping 1'].get()}", style="confirmation.TLabel").grid(row=1, column=1, sticky="w")
        # Row 3. Only one if/elif statement will run, depends on if flavor 2 is unchecked
        if order_info["Flavor 2"].get() == "Choose one:":
            flavor2 = ttk.Label(order_conf, text=f"Flavor 2: ---", style="confirmation.TLabel").grid(row=2, column=0, sticky="w")
            topping2 = ttk.Label(order_conf, text=f"Topping 2: ---", style="confirmation.TLabel").grid(row=2, column=1, sticky="w")
        elif order_info["Flavor 2"].get() != "Choose one:":
            flavor2 = ttk.Label(order_conf, text=f"Flavor 2: {order_info['Flavor 2'].get()}", style="confirmation.TLabel").grid(row=2, column=0, sticky="w")
            topping2 = ttk.Label(order_conf, text=f"Topping 2: {order_info['Topping 2'].get()}", style="confirmation.TLabel").grid(row=2, column=1, sticky="w")
        # Row 4. Only one if/elif statement will run, depends on if flavor 3 is unchecked
        if order_info["Flavor 3"].get() == "Choose one:":
            flavor3 = ttk.Label(order_conf, text=f"Flavor 3: ---", style="confirmation.TLabel").grid(row=3, column=0, sticky="w")
            topping1 = ttk.Label(order_conf, text=f"Topping 3: ---", style="confirmation.TLabel").grid(row=3, column=1, sticky="w")
        elif order_info["Flavor 3"].get() != "Choose one:":
            flavor3 = ttk.Label(order_conf, text=f"Flavor 3: {order_info['Flavor 3'].get()}", style="confirmation.TLabel").grid(row=3, column=0, sticky="w")
            topping3 = ttk.Label(order_conf, text=f"Topping 3: {order_info['Topping 3'].get()}", style="confirmation.TLabel").grid(row=3, column=1, sticky="w")
        # Row 5
        nuts = ttk.Label(order_conf, text=f"Nuts: {t_f[order_info['Nuts'].get()]}", style="confirmation.TLabel").grid(row=4, column=0, sticky="w")
        # Row 6
        whip = ttk.Label(order_conf, text=f"Whipping Cream: {t_f[order_info['Whip'].get()]}", style="confirmation.TLabel").grid(row=4, column=1, sticky="w")
        # Row 7
        cherry = ttk.Label(order_conf, text=f"Cherry on Top: {t_f[order_info['Cherry'].get()]}", style="confirmation.TLabel").grid(row=5, column=0, sticky="w")

    # Displays if dessert was a milkshake.
    # Rows 2-6
    elif order_info["Dessert"].get() == "Milkshake":
        size = ttk.Label(order_conf, text=f"Size: {order_info['Size'].get()}", style="confirmation.TLabel").grid(row=1, column=0, columnspan=2, sticky="w")
        flavor = ttk.Label(order_conf, text=f"Flavor: {order_info['Flavor 1'].get()}", style="confirmation.TLabel").grid(row=2, column=0, columnspan=2, sticky="w")
        nuts = ttk.Label(order_conf, text=f"Nuts: {t_f[order_info['Nuts'].get()]}", style="confirmation.TLabel").grid(row=3, column=0, sticky="w")
        whip = ttk.Label(order_conf, text=f"Whipping Cream: {t_f[order_info['Whip'].get()]}", style="confirmation.TLabel").grid(row=4, column=0, sticky="w")
        cherry = ttk.Label(order_conf, text=f"Cherry on Top: {t_f[order_info['Cherry'].get()]}", style="confirmation.TLabel").grid(row=5, column=0, sticky="w")

    # Buttons
    home_button = ttk.Button(page, text="Return Home", style="button.TLabel", width=12, command=lambda: init_home(home))  # return to homepage without submitting order
    submit_button = ttk.Button(page, text="Submit Order", style="button.TLabel", width=20, command=submit)  # submit order, then return to homepage


    # LAYOUT PAGE OBJECTS (five rows)

    banner_label.grid(row=0, column=0, columnspan=2)
    msg_label.grid(row=1, column=0, columnspan=2)
    order_conf.grid(row=2, column=0)
    thanks_kitty_label.grid(row=2, column=1, pady=[0,30])
    home_button.grid(row=3, column=1)
    submit_button.grid(row=3, column=0)
    go_home_label.grid(row=4, column=1)

    # RAISE PAGE
    page.tkraise()


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
exit_button = ttk.Button(logo_frame, padding=5, text="Close", style="exit.TLabel", command=scoops.destroy)

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
flavors = ["Chocolate", "Vanilla", "Strawberry"]  # list of ice cream flavors (both sundaes and milkshakes)
toppings = ["None", "Chocolate Syrup", "Vanilla Syrup", "Caramel Syrup", "Strawberry Syrup", "Blueberry Syrup", "Raspberry Syrup"]  # list of toppings (sundaes only)
table_number = 1


# set up dictionary and style
order_info = new_order()  # dictionary to hold order information
configure_styles(scoops)  # initializes default settings for application objects


# RUN APPLICATION
init_home(home)  # Raises home page to display first
scoops.mainloop()  # Runs tkinter mainloop
