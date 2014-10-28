import os, sys
import pygame
import pygame.transform
from game.registry import Registry
<<<<<<< HEAD
from game.duck import Duck
=======
from game.gun import Gun
>>>>>>> origin/master

# Game parameters
surface = pygame.display.set_mode((800, 500))
image = pygame.image.load('media/background.jpg')
registry = Registry()

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

class Controller(object):
    def __init__(self):
        self.running = True
        registry.set('surface', surface)

    def execute(self):
        surface.blit(image, (0, 0))
<<<<<<< HEAD
        gun = Gun()
        ducks = [Duck() for i in range(1,3)]
=======
        gun = Gun(registry)
>>>>>>> origin/master
        pygame.mixer.music.load('media/blast.ogg')
        while self.running:
            pygame.display.flip()
            for i in ducks:
                ducks[ducks.index(i)].execute()
            gun.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
        pygame.quit()
        
if __name__ == "__main__":
    controller = Controller()
    controller.execute()
