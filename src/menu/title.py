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


class Title:
    def __init__(self):
        image = pygame.image.load(
            f"{resources_path}/title.png")
        wd, ht = image.get_size()
        self.image = pygame.transform.scale(
            image, (wd * 2, ht * 2))

        self.rect = pygame.Rect(
            menu_data["title_position"], self.image.get_size())

    def draw(self, display):
        display.blit(self.image, self.rect)
