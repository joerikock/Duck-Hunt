import os, random
import pygame

surface = pygame.display.set_mode((800, 500))
running = True

class Duck(object):
    def __init__(self):     
        self.duck_clock = pygame.time.Clock()

        self.duck1 = pygame.image.load('../media/images/duck1.png')
        self.duck2 = pygame.image.load('../media/images/duck2.png')
        self.duck3 = pygame.image.load('../media/images/duck3.png')
        #self.ducklist = [duck1,duck2,duck3]
        self.pduck = 3
        
        #rsprites = pygame.transform.flip(sprites, True, False)

        xpos = random.choice([0, surface.get_width()-67])
        ypos = random.randint(0, surface.get_height() / 2)
        xspeed = 1
        yspeed = 1
        self.position = xpos, ypos
        self.vector = xspeed, yspeed

    def update(self):
        xpos, ypos = self.position
        xspeed, yspeed = self.vector
        self.position = (xpos + xspeed), (ypos + yspeed)

    def render(self):
        xpos, ypos = self.position
        if self.pduck == 3:
            surface.blit(self.duck1, (xpos,ypos))
            self.pduck = 1
        elif self.pduck == 1:
            surface.blit(self.duck2, (xpos,ypos))
            self.pduck = 2
        if self.pduck == 2:
            surface.blit(self.duck3, (xpos,ypos))
            self.pduck = 3      
        self.duck_clock.tick(5)

    def execute(self):
        self.update()
        self.render()

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
