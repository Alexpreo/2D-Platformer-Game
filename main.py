import pygame, sys
from settings import *
from level import Level
#initilize pygame
pygame.init()
pygame.display.set_caption("2D Platformer")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

level = Level()

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    level.run()
    
    #Tick rate and logic
    pygame.display.update()
    clock.tick(60)