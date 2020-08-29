from math import floor, sqrt

from game.display.character import Character


class Player:
    def __init__(self, screen, vision_range, x, y):
        self.x = x
        self.y = y
        self.range = None
        self.agent = None
        self.directions = set()
        self.display = Character(self, screen)
        self.update_range(vision_range)

    def update_range(self, r):
        # Contains the tiles at a distance "range" around 0
        self.range = r
        self.directions = set()
        for x in range(r + 1):
            y = floor(sqrt(r * r - x * x))
            self.directions.update([(x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)])

    def run(self):
        pass
