import pygame
from pygame.locals import *

import gamelib
from Ground import *
from Player import *

class MonsterRunGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(MonsterRunGame, self).__init__('MonsterRun', MonsterRunGame.BLACK)
        self.ground = Ground(color=MonsterRunGame.WHITE,
                         pos=90)
        self.player = Player(radius=20,pos=(200,440),color=MonsterRunGame.GREEN)
        self.score = 0

    def init(self):
        super(MonsterRunGame, self).init()
        self.render_score()

    def update(self):
        self.player.move(1./self.fps)
        self.ground.move()

        # self.ground.check_player(self.player)
        if(self.ground.check_player(self.player)):
            self.player.check_ground()

        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, MonsterRunGame.WHITE)

    def render(self, surface):
        self.ground.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = MonsterRunGame()
    game.run()

if __name__ == '__main__':
    main()