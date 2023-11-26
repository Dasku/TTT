from _typeshed import TraceFunction
import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_hieght = 300

screen = pygame.display.set_mode((screen_width, screen_hieght))
pygame.display.set_caption("TicTacToe")

run = True
while run:

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()