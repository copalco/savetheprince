import unittest

from savetheprince.circle import Circle
from savetheprince.game import Game
from savetheprince.hero import Hero
from tests.factories.area_factory import AreaFactory


class TestGame(unittest.TestCase):

    def test_changes_hero_position(self) -> None:
        hero = Hero()
        area_to_the_left = AreaFactory.create()
        game = Game(Circle(AreaFactory.create(), area_to_the_left), hero)
        game.move_left()
