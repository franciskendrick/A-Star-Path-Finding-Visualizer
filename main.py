from colors import Colors
from spot import Spot
from queue import PriorityQueue
import pygame
import math
import sys


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
    grid = make_grid(rows, rect.height)

    start_node = None
    end_node = None

    run = True
    started = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

        redraw_main(display, grid, rows, rect.height)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()

    # Initialize window
    rect = pygame.Rect(0, 0, 400, 400)
    # enlarge = 2
    enlarge = max(
        (pygame.display.Info().current_h - 80) / rect.width,
        (pygame.display.Info().current_h - 80) / rect.height)
    win_size = (
        int(rect.width * enlarge),
        int(rect.height * enlarge))

    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(rect.size)

    # Execute
    main_loop()
