from abc import ABC, abstractmethod
from .dice import Dice

class Character(ABC):
    @abstractmethod
    def __init__(self):
        stamina = self.__initStats()
        self.stamina = stamina
        self.modStamina = self.__modificatorStats(self.stamina)
        self.strength = self.__initStats()
        self.modStrength = self.__modificatorStats(self.strength)
        self.maxLifePoints = self.stamina + self.modStamina
        self.lifePoints = self.maxLifePoints
        self.maxManaPoints = self.stamina + self.modStrength
        self.manaPoints = self.maxManaPoints
    
    def getMaxLifePoints(self):
        return self.maxLifePoints
    
    def getLifePoints(self):
        return self.lifePoints
    
    def getMaxManaPoints(self):
        return self.maxManaPoints
    
    def getManaPoints(self):
        return self.manaPoints
    
    def getStamina(self):
        return self.stamina
    
    def getStrength(self):
        return self.strength
    
    def setLifePoints(self, lifePoints):
        self.lifePoints = lifePoints
    
    def __modificatorStats(self, stat):
        if stat < 5:
            return -1
        elif stat > 5 and stat < 10:
            return 0
        elif stat > 10 and stat < 15:
            return + 1
        elif stat > 15:
            return + 2
        return 0
    
    def __initStats(self):
        dice = []

        for i in range(4):
            dice.append(Dice(6).roll())
        
        dice.remove(min(dice))
        return sum(dice)
    
    def hit(self):
        degats = Dice(3).roll() + self.modStrength
        return degats