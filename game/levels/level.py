import pygame as pg

from config.constants import CELL, CELLSIZE, COLORS
from game.display.game_object import Sprite
from ..display.game_object import GameObject

LIGHTGREY = (100, 100, 100)


class Level(GameObject):
    priority = 0

    def __init__(self):
        super().__init__()
        self.level_map = []
        self._height = None
        self._width = None

    @property
    def height(self):
        if self._height is None:
            raise Exception("Height hasn't been set")
        return self._height

    @property
    def width(self):
        if self._width is None:
            raise Exception("Width hasn't been set")
        return self._width

    @height.setter
    def height(self, h):
        if not isinstance(h, int) or h <= 0:
            raise Exception("Height should be a positive integer")
        self._height = h

    @width.setter
    def width(self, w):
        if not isinstance(w, int) or w <= 0:
            raise Exception("Height should be a positive integer")
        self._width = w

    def get_view(self, character):
        xp = character.x
        yp = character.y
        r = character.range
        directions = character.directions

        view = [[CELL.UNKNOWN.value for _ in range(2 * r + 1)] for _ in range(2 * r + 1)]
        for x, y in directions:
            for step in range(1, r + 1):

                # The position of the cell in the real map
                xc = xp + round(step * x / r)
                yc = yp + round(step * y / r)

                # Break if outside the map
                if not (0 <= xc < self.width and 0 <= yc < self.height):
                    break

                # Update the cell
                view[r + yc - yp][r + xc - xp] = self.level_map[yc][xc]

                # If the view is blocked by a wall, stop
                if self.level_map[yc][xc] == CELL.WALL:
                    break

        view[r][r] = CELL.PLAYER.value
        return view

    def __str__(self):
        return "\n".join(["".join(map(str, x)) for x in self.level_map])

    def render(self):
        level_sprites = pg.sprite.Group()
        for x in range(self.width):
            for y in range(self.height):
                if self.level_map[x][y] == CELL.WALL:
                    Sprite(level_sprites, COLORS.BLACK.value, x, y)
        level_sprites.draw(self.screen.screen)
