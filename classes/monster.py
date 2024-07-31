from .character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.collectable = False
        self.giveGold = False