from .monster import Monster
from .dice import Dice

class Orc(Monster):
    def __init__(self):
        super().__init__()
        self.strength = self.strength + 1
        self.giveGold = True
        self.collectable = True
        self.nbGold = Dice(6).roll() if self.collectable else 0