import os
import pygame

ducklist = ['media/images/duck1.png','media/images/duck2.png','media/images/duck3.png']
screen = pygame.display.set_mode((800, 500))
while(true)
    for im in ducklist
        image = pygame.image.load('im')
        screen.fill((255,255,255))
        screen.blit(image, (20,20))
        pygame.display.flip()
