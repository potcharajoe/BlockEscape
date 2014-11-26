import pygame
from pygame.locals import *

class MySprites():

	def __init__(self,gameDisplay,gameWidth,gameHeight,sp_Path,sp_Total = 0,sp_Width = 0,sp_Height = 0):
		self.gameDisplay = gameDisplay
		self.gameWidth = gameWidth
		self.gameHeight = gameHeight
		
		self.SP = pygame.image.load(sp_Path)
		self.sp_Total = sp_Total
		self.sp_Width = sp_Width
		self.sp_Height = sp_Height

		self.cImage = 0
		self.delay = 0
		self.pauseDelay = 0
		self.cloop = 0

	def resetCountAndDelay():
		self.cImage = 0
		self.delay = 0
		self.pauseDelay = 0
		self.cloop = 0

	def play(self,x,y,delay):
		if self.cImage != self.sp_Total - 1:
			if self.delay > delay:  
					self.cImage += 1
					self.delay = 0
			else:
				self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def loop(self,x,y,delay):
		if self.cImage == self.sp_Total - 1:
			self.cImage = 0
			self.delay = 0
			self.cloop += 1
		elif self.delay > delay:  
				self.cImage += 1
				self.delay = 0
		else:
			self.delay += 1

		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def stopAt(self,x,y,delay,sp_Num):
		if self.cImage != sp_Num:
			if self.delay > delay:  
					self.cImage += 1
					self.delay = 0
			else:
				self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def pausePlay(self,x, y, delay, sp_Num,pauseDelay):
		if self.cImage != self.sp_total - 1:
			if self.cImage != sp_Num:
				if self.delay > delay:  
						self.cImage += 1
						self.delay = 0
				else:
					self.delay += 1
			else:
				if self.pauseDelay > pauseDelay:
					if self.delay > delay:  
						self.cImage += 1
						self.delay = 0
					else:
						self.delay += 1
		else:
			self.cloop += 1
		self.gameDisplay.blit(self.SP,(x,y),(self.cImage*self.sp_Width,0,self.sp_Width,self.sp_Height))

	def isStop(self):
		if self.cloop == 1:
			return True
		else:
			return False

	def renderImg(self,x,y):
		self.gameDisplay.blit(self.SP,(x,y))
