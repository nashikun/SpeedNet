from game.levels.text_level import TextLevel

from unittest import TestCase
import os


class TestLevel(TestCase):

    def test_get_view_1(self):
        m = TextLevel(1)
        m.read_file(os.path.join(os.getcwd(), "game", "assets", "text_levels", "0"))
        self.assertEqual(m.height, 7)
        self.assertEqual(m.width, 11)
        view = m.get_view(1, 1)
        self.assertEqual(len(view), 3)
        self.assertEqual(view, [["2", "1", "2"], ["1", "3", "0"], ["2", "0", "2"]])

    def test_get_view_2(self):
        m = TextLevel(2)
        m.read_file(os.path.join(os.getcwd(), "game", "assets", "text_levels", "1"))
        self.assertEqual(m.height, 6)
        self.assertEqual(m.width, 11)
        view = m.get_view(3, 4)
        self.assertEqual(len(view), 5)
        self.assertEqual(view, [["2", "2", "0", "2", "2"], ["2", "0", "0", "1", "2"], ["0", "0", "3", "0", "0"], ["2", "1", "1", "1", "2"], ["2", "2", "2", "2", "2"]])
