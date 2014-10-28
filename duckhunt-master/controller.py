import os, sys
import pygame
import pygame.transform

# Game parameters
screen = pygame.display.set_mode((800, 500))
image = pygame.image.load('media/background.jpg')

# Initialize pygame before importing modules
pygame.init()
pygame.display.set_caption("Duck Hunt")
pygame.mouse.set_visible(False)

class Controller(object):
    def __init__(self):
        self.running = True

    def execute(self):
        screen.blit(image, (0, 0))
        try:
            while self.running:
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
            pygame.quit()
        except SystemExit:
            pygame.quit()
       
if __name__ == "__main__":
    controller = Controller()
    controller.execute()
