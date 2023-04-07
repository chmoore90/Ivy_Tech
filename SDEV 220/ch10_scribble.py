# class Cat:
#     pass

# a_cat = Cat()
# b_cat = Cat()

# print(a_cat)
# print(b_cat)

# a_cat.age = 11
# a_cat.name = "Little Bit"
# a_cat.child = b_cat

# print(a_cat.age)

# a_cat.child.name = "Mr. Oranges"

# print(a_cat.child.name)
# print(b_cat.name)


class Cat():
    def __init__(self, name) -> None:
        self.name = name

kitty = Cat("Little Bit")

print(kitty.name)
