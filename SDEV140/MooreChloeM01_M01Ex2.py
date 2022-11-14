'''
Program calculates the cost a 18% tip, 7% sales tax, and the total cost of a meal
Author: Chloe Moore
Class: SDEV 140-26J
Module: 1
Ex: 2
'''

# 1) Initialization

subtotal = 0
tip = 0
tax = 0
total = 0
statement = ""

# 2) get data

subtotal = float(input("Enter the cost of your meal: "))

#3) proccess data - do all the calculations

tip = subtotal*0.18
tax = subtotal*0.07
total = subtotal + tip + tax
statement = f"Subtotal = ${subtotal: .2f}\nTip = ${tip: .2f}\nTax = ${tax: .2f}\nTOTAL = ${total: .2f}"

# 4) output information
print(statement)
