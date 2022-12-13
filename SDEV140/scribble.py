"""
Program creates GUI where users can customize sundae's and milkshakes
Author: Chloe Moore
Class: SDEV 140-26J
Final Project
"""

import tkinter as tk
from tkinter import ttk


def lets_go():
    """Determines which frame to raise and calls that function"""
    dessert = order_info["Dessert"].get()
    if dessert == "Sundae":
        init_sundae()
        sundae.tkraise()
    if dessert == "Milkshake":
        init_milkshake()
        milkshake.tkraise()


def toggle(check, flavor_menu, topping_menu):

    checked = check.get()
    if not checked:
        flavor_menu["state"] = "disabled"
        topping_menu["state"] = "disabled"
    if checked:
        flavor_menu["state"] = "normal"
        topping_menu["state"] = "normal"


def submit_order():
    for k, v in order_info.items():
        v = v.get()
        if v == "Choose one:":
            v = None
        print(f"{k}: {v}")

    thanks.tkraise()


def init_sundae():
    """Logic for creating, populating sundae order page"""
    banner = f"Let's make {order_info['Name'].get()}'s sundae!"
    msg = "Do things to get stuff."

    banner_label = ttk.Label(sundae, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(sundae, text=msg)
    flavors_label = ttk.Label(sundae, text="Choose your scoops...")
    toppings_label = ttk.Label(sundae, text="...and their toppings.")
    extras_label = ttk.Label(sundae, text="Add some extras:")

    flavor1_menu = ttk.OptionMenu(
        sundae, order_info["Flavor 1"], "Choose one:", *flavors
    )
    flavor1_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    flavor2_menu = ttk.OptionMenu(
        sundae, order_info["Flavor 2"], "Choose one:", *flavors
    )
    flavor2_menu["state"] = "disabled"
    flavor2_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    flavor3_menu = ttk.OptionMenu(
        sundae,
        order_info["Flavor 3"],
        "Choose one:",
        *flavors,
    )
    flavor3_menu["state"] = "disabled"
    flavor3_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    toppings1_menu = ttk.OptionMenu(
        sundae, order_info["Topping 1"], "Choose one:", *toppings
    )
    toppings1_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    toppings2_menu = ttk.OptionMenu(
        sundae, order_info["Topping 2"], "Choose one:", *toppings
    )
    toppings2_menu["state"] = "disabled"
    toppings2_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    toppings3_menu = ttk.OptionMenu(
        sundae, order_info["Topping 3"], "Choose one:", *toppings
    )
    toppings3_menu["state"] = "disabled"
    toppings3_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )

    flavor2_var = tk.BooleanVar()
    flavor2_check = ttk.Checkbutton(
        sundae,
        style="mini.TCheckbutton",
        variable=flavor2_var,
        command=lambda: toggle(flavor2_var, flavor2_menu, toppings2_menu),
    )
    flavor3_var = tk.BooleanVar()
    flavor3_check = ttk.Checkbutton(
        sundae,
        style="mini.TCheckbutton",
        variable=flavor3_var,
        command=lambda: toggle(flavor3_var, flavor3_menu, toppings3_menu),
    )

    nuts_check = ttk.Checkbutton(sundae, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(
        sundae, text="Whipping Cream", variable=order_info["Whip"]
    )
    cherry_check = ttk.Checkbutton(
        sundae, text="Cherry on Top", variable=order_info["Cherry"]
    )

    order_button = ttk.Button(
        sundae,
        text="Submit Order",
        style="button.TLabel",
        command=submit_order,
        width=15,
    )

    # LAYOUTS

    banner_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    msg_label.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=[0, 30])

    flavors_label.grid(row=2, column=1, sticky="w")
    toppings_label.grid(row=2, column=3, sticky="e")

    flavor1_menu.grid(row=3, column=1, sticky="e")
    ttk.Label(sundae, text="with").grid(row=3, column=2)
    toppings1_menu.grid(row=3, column=3)

    flavor2_check.grid(row=4, column=0, sticky="e")
    flavor2_menu.grid(row=4, column=1, sticky="e")
    ttk.Label(sundae, text="with").grid(row=4, column=2)
    toppings2_menu.grid(row=4, column=3)

    flavor3_check.grid(row=5, column=0, sticky="e")
    flavor3_menu.grid(row=5, column=1, sticky="e")
    ttk.Label(sundae, text="with").grid(row=5, column=2)
    toppings3_menu.grid(row=5, column=3)

    extras_label.grid(row=6, column=1, columnspan=2, sticky="w", pady=[20, 0])
    nuts_check.grid(row=7, column=1, columnspan=2, sticky="w")
    whip_check.grid(row=7, column=1, columnspan=2, sticky="e")
    cherry_check.grid(row=7, column=3, sticky="w")

    order_button.grid(row=8, column=0, columnspan=4, pady=[50, 0])


def init_milkshake():
    """Logic for creating, populating milkshake order page"""
    banner = f"Let's make {order_info['Name'].get()}'s milkshake!"
    msg = "Do things to get stuff."

    banner_label = ttk.Label(milkshake, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(milkshake, text=msg)

    banner_label.grid(row=0, column=0)
    msg_label.grid(row=0, column=0)

    pass


def init_thanks():
    pass


# -------------------------------------------------------------------------------APPLICATION FRAMEWORK--------------------------------------------------
scoops = tk.Tk()
scoops.title("What's the Scoop?")
scoops.geometry("1200x800")
scoops.configure(background="#fff391")
scoops.resizable(True, True)
scoops.grid_anchor("n")

logo_frame = ttk.Frame(scoops)
main_frame = ttk.Frame(scoops)
logo_frame.grid_anchor("n")  # sets grid default placement to top, center
logo_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_anchor("n")
main_frame.grid(row=1, column=0, sticky="nsew")

home = ttk.Frame(main_frame)
sundae = ttk.Frame(main_frame)
milkshake = ttk.Frame(main_frame)
thanks = ttk.Frame(main_frame)

for frame in (home, sundae, milkshake, thanks):
    frame.grid_anchor("n")
    frame.grid(row=0, column=0, sticky="nsew")

logo_img = tk.PhotoImage(file="ike_logo.png")
logo_label = ttk.Label(logo_frame, image=logo_img)
exit_button = ttk.Button(
    logo_frame,
    padding=5,
    text="X",
    style="exit.TLabel",
    command=scoops.destroy,
)

exit_button.grid(row=0, column=0, sticky="ne")
logo_label.grid(row=0, column=0, sticky="nsew")


style = ttk.Style(scoops)
# sets defaults for all frame objects
style.configure(
    "TFrame",
    background="#fff391",
)
# sets defaults for all label and button objects
style.configure(
    "TLabel",
    anchor="center",
    background="#fff391",
    font=("Helvetica", 16),
    foreground="#551802",
    justify="center",
    padding=8,
    wraplength=700,
)
# overrides specified label settings when called
style.configure(
    "banner.TLabel",
    font=("Ink Free", 32),
    padding=0,
    wraplength="",
)
style.configure(
    "button.TLabel",
    background="#551802",
    font=("Ink Free", 20, "bold"),
    foreground="white",
    width=10,
)
# sets defaults for specified dynamic values (for all buttons)
style.map(
    "button.TLabel",
    background=[("pressed", "!disabled", "brown"), ("active", "brown")],
    foreground=[("pressed", "white"), ("active", "white")],
    relief=[("pressed", "sunken"), ("!pressed", "raised")],
)
# sets defaults for specified dynamic values (for exit button)
style.map(
    "exit.TLabel",
    background=[("pressed", "!disabled", "brown"), ("active", "brown")],
    foreground=[("pressed", "white"), ("active", "white")],
    relief=[("pressed", "sunken"), ("active", "raised")],
)
# sets defaults for optionmenu objects
style.configure(
    "TMenubutton",
    background="white",
    font=("Helvetica", 16),
    width=15,
)
# sets defaults for checkbutton objects
style.configure(
    "TCheckbutton",
    background="#fff391",
    foreground="#551802",
    font=("Helvetica", 16),
    width=15,
)
style.configure("mini.TCheckbutton", width=0)

flavors = ["Chocolate", "Vanilla", "Strawberry"]
toppings = [
    "Chocolate Syrup",
    "Vanilla Syrup",
    "Caramel Syrup",
    "Strawberry Syrup",
    "Blueberry Syrup",
    "Raspberry Syrup",
]

order_info = {
    "Name": tk.StringVar(main_frame),
    "Dessert": tk.StringVar(main_frame),
    "Flavor 1": tk.StringVar(main_frame),
    "Flavor 2": tk.StringVar(main_frame),
    "Flavor 3": tk.StringVar(main_frame),
    "Topping 1": tk.StringVar(main_frame),
    "Topping 2": tk.StringVar(main_frame),
    "Topping 3": tk.StringVar(main_frame),
    "Nuts": tk.BooleanVar(main_frame),
    "Whip": tk.BooleanVar(main_frame),
    "Cherry": tk.BooleanVar(main_frame),
}


# -------------------------------------------------------------------------------HOME PAGE--------------------------------------------------
# BUILDING HOME WIDGETS

# build text strings
welcome_banner = "Welcome to Ike's Ice Cream Parlor!"
welcome_msg = "You can order sundaes and milkshakes from right here at your table! To begin, enter your name in the box below, then choose either Sundae or Milkshake."
name_msg = "This dessert is for:"
select_msg = "I want to order a:"

# build labels
welcome_banner_label = ttk.Label(home, style="banner.TLabel", text=welcome_banner)
welcome_msg_label = ttk.Label(home, text=welcome_msg)
name_label = ttk.Label(home, text=name_msg)

# build entry box for user name
name_entry = ttk.Entry(
    home,
    font=("Helvetica", 16),
    textvariable=order_info["Name"],
    width=20,
)

# build optionmenu
select_label = ttk.Label(home, text=select_msg)
options = ["Sundae", "Milkshake"]
home_menu = ttk.OptionMenu(home, order_info["Dessert"], "Choose one:", *options)
home_menu["menu"].config(
    background="white",
    font=("Helvetica", 16),
)

# build button to go next page
go_button = ttk.Button(home, text="Let's Go!", style="button.TLabel", command=lets_go)


# LAYOUTS

# layout for row 0
welcome_banner_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

# layout for row 1
welcome_msg_label.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=[0, 30])

# layout for row 2
name_label.grid(row=2, column=0, sticky="e", pady=[0, 8])
name_entry.grid(row=2, column=1, sticky="w")

# layout for row 3
select_label.grid(row=3, column=0, sticky="e")
home_menu.grid(row=3, column=1, sticky="w")

# layout for row 4
go_button.grid(row=4, column=0, columnspan=2, pady=[50, 0])


# run application
home.tkraise()
scoops.mainloop()
