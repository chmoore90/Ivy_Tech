# tkinter banaba survey

import tkinter as tk

# building the window
root = tk.Tk()
root.title("My first tkinter form")

# set window size
root.geometry("700x500+300+300")

# set sizable settings
root.resizable(False, False)

# building widgets
# title widget
title = tk.Label(root, text="Please take the survey", font= "Arial 16 bold", bg="dark green", fg="#FFFFFF")

# building name lable and text entry
name_label = tk.Label(root, text="What is your name?")
name_entry = tk.Entry(root)

# building check widget (has built in label)
eat_check = tk.Checkbutton(root, text="Check if you eat bananas")

# building spinbox label and spinbox
num_label = tk.Label(root, text="How many bananas do you eat per day?")
num_input = tk.Spinbox(root, from_=0, to=50, increment=1)

# building color label, input, choices
color_label = tk.Label(root, text="What is the best color for a banana?")
color_input = tk.Listbox(root, height=6)
color_choices = ("Any,", "Green", "Green-Yellow", "Yellow", "Brown-Spotted", "Black")
# inserting choices into listbox
for choice in color_choices:
    color_input.insert(tk.END, choice)

# layout application
# layout for row0 (putting the title widget in row0
title.grid(row=0, columnspan=2)

# layout row1 (name and entry)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

# layout row2 (checkbox)
eat_check.grid(row=2, columnspan=2, sticky="we")

# layout row3 (spinbox)
num_label.grid(row=3, column=0)
num_input.grid(row=3, column=1)

# layout row 4 (listbox)
color_label.grid(row=4, column=0)
color_input.grid(row=4, column=1)



root.mainloop()
