import unittest

from savetheprince.circle import Circle
from savetheprince.game import Game
from savetheprince.hero import Hero
from tests.factories.area_factory import AreaFactory


class TestGame(unittest.TestCase):

    def setUp(self) -> None:
        self.starting_area = AreaFactory.create()
        self.hero = Hero(location=self.starting_area.id)

    def test_moves_hero_to_the_left(self) -> None:
        area_to_the_left = AreaFactory.create()
        game = Game(Circle(self.starting_area, area_to_the_left), self.hero)
        game.move_playing_hero_left()
        self.assertEqual(self.hero.location(), area_to_the_left.id)

    def test_moves_hero_to_the_right(self) -> None:
        area_to_the_right = AreaFactory.create()
        game = Game(Circle(area_to_the_right, self.starting_area), self.hero)
        game.move_playing_hero_right()
        self.assertEqual(self.hero.location(), area_to_the_right.id)
