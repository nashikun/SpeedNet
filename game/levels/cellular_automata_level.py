from collections import Counter
from queue import Queue
from random import random

import numpy as np
from scipy.signal import convolve2d

from config.constants import CELL
from .level import Level


class CellularAutomataLevel(Level):

    def _flood_fill(self, level_map, xs, ys, color):
        q = Queue()
        if not (0 <= xs < self.width and 0 <= ys < self.height):
            return
        q.put((xs, ys))
        level_map[xs][ys] = color
        while not q.empty():
            x, y = q.get()
            for a, b in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if (0 <= a < self.width and 0 <= b < self.height) and level_map[a][b] == 0:
                    level_map[a][b] = color
                    q.put((a, b))

    def init_map(self, level_height, level_width, **kwargs):
        self.height = level_height
        self.width = level_width
        level_map = np.array([[int(random() < 0.35) for _ in range(self.height)] for _ in range(self.width)])

        for _ in range(4):
            r1 = convolve2d(level_map, np.ones((3, 3)), "same", fillvalue=1)
            r2 = convolve2d(level_map, np.ones((5, 5)), "same", fillvalue=1)
            level_map = r1 >= 5
            level_map |= r2 <= 3

        for _ in range(4):
            r1 = convolve2d(level_map, np.ones((3, 3)), "same", fillvalue=1)
            level_map = r1 >= 5

        level_map = level_map.astype(int)
        color = 2
        while not np.all(level_map):
            x, y = np.argwhere(level_map == 0)[0]
            self._flood_fill(level_map, x, y, color)
            color += 1

        color_counts = Counter(level_map.flatten())
        max_count = max(color_counts.items(), key=lambda x: x[1] if x[0] != 1 else -1)[0]
        level_map = level_map != max_count
        self.level_map = np.array([[CELL.WALL.value if x else CELL.EMPTY.value for x in row] for row in level_map])
