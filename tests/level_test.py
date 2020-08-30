from config.constants import CELL
from game.display.screen import Screen
from game.game import Game
from game.levels.text_level import TextLevel
from game.player.player import Player

from unittest import TestCase
import os


class TestLevel(TestCase):

    def test_get_view_1(self):
        g = Game()
        _ = Screen(1, 1, 60)
        m = TextLevel()
        m.init_map(os.path.join(os.getcwd(), "game", "assets", "text_levels", "0"))
        p = Player(g, 1, 1, 1)
        self.assertEqual(m.height, 7)
        self.assertEqual(m.width, 11)
        view = m.get_view(p)
        self.assertEqual(len(view), 3)
        self.assertEqual(view,
                         [[CELL.UNKNOWN.value, CELL.WALL.value, CELL.UNKNOWN.value],
                          [CELL.WALL.value, CELL.PLAYER.value, CELL.EMPTY.value],
                          [CELL.UNKNOWN.value, CELL.EMPTY.value, CELL.UNKNOWN.value]])

    def test_get_view_2(self):
        m = TextLevel()
        m.init_map(os.path.join(os.getcwd(), "game", "assets", "text_levels", "1"))
        g = Game()
        p = Player(g, 2, 3, 4)
        self.assertEqual(m.height, 6)
        self.assertEqual(m.width, 11)
        view = m.get_view(p)
        self.assertEqual(len(view), 5)
        self.assertEqual(view, [
            [CELL.UNKNOWN.value, CELL.UNKNOWN.value, CELL.EMPTY.value, CELL.UNKNOWN.value, CELL.UNKNOWN.value],
            [CELL.UNKNOWN.value, CELL.EMPTY.value, CELL.EMPTY.value, CELL.WALL.value, CELL.UNKNOWN.value],
            [CELL.EMPTY.value, CELL.EMPTY.value, CELL.PLAYER.value, CELL.EMPTY.value, CELL.EMPTY.value],
            [CELL.UNKNOWN.value, CELL.WALL.value, CELL.WALL.value, CELL.WALL.value, CELL.UNKNOWN.value],
            [CELL.UNKNOWN.value, CELL.UNKNOWN.value, CELL.UNKNOWN.value, CELL.UNKNOWN.value, CELL.UNKNOWN.value]])

    def test_str(self):
        m = TextLevel()
        m.init_map(os.path.join(os.getcwd(), "game", "assets", "text_levels", "0"))
        self.assertEqual(str(m),
                         "22222222222\n21111111112\n21111111112\n21111111112\n21111111112\n21111111112\n22222222222")
