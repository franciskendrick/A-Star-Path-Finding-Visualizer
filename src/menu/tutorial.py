from utils import clip_set_to_list_on_yaxis
import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources"
        )
    )

# Json
with open(f"{resources_path}/menu.json") as json_file:
    menu_data = json.load(json_file)


class Tutorial:
    def __init__(self):
        spriteset = pygame.image.load(
            f"{resources_path}/tutorial.png")
        self.tutorials = [
            [img, pos] for img, pos in zip(
                clip_set_to_list_on_yaxis(spriteset),
                menu_data["tutorial_positions"].values())
        ]

    def draw(self, display):
        for image, rect in self.tutorials:
            display.blit(image, rect)
