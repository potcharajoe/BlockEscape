import pygame
from pygame.locals import *
import random

WIDTH = int(random.uniform(300,500))
HEIGHT = int(random.uniform(100,200))
Y = 650-HEIGHT

class Ground(object):

    def __init__(self,color, pos):
        self.pos = pos
        self.color = color

    def move(self):
        self.pos -= 5

    def check_player(self,player):
        return 0<player.y-Y<5


    def render(self,surface):
        pygame.draw.rect(surface,self.color,(self.pos,Y,WIDTH,HEIGHT),0)

#####################################################################

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
        self.y += 10

    def check_ground(self):
        self.y=Y-self.radius/2

    def render(self,surface):
        pos=(int(self.x),int(self.y))
        pygame.draw.circle(surface,self.color,pos,self.radius,0)

