from .level import Level

from collections import Counter
from queue import Queue
from random import random
import numpy as np
from scipy.signal import convolve2d


class CellularAutomataLevel(Level):

    def _flood_fill(self, xs, ys, color):
        q = Queue()
        if not (0 <= xs < self.width and 0 <= ys < self.height):
            return
        q.put((xs, ys))
        self.level_map[xs][ys] = color
        while not q.empty():
            x, y = q.get()
            for a, b in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if (0 <= a < self.width and 0 <= b < self.height) and self.level_map[a][b] == 0:
                    self.level_map[a][b] = color
                    q.put((a, b))

    def init_map(self, h, w):
        self.height = h
        self.width = w
        self.level_map = np.array([[int(random() < 0.35) for _ in range(h)] for _ in range(w)])

        for _ in range(4):
            r1 = convolve2d(self.level_map, np.ones((3, 3)), "same", fillvalue=1)
            r2 = convolve2d(self.level_map, np.ones((5, 5)), "same", fillvalue=1)
            self.level_map = r1 >= 5
            self.level_map |= r2 <= 3

        for _ in range(4):
            r1 = convolve2d(self.level_map, np.ones((3, 3)), "same", fillvalue=1)
            self.level_map = r1 >= 5

        self.level_map = self.level_map.astype(int)
        color = 2
        while not np.all(self.level_map):
            x, y = np.argwhere(self.level_map == 0)[0]
            self._flood_fill(x, y, color)
            color += 1

        color_counts = Counter(self.level_map.flatten())
        max_count = max(color_counts.items(), key=lambda x: x[1] if x[0] != 1 else -1)[0]
        self.level_map = self.level_map != max_count
