import pygame
from pygame.locals import *

class Wall(object):

	def __init__(self,pos,width,height,color):
		(self.x,self.y)=pos
		self.width=width
		self.height=height
		self.color=color
		self.rectwall=pygame.Rect(self.x,self.y,self.width,self.height)

	def render(self,surface):

		pygame.draw.rect(surface,self.color,self.rectwall,0)

	def getRectwall(self):

		return self.rectwall
