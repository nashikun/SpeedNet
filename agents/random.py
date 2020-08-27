from .agent import Agent
import random

class RandomAgent(Agent):
    def __init__(self, name=None, **kwargs):
        if name:
            self.name = name
        else:
            self.name = "Random player {}".format(id(self))
        super(RandomAgent, self).__init__(**kwargs)

    def choose_move(self, grid):
        # Pick a random legal move
        return random.randint(0,3)
