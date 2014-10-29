import os, random
import pygame, time

class Duck(object):
    def __init__(self, registry):
        self.registry = registry;
        self.surface = self.registry.get('surface')
        
        self.duck1 = pygame.image.load('media/images/duck1.png')
        self.duck2 = pygame.image.load('media/images/duck2.png')
        self.duck3 = pygame.image.load('media/images/duck3.png')
        self.pduck = 4
        
        #rsprites = pygame.transform.flip(sprites, True, False)

        xpos = random.randrange(0,self.surface.get_width() - 67,67)
        ypos = random.randrange(0,self.surface.get_height() - 220)
        #xspeed = random.randint(4, 8)
        #yspeed = random.randint(4, 8)
        xspeed = 3
        yspeed = 3
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
        xpos, ypos = self.position
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
