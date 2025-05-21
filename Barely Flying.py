import pygame
import random
from math import * 
from classes import *

pygame.init()

# Constants 
WIDTH, HEIGHT = 1200, 700
FPS = 100

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
croc_img = pygame.image.load("assets/unnamed_no_bg_cleaned.png")
croc_img = pygame.transform.scale(croc_img, (WIDTH_CROCO, HEIGHT_CROCO))

# Cria os parametros iniciais do moviumento do background
bg_x = 0
bg_speed = 2

# Parametros iniciais do cano
cano_x = 0 
cano_speed = 3

bird = Bird(bird_image)

# Criando grupos para fazer as colisões
all_sprites = pygame.sprite.Group()
all_sprites.add(bird)
all_pipes = pygame.sprite.Group()
all_crocos = pygame.sprite.Group()

# Criação inicial
pipes = []
for i in range(4):
    x_pos = 600 + i * 350
    pair = PipePair(cano_baixo, cano_baixo, x_pos)
    pipes.append(pair)
    all_sprites.add(pair.top_pipe, pair.bottom_pipe)
    all_pipes.add(pair.top_pipe, pair.bottom_pipe)
    
for pair in pipes:
    pair.update()
    pair.draw(screen)

crocos = []
for i in range(3):
    y_posic = random.randint(200, 500)
    x_posic = 700 + i * 200
    croco = croc(croc_img, x_posic, y_posic)
    crocos.append(croco)
    all_sprites.add(croco)
    all_crocos.add(croco)

start_screen = StartScreen(screen, clock, WIDTH, HEIGHT, FPS, "assets/barely_flying_start.png")
if start_screen.run() == "quit":
    pygame.quit()
    exit()

# Game over setup
game_over = False
game_over_image = pygame.image.load("assets/GAMe over.png")
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

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

    # Cria o loop de movimento do background somente no eixo x e do cano tambem
    bg_x -= bg_speed
    if bg_x <= -WIDTH:
        bg_x = 0

    cano_x -= cano_speed
    if cano_x <= -WIDTH:
        cano_x = 0

    all_sprites.update()

    # Verifica se o passaro saiu da tela resultando em game over
    if bird.rect.top < 0 or bird.rect.bottom >= HEIGHT:
        game_over = True

    hits = pygame.sprite.spritecollide(bird, all_pipes, True)
    if len(hits) > 0:
        game_over = True

    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + WIDTH, 0))
    all_sprites.draw(screen)
    all_pipes.draw(screen)

    # Se game over, mostra imagem e espera tecla
    if game_over:
        screen.blit(game_over_image, (0, 0))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                        running = False  # Você pode mudar aqui para reiniciar o jogo
        continue

    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)  # Limit FPS

pygame.quit()


