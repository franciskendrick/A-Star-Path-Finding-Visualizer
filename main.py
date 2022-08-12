from colors import Colors
from spot import Spot
from queue import PriorityQueue
import pygame
import math
import sys


def get_clicked_pos(pos, rows, width, enlarge):
    gap = (width // rows) * enlarge
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for row in range(rows):
        grid.append([])
        for col in range(rows):
            spot = Spot(row, col, gap, rows)
            grid[row].append(spot)

    return grid


# Loop ------------------------------------------------------------ #
def redraw_main(display, grid, rows, width):
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


def main_loop():
    rows = 25
    grid = make_grid(rows, rect.width)

    start_node = None
    end_node = None

    run = True
    started = False
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Path finding has started
            if started:
                continue

            # Mouse down detection
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

        # Update display
        redraw_main(display, grid, rows, rect.width)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize window
    rect = pygame.Rect(0, 0, 400, 400)
    enlarge = int(pygame.display.Info().current_h / rect.height)
    win_size = (
        int(rect.width * enlarge),
        int(rect.height * enlarge))

    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(rect.size)

    # Execute
    main_loop()
