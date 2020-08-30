from random import choice

from config.constants import MOVES
from .agent import Agent


class RandomAgent(Agent):
    def choose_move(self, grid):
        # Pick a random legal move
        return choice(list(MOVES)).value
