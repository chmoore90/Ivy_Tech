"""
Chloe Moore
M03_lab
Asks user for information about a car, creates an object with that info and prints it for user.
"""


class Vehicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self) -> str:
        return f"Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"


# User enters info about the car
print("You are about to enter information for a new car.")

year = int(input("Enter the car's year: "))
make = input("Enter the car's make: ")
model = input("Enter the car's model: ")
doors = int(input("How many doors does the car have? "))
roof = input("What kind of roof does the car have (enter 'solid' or 'sun roof')? ")


# Create new object
new_vehicle = Automobile("Car", year, make, model, doors, roof)

# Output user info
print(new_vehicle)
