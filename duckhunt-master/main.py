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
from gpioHandler import GpioHandler

# Game parameters
surface = pygame.display.set_mode((800, 500))
background = pygame.image.load('media/background.jpg')
background_top = pygame.image.load('media/background_top.jpg')
background_bottom = pygame.image.load('media/background_bottom.jpg')
FRAMES_PER_SECOND = 1000

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
        self.gpio = GpioHandler()
        self.gunx = [0 for i in range(0,10)]
        self.guny = [0 for i in range(0,10)]
        self.duck1x = [0 for i in range(0,10)]
        self.duck1y = [0 for i in range(0,10)]
        self.duck2x = [0 for i in range(0,10)]
        self.duck2y = [0 for i in range(0,10)]

    # This method contains the main game loop.
    def execute(self):        
        while self.running:
            surface.blit(background_top, (0, 0))

            self.duck1x = self.gpio.getWord(1)
            self.duck1y = self.gpio.getWord(2)
            self.duck2x = self.gpio.getWord(3)
            self.duck2y = self.gpio.getWord(4)
            # This renders the ducks and makes them flap their wings.
            self.ducks[0].setPosition((int(''.join([str(bit) for bit in self.duck1x]), 2), int(''.join([str(bit) for bit in self.duck1y]), 2)))
            self.ducks[1].setPosition((int(''.join([str(bit) for bit in self.duck2x]), 2), int(''.join([str(bit) for bit in self.duck2y]), 2)))
            for i in self.ducks:
                if self.gpio.getWord(5)[self.ducks.index(i)+7] == 0:
                    self.ducks[self.ducks.index(i)].render()
                    
                    time1 = time.time()*1000
                    if (time1-self.time0)%200 < 30:
                        self.ducks[self.ducks.index(i)].update()
                    

            # Render the gun and the HUD.
            self.gunx = self.gpio.getWord(6)
            self.guny = self.gpio.getWord(7)
            self.gun.setPosition((int(''.join([str(bit) for bit in self.gunx]), 2), int(''.join([str(bit) for bit in self.guny]), 2)))
            self.gun.render()

            self.hud.setBullets(self.gpio.getWord(5))
            self.hud.setHitArray(self.gpio.getWord(8))
            self.hud.setScore(self.gpio.getWord(9))
            self.hud.update()
            self.gpio.updateData()
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
