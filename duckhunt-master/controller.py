import os, sys
import pygame
import pygame.transform

# Game parameters
FRAMES_PER_SEC = 50
white = (255, 64, 64)

# Initialize pygame before importing modules
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)
image = pygame.image.load('media', 'background.jpg')

class Controller(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 500))
        screen.fill((white))

    def loop(self):
        self.clock.tick(FRAMES_PER_SEC)

    def execute(self):
        while self.running:
            screen.blit(image, (0, 0))
            pygame.display.flip()
            if event.type == pygame.QUIT:
                self.running = False
       

if __name__ == "__main__":
    controller = Controller()
    controller.execute()
