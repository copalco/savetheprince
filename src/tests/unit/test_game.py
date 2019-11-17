import unittest

from savetheprince.main import Area
from savetheprince.main import Game
from savetheprince.main import Position
from savetheprince.main import Size


class TestGame(unittest.TestCase):

    def test_stores_current_hero_location(self) -> None:
        area = Area(Size(10, 10), Position(0, 0))
        game = Game()
        game.store_hero_location(area)
        self.assertEqual(game.locate_hero(), area)