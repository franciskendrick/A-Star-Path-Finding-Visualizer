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
            # Toggle status
            toggle_status = True if name == "25x25" else False

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
                toggle_status,  # toggle status
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
        # Draw play button
        mouse_is_over, orig_img, hover_img, rect, _ = self.play
        img = hover_img if mouse_is_over else orig_img

        display.blit(img, rect)

        # Draw gridsize label
        display.blit(*self.gridsize_label)

        # Draw gridsize buttons
        for button in self.gridsize.values():
            mouse_is_over, toggle_status, orig_img, hover_img, rect, _ = button
            # img = hover_img if mouse_is_over or toggle_status else orig_img
            if mouse_is_over or toggle_status:
                img = hover_img
            else:
                img = orig_img
            
            display.blit(img, rect)

    # Action detection -------------------------------------------- #
    def button_down_detection(self):
        # Gridsize buttons
        for button in self.gridsize.values():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                for new_button in self.gridsize.values():
                    new_button[1] = False
                button[1] = True  # toggle status

                break

        # Play button
        *_, hitbox = self.play
        
        mouse_pos = pygame.mouse.get_pos()
        if hitbox.collidepoint(mouse_pos):
            return "play"

    def button_over_detection(self):
        # Gridsize buttons
        for button in self.gridsize.values():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

        # Play button
        *_, hitbox = self.play

        mouse_pos = pygame.mouse.get_pos()
        self.play[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions --------------------------------------------------- #
    def get_rows(self):
        for (name, button) in self.gridsize.items():
            if button[1]:  # toggle status
                return int(name.split("x")[0])
