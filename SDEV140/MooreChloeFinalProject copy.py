"""
Program creates GUI where users can customize sundae's and milkshakes
Author: Chloe Moore
Class: SDEV 140-26J
Final Project
"""

import tkinter as tk
from tkinter import ttk


#navigation functions
def go_home():
    """Raises the home page"""
    pass


def go_order_sun():
    """Raises the sundae order page"""
    pass


def go_order_milk():
    """Raises the milkshake order page"""
    pass


def go_conf_sun():
    """Raises the sundae confirmation page"""
    pass


def go_conf_milk():
    """Raises the milkshake confirmation page"""
    pass


def go_thanks():
    """Raises the thank you page"""
    pass


#-------------------------------------------------------------------------------APPLICATION FRAMEWORK--------------------------------------------------
scoops = tk.Tk()
scoops.title("What's the Scoop?")       #sets title
scoops.geometry("1024x700+512+350")     #sets window size
scoops.config(background="#fff391")     #sets background color

logo_frame = ttk.Frame(scoops)          #creates frame for logo (to be displayed above app pages)

logo_img = tk.PhotoImage(file="ike_logo.png")
logo_label = ttk.Label(logo_frame, image=logo_img, background="#fff391")
logo_label.pack()                       #puts image into logo_frame

main = ttk.Frame(scoops)                #creates main frame where pages will be stacked

style = ttk.Style(main)
style.configure("TLabel", background="#fff391", foreground="#551802", font=("Arial", 12))     #sets the style for main (background/text will be yellow, font is Arial)

logo_frame.pack()                       #places logo_frame at top of window
main.pack()                             #places main frame under logo

#create pages for main frame
home = ttk.Frame(main)
order_sun = ttk.Frame(main)
order_milk = ttk.Frame(main)
conf_sun = ttk.Frame(main)
conf_milk = ttk.Frame(main)
thanks = ttk.Frame(main)

frames = [home, order_sun, order_milk, thanks]

#-------------------------------------------------------------------------------PAGES WIDGETS--------------------------------------------------
#home page
welcome_banner = "welcome message goes here"
welcome_msg = "general welcoming things"

welcome__banner_label = ttk.Label(thanks, text=welcome_banner, style="TLabel", font="Arial 24")

welcome_msg_label = ttk.Label(thanks, text=welcome_msg)
welcome_msg_label.config(style="TLabel", anchor="center", padding=30)





#sundae order


#milkshake order


#sundae confirmation


#milkshake confirmation


#thank you page



#-------------------------------------------------------------------------------BUILDING FRAMES--------------------------------------------------
#home page
welcome__banner_label.grid(row=0, column=1)
welcome_msg_label.grid(row=1, column=1, sticky="ew")



#sundae order



#milkshake order



#sundae confirmation



#milkshake confirmation



#thank you page




#-------------------------------------------------------------------------------RUN APPLICATION--------------------------------------------------




scoops.mainloop()
