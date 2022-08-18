from utils import separate_sets_from_yaxis
from utils import clip_set_to_list_on_yaxis
from utils import palette_swap
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


class Buttons:
    # Initialize -------------------------------------------------- #
    def __init__(self, enlarge):
        spriteset = pygame.image.load(
            f"{resources_path}/buttons.png")
        play_spriteset, gridsize_spriteset = separate_sets_from_yaxis(
            spriteset, (255, 0, 0))
        
        # Palette
        hover_palette = {
            (0, 0, 0): (64, 64, 64),
            (255, 255, 255): (128, 128, 128)}

        # Buttons
        self.init_play_btn(play_spriteset, hover_palette, enlarge)
        self.init_gridsize_btns(gridsize_spriteset, hover_palette, enlarge)

        # Gridsize Label
        self.init_gridsize_label()

    def init_play_btn(self, spriteset, hover_palette, enlarge):
        # Initialize image
        img = clip_set_to_list_on_yaxis(spriteset)
        wd, ht = img.get_size()
        resized_img = pygame.transform.scale(
            img, (wd * 2, ht * 2))

        # Initialize hover image
        hover_img = palette_swap(img.convert(), hover_palette)
        wd, ht = hover_img.get_size()
        resized_hoverimg = pygame.transform.scale(
            hover_img, (wd * 2, ht * 2))

        # Initialize rectangle
        rect = pygame.Rect(
            menu_data["buttons_positions"]["play"],
            resized_img.get_rect().size)
        hitbox = pygame.Rect(
            rect.x * enlarge, rect.y * enlarge,
            rect.width * enlarge, rect.height * enlarge)

        # Append button
        self.play = [
            False,  # if mouse if over
            resized_img,  # orignal image
            resized_hoverimg,  # hover image
            rect,  # image's rectangle
            hitbox  # hitbox
        ]

    def init_gridsize_btns(self, spriteset, hover_palette, enlarge):
        # Grid size buttons
        order = ["5x5", "10x10", "20x20", "25x25", "40x40", "50x50"]
        images = clip_set_to_list_on_yaxis(spriteset)

        self.gridsize = {}
        for name, img in zip(order, images):
            # Initialize image
            wd, ht = img.get_size()
            resized_img = pygame.transform.scale(
                img, (wd * 2, ht * 2))
                
            # Initialize hover image
            hover_img = palette_swap(img.convert(), hover_palette)
            wd, ht = hover_img.get_size()
            resized_hoverimg = pygame.transform.scale(
                hover_img, (wd * 2, ht * 2))
        
            # Initialize rectangle
            rect = pygame.Rect(
                menu_data["buttons_positions"][name],
                resized_img.get_rect().size)
            hitbox = pygame.Rect(
                rect.x * enlarge, rect.y * enlarge,
                rect.width * enlarge, rect.height * enlarge)

            # Append to buttons
            button = [
                False,  # if mouse is over
                resized_img,  # orignal image
                resized_hoverimg,  # hover image
                rect,  # image's rectangle
                hitbox  # hitbox
            ]
            self.gridsize[name] = button

    def init_gridsize_label(self):
        # Initialize image
        img = pygame.image.load(
            f"{resources_path}/buttons_label.png")
        wd, ht = img.get_size()
        resized_img = pygame.transform.scale(
            img, (wd * 2, ht * 2))

        # Initialize rectangle
        rect = pygame.Rect(
            menu_data["gridsizelabel_position"],
            resized_img.get_rect().size)

        # Append label
        self.gridsize_label = [resized_img, rect]

    # Draw -------------------------------------------------------- #
    def draw(self, display):
        pass

    # Action detection -------------------------------------------- #
    def button_down_detection(self):
        pass

    def button_over_detection(self):
        pass

    # Functions --------------------------------------------------- #
    def reset_overdetection(self):
        pass
