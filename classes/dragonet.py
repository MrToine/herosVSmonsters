from .monster import Monster
from .dice import Dice

class Dragonet(Monster):
    def __init__(self):
        super().__init__()
        self.stamina = self.stamina + 1
        self.collectable = True
        self.giveGold = True
        self.giveLeather = Dice(4).roll() if self.collectable else 0
        self.nbGold = Dice(6).roll() if self.collectable else 0