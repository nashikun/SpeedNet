from .game_object import Sprite

import pygame as pg


class Character(Sprite):
    priority = 2

    def __init__(self, player, color):
        self.player = player
        self.group = pg.sprite.Group()
        super().__init__(color, self.group)
