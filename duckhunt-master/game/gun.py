"""
This class defines the gun in our game. The location of the crosshair is
received from the FPGA, and this class blits the image to the surface,
which is received by the Controller in the constructor of Gun.
"""

# This file's imports.
import os, sys
import pygame

# The Gun class, responsible for blitting the crosshair.
class Gun(object):

    # The constructor of Gun.
    def __init__(self, surface):
        self.surface = surface
        self.mouseImg = pygame.image.load('media/crosshairs.png')
        self.position = (200, 100)

    # This method renders the image onto the surface. It is called by the main game loop.
    def render(self):
        self.surface.blit(self.mouseImg, (self.position))

    # Fetch the position of the crosshair.
    def getPosition(self):
        return self.position

    # Set a new X and Y value for the crosshair.
    def setPosition(self, (x, y)):
        if y < 297:
            self.position = (x, y)
