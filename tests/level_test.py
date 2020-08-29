from config.constants import CELL
from game.levels.text_level import TextLevel
from game.player.player import Player

from unittest import TestCase
import os


class TestLevel(TestCase):

    def test_get_view_1(self):
        m = TextLevel()
        m.read_file(os.path.join(os.getcwd(), "game", "assets", "text_levels", "0"))
        p = Player()
        p.update_range(1)
        p.x = 1
        p.y = 1
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
        m.read_file(os.path.join(os.getcwd(), "game", "assets", "text_levels", "1"))
        p = Player()
        p.x = 3
        p.y = 4
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
        m.read_file(os.path.join(os.getcwd(), "game", "assets", "text_levels", "0"))
        self.assertEqual(str(m),
                         "22222222222\n21111111112\n21111111112\n21111111112\n21111111112\n21111111112\n22222222222")
