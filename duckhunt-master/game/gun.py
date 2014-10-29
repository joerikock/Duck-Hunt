import os, sys
import pygame

POSITION = (200, 100)

class Gun(object):
    def __init__(self, surface):
        self.surface = surface
        self.rounds = 3
        self.mouseImg = pygame.image.load('media/crosshairs.png')
        
    def render(self):
        self.surface.blit(self.mouseImg, (POSITION))

    def reloadGun(self):
        self.rounds = 3

    def getPosition(self):
        return POSITION

    def setPosition(self, x, y):
        POSITION = (x, y)

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
