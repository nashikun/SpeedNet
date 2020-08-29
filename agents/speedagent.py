from .agent import Agent
from config.constants import MOVES


class SpeedAgent(Agent):
    def choose_move(self, grid):
        # The human player should input where to go
        # i.e: LEFT,RIGHT,UP,DOWN
        direction = input()
        assert direction in MOVES
        return MOVES[direction].value
