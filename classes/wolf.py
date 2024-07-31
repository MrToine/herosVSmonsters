from .monster import Monster
from .dice import Dice

class Wolf(Monster):
    def __init__(self):
        super().__init__()
        self.collectable = True
        self.giveLeather = Dice(4).roll() if self.collectable else 0