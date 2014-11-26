import pygame
from pygame.locals import *
import random


gameheight = 720
gamewidth = 1024

class Enemy(object):

	def __init__(self,color,pos,speed,rectwidth,rectheight):
		if(random.randint(0,9)<5):
			(self.vx,self.vy)=speed
		else:
			(self.vx,self.vy)=(-speed[0],-speed[1])
		(self.x,self.y)=pos
		self.rectwidth = rectwidth
		self.rectheight = rectheight
		self.color=color
		self.rectenemy=pygame.Rect(self.x,self.y,self.rectwidth,self.rectheight)

	def randommove(self):
		if(random.randint(0,9)<5):
			return 1
		else:
			return -1

	def getRectenemy(self):
		return self.rectenemy

	def move(self,delta_t,clock):

		self.x += self.vx*delta_t*clock
		self.y += self.vy*delta_t*clock


	def change_color(self,color):
		color = random.chioce(COLOR)

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










