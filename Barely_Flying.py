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

# Carregue os frames do pássaro a partir do sprite sheet Bird1-1.png
bird_images = []
sprite_sheet = pygame.image.load("assets/Flappy Bird Assets/Player/StyleBird1/Bird1-1v2.png")
for i in range(4):  # 4 frames na horizontal
    frame = sprite_sheet.subsurface(pygame.Rect(i * 16, 0, 16, 12))
    frame = pygame.transform.scale(frame, (WIDTH_BIRD, HEIGHT_BIRD))
    bird_images.append(frame)

bullet_img = pygame.image.load("ASSETS/Laser_bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (60,60))
all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
bird = Bird(bird_images, all_sprites, all_bullets, bullet_img)

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

# Criando grupos para fazer as colisões

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
for i in range(2):  # Agora só cria 2 crocodilos
    y_posic = random.randint(200, 500)
    x_posic = 700 + i * 200
    croco = croc(croc_img, x_posic, y_posic)
    crocos.append(croco)
    all_sprites.add(croco)
    all_crocos.add(croco)

for croco in crocos:
    croco.update()
    croco.draw(screen)

start = True
if start == True:
    start_screen = StartScreen(screen, clock, WIDTH, HEIGHT, FPS, "assets/barely_flying_start.png")
    if start_screen.run() == "quit":
        pygame.quit()
        exit()

# Game over setup
game_over = False
game_over_image = pygame.image.load("assets/GAMe over.png")
game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

# Adicione após a criação dos pipes
score = 0
font = pygame.font.SysFont(None, 60)

# Marcar se o pássaro já passou por cada pipe pair
for pair in pipes:
    pair.passed = False

running = True
print(crocos)

def reset_game():
    # Reset bird position and properties
    bird.rect.x = 200
    bird.rect.y = 300
    bird.gravidade = 1
    
    # Clear all sprites
    all_sprites.empty()
    all_pipes.empty()
    all_crocos.empty()
    all_bullets.empty()
    
    # Add bird back to sprites
    all_sprites.add(bird)
    
    # Reset pipes
    pipes.clear()
    for i in range(4):
        x_pos = 600 + i * 350
        pair = PipePair(cano_baixo, cano_baixo, x_pos)
        pipes.append(pair)
        all_sprites.add(pair.top_pipe, pair.bottom_pipe)
        all_pipes.add(pair.top_pipe, pair.bottom_pipe)
    
    # Reset crocodiles
    crocos.clear()
    for i in range(2):
        y_posic = random.randint(200, 500)
        x_posic = 700 + i * 200
        croco = croc(croc_img, x_posic, y_posic)
        crocos.append(croco)
        all_sprites.add(croco)
        all_crocos.add(croco)
    
    # Reset score
    global score
    score = 0
    
    # Reset pipe passed status
    for pair in pipes:
        pair.passed = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.gravidade = -10
            if event.key == pygame.K_s:
                # Atira um projétil
                bird.shoot()

    # Cria o loop de movimento do background somente no eixo x e do cano tambem
    bg_x -= bg_speed
    if bg_x <= -WIDTH:
        bg_x = 0

    cano_x -= cano_speed
    if cano_x <= -WIDTH:
        cano_x = 0

    all_sprites.update()
    for pair in pipes:
        pair.update()

    # Verifica se o passaro saiu da tela resultando em game over
    if bird.rect.top < 0 or bird.rect.bottom >= HEIGHT:
        game_over = True

    hits = pygame.sprite.spritecollide(bird, all_pipes, True)
    hits = hits + pygame.sprite.spritecollide(bird, all_crocos, True)
    hits2 = pygame.sprite.groupcollide(bird.all_bullets, all_crocos, True, True)
    if len(hits) > 0:
        game_over = True
        new_croc = croc(croc_img, 1200, random.randint(200, 500))
        all_sprites.add(new_croc)
        all_crocos.add(new_croc)

    if len(hits2) > 0:
        score += 1
        all_crocos.remove(croco)
        new_croc = croc(croc_img, 1200, random.randint(200, 500))
        all_sprites.add(new_croc)
        all_crocos.add(new_croc)
    # Atualiza score: se o pássaro passou pelo cano e ainda não contou ponto
    for pair in pipes:            
        # O pássaro passou pelo centro do cano (ajuste 200 para a posição x do pássaro)
        if not pair.passed and pair.top_pipe.rect.right < bird.rect.left:
            score += 1
            pair.passed = True

    screen.blit(background_image, (bg_x, 0))
    screen.blit(background_image, (bg_x + WIDTH, 0))
    all_sprites.draw(screen)
    all_pipes.draw(screen)

    # Desenha o score no canto superior esquerdo
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (20, 20))

    # Se game over, mostra imagem e espera tecla
    if game_over:
    # Mostrar tela de game over
        screen.blit(game_over_image, (0, 0))
        pygame.display.flip()

        esperando = True
        while esperando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esperando = False
        
        # if not running:
        #     break  # Sai do loop principal e fecha o jogo

        # Voltar para a tela inicial
        start_screen = StartScreen(screen, clock, WIDTH, HEIGHT, FPS, "assets/barely_flying_start.png")
        if start_screen.run() == "quit":
            running = False
            break

        # Reset the game completely
        reset_game()
        game_over = False
        continue


    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)  # Limit FPS

pygame.quit()
