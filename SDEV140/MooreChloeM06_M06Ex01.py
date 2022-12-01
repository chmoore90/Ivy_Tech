'''
Program creates a GUI that converts numbers from Fahrenheit to Celcius and vice versa.
Author: Chloe Moore
Class: SDEV 140-26J
Module: 6
Ex: 1
'''

import tkinter
from tkinter import ttk


# conversion functions
def get_c():
    """Converts input to C and creates display label"""
    f = ent_var.get()
    c = (float(f)-32)*5/9
    ttk.Label(frame, text=f"  {c:.2f} degrees C").grid(column=2, row=1, pady=10)

def get_f():
    """Converts input to F and creates display label"""
    c = ent_var.get()
    f = (9/5)*float(c) + 32
    ttk.Label(frame, text=f"  {f:.2f} degrees F").grid(column=2, row=2, pady=10)


# set up frame
root = tkinter.Tk()
frame = ttk.Frame(root, padding=50)
frame.grid()

# user entry
ttk.Label(frame, text="Enter a temperature: ").grid(column=0, row=0)

ent_var = tkinter.StringVar(frame)
ent = ttk.Entry(frame, textvariable=ent_var, width=5)
ent.grid(column=1, row=0, sticky=tkinter.W, pady=10)
ent.focus()

# buttons
ttk.Button(frame, text="Convert from Fahrenheit to Celcius", command=get_c).grid(column=1, row=1,sticky=tkinter.W, pady=10)
ttk.Button(frame, text="Convert from Celcius to Fahrenheit", command=get_f).grid(column=1, row=2, sticky=tkinter.W, pady=10)


# run program
root.mainloop()
