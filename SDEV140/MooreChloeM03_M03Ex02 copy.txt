'''
Program writes a series of random numbers to a file and displays the results
Author: Chloe Moore
Class: SDEV 140-26J
Module: 3
Ex: 2
'''

import random

reps = int(input("How many numbers do you want to enter into the file? "))

with open("scribble.py", "w") as w:
    for i in range(reps):
        w.write(str(random.randint(1, 500))+"\n")

with open("scribble.py", "r") as r:
    for line in r:
        print(line.strip())
