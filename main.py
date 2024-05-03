import pygame
import sys

from pygame import Vector2
from Settings import *
from Maze_Generator import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Maze Solver")
        self.clock = pygame.Clock()
        self.events = pygame.event.get()

        self.maze = Maze()

    def check_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.clock.tick(FPS)
        self.draw()
        pygame.display.update()

        pygame.display.set_caption("Maze Solver - " + str(int(self.clock.get_fps())))

    def draw(self):
        self.maze.draw(self.screen)

    def run(self):
        while True:
            self.check_events()
            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
