import pygame
from config import *
import random

class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
        def __init__(self, img, right, centery):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()

            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.centery = centery
            self.rect.right = right
            self.speedx = 10  # Velocidade fixa para cima

        def update(self):
            # A bala só se move no eixo y
            self.rect.x += self.speedx

            # Se o tiro passar do inicio da tela, morre.
            if self.rect.bottom < 0:
                self.kill()
class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_images, all_sprites, all_bullets, bullet_img):
        super().__init__()
        self.images = bird_images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 200
        self.rect.y = 300
        self.gravidade = 1      
        self.animation_counter = 0
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500
        self.groups = (self.all_sprites, self.all_bullets)
        self.bullet_img = bullet_img

    def update(self):
        self.gravidade += 0.2  
        self.rect.y += self.gravidade  

        # Animação: troca de frame a cada 5 updates
        self.animation_counter += 1
        if self.animation_counter >= 5:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.animation_counter = 0

        # Inclinação baseada na velocidade
        angle = -self.gravidade * 3  
        angle = max(-30, min(30, angle))  # Limita o ângulo entre -30 e 30 graus

        # Atualiza a imagem com rotação
        base_image = self.images[self.image_index]
        self.image = pygame.transform.rotate(base_image, angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shoot(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet = Bullet(self.bullet_img, self.rect.right, self.rect.centery)
            self.all_sprites.add(new_bullet)
            self.all_bullets.add(new_bullet)
            #self.assets[PEW_SOUND].play()

class Pipe(pygame.sprite.Sprite):
    def __init__(self, img, x, y, is_top):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.speedx = -3
        self.is_top = is_top

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speedx
        # if self.rect.x <= - self.rect.width:
        #      self.rect.x = 1300
        #      self.speedx = -3



class Pipe_2(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        

class PipePair(pygame.sprite.Sprite):
    def __init__(self, img_top, img_bottom, x_pos):
        super().__init__()
        
        self.top_pipe = Pipe(img_top, x_pos, 0, True)
        self.bottom_pipe = Pipe(img_bottom, x_pos, 0, False)
        self.passed = False
        
        self.reset_pipes(x_pos)

    def reset_pipes(self, x_pos):
        altura_al = random.randint(100, 300)
        self.top_pipe.rect.x = x_pos
        self.bottom_pipe.rect.x = x_pos

        self.top_pipe.rect.y = altura_al - self.top_pipe.rect.height
        self.bottom_pipe.rect.y = self.top_pipe.rect.bottom + 200 
    
    def update(self):
        # Quando o topo sair da tela, reposiciona ambos
        if self.top_pipe.rect.x <= -self.top_pipe.rect.width:
            self.reset_pipes(1300)
            self.passed = False  # Reseta o estado de passagem quando reposiciona

    def draw(self, screen):
        self.top_pipe.draw(screen)
        self.bottom_pipe.draw(screen)

class StartScreen:
    def __init__(self, screen, clock, width, height, fps, image_path):
        self.screen = screen
        self.clock = clock
        self.width = width
        self.height = height
        self.fps = fps
        
        self.image = pygame.image.load("assets/barelyflyingStartScreen.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.img_rect = self.image.get_rect(center=(width // 2, height // 2))
    
    def run(self):
        esperando = True
        while esperando:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.image, self.img_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.img_rect.collidepoint(event.pos):
                        esperando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esperando = False
            
            pygame.display.update()
            self.clock.tick(self.fps)

class croc(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.speedx = -5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x <= - self.rect.width:
             self.rect.x = random.randint(1200, 1400)
             self.speedx = -5
             self.rect.y = random.randint(200,500)
             
class GameOverScreen:
    def __init__(self, screen, clock, width, height, fps, image_path):
        self.screen = screen
        self.clock = clock
        self.width = width
        self.height = height
        self.fps = fps
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.img_rect = self.image.get_rect(center=(width // 2, height // 2))

    def run(self):
        esperando = True
        while esperando:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.image, self.img_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esperando = False
            
            pygame.display.update()
            self.clock.tick(self.fps)

    class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
        def __init__(self, img, bottom, centerx):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()

            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.speedx = -10  # Velocidade fixa para cima

        def update(self):
            # A bala só se move no eixo y
            self.rect.x += self.speedx

            # Se o tiro passar do inicio da tela, morre.
            if self.rect.bottom < 0:
                self.kill()
class BackToMenu:
    def __init__(self, screen, clock, width, height, fps, image_path):
        self.screen = screen
        self.clock = clock
        self.width = width
        self.height = height
        self.fps = fps
        
        self.image = pygame.image.load("assets/barelyflyingStartScreen.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.img_rect = self.image.get_rect(center=(width // 2, height // 2))
    
    def run(self):
        esperando = True
        while esperando:
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.image, self.img_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.img_rect.collidepoint(event.pos):
                        esperando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        esperando = False
            
            pygame.display.update()
            self.clock.tick(self.fps)
