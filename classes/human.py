from .hero import Hero

class Human(Hero):
    def __init__(self):
        super().__init__()
        print(f"Un humain est né avec des stats : {self.stamina} Endurance - {self.strength} Force")
        self.stamina = self.stamina + 1
        self.strength = self.strength + 1