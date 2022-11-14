# Text block:
'''
Program get user's first and last name, then concates them
Author: Louis Vician
Class: SDEV 140-26J
Module: 1
Ex: 1
'''

# 1) Initialization/Declaration - define and declare variables
first_name = ''
last_name = ''

# 2) get data - getting information from hard declare/user/file/
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')

#3) proccess data - do all the calculations
full_name = first_name + ' ' + last_name

# 4) output information
print('The name you entered is: ' + full_name + '.')
