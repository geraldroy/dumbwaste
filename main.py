import pygame
import time
import random
from specs import *


class Game():
	def __init__(self):
		self.dumbwaste = pygame.init()
		self.gameDisplay = pygame.display.set_mode((display_width, display_height))
		self.caption = pygame.display.set_caption('Dumbwaste')

	def run(self):
		gameDisplay.fill(white)
		clock = pygame.time.Clock()
		print "hello"


		pygame.quit()
		quit()
def main():
	app = Game()
	app.run() 
	print "hi"

main()
pygame.quit()
quit()        