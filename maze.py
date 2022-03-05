from global_values import *
from cell import Cell
import sys


def initiate_maze(SCREEN):
    maze = []
    for x in range(COLUMNS):
        for y in range(ROWS):
            cell = Cell(y, x, SCREEN)
            maze.append(cell)
    if sys.argv[3] == "U":
        maze[int(sys.argv[4])].walls[0] = False
        maze[int(sys.argv[4])].starting_point = True
    if sys.argv[3] == "D":
        maze[-int(sys.argv[4]) - 1].walls[1] = False
        maze[-int(sys.argv[4]) - 1].starting_point = True
    if sys.argv[3] == "L":
        maze[int(sys.argv[4]) * ROWS].walls[3] = False
        maze[int(sys.argv[4]) * ROWS].starting_point = True
    if sys.argv[3] == "R":
        maze[int(sys.argv[4]) * ROWS + (COLUMNS) - 1].walls[2] = False
        maze[int(sys.argv[4]) * ROWS + (COLUMNS) - 1].starting_point = True

    if sys.argv[5] == "U":
        maze[int(sys.argv[6])].walls[0] = False
        maze[int(sys.argv[6])].finishing_point = True
    if sys.argv[5] == "D":
        maze[-int(sys.argv[6]) - 1].walls[1] = False
        maze[-int(sys.argv[6]) - 1].finishing_point = True
    if sys.argv[5] == "L":
        maze[int(sys.argv[6]) * ROWS].walls[3] = False
        maze[int(sys.argv[6]) * ROWS].finishing_point = True
    if sys.argv[5] == "R":
        maze[(int(sys.argv[6]) + 1) * ROWS - 1].walls[2] = False
        maze[(int(sys.argv[6]) + 1) * ROWS - 1].finishing_point = True
    return maze


def in_bounds(x, y):
    return 0 <= x < COLUMNS and 0 <= y < ROWS


def find_neighbours(x, y):
    neighbors = []
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for d in range(4):
        # add cell to neighbor list if it is in bounds and not generated
        if in_bounds(x + dx[d], y + dy[d]):
            neighbors.append((x * ROWS + y, (x + dx[d]) * ROWS + (y + dy[d])))
    return neighbors


def find_edges():
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    edges = set()
    for x in range(COLUMNS):
        for y in range(ROWS):
            for d in range(4):
                if in_bounds(x + dx[d], y + dy[d]):
                    x1 = x * ROWS + y
                    x2 = (x + dx[d]) * ROWS + (y + dy[d])
                if x1 < x2:
                    x1, x2 = x2, x1
                    edges.add((x1, x2))
    return edges


def remove_wall(maze: list[Cell], c1: int, c2: int):
    # horizontal edge
    if c1 - c2 == 1:
        maze[c1].walls[3] = False
        maze[c2].walls[2] = False
    # vertical edge
    if c1 - c2 >= 3:
        maze[c1].walls[0] = False
        maze[c2].walls[1] = False
    maze[c1].generated = True
    maze[c2].generated = True
