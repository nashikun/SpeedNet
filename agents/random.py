from .agent import Agent
from config.constants import MOVES

from random import choice


class RandomAgent(Agent):
    def choose_move(self, grid):
        # Pick a random legal move
        return choice(list(MOVES)).value
