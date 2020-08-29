import importlib
import time
from queue import Queue
from random import choice

import pygame as pg
import numpy as np

from config.constants import CELL
from game.display.screen import Screen
from game.player.player import Player


class Game:
    def __init__(self, ticks=None, render=True, max_turns=None):
        self.level = None
        self.objects = Queue()
        self.ticks = ticks
        self.render = render
        self.max_turns = max_turns
        self.turn = 0
        self.screen = None
        self.exit = False

    def init_screen(self, screen_height, screen_width, fps):
        self.screen = Screen(screen_height, screen_width, fps)

    def init_level(self, level_type="CellularAutomataLevel", level_height=100, level_width=100, level_path=None):
        self.level = getattr(importlib.import_module("game.levels"), level_type)()
        self.level.init_map(level_height=level_height, level_width=level_width, level_path=level_path)

    def init_player(self):
        x, y = choice(np.argwhere(self.level.level_map == CELL.EMPTY.value))
        self.objects.put(Player(self.screen, x, y))

    def run(self):
        last_action = time.time()
        last_render = time.time()
        while not self.is_over():
            if self.ticks:
                if time.time() - last_action > 1 / self.ticks:
                    last_action = time.time()
                    for obj in list(self.objects.queue):
                        obj.run()
            if self.render:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        self.quit()
                        break
                if time.time() - last_render > 1 / self.screen.fps:
                    self.screen.render()
            self.turn += 1
        self.quit()

    def is_over(self):
        return self.exit or (self.max_turns is not None and self.turn >= self.max_turns)

    def quit(self):
        self.screen.quit()
        self.exit = True
