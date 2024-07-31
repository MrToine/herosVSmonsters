from .hero import Hero

class Dwarf(Hero):
    def __init__(self):
        super().__init__()
        self.stamina = self.stamina + 2

        print(f"Un héros est né : {self.stamina} en endurance, {self.strength} en force, {self.maxLifePoints} en points de vie.")
        print(f"Mods: {self.modStamina} en endurance, {self.modStrength} en force.")