from math import floor, sqrt

from config.constants import MOVES, QUIT, CELL
from game.display.character import Character


class Player:
    def __init__(self, game, vision_range, x, y):
        self.x = x
        self.y = y
        self.range = None
        self.agent = None
        self.directions = set()
        self.game = game
        self.level = game.level
        self.display = Character(self, game.screen)
        self.update_range(vision_range)

    def update_range(self, r):
        # Contains the tiles at a distance "range" around 0
        self.range = r
        self.directions = set()
        for x in range(r + 1):
            y = floor(sqrt(r * r - x * x))
            self.directions.update([(x, y), (x, -y), (-x, y), (-x, -y), (y, x), (y, -x), (-y, x), (-y, -x)])

    def run(self):
        view = self.level.get_view(self)
        move = self.agent.choose_move(view)
        self.act(move)

    def act(self, move):
        x, y = self.x, self.y
        if move == MOVES.UP:
            y -= 1
        elif move == MOVES.DOWN:
            y += 1
        elif move == MOVES.RIGHT:
            x += 1
        elif move == MOVES.LEFT:
            x -= 1
        elif move == QUIT:
            self.game.quit()
        if not (0 <= x < self.level.width and 0 <= y < self.level.height) or self.level.level_map[x][y] == CELL.WALL:
            return
        self.x, self.y = x, y
