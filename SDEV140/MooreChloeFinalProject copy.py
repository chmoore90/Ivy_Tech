"""
Program creates GUI where users can customize sundae's and milkshakes
Author: Chloe Moore
Class: SDEV 140-26J
Final Project
"""

import tkinter as tk
from tkinter import ttk


def new_order():
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
    dessert = order_info["Dessert"].get()
    if dessert == "Sundae":
        init_sundae(sundae)
        sundae.tkraise()
    if dessert == "Milkshake":
        init_milkshake(milkshake)
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
    init_thanks(thanks)
    thanks.tkraise()


def configure_styles(scoops):

    style = ttk.Style(scoops)

    style.configure(
        "TFrame",
        background="#fff391",
    )
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
    style.map(
        "button.TLabel",
        background=[("pressed", "!disabled", "brown"), ("active", "brown")],
        foreground=[("pressed", "white"), ("active", "white")],
        relief=[("pressed", "sunken"), ("!pressed", "raised")],
    )
    style.map(
        "exit.TLabel",
        background=[("pressed", "!disabled", "brown"), ("active", "brown")],
        foreground=[("pressed", "white"), ("active", "white")],
        relief=[("pressed", "sunken"), ("active", "raised")],
    )
    style.configure(
        "TMenubutton",
        background="white",
        font=("Helvetica", 16),
        width=15,
    )
    style.configure(
        "TCheckbutton",
        background="#fff391",
        foreground="#551802",
        font=("Helvetica", 16),
        width=15,
    )
    style.configure("mini.TCheckbutton", width=0)
    style.configure(
        "TRadiobutton",
        background="#fff391",
        foreground="#551802",
        font=("Helvetica", 16),
        width=15,
    )


def init_home(page):
    welcome_banner = "Welcome to Ike's Ice Cream Parlor!"
    welcome_msg = "You can order sundaes and milkshakes from right here at your table! To begin, enter your name in the box below, then choose either Sundae or Milkshake."
    name_msg = "This dessert is for:"
    select_msg = "I want to order a:"
    welcome_banner_label = ttk.Label(page, style="banner.TLabel", text=welcome_banner)
    welcome_msg_label = ttk.Label(page, text=welcome_msg)
    name_label = ttk.Label(page, text=name_msg)
    name_entry = ttk.Entry(
        page,
        font=("Helvetica", 16),
        textvariable=order_info["Name"],
        width=20,
    )
    select_label = ttk.Label(page, text=select_msg)
    options = ["Sundae", "Milkshake"]
    home_menu = ttk.OptionMenu(page, order_info["Dessert"], "Choose one:", *options)
    home_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    go_button = ttk.Button(
        page, text="Let's Go!", style="button.TLabel", command=lets_go
    )

    welcome_banner_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    welcome_msg_label.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=[0, 30])
    name_label.grid(row=2, column=0, sticky="e", pady=[0, 8])
    name_entry.grid(row=2, column=1, sticky="w")
    select_label.grid(row=3, column=0, sticky="e")
    home_menu.grid(row=3, column=1, sticky="w")
    go_button.grid(row=4, column=0, columnspan=2, pady=[50, 0])

    page.tkraise()


def init_sundae(page):
    banner = f"Let's make {order_info['Name'].get()}'s sundae!"
    msg = "Select up to 3 scoops of ice cream. You can pick one flavor and one topping per scoop. Then add on any number of extras. Hit 'Submit Order' when you're ready to order!"

    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    flavors_label = ttk.Label(page, text="Choose your scoops...")
    toppings_label = ttk.Label(page, text="...and their toppings.")
    extras_label = ttk.Label(page, text="Add some extras:")

    flavor1_menu = ttk.OptionMenu(page, order_info["Flavor 1"], "Choose one:", *flavors)
    flavor1_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    flavor2_menu = ttk.OptionMenu(page, order_info["Flavor 2"], "Choose one:", *flavors)
    flavor2_menu["state"] = "disabled"
    flavor2_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    flavor3_menu = ttk.OptionMenu(
        page,
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
        page, order_info["Topping 1"], "Choose one:", *toppings
    )
    toppings1_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    toppings2_menu = ttk.OptionMenu(
        page, order_info["Topping 2"], "Choose one:", *toppings
    )
    toppings2_menu["state"] = "disabled"
    toppings2_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )
    toppings3_menu = ttk.OptionMenu(
        page, order_info["Topping 3"], "Choose one:", *toppings
    )
    toppings3_menu["state"] = "disabled"
    toppings3_menu["menu"].config(
        background="white",
        font=("Helvetica", 16),
    )

    flavor2_var = tk.BooleanVar()
    flavor2_check = ttk.Checkbutton(
        page,
        style="mini.TCheckbutton",
        variable=flavor2_var,
        command=lambda: toggle(flavor2_var, flavor2_menu, toppings2_menu),
    )
    flavor3_var = tk.BooleanVar()
    flavor3_check = ttk.Checkbutton(
        page,
        style="mini.TCheckbutton",
        variable=flavor3_var,
        command=lambda: toggle(flavor3_var, flavor3_menu, toppings3_menu),
    )

    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(
        page, text="Whipping Cream", variable=order_info["Whip"]
    )
    cherry_check = ttk.Checkbutton(
        page, text="Cherry on Top", variable=order_info["Cherry"]
    )

    order_button = ttk.Button(
        page,
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

    flavor1_menu.grid(row=3, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=3, column=2)
    toppings1_menu.grid(row=3, column=3)

    flavor2_check.grid(row=4, column=0, sticky="e")
    flavor2_menu.grid(row=4, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=4, column=2)
    toppings2_menu.grid(row=4, column=3)

    flavor3_check.grid(row=5, column=0, sticky="e")
    flavor3_menu.grid(row=5, column=1, sticky="w")
    ttk.Label(page, text="--- with ---    ").grid(row=5, column=2)
    toppings3_menu.grid(row=5, column=3)

    extras_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=[20, 0])
    nuts_check.grid(row=7, column=0, columnspan=2, sticky="w")
    whip_check.grid(row=7, column=1, columnspan=3, padx=[0, 110])
    cherry_check.grid(row=7, column=3, sticky="e")

    order_button.grid(row=8, column=0, columnspan=4, pady=[50, 0])


def init_milkshake(page):
    banner = f"Let's make {order_info['Name'].get()}'s milkshake!"
    msg = "First, select a size and flavor. Then add on any number of extras that you want. Hit 'Submit Order' when you're ready to order."
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)
    extras_label = ttk.Label(page, text="Add some extras:")

    size_label = ttk.Label(page, text="Choose your size:")
    small_radiob = ttk.Radiobutton(
        page, text="Small", value="Small", variable=order_info["Size"]
    )
    large_radiob = ttk.Radiobutton(
        page, text="Large", value="Large", variable=order_info["Size"]
    )

    flavor_label = ttk.Label(page, text="Choose your flavor:")
    flavor1_radiob = ttk.Radiobutton(
        page,
        text="Chocolate",
        value="Chocolate",
        variable=order_info["Flavor 1"],
    )
    flavor2_radiob = ttk.Radiobutton(
        page, text="Vanilla", value="Vanilla", variable=order_info["Flavor 1"]
    )
    flavor3_radiob = ttk.Radiobutton(
        page,
        text="Strawberry",
        value="Strawberry",
        variable=order_info["Flavor 1"],
    )

    nuts_check = ttk.Checkbutton(page, text="Nuts", variable=order_info["Nuts"])
    whip_check = ttk.Checkbutton(
        page, text="Whipping Cream", variable=order_info["Whip"]
    )
    cherry_check = ttk.Checkbutton(
        page, text="Cherry on Top", variable=order_info["Cherry"]
    )

    order_button = ttk.Button(
        page,
        text="Submit Order",
        style="button.TLabel",
        command=submit_order,
        width=15,
    )

    banner_label.grid(row=0, column=0, columnspan=3, sticky="nsew")
    msg_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=[0, 30])
    size_label.grid(row=2, column=0, columnspan=2)
    small_radiob.grid(row=3, column=0, columnspan=2)
    large_radiob.grid(row=4, column=0, columnspan=2)
    flavor_label.grid(row=2, column=1, columnspan=2)
    flavor1_radiob.grid(row=3, column=1, columnspan=2)
    flavor2_radiob.grid(row=4, column=1, columnspan=2)
    flavor3_radiob.grid(row=5, column=1, columnspan=2)
    extras_label.grid(row=6, column=0, pady=[20, 0])
    nuts_check.grid(row=7, column=0)
    whip_check.grid(row=7, column=1)
    cherry_check.grid(row=7, column=2)

    order_button.grid(row=8, column=0, columnspan=3, pady=[50, 0])


def init_thanks(page):
    banner = f"Thank you {order_info['Name'].get()}! Your {order_info['Dessert'].get().lower()} will be ready soon."
    msg = "All you need to do now is wait! We will bring your dessert to you as soon as it's done. Return to the 'Home Page' to order something else."
    banner_label = ttk.Label(page, style="banner.TLabel", text=banner)
    msg_label = ttk.Label(page, text=msg)

    order_info.update(new_order())

    home_button = ttk.Button(
        page, text="Home Page", style="button.TLabel", command=lambda: init_home(home)
    )

    banner_label.grid(row=0, column=0)
    msg_label.grid(row=1, column=0, pady=[0, 30])
    home_button.grid(row=2, column=0)


scoops = tk.Tk()
scoops.title("What's the Scoop?")
scoops.geometry("1200x800")
scoops.configure(background="#fff391")
scoops.resizable(True, True)
scoops.grid_anchor("n")

logo_frame = ttk.Frame(scoops)
logo_frame.grid_anchor("n")  # sets grid default placement to top, center
logo_frame.grid(row=0, column=0, sticky="nsew")
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

main_frame = ttk.Frame(scoops)
main_frame.grid_anchor("n")
main_frame.grid(row=1, column=0, sticky="nsew")

home = ttk.Frame(main_frame)
sundae = ttk.Frame(main_frame)
milkshake = ttk.Frame(main_frame)
thanks = ttk.Frame(main_frame)

for frame in (home, sundae, milkshake, thanks):
    frame.grid_anchor("n")
    frame.grid(row=0, column=0, sticky="nsew")

order_info = new_order()

flavors = ["Chocolate", "Vanilla", "Strawberry"]
toppings = [
    "Chocolate Syrup",
    "Vanilla Syrup",
    "Caramel Syrup",
    "Strawberry Syrup",
    "Blueberry Syrup",
    "Raspberry Syrup",
]


configure_styles(scoops)
order_info = new_order()
init_home(home)
scoops.mainloop()
