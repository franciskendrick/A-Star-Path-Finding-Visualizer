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
        self.image = pygame.image.load(
            f"{resources_path}/title.png")
        self.rect = pygame.Rect(
            menu_data["title_position"], self.image.get_size())

    def draw(self, display):
        # Resize title image
        wd, ht = self.image.get_size()
        resized_image = pygame.transform.scale(
            self.image, (wd * 2, ht * 2))
        
        # Draw
        display.blit(resized_image, self.rect)
