class Agent:
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = f"{self.__class__.__name__} Player {id(self)}"

    def set_name(self, name):
        self.name = name

    def choose_move(self, grid):
        # Choose where to move based on the grid
        return None

    def __str__(self):
        return self.name
