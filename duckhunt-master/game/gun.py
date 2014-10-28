import os, sys
import pygame
from .. import main

position = (50, 50)

class Gun(object):
    def __init__(self):
        self.rounds = 3
        self.mouseImg = pygame.image.load('media/crosshairs.png')
        print "kaas"

    def render(self):
        surface = pygame.Surface((100, 100), pygame.SRCALPHA)
        screen.blit(self.mouseImg, position)
        print "yolo"

    def reloadGun(self):
        self.rounds = 3

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
