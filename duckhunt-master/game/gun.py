import os, sys
import pygame

class Gun(object):
    def __init__(self, registry):
        self.position = (0,0)
        self.registry = registry
        self.rounds = 3
        self.mouseImg = pygame.image.load('media/crosshairs.png')
        
    def render(self):
        self.surface = self.registry.get('surface')
        self.surface.blit(self.mouseImg, (self.position))

    def reloadGun(self):
        self.rounds = 3

    def getPosition(self):
        return self.position

    def setPosition(self, x, y):
        self.position = (x, y)

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
