from _typeshed import TraceFunction
import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_hieght = 300
line_width = 6
markers = []
clicked = False
pos = []

screen = pygame.display.set_mode((screen_width, screen_hieght))
pygame.display.set_caption("TicTacToe")

def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_hieght), line_width)


for x in range(3):
    row = [0] *3
    markers.append(row)

print(markers)


run = True
while run:

    draw_grid()

    #event handlers
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            run = False

        #mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked == False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
    
    pygame.display.update()

pygame.quit()