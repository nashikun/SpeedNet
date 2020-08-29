from dataclasses import dataclass, field
from typing import Any

import pygame as pg

from config.constants import CELLSIZE
from .screen import Screen


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class GameObject:
    priority = 100

    def __init__(self):
        self.prioritized_item = PrioritizedItem(self.priority, self)
        Screen.game_objects.put(self.prioritized_item)
        self.screen = Screen()

    def render(self):
        pass


class Sprite(pg.sprite.Sprite):
    def __init__(self, group, color, x=None, y=None):
        super().__init__(group)
        self.image = pg.Surface((CELLSIZE, CELLSIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x * CELLSIZE
        self.rect.y = self.y * CELLSIZE

    def render(self):
        self.rect.x = self.x * CELLSIZE
        self.rect.y = self.y * CELLSIZE
