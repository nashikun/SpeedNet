from queue import PriorityQueue

import pygame as pg

from config.constants import CELLSIZE, COLORS


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Screen(metaclass=Singleton):
    game_objects = PriorityQueue()
    instance = None

    def __init__(self, height, width, fps):
        pg.init()
        self.height = height
        self.width = width
        self.fps = fps
        self.instance = self
        self.screen = pg.display.set_mode((width * CELLSIZE, height * CELLSIZE))

    def render(self):
        self.screen.fill(COLORS.WHITE.value)
        for game_object in list(self.game_objects.queue):
            game_object.item.render()
        pg.display.flip()
        pg.display.update()

    def quit(self):
        pg.quit()
        self.game_objects = PriorityQueue()
