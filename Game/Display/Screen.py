from queue import PriorityQueue


class Screen:
    game_objects = PriorityQueue()

    def __init__(self, height, width):
        self.height = height
        self.width = width


    def render(self):
        for game_object in self.game_objects:
            game_object.item.render()

    def get_screen(self):
        # Should return a reference to the screen object (tktinter's for example)
        return None
