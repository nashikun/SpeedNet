from config.constants import MOVES
from .agent import Agent


class HumanAgent(Agent):
    def choose_move(self, grid):
        # The human player should input where to go
        # i.e: LEFT,RIGHT,UP,DOWN
        direction = input()
        assert direction in MOVES
        return MOVES[direction].value
