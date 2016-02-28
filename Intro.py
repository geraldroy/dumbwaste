import pygame
import time
import random

import d as _d
 
pygame.init()

display_width = 800
display_height = 600


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('dumbwaste')
clock = pygame.time.Clock()


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)


game_intro()
d.game_loop()
game_loop()
pygame.quit()
quit()        