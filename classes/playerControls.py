import pygame

class PlayerControls:
    def __init__(self, player, map):
        self.player = player
        self.map = map
        self.x, self.y = self.map.heroPosX, self.map.heroPosY
    
    def controls(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                self.map.refreshGridHero(self.map.heroPosX, self.map.heroPosY, self.move('z', self.map.heroPosX, self.map.heroPosY))
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                self.map.refreshGridHero(self.map.heroPosX, self.map.heroPosY, self.move('s', self.map.heroPosX, self.map.heroPosY))
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                self.map.refreshGridHero(self.map.heroPosX, self.map.heroPosY, self.move('q', self.map.heroPosX, self.map.heroPosY))
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                self.map.refreshGridHero(self.map.heroPosX, self.map.heroPosY, self.move('d', self.map.heroPosX, self.map.heroPosY))
    
    def move(self, direction, initPosX, initPosY):
        x = initPosX
        y = initPosY
        if direction == "z":
            y = initPosY - 1
        elif direction == "s":
            y = initPosY + 1
        elif direction == "d":
            x = initPosX + 1
        elif direction == "q":
            x = initPosX - 1
        
        print(f"Le héro bouge en {x}, {y}")
        return x, y

        # if x < 0 or x >= globals.SIZE_MAP or y < 0 or y >= globals.SIZE_MAP:
        #     print("Vous ne pouvez pas sortir de la carte, POSITION INCHANGÉE", x, y)
        # else:
        #     if direction == "z":
        #         y = initPosY - 1
        #     elif direction == "s":
        #         y = initPosY + 1
        #     elif direction == "d":
        #         x = initPosX + 1
        #     elif direction == "q":
        #         x = initPosX - 1
        #     print(f"Le héro bouge en {x}, {y}")
        # return x, y