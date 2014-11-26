import pygame
from pygame.locals import *

acc = 5

class Hero(object):

	def __init__(self,radius,color,pos):
		(self.x, self.y) = pos
		self.radius = radius
		self.color = color

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def move_right(self):
		self.x += 10*acc

	def move_left(self):
		self.x -= 10*acc

	def move_up(self):
		self.y -= 10*acc

	def move_down(self):
		self.y += 10*acc

	def resetspeed(self):
		self.vx=0
		self.vy=0

	def plusacc(self):
		acc+=acc

	def render(self,surface):
		pos = (int(self.x),int(self.y))
		pygame.draw.circle(surface,self.color,pos,self.radius,0)
