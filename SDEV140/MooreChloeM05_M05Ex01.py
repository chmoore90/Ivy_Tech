'''
Program calculates taxes based on a user's input
Author: Chloe Moore
Class: SDEV 140-26J
Module: 5
Ex: 1
'''

# initialize
sales = 0
county = 0
state = 0
total = 0

def county_tax(x):
    """calculates country taxes"""
    tax = x*0.025
    return tax

def state_tax(x):
    """calculates state taxes"""
    tax = x*0.05
    return tax

#get data
sales = input("Enter this month's total sales: ")
sales = float(sales)

# compute
county = county_tax(sales)
state = state_tax(sales)
total = county + state

# output
print(f"County tax = ${county:.2f}\nState tax = ${state:.2f}\nTotal taxes = ${total:.2f}")
