from classes.human import Human
from classes.dwarf import Dwarf
from classes.wolf import Wolf
from classes.orc import Orc
from classes.dragonet import Dragonet
from classes.map import Map
from classes.playerControls import PlayerControls
from random import randint
import pygame, globals

mobs = [Wolf, Orc, Dragonet]

grepMob = []


#? Mise en place de Pygame
pygame.init()
window = pygame.display.set_mode((globals.WINDOW_X, globals.WINDOW_Y))
pygame.display.set_caption("Heroes VS Monsters")

clock = pygame.time.Clock()
fps = globals.FPS

map = Map(window, globals.SIZE_MAP, globals.SIZE_MAP, globals.TILE_SIZE)
hero = Dwarf()

for i in range(10):
    grepMob.append(mobs[randint(0, len(mobs)-1)]())
    x = randint(1, globals.SIZE_MAP -1)
    y = randint(1, globals.SIZE_MAP -1)
    map.placeCharacter(grepMob[i], x, y)
    map.monsters[x,y] = grepMob[i]
    map.update_map()

map.placeHero(hero, 1, 1)

#? Boucle de jeu Pygame
while globals.run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            globals.run = False
        PlayerControls(hero, map).controls(event)

    window.fill((0, 0, 0))
    map.update_map()
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()