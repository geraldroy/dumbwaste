import pygame
import time

pygame.init()

EDEP_pogi = True

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)

bat_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('No Overcharging')
clock = pygame.time.Clock()

batImg = pygame.image.load('sprites/battery.png')
plugImg = pygame.image.load('sprites/plug.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def bat(x,y):
    gameDisplay.blit(batImg,(x,y))

def plug(x,y):
    gameDisplay.blit(plugImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    #game_loop()
    pygame.quit()
    quit()

    

def crash():
    message_display('Overcharged!!!')


def game_loop():
    x = (display_width/4)
    y = (display_height/4)
    x2 = (3 * display_width/4)

    x_change = 0

    thing_startx = x + 5
    thing_starty = y + 20 + 250
    thing_speed = 5
    thing_width = 200
    thing_height = 0
    color = red

    socketx = x2
    sockety = y
    socket_height = 50
    socket_width = 80
    socket_color = black

    gameExit = False
    
    
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (250-63) <= thing_height <= 250:
                    	print('you won')
                    	gameExit = True
               
        gameDisplay.fill(white)
        
        things(thing_startx, thing_starty, thing_width, thing_height, color)
        bat(x,y)
        plug(x2,y)

        ###########################
        #battery status update
        
        thing_height += 5
        thing_starty -= 5
        
        if thing_height > 250:
        	crash()
        elif (250-63) <= thing_height <= 250:
        	color = green
        elif 62 < thing_height < (250 - 62):
        	color = yellow
        else:
        	color = red
        ###########################3
            
        pygame.display.update()
        clock.tick(30)



game_loop()
