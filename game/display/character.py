from .game_object import GameObject


class Character(GameObject):
    priority = 2

    def __init__(self, player):
        self.player = player
        super().__init__()
