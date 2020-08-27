from .Map import Map

import os

class MapFile(Map):

    def read_file(self, path):
        if not os.path.isfile(path):
            raise Exception(f"File {path} not found")
        with open(path, 'r') as f:
            map = [list(x) for x in f.read().splitlines()]
        h = len(map)
        if not h:
            raise Exception(f"Map file {path} is empty")
        w = len(map[0])
        for row in map:
            if len(row) != w:
                raise Exception("All rows should have the same number of columns")
        if not w:
            raise Exception("Columns are empty")
        
        self.height = h
        self.width = w
        self.map = map
