import os, random
import pygame, time

class Duck(object):
    def __init__(self, surface):
        self.surface = surface

        #load duck images in normal duck image variables
        self.nduck1 = pygame.image.load('media/images/duck1.png')
        self.nduck2 = pygame.image.load('media/images/duck2.png')
        self.nduck3 = pygame.image.load('media/images/duck3.png')

        #flip the duck images
        self.rduck1 = pygame.transform.flip(self.nduck1, True, False)
        self.rduck2 = pygame.transform.flip(self.nduck2, True, False)
        self.rduck3 = pygame.transform.flip(self.nduck3, True, False)

        #set previous duck to last animation so update function starts with the first
        self.pduck = 4

        #initialize randomized starting position and speed of duck
        xpos = random.randrange(0,self.surface.get_width() - 67, 67)
        ypos = random.randrange(0,self.surface.get_height() - 220, 67)
        xspeed = random.randint(2, 5)
        yspeed = random.randint(2, 5)

        #if horizontal speed is positive, use normal duck image
        if xspeed >= 0:
            self.duck1 = self.nduck1
            self.duck2 = self.nduck2
            self.duck3 = self.nduck3
        #else use the reversed image
        else:
            self.duck1 = self.rduck1
            self.duck2 = self.rduck2
            self.duck3 = self.rduck3

        #initialize duck  
        self.duck = self.duck1 
        self.position = xpos, ypos
        self.speed = xspeed, yspeed

    #reverse the duck image when this method is called
    def flipducks(self):
        if self.duck1 == self.nduck1:
            self.duck1 = self.rduck1
        else:
            self.duck1 = self.nduck1
            
        if self.duck2 == self.nduck2:
            self.duck2 = self.rduck2
        else:
            self.duck2 = self.nduck2
            
        if self.duck3 == self.nduck3:
            self.duck3 = self.rduck3
        else:
            self.duck3 = self.nduck3

    def render(self):
        xpos, ypos = self.position
        xspeed, yspeed = self.speed

        #if duck hits vertical wall, reverse horizontal speed and flip image
        if xpos < 0 or xpos > self.surface.get_width() - 67:
            xspeed = -xspeed
            self.flipducks()
        #if duck hits horizontal wall, reverse vertical speed
        if ypos < 0 or ypos > self.surface.get_height() - 220:
            yspeed = -yspeed

        #update position and speed
        self.position = (xpos + xspeed), (ypos + yspeed)
        self.speed = xspeed, yspeed

        #render the duck
        self.surface.blit(self.duck,(xpos,ypos))

    #cycle through the flying animation
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
