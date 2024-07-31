import pygame
"""
Fichier comprenant toutes les valeurs globales lié au jeu
"""

SIZE_MAP = 15
TILE_SIZE = 48
WINDOW_X = SIZE_MAP * TILE_SIZE
WINDOW_Y = SIZE_MAP * TILE_SIZE
run = True

FPS = 30

def print_text(window, delay, text, delete=False, x=10, y=WINDOW_Y - 90, size=24, color=(0, 0, 0)):
    print(delete)
    font = pygame.font.Font(None, size)
    if delete:
        pygame.draw.rect(window, (255, 255, 255), (0, WINDOW_Y - 100, WINDOW_X, 100))
    text = font.render(text, True, color)
    window.blit(text, (x, y))
    pygame.display.flip()
    if delay > 0:
        pygame.time.delay(delay)

def create_button(window, x, y, width, height, text):
    button_color = (100, 100, 100)
    button = pygame.draw.rect(window, button_color, (x, y, width, height))
    print_text(window, 0, text, False, x + 10, y, 35, (255, 255, 255))

    return button