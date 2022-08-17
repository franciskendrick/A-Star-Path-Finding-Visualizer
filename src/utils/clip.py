import pygame


def clip(set, pos, size):
    clip_rect = pygame.Rect(pos, size)
    set.set_cilp(clip_rect)
    img = set.subsurface(set.get_clip())

    return img
