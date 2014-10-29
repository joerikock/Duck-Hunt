"""
This is the main class of our game. This controller is pretty much all about
the main while-loop in the 'execute'-method. This class constantly receives
input from the FPGA board. It creates the game window, en instantiates all
other classes of our application.
"""

# This file's imports.
import os, sys, time
import pygame
import pygame.transform
import pygame.mouse
from game.duck import Duck
from game.gun import Gun
from game.hud import HUD

# Game parameters
surface = pygame.display.set_mode((800, 500))
background = pygame.image.load('media/background.jpg')
FRAMES_PER_SECOND = 50

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

# The Controller class, responsible for the running of the game.
class Controller(object):

    # The constructor of Controller. It sets all the main objects and timers.
    def __init__(self):
        self.running = True
        surface.blit(background, (0, 0))
        self.hud = HUD(surface)
        self.ducks = [Duck(surface) for i in range(0,2)]
        self.gun = Gun(surface)
        self.animationclock = pygame.time.Clock()
        self.time0 = time.time()*1000

    # This method contains the main game loop.
    def execute(self):        
        while self.running:
            surface.blit(background, (0, 0))
            for i in self.ducks:
                self.ducks[self.ducks.index(i)].render()
                time1 = time.time()*1000
                if (time1-self.time0)%200 < 30:
                    self.ducks[self.ducks.index(i)].update()
            self.gun.render()
            self.hud.update()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.animationclock.tick(FRAMES_PER_SECOND)
        pygame.quit()

# This is the execution of our application. A Controller object is created and executed. 
controller = Controller()
controller.execute()
