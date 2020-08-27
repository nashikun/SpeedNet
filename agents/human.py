from .agent import Agent
from .config import *


class HumanAgent(Agent):
    def __init__(self, name=None, **kwargs):
        if name:
            self.name = name
        else:
            self.name = "Human player {}".format(id(self))

        super(HumanAgent, self).__init__(**kwargs)

    def choose_move(self, grid):
        # The human player should input where to go
        # i.e: LEFT,RIGHT,UP,DOWN
        direction = input()
        assert direction in MOVES
        return MOVES_INV[direction]
