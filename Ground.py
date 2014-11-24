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

