'''
Program finds and displays all positive prime integers <= a user input
Author: Chloe Moore
Class: SDEV 140-26J
Module: 4
Ex: 1
'''

n = input("Enter an integer greater than 1: ")
n = int(n)
prime = []

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(2, n+1):
    if is_prime(i):
        prime.append(i)

print(prime)
