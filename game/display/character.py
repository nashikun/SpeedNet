from config.constants import COLORS, CELLSIZE
from game.display.game_object import GameObject
from .game_object import Sprite

import pygame as pg


class Character(Sprite, GameObject):
    priority = 2

    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.group = pg.sprite.Group()
        GameObject.__init__(self)
        Sprite.__init__(self, self.group, COLORS.RED.value, player.x, player.y)

    def render(self):
        self.rect.x = self.player.x * CELLSIZE
        self.rect.y = self.player.y * CELLSIZE
        self.group.draw(self.screen.screen)
