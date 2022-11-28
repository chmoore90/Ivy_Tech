'''
Program writes a series of random numbers to a file and displays the results
Author: Chloe Moore
Class: SDEV 140-26J
Module: 3
Ex: 2
'''

import random

# get data
reps = int(input("How many numbers do you want to enter into the file? "))

# write numbers to a file
with open("scribble.txt", "w") as w:
    for i in range(reps):
        w.write(str(random.randint(1, 500))+"\n")

# read numbers from the file
with open("scribble.txt", "r") as r:
    for line in r:
        print(line.strip())
