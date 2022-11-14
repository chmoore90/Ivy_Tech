'''
Program displays the factorial of a non-negative integer
Author: Chloe Moore
Class: SDEV 140-26J
Module: 2
Ex: 2
'''

n = 0
result = 1

n = float(input(f"Enter a non-negative integer: "))
n = int(round(n))

for i in range(1,n+1):
    result = result * i

print(f"The factorial of {n} is {result}.")
