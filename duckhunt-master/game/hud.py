"""
The class for the HUD (Head-Up Display) in our game. It shows the current
number of bullets, the score, and all the ducks of the current round. If
a duck is red, it is killed. A white duck is yet to be killed or the player
failed to kill this duck. This class uses the input of the FPGA board to
visualize the display.
"""

# This file's imports.
import os, sys
import pygame

#class variables
BULLETS = [1,0]
DUCK_COORDINATES = [320, 340, 360, 380, 400, 420, 440, 460, 480, 500]

#received red/white data. True = red, False = white
HIT_ARRAY= [1,0,0,1,0,0,1,1,1,1]
SCORE = [1,0,1,0,0,0,0,0,0,1,1,0]

#The HUD class responsible for showing the on-screen HUD
class HUD(object):
    
    # The initialisation class. It receives a surface to blit on.
    def __init__(self, surface):
        self.surface = surface
        self.shot = pygame.image.load('media/shot.png')
        self.bullet = pygame.image.load('media/bullet.png')
        self.hit = pygame.image.load('media/hit.png')
        self.score = pygame.image.load('media/score.png')
        self.red = pygame.image.load('media/red.png')
        self.white = pygame.image.load('media/white.png')
        self.font = pygame.font.Font("media/arcadeclassic.ttf", 20)

    #This update method is called in every iteration in the main game loop.
    def update(self):
        
        #Show the general HUD
        self.surface.blit(self.shot, (60,440))
        self.surface.blit(self.hit, (245,440))
        self.surface.blit(self.score, (620,440))

        #Show the bullets
        if int(''.join([str(bit) for bit in BULLETS]), 2) == 1:
            self.surface.blit(self.bullet, (72,445))
        elif int(''.join([str(bit) for bit in BULLETS]), 2) == 2:
            self.surface.blit(self.bullet, (72,445))
            self.surface.blit(self.bullet, (90,445))
        elif int(''.join([str(bit) for bit in BULLETS]), 2) == 3:
            self.surface.blit(self.bullet, (72,445))
            self.surface.blit(self.bullet, (90,445))
            self.surface.blit(self.bullet, (108,445))

        #Show the ducks that are hit and are not hit
        for i in DUCK_COORDINATES:
            if HIT_ARRAY[DUCK_COORDINATES.index(i)] == 0:
                self.surface.blit(self.white, (i, 445))
            else:
                self.surface.blit(self.red, (i, 445))

        #Show the score
        label = self.font.render(str(int(''.join([str(bit) for bit in SCORE]), 2)), 1, (255,255,255))
        self.surface.blit(label, (630, 442))
