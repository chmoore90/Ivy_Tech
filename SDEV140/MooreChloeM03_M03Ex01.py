'''
Program adds digits of a number and returns sum
Author: Chloe Moore
Class: SDEV 140-26J
Module: 3
Ex: 1
'''

n = 0
sum = 0

n = input("Enter a number with multiple digits: ")

for i in n:
    sum += int(i)

print(sum)
