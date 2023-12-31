import random

import pygame
import numpy as np

pygame.init()
SCREEN_WIDTH = 528
SCREEN_HEIGHT = 528
box_area = SCREEN_WIDTH/24


run = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
box_arr = np.zeros(784)

color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "gray": (128, 128, 128),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

def set_box_array(box_row, box_col):
    iterable = [int((box_row + 1) * 24 + box_col), int((box_row + 2) * 24 + box_col), int(box_row * 24 + box_col+1), int(box_row * 24 + box_col+2), int(box_row * 24 + box_col-1), int(box_row * 24 + box_col-2), int((box_row - 1) * 24 + box_col), int((box_row - 2) * 24 + box_col)]
    for index, i in enumerate(iterable):
        if box_arr[i] != 255 and index % 2 == 0:
            box_arr[i] = 50 / ((index % 2) + 1)

while run:
    screen.fill(color_dict["black"])

    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()

    if mouse[0]:
        mouse_pos = pygame.mouse.get_pos()
        box_row, box_col = mouse_pos[1]//box_area, mouse_pos[0]//box_area
        box_arr[int(box_row*24 + box_col)] = 255
        set_box_array(box_row, box_col)


    for i in range(len(box_arr)):
        if box_arr[i] != 0:
            box_row, box_col = i // 24, i % 24
            box = pygame.Rect(box_col * box_area, box_row * box_area, 24, 24)
            pygame.draw.rect(screen, (box_arr[i],box_arr[i],box_arr[i]), box)

    for i in range(23):
        pygame.draw.line(screen, color_dict["gray"], ((i+1)*SCREEN_WIDTH/24, 0), ((i+1)*SCREEN_WIDTH/24, SCREEN_HEIGHT))
        pygame.draw.line(screen, color_dict["gray"], (0, (i+1)*SCREEN_HEIGHT/24), (SCREEN_WIDTH, (i+1)*SCREEN_HEIGHT/24))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(box_arr)
            run = False

    pygame.display.update()
