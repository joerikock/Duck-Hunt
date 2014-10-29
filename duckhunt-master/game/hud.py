import os, sys
import pygame

#class variables
BULLETS = 2
DUCK_COORDINATES = [320, 340, 360, 380, 400, 420, 440, 460, 480, 500]
#received red/white data. True = red, False = white
HIT_ARRAY= [True, False, False, True, True, False, False, False, False, False]
SCORE = 2655

class HUD(object):
    def __init__(self, surface):
        self.surface = surface
        self.shot = pygame.image.load('media/shot.png')
        self.bullet = pygame.image.load('media/bullet.png')
        self.hit = pygame.image.load('media/hit.png')
        self.score = pygame.image.load('media/score.png')
        self.red = pygame.image.load('media/red.png')
        self.white = pygame.image.load('media/white.png')
        self.font = pygame.font.Font("media/arcadeclassic.ttf", 20)

    def render(self):
        #Show the general HUD
        self.surface.blit(self.shot, (60,440))
        self.surface.blit(self.hit, (245,440))
        self.surface.blit(self.score, (620,440))

        #Show the bullets
        if BULLETS == 1:
            self.surface.blit(self.bullet, (72,445))
        elif BULLETS == 2:
            self.surface.blit(self.bullet, (72,445))
            self.surface.blit(self.bullet, (90,445))
        elif BULLETS == 3:
            self.surface.blit(self.bullet, (72,445))
            self.surface.blit(self.bullet, (90,445))
            self.surface.blit(self.bullet, (108,445))

        #Show the ducks that are hit and are not hit
        for i in DUCK_COORDINATES:
            if HIT_ARRAY[DUCK_COORDINATES.index(i)] == False:
                self.surface.blit(self.white, (i, 445))
            else:
                self.surface.blit(self.red, (i, 445))

        #Show the score
        label = self.font.render(str(SCORE), 1, (255,255,255))
        self.surface.blit(label, (630, 442))