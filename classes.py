import pygame
from config import *
import random
WIDTH, HEIGHT = 800, 600
FPS = 60
class Bird(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300
        self.speedy = 1
        self.m = 1
        self.g = 0.5

    def update(self):
        self.speedy += self.g
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.bottom < 0:
            state = GAME_OVER


class Pipe(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(-100, HEIGHT_CANO)
        self.speedx = 3

    # def jump(self):
    #     self

class Pipe_2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 
