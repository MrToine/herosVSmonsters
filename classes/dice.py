import random

class Dice:
    def __init__(self, sides):
        self.__sides = sides

    def roll(self):
        return random.randint(1, self.__sides)