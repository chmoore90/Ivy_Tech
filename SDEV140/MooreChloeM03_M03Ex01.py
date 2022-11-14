'''
Program takes input of single digits and returns a sum
Author: Chloe Moore
Class: SDEV 140-26J
Module: 3
Ex: 1
'''

n = 0
sum = 0

while True:
    n = input("Enter a single digit integer: ")
    if n.isnumeric():
        sum += int(n)
    else:
        break

print("Sum of these numbers is " + str(sum))
