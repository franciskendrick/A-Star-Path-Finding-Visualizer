from spot import Spot
from queue import PriorityQueue
import pygame
import sys


def get_heuristic(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current_node, redraw):
    while current_node in came_from:
        # Make path
        current_node = came_from[current_node]
        current_node.make_path()

        # Update display
        redraw()


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
            reconstruct_path(came_from, end_node, redraw)
            start_node.make_start()
            end_node.make_end()
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

    return int(row), int(col)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for row in range(rows):
        grid.append([])
        for col in range(rows):
            spot = Spot(row, col, gap, rows)
            grid[row].append(spot)

    return grid
