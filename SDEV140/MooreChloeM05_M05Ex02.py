'''
Program is a guessing game. Try to guess the computer's number! Includes a counter for number of guesses.
Author: Chloe Moore
Class: SDEV 140-26J
Module: 5
Ex: 1
'''

import random

# initialize
n = 0
guess = ""
count = 0

def generate_random():
    """Generates a random number between 1 and 100"""
    print("The computer has chosen a number between 1 and 100.")
    n = random.randint(1, 100)
    return n

def check_guess(n, x):
    """Checks if guess is higher or lower than n, tells the user."""
    if x > n:
        print("Too high, try again.")

    elif x < n:
        print("Too low, try again.")

def enter_guess():
    """Gets input from user and converts to integer."""
    guess = input("Enter a guess between 1 and 100: ")
    guess = int(guess)
    return guess

# get data
n = generate_random()
guess = enter_guess()

# play the game!

while True:

    while n != guess:
        check_guess(n, guess)
        count += 1
        guess = enter_guess()


    print(f"Congratulations! The number was {n}. It took you {count} guesses.")

    n = generate_random()
    count = 0
    guess = enter_guess()
