from config.constants import MOVES, QUIT
from .agent import Agent
import pygame as pg


class HumanAgent(Agent):
    def choose_move(self, grid):
        # The human player should input where to go
        # i.e: LEFT,RIGHT,UP,DOWN
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    return MOVES.LEFT.value
                elif event.key == pg.K_RIGHT:
                    return MOVES.RIGHT.value
                elif event.key == pg.K_UP:
                    return MOVES.UP.value
                elif event.key == pg.K_DOWN:
                    return MOVES.DOWN.value
            elif event.type == pg.QUIT:
                return QUIT
