import os, sys, random
import pygame
import pygame.transform
from game.duck import Duck

# Game parameters
surface = pygame.display.set_mode((800, 500))
image = pygame.image.load('media/background.jpg')
position = (200, 100)

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

class Controller(object):
    def __init__(self):
        self.running = True

    def execute(self):
        surface.blit(image, (0, 0))
        gun = Gun()
        pygame.mixer.music.load('media/blast.ogg')
        while self.running:
            pygame.display.flip()
            gun.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.mixer.music.queue('media/blast.ogg')
            pygame.mixer.music.play(0)
        pygame.quit()

class Gun(object):
    def __init__(self):
        self.rounds = 3
        self.mouseImg = pygame.image.load('media/crosshairs.png')

    def render(self):
        surface.blit(self.mouseImg, position)

    def reloadGun(self):
        self.rounds = 3

    def shoot(self):
        if self.rounds <= 0:
            return False

        self.registry.get('soundHandler').enqueue('blast')
        self.rounds = self.rounds - 1
        return True
        
if __name__ == "__main__":
    controller = Controller()
    ducks = [Duck() for i in range(1,3)]
    controller.execute()
    #for i in ducks:
    #    ducks[ducks.index(i)].execute()
