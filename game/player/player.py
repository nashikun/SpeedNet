from math import floor, sqrt


class Player:
    def __init__(self):
        self.x = None
        self.y = None
        self.range = None
        self.directions = set()

        self.update_range(2)

    def update_range(self, r):
        # Contains the tiles at a distance "range" around 0
        self.range = r
        self.directions = set()
        for x in range(r + 1):
            y = floor(sqrt(r * r - x * x))
            self.directions.update([(x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)])
