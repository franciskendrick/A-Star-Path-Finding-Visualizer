from colors import Colors
import pygame


class Spot:
    # Initialization ---------------------------------------------- #
    def __init__(self, row, col, width, total_rows):
        self.row, self.col = row, col
        self.x, self.y = row * width, col * width
        self.width = width
        self.total_rows = total_rows
        self.color = Colors.white
        self.neighbors = []

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pygame.draw.rect(
            display, self.color, 
            (self.x, self.y, self.width, self.width)
        )

    # Update ------------------------------------------------------ #
    def update_neighbors(self, grid):
        self.neighbors = []

        # Bottom neighbor
        if (self.row < self.total_rows - 1) and (  # check if can go down
                not grid[self.row + 1][self.col].is_barrier()):  # neighbor below is not a barrier
            self.neighbors.append(grid[self.row + 1][self.col])

        # Top neighbor
        if (self.row > 0) and (  # check if can go up
                not grid[self.row - 1][self.col].is_barrier()):  # neighbor above is not a barrier
            self.neighbors.append(grid[self.row - 1][self.col])

        # Right neighbor
        if (self.col < self.total_rows - 1) and (  # check if can go right
                not grid[self.row][self.col + 1].is_barrier()):  # right neighbor is not a barrier
            self.neighbors.append(grid[self.row][self.col + 1])

        # Left neighbor
        if (self.col > 0) and (  # check if can go left
                not grid[self.row][self.col - 1].is_barrier()):  # left neighbor is not a barrier
            self.neighbors.append(grid[self.row][self.col - 1])

    # Get position ------------------------------------------------ #
    def get_position(self):
        return (self.row, self.col)

    # Get color values -------------------------------------------- #
    def is_closed(self):
        return self.color == Colors.red

    def is_open(self):
        return self.color == Colors.green

    def is_barrier(self):
        return self.color == Colors.black

    def is_start(self):
        return self.color == Colors.orange

    def is_end(self):
        return self.color == Colors.turquoise

    # Update color ----------------------------------------------- #
    def reset(self):
        self.color = Colors.white

    def make_closed(self):
        self.color = Colors.red

    def make_open(self):
        self.color = Colors.green
        
    def make_barrier(self):
        self.color = Colors.black
    
    def make_start(self):
        self.color = Colors.orange

    def make_end(self):
        self.color = Colors.turquoise

    def make_path(self):
        self.color = Colors.purple
