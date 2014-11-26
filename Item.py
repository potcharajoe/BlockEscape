import pygame
from pygame.locals import *
import random



class Item(object):

	def __init__(self,pos,width=30,height=30):
		(self.x,self.y)=pos
		width = 30
		height = 30
		self.image = pygame.image.load("item.png")

	def randomspawn(self):
		self.x = random.randint(0,window_size[0]-self.width)
		self.y = random.randint(0,window_size[1]-self.height)


	def render(self,surface):
		pos = (int(self.x),int(self.y))

		surface.blit(self.image,pos)
