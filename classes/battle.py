from .dice import Dice
import os

class Battle:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
        self.monster_name = monster.__class__.__name__
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def attack(self, target):
        if target == "hero":
            damage = self.monster.hit()
            self.hero.lifePoints -= damage
            return f"Le {self.monster_name} vous attaque et vous inflige {damage} points de dégâts ! Il vous reste {self.hero.lifePoints} points de vie"
        else:
            damage = self.hero.hit()
            self.monster.lifePoints -= damage
            return f"Vous attaquez le {self.monster_name} et lui infligez {damage} points de dégâts ! Il lui reste {self.monster.lifePoints} points de vie"
    
    def heal(self):
        if self.hero.lifePoints < self.hero.maxLifePoints and self.hero.manaPoints >= 3:
            result = Dice(6).roll() + self.hero.modStamina
            if result + self.hero.lifePoints > self.hero.maxLifePoints:
                self.hero.lifePoints = self.hero.maxLifePoints
            self.hero.lifePoints += result
            self.hero.manaPoints -= 3
            return f"Vous avez maintenant {self.hero.lifePoints} points de vie"
        else:
            return "Vous avez déjà toute votre vie ou vous n'avez pas assez de mana"
    
    def win(self):
        reward = f"Vous avez tué le {self.monster_name} ! "
        self.hero.setLifePoints(self.hero.getMaxLifePoints())
        if self.monster.__class__.__name__ == "Wolf":
            reward += f"Vous récupérez {self.monster.giveLeather} cuirs"
        elif self.monster.__class__.__name__ == "Orc":
            reward += f"Vous récupérez {self.monster.nbGold} pièces d'or"
        elif self.monster.__class__.__name__ == "Dragonet":
            reward += f"Vous récupérez {self.monster.nbGold} pièces d'or et {self.monster.giveLeather} cuirs"
        return reward
    
    def lose(self):
        return 'lose'