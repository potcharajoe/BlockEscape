import pygame
from pygame.locals import *
from Ground import *
import random
class Player(object):

    global gravity
    gravity = 4

    def __init__(self,radius,color,pos,speed=(20,0)):
        (self.x,self.y) = pos
        (self.vx,self.vy) = speed
        self.color = color
        self.radius = radius

    def move(self,delta_t):
        self.x += self.vx*delta_t
        self.y += gravity

    def jump(self):
        self.y += 20

    def check_ground(self):
        self.y = Y - self.radius / 2 - 20
        # 

    def render(self,surface):
        pos=(int(self.x),int(self.y))
        pygame.draw.circle(surface,self.color,pos,self.radius,0)
