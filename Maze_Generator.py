import pygame
import random

from pygame import Vector2
from Settings import *


class Maze:
    def __init__(self):
        self.maze_x = int(WIDTH/CELL_SIZE)
        self.maze_y = int(HEIGHT/CELL_SIZE)
        self.maze_size = Vector2(self.maze_x, self.maze_y)
        self.maze = []

        for row in range(self.maze_y):
            row_to_add = []
            for row_fill in range(self.maze_x):
                row_to_add.append(random.randint(0, 1))
            self.maze.append(row_to_add)
        self.maze_init()

    def maze_init(self):
        print(self.maze)

    def draw(self,  screen):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                rect = pygame.Rect(Vector2(j * CELL_SIZE, i * CELL_SIZE), Vector2(CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, self.cell_color(cell), rect)

    @staticmethod
    def cell_color(cell):
        match cell:
            case  0:
                return pygame.Color("black")
            case 1:
                return pygame.Color("white")
            case 2:
                return pygame.Color("blue")
            case 3:
                return pygame.Color("red")
