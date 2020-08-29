from .level import Level
from config.constants import CELL

import os


class TextLevel(Level):

    def init_map(self, path):
        if not os.path.isfile(path):
            raise Exception(f"File {path} not found")
        with open(path, 'r') as f:
            level_map = [list(map(int, x)) for x in f.read().splitlines()]
        h = len(level_map)
        if not h:
            raise Exception(f"Map file {path} is empty")
        w = len(level_map[0])
        for row in level_map:
            if len(row) != w:
                raise Exception("All rows should have the same number of columns")
        if not w:
            raise Exception("Columns are empty")

        self.height = h
        self.width = w
        self.level_map = [[CELL.WALL.value if x else CELL.EMPTY.value for x in row] for row in level_map]
