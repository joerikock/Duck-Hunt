import os, sys
import pygame
import pygame.transform
import pygame.mouse
from game.registry import Registry
from game.duck import Duck
from game.gun import Gun
from game.hud import HUD

# Game parameters
surface = pygame.display.set_mode((800, 500))
background = pygame.image.load('media/background.jpg')
FRAMES_PER_SECOND = 50
registry = Registry()

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

class Controller(object):
    def __init__(self):
        self.running = True
        registry.set('surface', surface)
        surface.blit(background, (0, 0))
        self.hud = HUD(surface)
        self.ducks = [Duck(registry) for i in range(1,3)]
        self.gun = Gun(registry)
        self.animationclock = pygame.time.Clock()

    def execute(self):        
        while self.running:
            surface.blit(background, (0, 0))
            for i in self.ducks:
                self.ducks[self.ducks.index(i)].execute()
            #print pygame.mouse.get_pos()
            self.gun.render()
            self.hud.render()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.animationclock.tick(FRAMES_PER_SECOND)
        pygame.quit()
        
if __name__ == "__main__":
    controller = Controller()
    controller.execute()
