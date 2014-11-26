import pygame
from pygame.locals import *
import random



class Item(object):

	def __init__(self,pos,color,width=30,height=30):
		(self.x,self.y)=pos
		self.width=width
		self.height=height
		self.color=color
		self.image = pygame.image.load("item.png")
		self.rectitem=pygame.Rect(self.x,self.y,self.width,self.height)

	def randomspawn(self,display):
		self.x = random.randint(0,display.get_width()-self.width)
		self.y = random.randint(0,display.get_height()-self.height)


	def render(self,surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.rect(surface,self.color,self.rectitem,1)
		surface.blit(self.image,pos)

	def getRectitem(self):
		return self.rectitem

	def update(self):

		self.rectitem=pygame.Rect(self.x,self.y,self.width,self.height)








