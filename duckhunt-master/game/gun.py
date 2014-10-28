import os, sys
import pygame

position = (50, 50)

class Gun(object):
    def __init__(self):
        self.rounds = 3
        #self.mousePos = (0,0) # Starting postion
        self.mouseImg = pygame.image.load(os.path.join('media', 'crosshairs.png'))

    def render(self):
        surface = self.registry.get('surface')
        surface.blit(self.mouseImg, position)

    def reloadIt(self):
        self.rounds = 3

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
