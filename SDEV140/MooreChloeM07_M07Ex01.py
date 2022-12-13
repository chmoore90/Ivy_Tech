"""
Program creates and prints info on a class
Author: Chloe Moore
Class: SDEV 140-26J
Module: 7
Ex: 1
"""


class Person:
    """person class with name, address, phone attributes"""

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


class Customer(Person):
    """customer class with person parent class"""

    def __init__(self, name, address, phone, number, mail_sub):
        super().__init__(name, address, phone)
        self.number = number
        self.mail_sub = mail_sub


# initialize x
x = Person("Greg", "somewhere in Canada", None)

# initialize y, with values from x
y = Customer(x.name, x.address, x.phone, number=1, mail_sub=False)

# print arrtibutes for y
print(
    f"""Name: {y.name}
Address: {y.address}
Phone: {y.phone}
Number: {y.number}
Mail subscription: {y.mail_sub}"""
)
