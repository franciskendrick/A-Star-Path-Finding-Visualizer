from spot import Spot
from queue import PriorityQueue
import pygame
import math
import sys


def main_loop():
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

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # Initialize window
    rect = pygame.Rect(0, 0, 640, 360)
    enlarge = 2
    win_size = (
        int(rect.width * enlarge),
        int(rect.height * enlarge))

    win = pygame.display.set_mode(win_size)
    display = pygame.Surface(rect.size)

    # Execute
    main_loop()
