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

background_image = pygame.image.load("Backgorun1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))