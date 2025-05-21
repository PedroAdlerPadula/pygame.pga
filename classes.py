import pygame
from config import *
import random
FPS = 60
class Bird(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.original_image = img
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
        angle = min(self.speedy * 3, 45)  # Limita a rotação a 45 graus
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.rect.top > HEIGHT or self.rect.bottom < 0:
            state = GAME_OVER


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
        if self.rect.x <= - self.rect.width:
             self.rect.x = 1300
             self.speedx = -3



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
        
        self.reset_pipes(x_pos)

    def reset_pipes(self, x_pos):
        altura_al = random.randint(100, 300)
        self.top_pipe.rect.x = x_pos
        self.bottom_pipe.rect.x = x_pos

        self.top_pipe.rect.y = altura_al - self.top_pipe.rect.height
        self.bottom_pipe.rect.y = self.top_pipe.rect.bottom + 200 
    
    def update(self):
        self.top_pipe.update()
        self.bottom_pipe.update()

        # Quando o topo sair da tela, reposiciona ambos
        if self.top_pipe.rect.x <= -self.top_pipe.rect.width:
            self.reset_pipes(1300)

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
