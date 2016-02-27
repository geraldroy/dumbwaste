import pygame
import time
import random

display_width = 800
display_height = 600
 

black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
green = (0, 150 ,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 
car_width = 80
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dumbwaste')
clock = pygame.time.Clock()
gameDisplay.fill(white)