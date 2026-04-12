import pygame
import time

CELL_SIZE = 30

def run_simulation(env, path, start, goal):
    pygame.init()

    width = env.width * CELL_SIZE
    height = env.height * CELL_SIZE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Autonomous Navigation")

    running = True
    path_index = 0

    while running:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # draw grid
        for y in range(env.height):
            for x in range(env.width):
                rect = pygame.Rect(x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if env.grid[y][x] == 1:
                    pygame.draw.rect(screen, (0,0,0), rect)

                pygame.draw.rect(screen, (200,200,200), rect, 1)

        # draw path
        for node in path:
            pygame.draw.rect(screen, (0,255,0),
                (node[1]*CELL_SIZE, node[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # draw agent
        if path_index < len(path):
            node = path[path_index]
            pygame.draw.rect(screen, (255,0,0),
                (node[1]*CELL_SIZE, node[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            path_index += 1
            time.sleep(0.1)

        pygame.display.flip()

    pygame.quit()