base_stats = {
    "constitution": 5,
    "strength": 5,
    "dexterity": 5,
    "intellect": 5,
    "charisma": 5,
}


class Character:
    def __init__(self, name, race, cls):
        self.name = name
        self.race = race
        self.cls = cls
        self.stats = base_stats
        self.roll_modifiers = {}
        self.armor = []
        self.weapons = []
        self.items = []
