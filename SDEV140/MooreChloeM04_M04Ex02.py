'''
Program returns three most expensive items from a dictionary.
Author: Chloe Moore
Class: SDEV 140-26J
Module: 4
Ex: 2
'''

fruit_prices = {
    'Apple': 0.50,
    'Banana': 0.20,
    'Mango': 0.99,
    'Coconut': 2.99,
    'Pineapple': 3.99
}

first = ("", 0.00)
second = ("", 0.00)
third = ("", 0.00)

for fruit in fruit_prices:
    price = fruit_prices[fruit]

    if price > first[1]:
        third = second
        second = first
        first = (fruit, price)
    elif price > second[1]:
        third = second
        second = (fruit, price)
    elif price > third[1]:
        third = (fruit, price)

print("Top 3 most expensive fruits are:")
for pricey_fruit in [first, second, third]:
    print(pricey_fruit[0], pricey_fruit[1])
