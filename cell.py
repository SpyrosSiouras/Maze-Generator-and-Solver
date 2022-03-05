from global_values import *
import pygame

class Cell(object):
    def __init__(self, x, y, SCREEN):
        # position in matrix 
        self.x = x
        self.y = y
        self.SCREEN = SCREEN
        # keeps track of which walls are still visible
        self.walls = [True, True, True, True]


        # checks if cell has been visited during generation 
        self.generated = False
        # checks if cell is on path during solving 
        self.on_path = False
        # checks if cell has been visited during solving 
        self.visited = False

        self.starting_point = False
        self.finishing_point = False

    def draw_cell(self):
        # coordinates on self.SCREEN
        x = self.x * CELL_SIZE + 10
        y = self.y * CELL_SIZE + 10  
        # draws a wall if it still exists
        if self.walls[0]:
            pygame.draw.line(self.SCREEN, WHITE, (x, y), (x + CELL_SIZE, y), 5)
        if self.walls[1]:
            pygame.draw.line(self.SCREEN, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 5)
        if self.walls[2]:
            pygame.draw.line(self.SCREEN, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 5)
        if self.walls[3]:
            pygame.draw.line(self.SCREEN, WHITE, (x, y), (x, y + CELL_SIZE), 5)
        # marks blue if generated during generation
        if self.generated:
            pygame.draw.rect(self.SCREEN, BLUE, (x, y, CELL_SIZE, CELL_SIZE))
        # marks green if on path during solving
        if self.on_path:
            pygame.draw.rect(self.SCREEN, GREEN, (x + 5, y + 5 , CELL_SIZE* 0.75, CELL_SIZE* 0.75))
        if self.starting_point:
            pygame.draw.rect(self.SCREEN, LIGHT_BLUE, (x + 5, y + 5, CELL_SIZE*0.75 , CELL_SIZE*0.75))
        if self.finishing_point:
            pygame.draw.rect(self.SCREEN, PURPLE, (x + 5, y + 5 , CELL_SIZE* 0.75, CELL_SIZE* 0.75))
 
