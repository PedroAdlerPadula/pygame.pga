import pygame
import random
from math import * 
from classes import *

pygame.init()


# Constants 
WIDTH, HEIGHT = 800, 600
FPS = 60
# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barely Flying")
clock = pygame.time.Clock()
# Load images

background_image = pygame.image.load("assets/background/Background1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
bird_image = pygame.image.load("assets/Flappy Bird Assets/Player/StyleBird1/Bird1-1.png")
bird_image = bird_image.subsurface((pygame.Rect(0, 0, 16, 16)))
bird_image = pygame.transform.scale(bird_image, (WIDTH_BIRD, HEIGHT_BIRD))
background_rect = background_image.get_rect()

bird = Bird(bird_image)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.speedy = -5
        
    bird.update()
    screen.fill((255 ,255 ,255))
    screen.blit(background_image, background_rect)
    screen.blit(bird_image, bird.rect)

    pygame.display.flip()
    pygame.display.update()
pygame.quit()

