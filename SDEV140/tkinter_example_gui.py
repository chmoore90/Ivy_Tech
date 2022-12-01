from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Hello class!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

root.mainloop()
