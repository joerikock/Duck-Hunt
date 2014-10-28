import os, random
import pygame
#surface = pygame.display.set_mode((800, 500))
#running = True

class Duck(object):
    def __init__(self, registry):
        self.registry = registry;
        self.surface = self.registry.get('surface')
        self.animationclock = pygame.time.Clock()

        self.duck1 = pygame.image.load('media/images/duck1.png')
        self.duck2 = pygame.image.load('media/images/duck2.png')
        self.duck3 = pygame.image.load('media/images/duck3.png')
        self.pduck = 4
        
        #rsprites = pygame.transform.flip(sprites, True, False)

        xpos = random.randrange(0,self.surface.get_width() - 67,67)
        ypos = random.randrange(0,self.surface.get_height() - 67,67)
        xspeed = 10
        yspeed = 10
        self.position = xpos, ypos
        self.speed = xspeed, yspeed

    def update(self):
        xpos, ypos = self.position
        xspeed, yspeed = self.speed

        if xpos < 0 or xpos > self.surface.get_width() - 67:
            xspeed = -xspeed
        if ypos < 0 or ypos > self.surface.get_height() - 67:
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
        self.animationclock.tick(5)

    def execute(self):
        self.update()
        self.render()
"""
ducks = [Duck() for i in range(1,3)]
while running:
    surface.fill((255,255,255))
    for i in ducks:
        ducks[ducks.index(i)].execute()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
"""
