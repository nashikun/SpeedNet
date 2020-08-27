from ..Display.GameObject import GameObject

from math import floor, sqrt

class Map(GameObject):
    priority = 0

    def __init__(self, r):
        super().__init__()
        self.map = []
        self.range = r
        self._height = None
        self._width = None
        
        # Contains the tiles at a distance "range" around 0
        self.directions = set()
        for x in range(r+1):
            y = floor(sqrt(r*r - x*x))
            self.directions.update([(x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)])


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
                
    def get_view(self, xp, yp):
        view = [["2" for _ in range(2 * self.range + 1)] for _ in range(2 * self.range + 1)]
        for x, y in self.directions:
            for step in range(self.range + 1):
            
                # The position of the cell in the real map
                xc = xp + round(step * x / self.range)
                yc = yp + round(step * y / self.range)
            
                # Break if outside the map
                if not (0 <= xc < self.width and 0 <= yc < self.height):
                    break
                
                # Update the cell
                view[self.range + yc - yp][self.range + xc - xp] = self.map[yc][xc]
                
                # If the view is blocked by a wall, stop
                if self.map[yc][xc] == "1":
                    break
                    
        view[self.range][self.range] = "3"
        return view
