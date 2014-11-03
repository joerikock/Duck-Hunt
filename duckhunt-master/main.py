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
from gpioHandler import Words

# Game parameters
surface = pygame.display.set_mode((800, 500))
background = pygame.image.load('media/background.jpg')
background_top = pygame.image.load('media/background_top.jpg')
background_bottom = pygame.image.load('media/background_bottom.jpg')
FRAMES_PER_SECOND = 1000
GUNX = [0,0,1,1,0,0,1,0,0,0]
GUNY = [0,0,1,1,0,0,1,0,0]

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

# The Controller class, responsible for the running of the game.
class Controller(object):

    # The constructor of Controller. It sets all the main objects and timers.
    def __init__(self):
        self.running = True
        surface.blit(background_top, (0, 0))
        surface.blit(background_bottom, (0, 347))
        self.hud = HUD(surface)
        self.ducks = [Duck(surface) for i in range(0,2)]
        self.gun = Gun(surface)
        self.animationclock = pygame.time.Clock()
        self.time0 = time.time()*1000

    # This method contains the main game loop.
    def execute(self):        
        while self.running:
            surface.blit(background_top, (0, 0))

            # This renders the ducks and makes them flap their wings.
            for i in self.ducks:
                self.ducks[self.ducks.index(i)].render()
                time1 = time.time()*1000
                if (time1-self.time0)%200 < 30:
                    self.ducks[self.ducks.index(i)].update()

            # Render the gun and the HUD.
            self.gun.setPosition((int(''.join([str(bit) for bit in GUNX]), 2), int(''.join([str(bit) for bit in GUNY]), 2)))
            self.gun.render()
            self.hud.update()
            text = "Duck Hunt    FPS: {0:.2f}".format(self.animationclock.get_fps())
            pygame.display.set_caption(text)
            pygame.display.flip()

            # When the window is closed, shut pygame down.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.animationclock.tick(FRAMES_PER_SECOND)
        pygame.quit()

# This is the execution of our application. A Controller object is created and executed. 
controller = Controller()
controller.execute()
