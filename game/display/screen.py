from queue import PriorityQueue


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Screen(metaclass=Singleton):
    game_objects = PriorityQueue()

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        for game_object in list(self.game_objects.queue):
            game_object.item.render()
