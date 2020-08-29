import importlib
from queue import Queue

from game.display.screen import Screen
import time

from game.player.player import Player


class Game:
    def __init__(self, level_type="CellularAutomataLevel", ticks=None, render=True, max_turns=None):
        self.level = getattr(importlib.import_module("game.levels"), level_type)()
        self.objects = Queue()
        self.ticks = ticks
        self.render = render
        self.max_turns = max_turns
        self.turn = 0
        self.screen = None

    def init_screen(self, screen_height, screen_width):
        self.screen = Screen(screen_height, screen_width)

    def init_level(self, level_height=100, level_width=100, level_path=None):
        self.level.init_map(level_height=level_height, level_width=level_width, level_path=level_path)

    def init_player(self):
        self.objects.put(Player())

    def run(self):
        t = time.time()
        while not self.is_over():
            if self.ticks:
                if time.time() - t < 1 / self.ticks:
                    continue
            t = time.time()
            for obj in list(self.objects.queue):
                obj.run()
            if self.ticks and self.render:
                self.screen.render()
            self.turn += 1

    def is_over(self):
        return self.max_turns is not None and self.turn >= self.max_turns
