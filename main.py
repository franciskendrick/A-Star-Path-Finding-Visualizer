from colors import Colors
from spot import Spot
from queue import PriorityQueue
import pygame
import math
import sys


def get_heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def algorithm(redraw, grid, start_node, end_node):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start_node))
    open_set_hash = {start_node}
    came_from = {}

    # G score
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start_node] = 0

    # F score
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start_node] = get_heuristic(
        start_node.get_position(), end_node.get_position())

    # Algorithm
    while not open_set.empty():
        # Event loop
        for event in pygame.event.get():
        # Quit detection
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_node = open_set.get()[2]
        open_set_hash.remove(current_node)

        # Found the shortest path, hence, reconstruct the path for the visualization
        if current_node == end_node:
            return True

        # Determine best path to get to every single node
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + get_heuristic(
                    neighbor.get_position(), end_node.get_position())

                if neighbor not in open_set_hash:  # make the neighbor open
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        # Close the start node
        if current_node != start_node:
            current_node.make_closed()

        # Update display
        redraw()

    # Shortest path has not been found
    return False
        

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

            # Keydown detection
            if event.type == pygame.KEYDOWN:
                # Run algorithm
                if event.key == pygame.K_SPACE and not started:
                    # Update all spots' neighbors
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    # Run algorithm
                    algorithm(
                        lambda: redraw_main(
                            display, grid, rows, rect.width), 
                                grid, start_node, end_node)

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
