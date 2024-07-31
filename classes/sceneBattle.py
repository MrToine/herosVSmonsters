from .battle import Battle
import pygame, globals

class SceneBattle:
    def __init__(self, player, monster, pos, pygameInstance):
        self.player = player
        self.monster = monster
        self.x = pos[0]
        self.y = pos[1]
        self.window = pygameInstance
        self.running = True
        self.buttons = []
        self.battle = Battle(player, monster)
        self.isWin = None
        self.battler_hero = pygame.transform.scale(pygame.image.load("assets/hero/dwarf_battle.png").convert_alpha(), (250, 250))
        if self.monster.__class__.__name__ == "Wolf":
            self.battler_monster = pygame.transform.scale(pygame.image.load("assets/wolf/wolf_battle.png").convert_alpha(), (250, 250))
        elif self.monster.__class__.__name__ == "Orc":
            self.battler_monster = pygame.transform.scale(pygame.image.load("assets/orc/orc_battle.png").convert_alpha(), (250, 250))
        elif self.monster.__class__.__name__ == "Dragonet":
            self.battler_monster = pygame.transform.scale(pygame.image.load("assets/dragon/dragon_battle.png").convert_alpha(), (250, 250))

        self.parralax = pygame.transform.scale(pygame.image.load("assets/parralax.png").convert_alpha(), (globals.WINDOW_Y, globals.WINDOW_Y))

        self.battler_monster = pygame.transform.flip(self.battler_monster, True, False)

    def fight(self):
        self.displayBattle()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_event(event)
            pygame.display.flip()
        return self.isWin
    
    def displayBattle(self):
        self.refresh_screen()
        self.update_hud()

        pygame.draw.rect(self.window, (255, 255, 255), (0, globals.WINDOW_Y - 100, globals.WINDOW_X, 100))        
        
        globals.print_text(self.window, 1500, f"Un {self.monster.__class__.__name__} vous attaque !")
        globals.print_text(self.window, 1000, "Choisissez votre action :", True)
        self.displayActions()
    
    def displayActions(self):
        buttonAttack = globals.create_button(self.window, 25, globals.WINDOW_Y - 70, 115, 25, "Attaquer")
        buttonHeal = globals.create_button(self.window, 150, globals.WINDOW_Y - 70, 170, 25, "Se soigner")
        buttonFlee = globals.create_button(self.window, 330, globals.WINDOW_Y - 70, 100, 25, "Fuir")

        self.buttons = [
            buttonAttack,
            buttonHeal,
            buttonFlee
        ]
    
    def handle_mouse_event(self, event):
        x, y = event.pos
        if self.buttons[0].collidepoint(x, y):
            self.battleAction("attack")
            self.displayActions()
        elif self.buttons[1].collidepoint(x, y):
            self.battleAction("heal")
            self.displayActions()
        elif self.buttons[2].collidepoint(x, y):
            globals.print_text(self.window, 1500, "Vous avez fui le combat !", True)
            self.running = False
        
    def battleAction(self, action):
        if action == "attack":
            attack = self.battle.attack("monster")
            self.update_hud()
            globals.print_text(self.window, 4500, attack, True)
            self.update_hud()
        elif action == "heal":
            self.battle.heal()
            globals.print_text(self.window, 1500, "Vous vous soignez", True)
            heal = self.battle.heal()
            self.update_hud()
            globals.print_text(self.window, 4500, heal, True)

        else:
            print("Action inconnue !")
            return False
        
        if self.monster.lifePoints <= 0:
            reward = self.battle.win()
            globals.print_text(self.window, 3000, reward, True)
            self.isWin = True
            self.running = False
            return
        
        attack = self.battle.attack("hero")
        globals.print_text(self.window, 1500, attack, True)
        self.update_hud()

        if self.player.lifePoints <= 0:
            self.battle.lose()
            self.isWin = False
            self.running = False 
        return
    
    def refresh_screen(self):
        self.window.fill((0,0,0))
        self.window.blit(self.parralax, (0, 0))
        self.window.blit(self.battler_hero, (0, globals.WINDOW_Y - 350))
        self.window.blit(self.battler_monster, (globals.WINDOW_X - 250, globals.WINDOW_Y - 350))

        pygame.draw.rect(self.window, (255, 255, 255), (0, globals.WINDOW_Y - 100, globals.WINDOW_X, 100))
    
    def update_hud(self):
        self.refresh_screen()
        
        temp_surface1 = pygame.Surface((100, 50), pygame.SRCALPHA)
        temp_surface1.fill((255, 255, 255, 128))  # 128 est la valeur alpha pour 50% de transparence
        
        self.window.blit(temp_surface1, (100, globals.WINDOW_Y - 400))

        temp_surface2 = pygame.Surface((100, 50), pygame.SRCALPHA)
        temp_surface2.fill((255, 255, 255, 128))  # 128 est la valeur alpha pour 50% de transparence
       
        self.window.blit(temp_surface2, (globals.WINDOW_X - 150, globals.WINDOW_Y - 400))


        if self.player.lifePoints <= self.player.getMaxLifePoints() / 2:
            colorPlayer = (200, 0, 0)
        else:
            colorPlayer = (0, 100, 50)

        if self.monster.lifePoints <= self.monster.getMaxLifePoints() / 2:
            colorMonster = (200, 0, 0)
        else:
            colorMonster = (0, 100, 50)

        globals.print_text(self.window, 0, f"{self.player.getLifePoints()}/{self.player.getMaxLifePoints()} PV", True, 110, globals.WINDOW_Y - 390, 30, colorPlayer)
        globals.print_text(self.window, 0, f"{self.monster.getLifePoints()}/{self.monster.getMaxLifePoints()} PV", True, globals.WINDOW_X - 140, globals.WINDOW_Y - 390, 30, colorMonster)