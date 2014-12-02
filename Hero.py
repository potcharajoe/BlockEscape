import pygame
from pygame.locals import *


class Hero(object):

	def __init__(self,radius,color,pos,heroheight=16,herowidth=16):
		(self.x, self.y) = pos
		self.radius = radius
		self.color = color
		self.herowidth=herowidth
		self.heroheight=heroheight
		self.recthero=pygame.Rect(self.x-self.radius,self.y-self.radius,self.herowidth,self.heroheight)
		self.herospeed = 2

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def move_right(self):
		self.x += self.herospeed

	def move_left(self):
		self.x -= self.herospeed

	def move_up(self):
		self.y -= self.herospeed

	def move_down(self):
		self.y += self.herospeed

	def resetspeed(self):
		self.vx=0
		self.vy=0

	def resetpos(self,display):
		self.x=display.get_width()/2
		self.y=display.get_height()/2

	def checkplayer(self,display):

		if self.x < self.radius:
			return True
		elif self.y < self.radius:
			return True
		elif self.x > display.get_width()-self.radius:
			return True
		elif self.y > display.get_height()-self.radius:
			return True

	def render(self,surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface,self.color,pos,self.radius,0)

	def getRecthero(self):

		return self.recthero

	def update(self):
		self.recthero=pygame.Rect(self.x-self.radius,self.y-self.radius,self.herowidth,self.heroheight)








