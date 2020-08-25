from .Map import Map

import os

class MapFile(Map):

    def read_file(self, path):
        if not os.path.file(path):
            raise Exception(f"File {path} not found")
        with open(path, 'r') as f:
            self.map = f.readlines()
