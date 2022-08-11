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
        pass

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

    # Less than --------------------------------------------------- #
    def __lt__(self):
        pass
