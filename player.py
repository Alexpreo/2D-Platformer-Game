import pygame
from settings import*

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

        #player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        if keys[pygame.K_UP]:
            self.direction.y = 1
        if keys[pygame.K_DOWN]:
            self.direction.y = -1
        