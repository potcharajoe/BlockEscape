import pygame
from pygame.locals import *
import random

import gamelib
from Enemy import *
from Hero import *
from Item import *
from Wall import *



class MonsterRunGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    RED = pygame.Color('red')
    
    def __init__(self):
        super(MonsterRunGame, self).__init__('MonsterRun', MonsterRunGame.BLACK)
        self.hero = Hero(radius=8,pos=(self.window_size[0]/2,self.window_size[1]/2),color=MonsterRunGame.RED)
        self.topwall=Wall(pos=(0,-1),width=self.window_size[0],height=1,color=MonsterRunGame.WHITE)
        self.bottomwall=Wall(pos=(0,self.window_size[1]-1),width=self.window_size[0],height=1,color=MonsterRunGame.WHITE)
        self.rightwall=Wall(pos=(self.window_size[0],0),width=1,height=self.window_size[1],color=MonsterRunGame.WHITE)
        self.leftwall=Wall(pos=(-1,0),width=1,height=self.window_size[1],color=MonsterRunGame.WHITE)
        self.enemies=[]
        self.item=Item(pos=(random.randint(10,1014),random.randint(10,710)))
        self.score = 0

        for i in range(0,6):            
            enemy = Enemy(color=MonsterRunGame.GREEN,pos=(random.randrange(20,800,80),random.randrange(20,500,80)),speed=(100,50),rectwidth=random.randrange(30,120),rectheight=random.randrange(30,120))
            self.enemies.append(enemy)

    def init(self):
        super(MonsterRunGame, self).init()
        self.render_score()

    def update(self):

        for enemy in self.enemies:
            enemy.update()
            enemy.move(1./self.fps,pygame.time.get_ticks()/1000)

            if(enemy.getRectenemy().colliderect(self.topwall.getRectwall()) and enemy.y<5 ):
                enemy.y = 1
                enemy.moveinverseone()
            elif (enemy.getRectenemy().colliderect(self.bottomwall.getRectwall()) and (enemy.y>715-enemy.rectheight)):
                enemy.y = 719-enemy.rectheight
                print "collision"
                enemy.moveinverseone()


        if self.is_key_pressed(K_UP):
            self.hero.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.hero.move_down()
        elif self.is_key_pressed(K_LEFT):
            self.hero.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.hero.move_right()
        print pygame.time.get_ticks()/1000

        
    def render_score(self):

        self.score_image = self.font.render("Score = %d" % self.score, 0, MonsterRunGame.WHITE)

    def render(self, surface):

        for enemy in self.enemies:
            enemy.render(surface)
        self.hero.render(surface)
        self.topwall.render(surface)
        self.bottomwall.render(surface)
        self.leftwall.render(surface)
        self.rightwall.render(surface)
        self.item.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = MonsterRunGame()
    game.run()

if __name__ == '__main__':
    main()