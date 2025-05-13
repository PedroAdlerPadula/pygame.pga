import pygame 
import random
from math import * 


pygame.init()


# Constants 
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
# Game Variables    
GRAVITY = 0.5
JUMP_STRENGTH = 10

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Barely Flying")
clock = pygame.time.Clock()
# Load images

background_image = pygame.image.load("Backgorun1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))