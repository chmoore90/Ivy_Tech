"""
Program prompts, stores, prints data
Author: Chloe Moore
Class: SDEV 140-26J
Module: 7
Ex: 1
"""


class Employee:
    """class for all employee attributes"""

    real = True

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number


class Production_Worker(Employee):
    """subclass of employee"""

    def __init__(self, name, number, shift, rate):
        super().__init__(name, number)
        self.shift = shift
        self.rate = rate

    def set_shift(self, shift):
        self.shift = shift

    def get_shift(self):
        return self.shift

    def set_rate(self, rate):
        self.rate = rate

    def get_rate(self):
        return self.rate


# initialize production worker class object
new_employee = Production_Worker("", "", "", "")

# get information
name = input("Enter employee name: ")
number = input("Enter employee number: ")
shift = input("Enter shift number: ")
rate = input("Enter hourly wage: ")

# put info into production worker class
new_employee.set_name(name)
new_employee.set_number(int(number))
new_employee.set_shift(int(shift))
new_employee.set_rate(float(rate))

# output
print(
    f"""Name: {new_employee.get_name()}
Employee Number: {new_employee.get_number()}
Shift Number: {new_employee.get_shift()}
Hourly Rate: ${new_employee.get_rate():.2f}
"""
)
