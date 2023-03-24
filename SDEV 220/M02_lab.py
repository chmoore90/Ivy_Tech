
# Chloe Moore
# M02_lab
# Checks if student input means student qualifies for academic achievements

# initial last_name value so while loop will start
last_name = ''

while last_name != 'ZZZ':

    # sentinal value to end program
    last_name = input("Enter last name (or enter 'ZZZ' to exit): ")
    if last_name == "ZZZ":
        break

    # gather student information
    first_name = input('Enter first name: ')
    gpa = float(input('Enter GPA as a decimal: '))

    # check for valid GPA input
    while gpa < 0 or gpa > 4:
        print('Invalid number. GPA must be between 0 and 4.0')
        gpa = float(input('Enter GPA as a decimal: '))

    # determine academic eligibility
    if gpa >= 3.5:
        print(f"Congrats {first_name}! You made the Dean's List.")
    elif gpa >= 3.25:
        print(f"Well done {first_name}. You made the Honor Roll.")
    else:
        print(f"Sorry {first_name}, you didn't quite make it this time.")
