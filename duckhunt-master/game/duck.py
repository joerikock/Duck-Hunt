import os, random
import pygame, time

class Duck(object):
    def __init__(self, surface):
        self.surface = surface
        self.duck1 = pygame.image.load('media/images/duck1.png')
        self.duck2 = pygame.image.load('media/images/duck2.png')
        self.duck3 = pygame.image.load('media/images/duck3.png')
        self.pduck = 4
        
        #rsprites = pygame.transform.flip(sprites, True, False)

        xpos = random.randrange(0,self.surface.get_width() - 67, 67)
        ypos = random.randrange(0,self.surface.get_height() - 220, 67)
        xspeed = random.randint(2, 5)
        yspeed = random.randint(2, 5)
        self.position = xpos, ypos
        self.speed = xspeed, yspeed
        self.duck = self.duck1

    def render(self):
        xpos, ypos = self.position
        xspeed, yspeed = self.speed

        if xpos < 0 or xpos > self.surface.get_width() - 67:
            xspeed = -xspeed
        if ypos < 0 or ypos > self.surface.get_height() - 220:
            yspeed = -yspeed
        
        self.position = (xpos + xspeed), (ypos + yspeed)
        self.speed = xspeed, yspeed
        self.surface.blit(self.duck,(xpos,ypos))

    def update(self):
        if self.pduck == 4:
            self.duck = self.duck1
            self.pduck = 1
        elif self.pduck == 1:
            self.duck = self.duck2
            self.pduck = 2
        elif self.pduck == 2:
            self.duck = self.duck3
            self.pduck = 3
        elif self.pduck == 3:
            self.duck = self.duck2
            self.pduck = 4
