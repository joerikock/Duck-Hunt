import os, random
import pygame

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
        ypos = random.randrange(0,self.surface.get_height() - 67,67)
        xspeed = random.randint(6, 11)
        yspeed = random.randint(6, 11)
        self.position = xpos, ypos
        self.speed = xspeed, yspeed

    def update(self):
        xpos, ypos = self.position
        xspeed, yspeed = self.speed

        if xpos < 0 or xpos > self.surface.get_width() - 67:
            xspeed = -xspeed
        if ypos < 0 or ypos > self.surface.get_height() - 220:
            yspeed = -yspeed
        
        self.position = (xpos + xspeed), (ypos + yspeed)
        self.speed = xspeed, yspeed

    def render(self):
        xpos, ypos = self.position
        if self.pduck == 4:
            self.surface.blit(self.duck1,(xpos,ypos))
            self.pduck = 1
        elif self.pduck == 1:
            self.surface.blit(self.duck2,(xpos,ypos))
            self.pduck = 2
        elif self.pduck == 2:
            self.surface.blit(self.duck3,(xpos,ypos))
            self.pduck = 3
        elif self.pduck == 3:
            self.surface.blit(self.duck2,(xpos,ypos))
            self.pduck = 4

    def execute(self):
        self.update()
        self.render()
