'''
Program displays the results of combining two primary colors
Author: Chloe Moore
Class: SDEV 140-26J
Module: 2
Ex: 1
'''

# Declarations

primary_array = {"red", "blue", "yellow"}
primary1 = ""
primary2 = ""
result = ""

# Get data

while True:
    primary1 = input("Enter a primary color (red, blue, or yellow): ").lower()
    if primary1 not in (primary_array):
        print("Input error: Please enter a valid primary color.")
        continue
    else:
        break

while True:
    primary2 = input("Enter another primary color (red, blue, or yellow): ").lower()
    if primary2 not in (primary_array):
        print("Input error: Please enter a valid primary color.")
        continue
    if primary2 == primary1:
        print(f"Input error: You have already selected {primary1}. Please enter a different color.")
        continue
    else:
        break

# Process data

if primary1 == "red" or primary2 == "red":
    if primary1 == "yellow" or primary2 == "yellow":
        result = "orange"
    else:
        result = "purple"
else:
    result = "green"

# Output data

print(f"{primary1.capitalize()} and {primary2} combine to make {result}.")
