import pygame
import random
from math import * 
from classes import *

pygame.init()


# Constants 
WIDTH, HEIGHT = 1200, 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barely Flying")
clock = pygame.time.Clock()


background_image = pygame.image.load("assets/background/Background1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
bird_image = pygame.image.load("assets/Flappy Bird Assets/Player/StyleBird1/Bird1-1.png")
bird_image = bird_image.subsurface((pygame.Rect(0, 0, 16, 16)))
bird_image = pygame.transform.scale(bird_image, (WIDTH_BIRD, HEIGHT_BIRD))
background_rect = background_image.get_rect()
cano_baixo = pygame.image.load("assets/Flappy Bird Assets/Tiles/Style 1/PipeStyle1.png")
cano_baixo = cano_baixo.subsurface((pygame.Rect(0, 0, 32, 80)))
cano_baixo = pygame.transform.scale(cano_baixo, (WIDTH_CANO, HEIGHT_CANO))


# Cria os parametros iniciais do moviumento do background
bg_x = 0
bg_speed = 2

# Parametros iniciais do cano
cano_x = 0 
cano_speed = 3

bird = Bird(bird_image)
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.speedy = -10

    # Cria o loop de movimento do background somente no eixo x 
    bg_x -= bg_speed
    if bg_x <= -WIDTH:
        bg_x = 0

    cano_x -= cano_speed
    if cano_x <= -WIDTH:
        cano_x = 0

    if bird.rect.top < 0:
        running = False

    bird.update()

    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + WIDTH, 0))
    screen.blit(bird_image, bird.rect)
    screen.blit(cano_baixo, (cano_x,0))
    screen.blit(cano_baixo, (cano_x + WIDTH, 0))
    
    


    pygame.display.flip()
    clock.tick(FPS)  # Limit FPS

pygame.quit()

