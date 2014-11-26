import pygame
from pygame.locals import *
import random

class Item(object):

	def __init__(self,pos):
		(self.x,self.y)=pos
		self.image = pygame.image.load("item.png")

	def randomspawn(self):
		self.x = random.randint(10,1014)
		self.y = random.randint(10,710)

	def render(self,surface):
		pos = (int(self.x),int(self.y))

		surface.blit(self.image,pos)
