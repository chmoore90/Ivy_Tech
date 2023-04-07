def new_character(name, race, ch_class):
    return {
        "name": name,
        "race": race,
        "class": ch_class,
        "speed": 6,
        "stats": {},
        "position": {
            "directon": None,
            "distance": 0,
        },
        "armor": 0,
    }

def add_stats(character, stats):
    character["stats"] = stats

def move(character, direction):
    character["position"] = {
        "direction": direction,
        "distance": character["position"]["distance"] + character["speed"]
    }

# pippin = new_character("Pippin", "Cockatiel", "Bard")
# kalos = new_character("Kalos", "Cockatiel", "Fighter")

# add_stats(pippin, {
#     "strength": 10,
#     "dexterity": 12,
#     "charisma": 18,
# })
# add_stats(kalos, {
#     "strength": 18,
#     "dexterity": 12,
#     "charisma": 10,
# })

# move(pippin, "up")
# move(kalos, "down")
# move(kalos, "right")

# print(pippin.items())
# print(kalos.items())


class Character():
    def __init__(self, name, race, ch_class):
        self.name = name
        self.race = race
        self.ch_class = ch_class
        self.speed = 6
        self.stats = {}
        self.position = {
            "direction": None,
            "distance": 0,
        }
        self.armor = 0

    def add_stats(self, stats):
        self.stats = stats

    def move(self, direction):
        self.position = {
            "direction": direction,
            "distance": self.position["distance"] + self.speed
        }

pippin = Character("Pippin", "Cockatiel", "Bard")
kalos = Character("Kalos", "Cockatiel", "Fighter")

pippin.add_stats({
    "strength": 10,
    "dexterity": 12,
    "charisma": 18,
})
kalos.add_stats({
    "strength": 18,
    "dexterity": 12,
    "charisma": 10,
})

pippin.move("up")
kalos.move("down")
kalos.move("right")

print(pippin.__dict__)
print(kalos.__dict__)
