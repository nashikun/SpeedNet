from .agent import Agent
from .config import *


class SpeedAgent(Agent):
    def __init__(self, name=None, **kwargs):
        if name:
            self.name = name
        else:
            self.name = "SpeedNet Player {}".format(id(self))

        super(SpeedAgent, self).__init__(**kwargs)

    def choose_move(self, grid):
        # The human player should input where to go
        # i.e: LEFT,RIGHT,UP,DOWN
        direction = input()
        assert direction in MOVES
        return MOVES.index(direction)
