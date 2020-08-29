import importlib
from queue import Queue

from game.display.screen import Screen
import time


class Game:
    def __init__(self, level_type="CellularAutomataLevel", level_args={"h": 10, "w": 10}, screen_height=100,
                 screen_width=100, ticks=None, render=True):
        self.level = getattr(importlib.import_module("game.levels"), level_type)()
        self.level.init_map(**level_args)
        self.screen = Screen(screen_height, screen_width)
        self.ticks = ticks
        self.render = render
        self.objects = Queue()

    def run(self):
        while True:
            if self.ticks:
                t = time.time()
                if time.time() - t < 1 / self.ticks:
                    continue
            for obj in self.objects:
                obj.run()
            if self.ticks and self.render:
                self.screen.render()
