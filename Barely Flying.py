import pygame
import random
from math import * 


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
background_rect = background_image.get_rect()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255 ,255 ,255))
    screen.blit(background_image, background_rect)

    pygame.display.flip()
    pygame.display.update()

pygame.quit()