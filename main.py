import pygame
import random

from global_values import *
from maze import *
from disjoint_set import DisjointSet
from graph import *


# Init pygame and its variables
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()
fps = 60  # frames per second


def bfs(maze: list[Cell], s: int, f: int, path: list[tuple]):
    vertices = [i for i in range(ROWS * COLUMNS)]  # vertices representing cells of maze
    start = f
    queue = [start]
    maze[start].visited = True
    bfsPath = {}
    graph = make_graph(vertices, path)
    while queue:
        current = queue.pop(0)
        if current == s:
            break
        for d in [-ROWS, ROWS, -1, 1]:
            if current + d in graph[current]:
                child = current + d
            else:
                continue
            if maze[child].visited:
                continue
            queue.append(child)
            maze[child].visited = True
            maze[child].on_path = True
            draw_screen(maze)
            pygame.time.delay(100)
            bfsPath[child] = current
    for cell in maze:
        cell.on_path = False
    fwdPath = {}
    t = s
    while t != start:
        fwdPath[bfsPath[t]] = t
        t = bfsPath[t]
        maze[t].on_path = True


def draw_screen(maze: list[Cell]):
    SCREEN.fill(BLACK)
    for i in range(ROWS * COLUMNS):
        maze[i].draw_cell()
    pygame.display.update()


def main():

    maze = initiate_maze(SCREEN)
    edges = find_edges()
    path = []

    # find positions in maze of starting point and finishing point
    for i in range(len(maze)):
        if maze[i].starting_point:
            s = i
        elif maze[i].finishing_point:
            f = i
    # make disjoint set
    ds = DisjointSet()
    for i in range(ROWS * COLUMNS):
        ds.find(i)

    #######  GAME LOOP #################################
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ########  Maze creation Algortihm  ##############

        # if disjoint set becomes singleton, start finding path and end program
        if len(list(ds.itersets())) == 1:
            bfs(maze, s, f, path)
            draw_screen(maze)
            pygame.time.delay(5000)  # after 5 seconds game loop breaks
            break

        # Maze Generations algorithm
        e = random.sample(edges, 1)
        edges.remove((e[0][0], e[0][1]))
        u = ds.find(e[0][0])
        v = ds.find(e[0][1])
        if not ds.connected(u, v):
            path.append((e[0][0], e[0][1]))
            ds.union(u, v)
            remove_wall(maze, e[0][0], e[0][1])
        draw_screen(maze)


if __name__ == "__main__":
    main()
pygame.quit()
