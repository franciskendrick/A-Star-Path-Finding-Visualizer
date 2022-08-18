from .title import Title
from .buttons import Buttons
from .tutorial import Tutorial
import pygame

pygame.init()


class Menu:
    display_size_divider = 2

    def __init__(self, window_size, enlarge):
        wd, ht = window_size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA
        )

        self.title = Title()
        self.buttons = Buttons(self.display_size_divider * enlarge)
        self.tutorial = Tutorial()

    def draw(self, display):
        # Fill menu's display with a transparent background
        self.display.fill((0, 0, 0, 0))

        # Draw menu window on menu's display
        self.title.draw(self.display)
        self.buttons.draw(self.display)
        self.tutorial.draw(self.display)

        # Blit menu's display to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
