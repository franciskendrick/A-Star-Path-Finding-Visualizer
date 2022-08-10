from queue import PriorityQueue
import pygame
import math


class Spot:
    # Initialization ---------------------------------------------- #
    def __init__(self, row, col, width, total_rows):
        self.row, self.col = row, col
        self.x, self.y = row * width, col * width
        self.width = width
        self.total_rows = total_rows
        self.color = colors["white"]
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
        return self.color == colors["red"]

    def is_open(self):
        return self.color == colors["green"]

    def is_barrier(self):
        return self.color == colors["black"]

    def is_start(self):
        return self.colors == colors["orange"]

    def is_end(self):
        return self.colors == colors["turquoise"]

    # Update colors ----------------------------------------------- #
    def reset(self):
        self.color = colors["white"]

    def make_closed(self):
        self.color = colors["red"]

    def make_open(self):
        self.color = colors["green"]
        
    def make_barrier(self):
        self.color = colors["black"]
    
    def make_start(self):
        self.color = colors["orange"]

    def make_end(self):
        self.color = colors["turquoise"]

    def make_path(self):
        self.color = colors["purple"]

    # Less than --------------------------------------------------- #
    def __lt__(self):
        pass


if __name__ == "__main__":
    rect = pygame.Rect(0, 0, 640, 360)
    enlarge = 2
    win_size = (
        int(rect.width * enlarge),
        int(rect.height * enlarge))

    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(rect.size)

    colors = {
        "red": (255, 0, 0),  # closed
        "green": (0, 255, 0),  # open
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255),
        "black": (0, 0, 0),  # a barrier
        "purple": (128, 0, 128),  # path
        "orange": (255, 165, 0),  # start node
        "grey": (128, 128, 128),
        "turquoise": (64, 224, 208)  # end node
    }
