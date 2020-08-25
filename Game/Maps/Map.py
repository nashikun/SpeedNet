from ..Display.GameObject import GameObject


class Map(GameObject):
    priority = 0

    def __init__(self):
        self.map = []
