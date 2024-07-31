from .sceneBattle import SceneBattle
import pygame, random, globals

class Map:
    def __init__(self, pygameInstance,width, height, size_tile):
        self.window = pygameInstance
        self.__width = width
        self.__height = height
        self.heroPosX = 0
        self.heroPosY = 0
        self.hero = ''
        self.monsters = {}
        self.pygameInstance = pygameInstance
        self.TILE_SIZE = size_tile
        self.img_grass = pygame.transform.scale(pygame.image.load("assets/grassTile.png"), (self.TILE_SIZE, self.TILE_SIZE))
        self.img_wolf = pygame.transform.scale(pygame.image.load("assets/wolf/tile000.png").convert_alpha(), (self.TILE_SIZE, self.TILE_SIZE))
        self.img_orc = pygame.transform.scale(pygame.image.load("assets/orc/tile000.png").convert_alpha(), (self.TILE_SIZE, self.TILE_SIZE))
        self.img_dragon = pygame.transform.scale(pygame.image.load("assets/dragon/tile000.png").convert_alpha(), (self.TILE_SIZE, self.TILE_SIZE))
        self.img_dwarf = pygame.image.load("assets/hero/dwarf.png").convert_alpha()
        self.grass = self.window.blit(self.img_grass, (self.__width * self.TILE_SIZE, self.__height * self.TILE_SIZE))
        self.__grid = [[' ' for x in range(self.__width)] for y in range(self.__height)]
    
    def generateMonsters(self, number, mobs):
        pass
    
    def placeCharacter(self, character, x, y):
        if self.__grid[y][x] == ' ' and self.isValidPosition(x, y):       
            self.__grid[y][x] = character.__class__.__name__[0]
            print(f"{self.__grid[y][x]}")
    
    def placeHero(self, hero, x, y):
        if self.__grid[y][x] == ' ' and self.isValidPosition(x, y):       
            self.__grid[y][x] = 'H'
            self.heroPosX = x
            self.heroPosY = y
            self.hero = hero
            print(f"Le héros : {self.hero}")
    
    def refreshGridHero(self, initPosX, initPosY, pos):
        if (0 <= pos[0] < len(self.__grid[0]) and 0 <= pos[1] < len(self.__grid)):
            self.__grid[pos[1]][pos[0]] = 'H'
            self.heroPosX = pos[0]
            self.heroPosY = pos[1]
            self.__grid[initPosY][initPosX] = ' '
            self.update_map()
            
            adjacent_position = [
                (self.heroPosX, self.heroPosY - 1),
                (self.heroPosX, self.heroPosY + 1),
                (self.heroPosX - 1, self.heroPosY),
                (self.heroPosX + 1, self.heroPosY)
            ]

            for pos in adjacent_position:
                if pos in self.monsters.keys():
                    result = SceneBattle(self.hero, self.monsters[pos], pos, self.window).fight()
                    if result == True:
                        self.__grid[pos[1]][pos[0]] = ' '
                        del self.monsters[pos]
                    elif result == False:
                        self.__grid[self.heroPosY][self.heroPosX] = ' '
                        self.window.fill((0,0,0))
                        globals.print_text(self.window, 4500, "Vous avez perdu car vous êtes mort !", True, 10, globals.WINDOW_Y - 90, 54, (200, 0, 0))
                        globals.run = False
                        return
    
    def isValidPosition(self, x, y):
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__grid[i][j] != ' ':
                    if abs(i - y) + abs(j - x) < 2:
                        return False
        return True
    
    def update_map(self):
        if len(self.monsters) == 0:
            self.window.fill((0,0,0))
            globals.print_text(self.window, 4500, "Vous avez gagné !", True, 10, globals.WINDOW_Y - 90, 54, (0, 160, 0))
            print("Vous avez gagné !")
            globals.run = False
            return 
        for y in range(self.__height):
            for x in range(self.__width):
                self.window.blit(self.img_grass, (x * self.TILE_SIZE, y * self.TILE_SIZE))
                if self.__grid[y][x] == 'W':
                    self.window.blit(self.img_wolf, (x * self.TILE_SIZE, y * self.TILE_SIZE))
                elif self.__grid[y][x] == 'O':
                    self.window.blit(self.img_orc, (x * self.TILE_SIZE, y * self.TILE_SIZE))
                elif self.__grid[y][x] == 'D':
                    self.window.blit(self.img_dragon, (x * self.TILE_SIZE, y * self.TILE_SIZE))
                elif self.__grid[y][x] == 'H':
                    self.window.blit(self.img_dwarf, (x * self.TILE_SIZE, y * self.TILE_SIZE))
        pygame.display.update()