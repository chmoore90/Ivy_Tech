'''
Program converts values of Celsius temperatures to Fahrenheit
Author: Chloe Moore
Class: SDEV 140-26J
Module: 1
Ex: 1
'''

# 1) Initialization

c = 0
f = 0
statement = ""

# 2) get data

c = float(input("Enter the temperature in Celsius: "))
# c = int(c)

#3) proccess data - do all the calculations

f = int(c*(9/5) + 32)
statement = f"{c} degrees Centigrade is {f} degrees Fahrenheit."

# 4) output information
print(statement)
