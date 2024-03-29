import pygame
from pygame.locals import *
import random


gameheight = 720
gamewidth = 1024


class Enemy(object):

	def __init__(self,color,pos,speed,rectwidth,rectheight,addspeed=1):
		if(random.randint(0,9)<5):
			(self.vx,self.vy)=speed
		else:
			(self.vx,self.vy)=(-speed[0],-speed[1])
		(self.x,self.y)=pos
		self.rectwidth = rectwidth
		self.rectheight = rectheight
		self.color=color
		self.addspeed=addspeed
		self.rectenemy=pygame.Rect(self.x,self.y,self.rectwidth,self.rectheight)


	def getRectenemy(self):
		return self.rectenemy

	def resetspeed(self):
		if(random.randint(0,9)<5):
			dir=1
		else:
			dir=-1
		self.vx = 100*dir
		self.vy = 50*dir

	def move(self,delta_t):

		self.x += self.vx*delta_t*self.addspeed
		self.y += self.vy*delta_t*self.addspeed


	def change_color(self):
		self.color = pygame.Color(random.randrange(150,255,40),random.randrange(0,150,40),random.randrange(150,255,40))

	def render(self,surface):
		
		pygame.draw.rect(surface,self.color,self.rectenemy,10)

	def moveinverseone(self):
		self.vx = (self.vx)
		self.vy = -(self.vy)

	def moveinversetwo(self):
		self.vx = -(self.vx)
		self.vy = (self.vy)

	def update(self):
		self.rectenemy=pygame.Rect(self.x,self.y,self.rectwidth,self.rectheight)










