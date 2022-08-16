from game.utils import *
from game.colors import Colors
import pygame
import sys


# Redraw 
def redraw_menu():
    # Draw background color
    display.fill(Colors.white)

    # Blit display to window
    resized_display = pygame.transform.scale(
        display, (
            int(rect.width * enlarge), 
            int(rect.height * enlarge))
        )
    win.blit(resized_display, (0, 0))

    # Update display
    pygame.display.update()


def redraw_game(display, grid, rows, width):
    # Draw background color
    display.fill(Colors.white)

    # Draw spots
    for row in grid:
        for spot in row:
            spot.draw(display)

    # Draw gird
    gap = width // rows
    for row in range(rows):  # draw rows
        pygame.draw.line(
            display, Colors.grey,
            (0, row * gap), (width, row * gap)
        )

        for col in range(rows):  # draw columns
            pygame.draw.line(
                display, Colors.grey,
                (col * gap, 0), (col * gap, width)
            )

    # Blit display to window
    resized_display = pygame.transform.scale(
        display, (
            int(rect.width * enlarge), 
            int(rect.height * enlarge))
        )
    win.blit(resized_display, (0, 0))

    # Update display
    pygame.display.update()


# Loop
def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False
            
        # Update display
        redraw_menu()

    pygame.quit()
    sys.exit()


def game_loop():
    rows = 25
    grid = make_grid(rows, rect.width)
    algorithm_runned = False
    start_node = None
    end_node = None

    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Mouse down detection
            if not algorithm_runned:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:  # left click (make nodes)
                    # Get spot
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(
                        mouse_pos, rows, rect.width, enlarge)
                    spot = grid[row][col]

                    # Make nodes
                    if not start_node and spot != end_node:  # make start node
                        start_node = spot
                        start_node.make_start()
                    elif not end_node and spot != start_node:  # make end node
                        end_node = spot
                        end_node.make_end()
                    elif spot != start_node and spot != end_node:  # make barrier
                        spot.make_barrier()

                elif pressed[2]:  # right click (delete nodes)
                    # Get spot
                    mouse_pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(
                        mouse_pos, rows, rect.width, enlarge)
                    spot = grid[row][col]

                    # Delete nodes
                    spot.reset()
                    if spot == start_node:
                        start_node = None
                    elif spot == end_node:
                        end_node = None

            # Keydown detection
            if event.type == pygame.KEYDOWN:
                # Run algorithm
                if (event.key == pygame.K_SPACE) and (  # space bar is down
                        start_node and end_node) and (  # start node and end node has been placed
                        not algorithm_runned):  # the algorithm has not been runned
                    # Update all spots' neighbors
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    # Run algorithm
                    algorithm(
                        lambda: redraw_game(
                            display, grid, rows, rect.width), 
                                grid, start_node, end_node)

                    # Update algorithm runned
                    algorithm_runned = True

                # Clear the grid
                if event.key == pygame.K_c:
                    grid = make_grid(rows, rect.width)
                    algorithm_runned = False
                    start_node = None
                    end_node = None

        # Update display
        redraw_game(display, grid, rows, rect.width)

    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()

    # Initialize window
    rect = pygame.Rect(0, 0, 400, 400)
    enlarge = (pygame.display.Info().current_h - 80) / rect.height
    win_size = (
        int(rect.width * enlarge),
        int(rect.height * enlarge))

    pygame.display.set_caption("A* Path Finding Visualizer")
    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(rect.size)

    # Execute
    game_loop()
